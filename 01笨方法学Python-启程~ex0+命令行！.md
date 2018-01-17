干土木的也要学编程啊！
#教程选择：
学习编程最好的方法就是赶紧敲起来！所以没有太纠结教程，选择多数人推荐的**Learn Python the Hard Way，3rd**, [英文第三版](http://www.souravsengupta.com/cds2015/python/LPTHW.pdf)，顺便熟悉相关术语。看不懂再参考《笨方法学Python》[中文在线第三版](https://flyouting.gitbooks.io/learn-python-the-hard-way-cn/content/learn-python-the-hard-way-exercise0.html);
配合阅读：**《跟着老齐学python》**。偶然发现，喜欢他的语言风格，水货很多，不枯燥。
以上两本都推荐学**Python 2**，不纠结，OK! 
#关于shell和terminal
笨方法学Python的第0课不容易，要求必须学会基本的terminal操作（附录A要全部学完）才能开始，。这里有两个概念：
**shell**,“壳”，与“核”对应。电脑的“核”我们接触不到，我们要通过“shell”给他们指令~
有两种shell，也就是说，两种给电脑指令的方法：
- 图形界面的Shell，术语叫做 **GUI** graphical user interface
也就是我们一般人最常用，在电脑屏幕上有图标，有窗口，我们用鼠标点击告诉他，双击“打开文件”，右键点“复制文件”等
- 命令行的Shell,术语叫做 **CLI** command line interface
想想电影中怎么体现黑客水平？对着满是代码的电脑各种敲，观众不明觉厉。。是的，命令行shell就是基本只靠键盘敲代码来控制，不是快捷键啊！！
比如“打开文件夹aa”，按照命令行方式，就是写下一行代码 *ls aa*，然后电脑就懂了，会弹出一个aa文件夹里面的文件清单列表。
似乎听着很麻烦，但是比如建立个循环文件夹，11文件夹里有22文件夹，再包着33文件夹，33里面再包着44文件夹。只要一行命令
```
mkdir 11/22/33/44
```
只要这么一行，4个母子文件夹就建出来了！很帅，很高效！
**terminal**
terminal就是我们输入命令行的地方。不同电脑系统有不同的terminal,我是windows 10,用powershell，也就是以前cmd的华丽升级版。

---
ex0 and appendix A: from 2017. 12.28 to 12-31
#0. open the terminal 打开terminal,
在window里，按住“win”键，电脑会弹出开始菜单，直接再按字母P 就出来了。"windows powershell"
press win,then type "p".
#1. **pwd**
print working directory = tell me where I am.
- what is a directory? A directory= A folder.
#2. **cd**
change directory
**cd ~**   notice there is a space between cd and ~. if we are lost,and we type "cd ~",it will take us back home.(the default directory)
**cd\\** go to directly the root of C drive
**cd..**   go to one folder up(go to parent folder)
**cd ../../../..**  移动到目录的上上上上层

cd 如同我们鼠标双击或者退出的行为。我们想打开文件夹“stuff”, 那么就输入 cmd stuff. 如果stuff 在默认文件夹中的temp里，那么我们需要输入cd temp/stuff. 斜线表示包含。
cd 不能跨越文件夹打开，正像我们鼠标点击时，也只能一个一个点一样。
#3. **mkdir**
make directory=create a new folder
before doing this, always go home first!
**mkdir foldername1/foldername2/3/4** creat a folder 4 in folder 3 in folder 2 in folder 1
比用鼠标点快多了~
**-p** 指示符: parents, will also create all directories leading up to the given directory that do not exist already. If the given directory already exists, ignore the error.
#4. **ls**
list directory 生成所有文件清单，告诉我这里都有啥
也可以后面加子文件夹的名字，直接看子文件夹中东西
例子：路径如aa/bb/cc
在aa里输入ls,看到aa 里有bb; 
在aa 里输入 ls bb, 看到cc
**dir -r** find files 透视文件夹！文件夹里面的文件夹里的文件也都看看到。

#5. **man**+空格+“任意命令”
即帮助。
比如"man dir",解释是 get child items,好形象~
Remember that if you get lost, then use ls and pwd to figure out where you are, then go to where you need to be with cd.
#6. **rmdir**
remove directory 删除空文件夹
#7. **pushd** 和 **popd**
两个文件夹之间切换。
pushd + 地址B 意思是，记着现在的地址A（即输入pushd之前的地址），然后我要去地址B.
popd 意思是，回到地址A。
#8. **touch**
创建新文件，注意文件名后面要注明文件类型。可惜，windows系统上不能用这个。
**new-item aa.txt** 或者**new-item aa.txt -type file**
#9. **cp**
copy a file or folder  from one location to another location. 复制文件 or 文件夹
当前文件夹有个aa.txt 和bb子文件夹
输入cp aa.txt bb.txt 则效果是 在当前文件夹直接复制aa,生成新文本bb；
输入cp aa.txt bb/ 效果是 直接把aa文本复制到bb子文件夹内;
输入cp bb cc 效果是 复制bb文件夹，生成新文件夹cc;
在名称后面加上斜线/，确认这是个文件夹。
如果想复制的目标位置不是当前文件夹的子文件夹，那么就要输入完整路径。比如把aa.txt复制到桌面，需要输入cp aa.txt C:/user/lenovo/desktop；
**cp -r** -r的意思是带着里面的文件一起复制。如果复制文件夹时不输入-r,那其实等同于新建空文件夹。
#10. **mv**
move a file or folder
#11.  **more** 
看文件内容。只支持txt,其他的如pdf,jpg都是乱码，按q退出。 在linux里是less~
#12. **cat** 
也是看文件内容。和上面的more有啥区别咧？
more是自动只给你放一页屏幕的东西，如果想显示更多，需要按空格。而cat则是一股脑全放出来~
Cat displays file contents. If the file is large the contents scroll off the screen before we view it. So command 'more' is like a pager which displays the contents page by page.
#13. **rm**
 remove,删除文件。 rmdir是删除文件夹。在linux中rmdir只能删除空文件夹，所以需要先用rm命令把文件夹里的东西都删除，再删除文件夹。而其实在windows里面，rmdir + y 可以直接删除带内容的文件夹。
#14. 其他
**hostname** print computer's network name
**echo**  相当于print,比如前面说的回家，那么家默认在哪呢？可以通过echo $home看到.
**clear** 
**history** 看command line 输入过的命令

最后，学了命令行操作，明白了文件夹命名不要带空格。。



