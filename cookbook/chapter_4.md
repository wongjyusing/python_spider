### 什么是Scrapy？  
不如说Scrapy可以做什么？  
Scrapy的最大特性是**异步**，讲辣么多都是废话。  
实践出真理，先运行起来再讲特性。  
### 创建第一个Scrapy爬虫项目  
这次依旧是爬取小说，相信一开始，都安装好scrapy了吧？   
安装过程就不讲了，回头看第一篇爬虫系列文章。   
进入虚拟环境，把终端操作的目录路径切换到你想创建项目的路径。  
`scrapy startproject scrapy_learn`  
这样，我们当前目录下就多了一个名为**scrapy_learn**的目录了。  
进入该目录：
`cd scrapy_learn`  
创建一个爬虫文件  
`scrapy genspider novel www.gulongwang.com`  
上面的**novel**是我们的爬虫的名字，后面的网址是我们爬取的网站。  
这时，我们的项目结构如下：  
输入`tree`  
```tree
├── scrapy.cfg           # 配置文件
└── scrapy_learn         # 项目名
    ├── __init__.py      # 声明该目录是python的包
    ├── items.py         # 获取的字段文件
    ├── middlewares.py   # 中间件处理文件
    ├── pipelines.py     # 管道文件
    ├── settings.py      # 爬虫设置或者说项目配置文件
    └── spiders          # 爬虫文件存放的目录
        ├── __init__.py  # 声明该目录是python的包
        └── novel.py     # 我们刚刚创建的爬虫文件

```  
首先到**settings.py**文件中修改一下，  
`ROBOTSTXT_OBEY = True`，把True改成False。  
然后打开我们的novel.py文件。  
根据下面的提示修改内容：
```python
# -*- coding: utf-8 -*-
import scrapy


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['www.gulongwang.com']
    start_urls = ['http://www.gulongwang.com/']

    def parse(self, response):

        # 改这里
        print(response.text)
```
运行爬虫  
`scrapy crawl novel`（注意在项目的根目录下运行，有scrapy.cfg文件的地方就是根目录）  
看到效果了吧，比之前写requests代码少多了。  
其实呢，由于这个网站的反爬措施为0而已，不要高兴太早了。  
我们连浏览器头都没有的哟。   
反爬方面先不谈，异步特性也先不谈。一会实践过后，感受一下就知道了。     
如果按照以前requests的思维去编写这个爬虫很大可能性会失败。  
这里先演示一下这里的函数是怎么传输数据的。  
