#!/bin/bash
set -ex


trap 'echo "Last command exit code: $?"' EXIT

BRANCH_NAME=commits
COMMIT_COUNT=${1:-2}
#REPO=git@gitlab.alberblanc.com:trading/mlrobot.git
#WORK_PATH=/tmp/repo_$(uuidgen)

echo creating branch: ${BRANCH_NAME}
git branch ${BRANCH_NAME}
git checkout ${BRANCH_NAME}
# git push --set-upstream origin ${BRANCH_NAME}

for i in $( seq 0 ${COMMIT_COUNT} )
do
	echo "change" >> changes
	git add changes
	git commit -m "change"
	git push --set-upstream origin ${BRANCH_NAME}
done

