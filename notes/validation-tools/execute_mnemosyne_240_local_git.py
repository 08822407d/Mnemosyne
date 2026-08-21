#!/usr/bin/env python3
"""One-shot Ubuntu/Linux Phase-A local Git publisher for MNEMOSYNE-240. No PR action."""
from __future__ import annotations
import argparse,datetime as dt,hashlib,json,os,subprocess,sys,urllib.parse,urllib.request,zipfile
from pathlib import Path
PRIMARY='08822407d/Mnemosyne';VALIDATION='08822407d/mnemosyne-target-lifecycle-validation-002';EXPECTED_VALIDATION='e8e3296922185b4b70997c2351d6f39423f2cd4f';OLD_BRANCH='mnemosyne-235-f2-g2a-and-handoff-audit-closeout';FAILED_BRANCH='mnemosyne-239-f2-g2a-and-handoff-audit-closeout';A1=['v2a-a1-001-controller','v2a-a1-001-alpha','v2a-a1-001-beta','v2a-a1-001-order-alpha-beta','v2a-a1-001-order-beta-alpha']
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def safe(v):
 if '://' not in v:return v
 u=urllib.parse.urlsplit(v)
 if not u.username and not u.password:return v
 host=u.hostname or '';host+=f':{u.port}' if u.port else ''
 return urllib.parse.urlunsplit((u.scheme,host,u.path,u.query,u.fragment))
def cmd(r,args,cwd=None):
 env=os.environ.copy();env['GIT_TERMINAL_PROMPT']='0';cp=subprocess.run(args,cwd=cwd,text=True,capture_output=True,check=False,env=env)
 rec={'seq':len(r['commands'])+1,'timestamp_utc':now(),'command':[safe(str(x)) for x in args],'cwd':str(cwd) if cwd else None,'exit_status':cp.returncode,'retry_count':0,'stdout':cp.stdout,'stderr':cp.stderr};r['commands'].append(rec)
 if cp.returncode:raise RuntimeError(f"command failed at sequence {rec['seq']}")
 return cp.stdout
def refs(s):
 out={}
 for line in s.splitlines():
  if line.strip():sha,ref=line.split(maxsplit=1);out[ref]=sha
 return out
def api_json(url):
 headers={'User-Agent':'MNEMOSYNE-240-executor','Accept':'application/vnd.github+json'}
 token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
 if token:headers['Authorization']=f'Bearer {token}'
 with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as resp:return json.loads(resp.read().decode())
def open_prs():
 total=[]
 for b in [OLD_BRANCH,FAILED_BRANCH,'mnemosyne-240-f2-g2a-and-handoff-audit-closeout']:
  q=urllib.parse.urlencode({'state':'open','head':f'08822407d:{b}','per_page':100})
  rows=api_json(f'https://api.github.com/repos/{PRIMARY}/pulls?{q}')
  total.extend([{'number':x['number'],'head':b,'url':x['html_url']} for x in rows])
 return total
def primary(r,url,m):
 got=refs(cmd(r,['git','ls-remote','--heads',url,'master',OLD_BRANCH,FAILED_BRANCH,m['branch']]))
 exp={'refs/heads/master':m['base_commit'],f'refs/heads/{OLD_BRANCH}':m['base_commit']}
 if got!=exp:raise RuntimeError(f'primary refs mismatch: {got!r}')
 return got
def validation(r,url):
 got=refs(cmd(r,['git','ls-remote','--heads',url,'master',*A1]))
 if got.get('refs/heads/master')!=EXPECTED_VALIDATION:raise RuntimeError('validation master mismatch')
 if any(f'refs/heads/{b}' in got for b in A1):raise RuntimeError('A1 branch present')
 return got
