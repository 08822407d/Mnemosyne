#!/usr/bin/env python3
"""Deterministic verifier/materializer for MNEMOSYNE-240."""
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path
EXPECTED_MANIFEST_ID='MNEMOSYNE-240-OPERATOR-PAYLOAD-MANIFEST-001'
EXPECTED_BRANCH='mnemosyne-240-f2-g2a-and-handoff-audit-closeout'
EXPECTED_MODIFY_PATHS={'handoff/handoff-current.md','current/fable5-cross-repository-safe-concurrency-research-status.md','notes/todos/MNE-HANDOFF-CORRECTNESS-VALIDATION-AND-PROTOCOL-HARDENING-TODO-001.md','notes/registries/project-research-display-name-registry-v0.1.md'}
FORBIDDEN_EXACT={'README.md','current/human-approved-spec.md'}; FORBIDDEN_PREFIXES=('commands/',)
def blob_sha(data:bytes)->str:return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()
def run(args,cwd,binary=False,check=True):
 cp=subprocess.run(args,cwd=cwd,capture_output=True,text=not binary,check=False)
 if check and cp.returncode:
  err=cp.stderr if not binary else cp.stderr.decode('utf-8','backslashreplace');raise RuntimeError(f"command failed {args!r}: {err!r}")
 return cp.stdout
def load(path):
 m=json.loads(path.read_text(encoding='utf-8'))
 if m.get('manifest_id')!=EXPECTED_MANIFEST_ID or m.get('branch')!=EXPECTED_BRANCH:raise RuntimeError('manifest identity mismatch')
 return m
def policy(m):
 entries=m['files'];paths=[e['path'] for e in entries]
 if paths!=sorted(paths) or len(paths)!=m['changed_path_count'] or len(paths)!=len(set(paths)):raise RuntimeError('path order/count/duplicate mismatch')
 folded={}
 for p in paths:
  parts=Path(p).parts
  if p.startswith('/') or '..' in parts or p in FORBIDDEN_EXACT or p.startswith(FORBIDDEN_PREFIXES):raise RuntimeError(f'unsafe/forbidden path: {p}')
  if p.startswith('current/') and p not in EXPECTED_MODIFY_PATHS:raise RuntimeError(f'unexpected current path: {p}')
  if any(len(x.encode('utf-8'))>255 for x in parts):raise RuntimeError(f'filesystem component too long: {p}')
  folded.setdefault(p.casefold(),[]).append(p)
 if any(len(v)>1 for v in folded.values()):raise RuntimeError('casefold collision')
 mods={e['path'] for e in entries if e['operation']=='modify'}
 if mods!=EXPECTED_MODIFY_PATHS or set(m['allowed_modify_paths'])!=EXPECTED_MODIFY_PATHS:raise RuntimeError('modify set mismatch')
 return paths
def verify_sources(m,root):
 for e in m['files']:
  data=(root/e['path']).read_bytes()
  if len(data)!=e['bytes'] or hashlib.sha256(data).hexdigest()!=e['sha256'] or blob_sha(data)!=e['git_blob_sha1']:raise RuntimeError(f"source identity mismatch: {e['path']}")
def verify_base(m,repo,require_head=True):
 base=m['base_commit']
 if run(['git','rev-parse',f'{base}^{{tree}}'],repo).strip()!=m['base_tree']:raise RuntimeError('base tree mismatch')
 if require_head and run(['git','rev-parse','HEAD'],repo).strip()!=base:raise RuntimeError('HEAD/base mismatch')
 for e in m['files']:
  cp=subprocess.run(['git','cat-file','-e',f"{base}:{e['path']}"],cwd=repo,capture_output=True)
  exists=cp.returncode==0
  if e['operation']=='add' and exists:raise RuntimeError(f"add exists: {e['path']}")
  if e['operation']=='modify':
   if not exists:raise RuntimeError(f"modify missing: {e['path']}")
   if run(['git','rev-parse',f"{base}:{e['path']}"],repo).strip()!=e['expected_base_blob']:raise RuntimeError(f"base blob mismatch: {e['path']}")
def parse_ns(data:bytes):
 parts=data.split(b'\0');
 if parts and parts[-1]==b'':parts.pop()
 if len(parts)%2:raise RuntimeError('name-status shape')
 return {parts[i+1].decode():parts[i].decode() for i in range(0,len(parts),2)}
def expected(m):return {e['path']:('M' if e['operation']=='modify' else 'A') for e in m['files']}
def materialize(m,root,repo,paths):
 for e in m['files']:
  dst=repo/e['path'];dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((root/e['path']).read_bytes())
 pathspec=repo/'.git'/'mne240-pathspec';pathspec.write_bytes(b''.join(p.encode('utf-8')+b'\0' for p in paths))
 subprocess.check_call(['git','-c','core.autocrlf=false','add',f'--pathspec-from-file={pathspec}','--pathspec-file-nul'],cwd=repo)
 got=parse_ns(run(['git','diff','--cached','--name-status','--no-renames','-z'],repo,binary=True))
 if got!=expected(m):raise RuntimeError('index path/status mismatch')
 if run(['git','diff','--name-only','-z'],repo,binary=True):raise RuntimeError('unstaged tracked changes')
 if run(['git','ls-files','--others','--exclude-standard','-z'],repo,binary=True):raise RuntimeError('untracked files')
 for e in m['files']:
  if run(['git','rev-parse',f":{e['path']}"],repo).strip()!=e['git_blob_sha1']:raise RuntimeError(f"index blob mismatch: {e['path']}")
def verify_commit(m,root,repo,commit):
 if run(['git','rev-parse',f'{commit}^'],repo).strip()!=m['base_commit']:raise RuntimeError('parent mismatch')
 got=parse_ns(run(['git','diff-tree','--no-commit-id','--name-status','--no-renames','-r','-z',commit],repo,binary=True))
 if got!=expected(m):raise RuntimeError('commit path/status mismatch')
 for e in m['files']:
  if run(['git','show',f"{commit}:{e['path']}"],repo,binary=True)!=(root/e['path']).read_bytes():raise RuntimeError(f"commit byte mismatch: {e['path']}")
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--payload-root',type=Path,required=True);ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--materialize',action='store_true');ap.add_argument('--verify-commit')
 a=ap.parse_args();m=load(a.manifest);paths=policy(m);verify_sources(m,a.payload_root);verify_base(m,a.repo,not bool(a.verify_commit))
 if a.materialize:materialize(m,a.payload_root,a.repo,paths)
 if a.verify_commit:verify_commit(m,a.payload_root,a.repo,a.verify_commit)
 print(json.dumps({'status':'PASS','manifest_id':m['manifest_id'],'changed_path_count':len(paths),'G2A_issued':False,'A1_executed':False},indent=2))
if __name__=='__main__':main()
