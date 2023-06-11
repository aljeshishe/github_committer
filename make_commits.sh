#!/bin/bash
set -ex


trap 'echo "Last command exit code: $?"' EXIT

BRANCH_NAME=commits_$(uuidgen)
COMMIT_COUNT=${1:-2}
echo creating branch: ${BRANCH_NAME}
git config --global user.email "ax66@bk.ru"
git config --global user.name "Aleksei Grachev"
git branch ${BRANCH_NAME}
git push --set-upstream origin ${BRANCH_NAME}

for i in $( seq 1 ${COMMIT_COUNT} )
do
	MESSAGE=$(date "+%Y-%m-%d %H:%M:%S")
	echo ${MESSAGE} >> changes
	git add changes
	git commit -m "change"
	git push 
done

echo deleting branch ${BRANCH_NAME}
git checkout main
git branch -d ${BRANCH_NAME}
git push origin --delete ${BRANCH_NAME}