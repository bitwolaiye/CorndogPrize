CorndogPrize
============

Corndog Prize

## 使用方式

先将代码clone下来，在终端中敲入

	$ git clone https://github.com/bitwolaiye/CorndogPrize.git
	
然后进入该目录

	$ cd CorndogPrize.git
	
运行命令,命令需要填入一个简单参数mid，以王菲的一条微博为例 http://weibo.com/1629810574/AmKH3i3aX 他最后一个串AmKH3i3aX填入就可以了

	$ python app.py mid=AmKH3i3aX
	
因为不是前端程序员，故此处借助markdown来显示内容。T_T。mac下推荐markdown的编辑器 [Mou](http://mouapp.com/) 免费。装完后还是命令行，敲入

	$ open 1.md
	
既可以看了。


## 尚未完成的

* 一次只能取200条评论。新浪说好的2000条呢？后续可以加好逻辑把所有评论取了。
* 还没考虑转发
* 无随机逻辑
* 无法微博逻辑