def write(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo-url',required=True);p.add_argument('--validation-repo-url',required=True);p.add_argument('--payload-zip',type=Path,required=True);p.add_argument('--manifest',type=Path,required=True);p.add_argument('--verifier',type=Path,required=True);p.add_argument('--workdir',type=Path,required=True);p.add_argument('--receipt',type=Path,required=True);p.add_argument('--git-user-name');p.add_argument('--git-user-email')
 a=p.parse_args();r={'task_id':'MNEMOSYNE-240','status':'RUNNING','started_at_utc':now(),'commands':[],'retry_count':0,'G2A_issued':False,'A1_execution_authorized':False,'A1_executed':False,'validation_repository_written':False};stage='INIT';extracted=None
 try:
  if sys.platform!='linux':raise RuntimeError('formal execution requires Linux')
  if a.workdir.exists():raise RuntimeError('workdir exists; reuse/cleanup prohibited')
  m=json.loads(a.manifest.read_text(encoding='utf-8'))
  if m.get('manifest_id')!='MNEMOSYNE-240-OPERATOR-PAYLOAD-MANIFEST-001' or m.get('branch')!='mnemosyne-240-f2-g2a-and-handoff-audit-closeout':raise RuntimeError('manifest identity mismatch')
  if a.payload_zip.stat().st_size!=m['payload_zip']['bytes'] or sh(a.payload_zip)!=m['payload_zip']['sha256']:raise RuntimeError('payload ZIP identity mismatch')
  entries={e['path']:e for e in m['files']}
  for rp,lp in [('notes/validation-tools/execute_mnemosyne_240_local_git.py',Path(__file__)),('notes/validation-tools/verify_mnemosyne_240_publication.py',a.verifier)]:
   e=entries[rp];data=lp.read_bytes()
   if len(data)!=e['bytes'] or hashlib.sha256(data).hexdigest()!=e['sha256']:raise RuntimeError(f'external tool identity mismatch: {rp}')
  stage='REMOTE_PREFLIGHT';p0=primary(r,a.repo_url,m);v0=validation(r,a.validation_repo_url);prs=open_prs()
  if prs:raise RuntimeError(f'related open PRs: {prs!r}')
  r['preflight']={'primary_refs':p0,'validation_refs':v0,'related_open_PRs':prs}
  stage='CLONE';cmd(r,['git','clone','--no-tags','--branch','master',a.repo_url,str(a.workdir)]);cmd(r,['git','switch','-c',m['branch'],m['base_commit']],a.workdir);cmd(r,['git','config','core.autocrlf','false'],a.workdir);cmd(r,['git','config','core.safecrlf','true'],a.workdir)
  if a.git_user_name:cmd(r,['git','config','user.name',a.git_user_name],a.workdir)
  if a.git_user_email:cmd(r,['git','config','user.email',a.git_user_email],a.workdir)
  name=cmd(r,['git','config','--get','user.name'],a.workdir).strip();email=cmd(r,['git','config','--get','user.email'],a.workdir).strip()
  if not name or not email:raise RuntimeError('git identity absent')
  stage='EXTRACT';extracted=a.workdir.parent/'payload';
  if extracted.exists():raise RuntimeError('extraction path exists')
  extracted.mkdir()
  with zipfile.ZipFile(a.payload_zip) as z:
   names=[e['path'] for e in m['files']]
   if z.namelist()!=names:raise RuntimeError('ZIP/manifest order mismatch')
   for info in z.infolist():
    if info.filename.startswith('/') or '..' in Path(info.filename).parts:raise RuntimeError('unsafe ZIP path')
    dst=extracted/info.filename;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(z.read(info.filename))
  stage='VERIFY_BASE';cmd(r,[sys.executable,str(a.verifier),'--manifest',str(a.manifest),'--payload-root',str(extracted),'--repo',str(a.workdir)])
  stage='RECHECK_BEFORE_MATERIALIZE'
  if primary(r,a.repo_url,m)!=p0 or validation(r,a.validation_repo_url)!=v0 or open_prs():raise RuntimeError('remote state moved')
  stage='MATERIALIZE';cmd(r,[sys.executable,str(a.verifier),'--manifest',str(a.manifest),'--payload-root',str(extracted),'--repo',str(a.workdir),'--materialize'])
  stage='RECHECK_BEFORE_COMMIT'
  if primary(r,a.repo_url,m)!=p0 or validation(r,a.validation_repo_url)!=v0 or open_prs():raise RuntimeError('remote state moved')
  stage='COMMIT';cmd(r,['git','-c','commit.gpgsign=false','commit','-m','MNEMOSYNE-240: publish F2 G2A, handoff audit, HVAL and incident closeout'],a.workdir);commit=cmd(r,['git','rev-parse','HEAD'],a.workdir).strip();cmd(r,[sys.executable,str(a.verifier),'--manifest',str(a.manifest),'--payload-root',str(extracted),'--repo',str(a.workdir),'--verify-commit',commit])
  stage='RECHECK_BEFORE_PUSH'
  if primary(r,a.repo_url,m)!=p0 or validation(r,a.validation_repo_url)!=v0 or open_prs():raise RuntimeError('remote state moved')
  stage='ONE_NON_FORCE_PUSH';cmd(r,['git','push','origin',f'HEAD:refs/heads/{m["branch"]}'],a.workdir)
  stage='POST_PUSH_READBACK';after=refs(cmd(r,['git','ls-remote','--heads',a.repo_url,'master',OLD_BRANCH,FAILED_BRANCH,m['branch']]))
  if after.get('refs/heads/master')!=m['base_commit'] or after.get(f'refs/heads/{OLD_BRANCH}')!=m['base_commit'] or f'refs/heads/{FAILED_BRANCH}' in after or after.get(f'refs/heads/{m["branch"]}')!=commit:raise RuntimeError('post-push refs mismatch')
  if validation(r,a.validation_repo_url)!=v0:raise RuntimeError('validation moved')
  cmd(r,['git','fetch','origin',m['branch']],a.workdir);fetched=cmd(r,['git','rev-parse','FETCH_HEAD'],a.workdir).strip()
  if fetched!=commit:raise RuntimeError('fetch readback mismatch')
  cmd(r,[sys.executable,str(a.verifier),'--manifest',str(a.manifest),'--payload-root',str(extracted),'--repo',str(a.workdir),'--verify-commit',fetched])
  r.update({'status':'MNEMOSYNE_240_BRANCH_PUSHED_PENDING_READY_PR','completed_at_utc':now(),'stage':'PHASE_A_COMPLETE','commit':commit,'branch':m['branch'],'changed_path_count':m['changed_path_count']});write(a.receipt,r);print(json.dumps(r,ensure_ascii=False,indent=2));print('MNEMOSYNE_240_BRANCH_PUSHED_PENDING_READY_PR');return 0
 except Exception as e:
  r.update({'status':'MNEMOSYNE_240_BLOCKED','completed_at_utc':now(),'stage':stage,'error':repr(e),'local_workdir_preserved':str(a.workdir),'payload_extraction_preserved':str(extracted) if extracted else None});write(a.receipt,r);print(json.dumps(r,ensure_ascii=False,indent=2));print('MNEMOSYNE_240_BLOCKED');return 1
if __name__=='__main__':raise SystemExit(main())
