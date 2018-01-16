BASEGIT 操作指令：
初始化仓库 
	git init
提交文件 
	git add 文件 & git commit -m 提交内容
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
	git diff HEAD -- 文件
丢弃工作区修改（用版本库里的版本替换工作区的版本）
	git checkout -- 文件
暂存区修改撤销
	git reset HEAD file
删除
	git rm 文件&git commit -m 内容
远程仓库
	git remote add origin {github ssh/https}
	eg: remote add origin git@github.com:lance2038/lanceEdit.git
首次推送
	git push -u origin master
之后推送
	git push origin master
远程仓库克隆到本地
	git clone {github ssh/https}
拉取远程库内容
	git pull
