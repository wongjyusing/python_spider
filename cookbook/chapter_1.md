## 第一条小爬虫  
写任何代码前，我们必须确定这次写的代码是用来干什么的？  
这次我们要把[古龙小说全集](https://www.gulongwang.com/)中的所有小说按照**书名**保存成一个txt文件。  
这次使用python中的第三方包**requests**来进行爬取。  
大家可以打开上面的网址到里面进行观察一下该网站的网址的变化（随便点击几本小说进行观察）  
思考一下，我们人类是怎么获取里面的内容的？  
不难发现，我们进入首页，看到一堆书名。  
点开书名后到达章节列表，点开章节后进入小说内容的详情页，也就是我们需要获取的小说内容。  
这里我们可以把这个网站分为三层结构，如下：
- 书名列表页（首页）
- 章节列表页
- 内容页  

## 打开首页    
关于代码的解释写在代码的注释中。  
首先，我们先把终端的操作路径切换到我们需要创建爬虫文件的目录下。  
我这里是直接在桌面上创建了一个名为python_spier的目录。  
进入该目录并切换到虚拟环境。  
新开一个终端：  
`cd Desktop/python_spider  && source activate py_spider`  
新建一个名为requests_0.py的文件  
`touch requests_0.py`  
写入以下内容：
```python
import requests   # 导入requests包

# 把我们要爬取的网址赋值给url这个变量
url = 'https://www.gulongwang.com/'

# 使用requests中的get方法来请求我们的网址
# 采取该方法后会返回一个响应,相当与我们打开网页后会返回页面一样

# 简单来说，我们在浏览器输入一个网址是请求该网站
# 返回会的内容是该网站对我们的请求的响应。
# 响应中包括cookice、网页内容、状态码、header等

response = requests.get(url=url)

# 直接打印response是打印出该请求的状态码
print(response)

# 打印出该响应的文本信息，也就是该网址的网页源代码
print(response.text)
```
上面的代码就是最最基本打开一个网址的代码。  
回头想一下，我们打开首页后要做什么呢？？  
要**点击书名**，然后进入章节列表。而我们输入对应书名的链接也是可以进入该章节列表的。  
例如在浏览器中输入`https://www.gulongwang.com/cang/`也是可以进入该小说的章节列表。  
和在首页点击的效果是一样的。  
所以，我们可以在首页的内容中获取小说的章节列表的url。  
怎么获取呢？  
这个时候需要用到解析方法。  
通常我们用的解析网页元素的方法有bs4、xpath、re、pyquery、css选择器、pandas（对表结构的解析很强后面会介绍）等等。  
现在我们采取bs4的方式进行解析，这里就不介绍bs4的用法了。可自行查阅[bs4的文档](https://beautiful-soup-4.readthedocs.io/en/latest/)进行学习，挺简单的。  
同时也推荐一款在谷歌浏览器的插件**infolife**可以帮助我们初学者快速获取**bs4解析式**，文件在该项目对应的github上，[地址](https://github.com/wongjyusing/python_spider/tree/master/download)，大家自行点开后，安装到谷歌浏览器即可。  
## infolife使用方法  
点开infolie插件，在右上角会出现一个小窗口，  
这时，我们使用鼠标点击我们想要的内容。  
结合本次的教程来说我们需要的数据是页面中右边的书名的部分。  
首先，点击右边的书名（随便点一本书，注意：不是点击图片）  
不出意外的话，左边侧栏的链接也会被选中，变成黄色，然后我们点击左边黄色的链接。变成红色后。  
可以发现右上角小窗口中的Clear按钮的数字是**150**。  
我们再点击图片（图片也是黄色）。  
右上角小窗口中的Clear按钮的数字是**75**。  
旁边的`p a`就是我们想要的解释式。  
不过，建议大家后面忘了这个使用方法。尽量用肉眼去观察得出解析式，因为不担保每次都可以正确获得解析式。即使是xpath的插件，也不能保证每次的解析式是正确的。  
## 获取书名和链接  
新建一个名为requests_1.py的文件  
`touch requests_1.py`  
写入以下内容：  
```python
import requests   # 导入requests包

# 从bs4中导入 BeautifulSoup （美味的汤） 实例化为bs
# BeautifulSoup太长了
from bs4 import BeautifulSoup as bs


# 把我们要爬取的网址赋值给url这个变量
url = 'https://www.gulongwang.com/'

# 使用requests中的get方法来请求我们的网址
# 采取该方法后会返回一个响应,相当与我们打开网页后会返回页面一样

# 简单来说，我们在浏览器输入一个网址是请求该网站
# 返回会的内容是该网站对我们的请求的响应。
# 响应中包括cookice、网页内容、状态码、header等

response = requests.get(url=url)

# 不知道大家有没有发现，在上面的代码中，我们打印出来的内容的有一大堆乱码
# 这是因为我们没有对其进行转码。
# 通常我们中文使用的编码是 gbk 或者utf-8
# 大多数情况下，见到乱码，把编码切换成另一个即可
# 也可以通过开发者工具进行观察 charset=gb2312  还是 charset=utf-8
# 本次爬取的网页编码是gb2312 其实可以写成gbk
response.encoding = 'gbk'
#response.encoding = 'utf-8'


# 利用BeautifulSoup方法对获取到的文本内容进行解析,解析采取lxml的形式解析
soup = bs(response.text,'lxml')

# 通过bs4的选择器 根据解析式选择内容，得到书名和链接的a标签列表
booklist = soup.select('p a')
# 打印书的a标签列表
print(booklist)

# 逐一打印出书名和链接
for book in booklist:
    booklink = book['href']  # 获取a标签中的href属性
    bookname = book.text     # 获取a标签中的文本信息
    print(bookname,booklink)
```  
## 打开书的链接并获取内容  
在开始前，先讲两个关于爬虫的重点知识  
### header
由于这次爬取的网站相对来说比较简单  
该网站的反爬措施几乎为0。  
但为了程序的可持续爬取。我们需要加上请求头header，来伪装成我们是浏览器访问网页，而不是明目张胆的小爬虫。  
```python
headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
```  
加上上面的这句代码。  
后面再讲怎么应用。  
### 相对路径和绝对路径。  
相信经过运行上一小节的代码，不难发现，我们获取到的**书的链接**，只是一个`/jue`的内容。  
这个是**相对路径**，在我们点击网页时，浏览器会将其在我们的当前网页的网址和相对路径进行拼接。组成`https://www.gulongwang.com/jue`从而使我们可以直接跳转到该地址。  
而**绝对路径**就是说我们获取从a标签到的路径是`https://www.gulongwang.com/jue`这种形式的链接。  
总的来说，本次爬取需要我们对这个链接进行字符拼接操作。  
### 写代码  
新建一个名为requests_2.py的文件  
`touch requests_2.py`  
写入以下内容，详情看注释：
```python
import requests   # 导入requests包

# 从bs4中导入 BeautifulSoup （美味的汤） 实例化为bs
# BeautifulSoup太长了
from bs4 import BeautifulSoup as bs


# 把我们要爬取的网址赋值给url这个变量
url = 'https://www.gulongwang.com'

# 请求头 里面是我们谷歌浏览器的请求头
headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
# 使用requests中的get方法来请求我们的网址
# 采取该方法后会返回一个响应,相当与我们打开网页后会返回页面一样

# 简单来说，我们在浏览器输入一个网址是请求该网站
# 返回会的内容是该网站对我们的请求的响应。
# 响应中包括cookice、网页内容、状态码、header等


# 加上我们的请求头后 再去请求该网址
response = requests.get(url=url,headers=headers)

# 不知道大家有没有发现，在上面的代码中，我们打印出来的内容的有一大堆乱码
# 这是因为我们没有对其进行转码。
# 通常我们中文使用的编码是 gbk 或者utf-8
# 总之见到乱码，把编码切换成另一个即可
# 也可以通过开发者工具进行观察 charset=gb2312  还是 charset=utf-8
# 本次爬取的网页编码是gb2312 其实可以写成gbk
response.encoding = 'gbk'
#response.encoding = 'utf-8'


# 利用BeautifulSoup方法对获取到的文本内容进行解析,解析采取lxml的形式解析
soup = bs(response.text,'lxml')

# 通过bs4的选择器 根据解析式选择内容，得到书名和链接的a标签列表
booklist = soup.select('p a')
# 打印书的a标签列表
print(booklist)

# 逐一打印出书的章节列表页的内容
for book in booklist:
    booklink = url + book['href']  # 获取a标签中的href属性
    bookname = book.text     # 获取a标签中的文本信息
    response = requests.get(url=booklink,headers=headers)
    response.encoding = 'gbk'
    print(response.text)

```     
### 函数化编程  
大家有没有发现，其实上面的代码很多都是相似的。  
特别是我们每一次都需要去使用打开网页的这个方面的代码。  
所以，重复的内容统统使用函数来解决。如下：
新建一个名为requests_3.py的文件  
`touch requests_3.py`
```python
import requests     # requests是python的一个轻量级爬虫框架
from bs4 import BeautifulSoup as bs  # BeautifulSoup这个名字太长了，简写成bs


# 打开网页函数
def get_response(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    response = requests.get(url, headers)
    #response.encoding = 'utf-8'
    response.encoding = 'gbk'
    return response

# 主函数
def main():
    url = 'https://www.gulongwang.com'
    response = get_response(url)
    # 利用BeautifulSoup方法对获取到的文本内容进行解析,解析采取lxml的形式解析
    soup = bs(response.text,'lxml')

    # 逐一打印出书的章节列表页的内容
    for book in soup.select('p a'):
        booklink = url + book['href']  # 获取a标签中的href属性
        bookname = book.text     # 获取a标签中的文本信息
        print(bookname,booklink)

    # 当.py文件运行时，在if __name__ == "__main__":下的的代码将会运行
    # 当该文件被当成模块运行时，if __name__ == "__main__":下的代码不会被运行
if __name__ == "__main__":
    main()

```  
再次观察该网页结构，并根据我们一开始的决定的需求，来分析我们需要获取的数据。  
得出的结论如下：  
- 书名   （用于生成文件名）
- 书的链接 （用于和后续的章节链接进行拼接使用）
- 章节名  （用于生成每个章节的内容的开头）
- 章节链接 （用于打开页面获取小说每一章节的正文内容）  
- 小说正文  （不拿内容你看什么？）  

同时，发现**首页**和**章节列表页**结构几乎一样，只是他们的解析式不一样。  
采取**传参函数**来优化代码量。  
这是因为我们在首页和章节列表页都是获取**a标签中的链接和文本**。  
所以我们后续的代码采取python的**字典**和**生成器**来传输内容。  
改写后代码如下：
```python
import requests     # requests是python的一个轻量级爬虫框架
from bs4 import BeautifulSoup as bs  # BeautifulSoup这个名字太长了，简写成bs


# 打开网页函数
def get_response(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    response = requests.get(url, headers)
    #response.encoding = 'utf-8'
    response.encoding = 'gbk'
    return response

# 获取网页中a标签中的文本和链接信息
# 参数说明（顺序对应下面的参数位置）：
# 需要解析的url、解析式、链接的键名、文本信息的键名、传入的字典
def get_text_and_link(url,req,link_name,text_name,items):
    response = get_response(url)
    soup = bs(response.text, 'lxml')
    #print(len(soup.select(req)))
    for item in soup.select(req):
        # 由于获取到的链接是相对路径，故此需要进行url拼接组成链接
        items[link_name] = url + item['href']
        items[text_name] = item.text
        yield items



# 主函数
def main():
    # 根url 根网址
    base_url = 'https://www.gulongwang.com'
    # 生成一个空字典，来接收内容
    items = {}
    # 获取书名的列表
    # 第一次从首页获取书的书名和书的链接
    # 函数传入的参数 首页的地址、解析式、赋予书的链接名的键名、赋予书名的键名、字典
    book_links = get_text_and_link(base_url,'p a','book_link','book_name',items)
    # 从书名的列表逐一获取出每一本书的书名和书的链接
    for item in book_links:
        # 第二次获取书的章节名和小说的正文链接
        # 函数传入的参数有、书的链接、章节列表的解析式、章节链接的键名、章节的名字、字典
        chapter = get_text_and_link(item['book_link'],'#right li a','chapter_link','chapter_name',items)
        for item in chapter:
            # 打印每一章节的章节名和章节链接
            print(item['chapter_name'],item['chapter_link'])

    # 当.py文件运行时，在if __name__ == "__main__":下的的代码将会运行
    # 当该文件被当成模块运行时，if __name__ == "__main__":下的代码不会被运行
if __name__ == "__main__":
    main()
```  
通过上面的这段代码，我们已经把该网站的所有小说章节的正文内容链接的链接获取下来。  
剩下的就是把正文内容保存成txt档案。  
这些内容留到下一章节再讲。
