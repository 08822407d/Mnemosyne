#!/usr/bin/env bash
# 写前预检脚本（MNEMOSYNE-258）——把谱系防护 §3/§4.3/§5 与跨族约定一/三的机械部分固化：
#   1) fetch 并钉住 master；2) 当前分支若已有 PR 且已合并/关闭则拒绝继续（须新任务号新分支）；
#   3) 枚举 open PR 及其变更路径，供路径交集判断。任何仓库写入批次开始前运行。
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
git fetch origin --quiet
echo "pinned_master: $(git rev-parse --short origin/master)"
br=$(git rev-parse --abbrev-ref HEAD)
echo "current_branch: $br"
if [ "$br" != "master" ]; then
  st=$(gh pr list --head "$br" --state all --limit 1 --json number,state --jq '.[0] | "#\(.number) \(.state)"' 2>/dev/null || true)
  echo "branch_pr: ${st:-none}"
  case "${st:-}" in
    *MERGED*|*CLOSED*) echo "STOP: 当前分支的 PR 已合并/关闭。按谱系防护 §4.3：改用新任务号、从最新 master 新建分支。"; exit 2;;
  esac
  behind=$(git rev-list --count "$br"..origin/master || echo "?")
  echo "commits_master_ahead_of_branch: $behind"
fi
echo "open_prs_and_changed_paths:"
for n in $(gh pr list --state open --json number --jq '.[].number'); do
  printf '  #%s: ' "$n"; gh pr diff "$n" --name-only 2>/dev/null | tr '\n' ' '; echo
done
echo "preflight_ok"
