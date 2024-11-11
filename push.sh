#! /bin/bash
set -e


echo '>>> ===== starting push... ===== <<<'
git add . && git status
# shellcheck disable=SC2162
read -t 60 -p "[commit] >>> " commit_msg
if [ "$commit_msg" == "" ]; then
  git reset
  echo "[dev] You haven't entered any comments !"
  exit 1
else
  git commit -m "[commit]: $commit_msg"
  git pull origin main
  git push origin main
  exit 0
fi
echo '>>> ===== ending push... ===== <<<'
