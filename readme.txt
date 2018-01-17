BASEGIT 操作指令：https://git-scm.com/
初始化仓库 
	git init
提交文件 
	git add {fileName} & git commit -m {提交内容}
查看日志
	git log
回退
	git reset --hard HEAD^(^一次，^^两次，～n n次)
回归指定版本
	 git reset --hard ****（无需全部写全）
查看命令历史
	git reflog
查看分支状态
	git status
仓库最新版本与工作区的区别
	git diff HEAD -- {fileName}
丢弃工作区修改（用版本库里的版本替换工作区的版本）
	git checkout -- {fileName}
暂存区修改撤销
	git reset HEAD file
删除
	git rm {fileName}&git commit -m 内容
远程仓库
	git remote add origin {github ssh/https}
	eg:git remote add origin git@github.com:lance2038/lanceEdit.git
首次推送
	git push -u origin master
之后推送
	git push origin master
远程仓库克隆到本地
	git clone {github ssh/https}
拉取远程库内容
	git pull
创建新的分支
	git branch {branchName}
切换到新分支
	git checkout {branchName}
二合一,创建新的分支并切换到新分支
	git checkout -b {branchName}
查看当前分支
	git branch
在master使用用于合并指定分支到master
	git merge {branchName}
删除分支
	git branch -d {branchName}
强制删除分支
	git branch -D {branchName}
查看分支合并图
	git log --graph
禁用快速合并到合并
	git merge --no-ff -m {"合并信息"} {branchName}
暂时隐藏工作区
	git stash
查看隐藏工作区列表
	git stash list
恢复隐藏工作区
	1.git stash apply {工作区} + 删除stash内容 git stash drop
	2.git stash pop
查看远程仓库名称
	git remote
在本地创建和远程分支对应的分支，本地和远程分支的名称最好一致
	git checkout -b {branchName} origin/{branchName}
建立本地分支和远程分支的关联
	git branch --set-upstream {branchName} origin/{branchName}
在最新提交上打标签
	git tag {tagName} 或 git tag -a {tagName} -m {说明文字}
使用git log找到commitID打标签
	git tag {tagName} {commitID}
查看标签
	git tag
查看标签信息
	git show {tagName}
删除一个本地标签
	git tag -d {tagName}
删除一个远程标签
	git push origin :refs/tags/{tagName}
推送一个本地标签
	git push origin {tagName}
推送全部未推送过的本地标签
	git push origin --tags
