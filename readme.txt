BASEGIT 操作指令：https://git-scm.com/
初始化仓库 
	git init
添加文件到暂存区
	git add {fileName}
添加全部文件到暂存区
	git add {fileName}
提交文件 
	git add -A 或 git add .
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
只删除暂存区不删除工作目录
	git rm --cached {fileName}
重命名
	git mv {fileNameOld} {fileNameNew}
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
	git log --oneline --decorate --graph -all
			--单行--commit引用信息--图形化--所有分支
查找(工作区/暂存区)差异信息
	git diff
查找(暂存区/历史提交)差异信息
	git diff --cached
查找(暂存区/其他历史提交)中某个文件的差异信息
	git diff {历史提交} -- {文件名}
查找文本的差异信息
	git diff --color-words -- {文件名}
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


gitignore
eg:
[
	*.[ao] 		-- 以o或a结尾的不添加到git仓库
	*~     		-- 含~的不添加
	*.pyc  		-- 后缀为pyc的不添加
	!test.pyc 	-- 不忽略，若开头含!则 \!
	foo/ 		-- 匹配到目录
	**/res 	    -- 匹配所有res
]
分支eg:
新建test分支：git branch test
切换test分支: git checkout test

添加一个本地轻量级的tag: git tag "V0" 7位的hash
带注解的可推到服务器的tag: git tag -a "一般大写" 7位hash

查看历史示意图: git log --oneline --decorate --graph -all
给命令起别名: git config --global alias.bfv "log --oneline --decorate --graph -all"
使用别名操作: git bfv
查看tag内容: git show
回到tag: git checkout V0
但以上有警告，可能会丢弃修改内容，故创建新的分支并切换到新分支:git checkout -b fix_V0
修改内容并提交后，则会发出警告，如果执行 git checkout master 则会丢失已提交内容，故采用stash保存分支修改
git stash save -a "stash 信息"	
git stash list可以看到stash信息,如 stash@{0}
若需要还原暂存区则需要执行 git stash pop --index stash@{0}
还原暂存区且不删除stashlist,则 git stash apply --index stash@{0}
清除stash git stash drop stash@{0}
清理多个 git stash clear

合并分支需切换回主分支：
git checkout master
若和要合并的分支产生冲突，若取消合并: git merge --abort
不取消合并，可以编辑冲突文件，修改完成并add到暂存区并commit即可
