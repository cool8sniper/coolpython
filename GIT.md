1. 拉取远程代码并且覆盖本地更改

git fetch origin && git reset –hard origin/master


2. 回滚一个 merge

git revert -m 1 xxxx

3. 修改之前的提交记录或者很久前提交的记录

git rebase –interactive ID^
将需要修改的记录的 pick 改成 edit
执行更改
git commit –all –amend
git rebase –continue


4. 使用多个远程代码库，并且使用多个不同的 SSH Key

修改 ~/.ssh/config

Host bitbucket.org
HostName bitbucket.org
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
User git

Host bitbucket.org-key2
HostName bitbucket.org
IdentityFile ~/.ssh/key2_id_rsa
User git

修改 .git/config

[remote "origin"]
url = git@bitbucket.org-key2:XXXX/yyyy.git
fetch = +refs/heads/*:refs/remotes/origin/*

5. 撤销 Git 的最后一次提交

git reset –soft HEAD~1

6. 和外部团队协作需要的维护多个远程库，合并其他库的更新的过程

git remote rename origin upstream
git remote add origin URL_TO_GITHUB_REPO
git push origin master
git pull upstream master && git push origin master