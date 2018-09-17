## 什么是爬虫？  
还是按之前《手把手教你用Django搭建个人博客》的习惯来解释**什么是爬虫？**  
把问题转化为**我们为什么需要爬虫？**  
现在给你个任务，把[古龙小说全集网](https://www.gulongwang.com/)里面的全部小说，按照书名保存成一个txt文件。  
没有使用爬虫的话，正常情况下是怎么做呢？？  
- 生成一个名为**苍穹神剑**的txt文件，并打开。  
- 然后点进该小说的目录页，打开第一章节，复制所有的内容到我们的txt文件中。  
- 再打开第二章节，复制所有的内容到我们的txt文件中。
- ……
- 直到我们复制完该小说的所有章节后，然后打开第二本小说**多情剑客无情剑**，生成新的一个txt文件，继续上面的步骤。  

使用爬虫的话，我们只需要分析网页结构，和需要的内容的复制规律，写一个程式，即可把上面的步骤让程式来帮我们完成。  
简单来说，爬虫就是**一个机器人，重复操作我们的浏览器（模拟浏览器），去浏览一些特定的内容**  
## 爬取前的准备工作  
首先，需要python基础知识有变量、函数、函数传参（很重要）、字典、列表、文件操作、包引用。  
还有一点点html和js的知识（尽量选用简单的网站进行爬取，后续再找一些难度高一点的）。  
## 开发环境准备  
最好选用anaconda安装的python3。来减少后续安装出错的可能性。  
生成一个python的虚拟环境来进行爬取。  
### anaconda创建虚拟环境  
`conda create -n py_spider python=3.6`  
python_spider是我们的虚拟环境名。当然你也可以换成你喜欢的名字。  
启动虚拟环境：  
`source activate py_spider`  
退出虚拟环境  
`source deactivate`   
### linux自带的python生成虚拟环境  
安装virtualenv，不需要指定python版本。  
`sudo apt-get install python-virtualenv`  
`sudo apt-get install virtualenvwrapper`  
到你想创建的虚拟环境的目录下创建虚拟环境目录，通常在项目的根目录下   
`virtualenv -p /usr/bin/python3 py_spider`  
启动虚拟环境：  
`source /home/sing/Desktop/python_spider/py_spider/bin/activate`  
注意把上面的路径替换成你的虚拟环境目录中的bin目录下的activate文件的路径。  
退出虚拟环境  
`deactivate`
## 必要的python爬虫包安装   
确保你在虚拟环境中依次执行下面的命令（最好是使用anaconda安装的python3.6，安装时会自动安装上依赖）
```linux
pip install requests lxml bs4 scrapy

pip install pandas
```
安装成功后就可以开始后面的内容了。
