# 获取内容并保存  
其实这个内容要分为两个函数来解决，因为要保持代码的**可复用性**  
效果最后会讲到。   
注意，本次代码和上次的代码有一定的区别。   
获取正文函数：
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
# 根路径（需要和相对路径进行拼接），需要解析的url、解析式、链接的键名、文本信息的键名、传入的字典
def get_text_and_link(base_url,url,req,link_name,text_name,items):
    response = get_response(url)
    soup = bs(response.text, 'lxml')
    #print(len(soup.select(req)))
    for item in soup.select(req):
        # 由于获取到的链接是相对路径，故此需要进行url拼接组成链接
        items[link_name] = base_url + item['href']
        items[text_name] = item.text
        yield items

# 获取内容函数
def get_content(url,req_start,req_end,items):
    response = get_response(url)

    # 把获取到的文本信息用html的解析器解析
    soup = bs(response.text, 'html.parser')
    # 通过传入的解析式解析小说正文，这里的写法最好用肉眼观察
    # 这里有两个解析式，是因为获取一大段内容需要 开始 和 结束 标记

    content = soup.find(req_start,class_=req_end).strings
    # 把书名、章节名、小说正文内容传入writeFile函数进行保存
    writeFile(items['book_name'],items['chapter_name'],content)

# 保存文件函数
def writeFile(book_name,title,content):
    # 把书名后面加上.txt保证文件是txt类型文件
    # 写入方式是 a 添加写法   w是覆盖写法  编码格式是utf-8
    with open(book_name + '.txt','a',encoding='utf-8')as txt_file:
        #设置文件编码，避免写入时乱码
        # 每一次写入章节名时进行换行
        txt_file.write('\n'+title+'\n')
        for line in content:
            #content是一个生成器，采用for循环逐次写入文件
            txt_file.write(line)
    print(f'{ title } 写入到{ book_name }.txt 完成')

# 主函数
def main():
    # 根url 根网址
    base_url = 'https://www.gulongwang.com'
    # 生成一个空字典，来接收内容
    items = {}
    # 获取书名的列表
    # 第一次从首页获取书的书名和书的链接
    # 函数传入的参数 根路径，首页的地址、解析式、赋予书的链接名的键名、赋予书名的键名、字典
    book_links = get_text_and_link(base_url,base_url,'p a','book_link','book_name',items)
    # 从书名的列表逐一获取出每一本书的书名和书的链接
    for item in book_links:
        # 第二次获取书的章节名和小说的正文链接
        # 函数传入的参数有跟路径、书的链接、章节列表的解析式、章节链接的键名、章节的名字、字典
        chapter = get_text_and_link(base_url,item['book_link'],'#right li a','chapter_link','chapter_name',items)
        for item in chapter:
            # 打印每一章节的章节名和章节链接
            get_content(item['chapter_link'],'div','nr_con',items)

    # 当.py文件运行时，在if __name__ == "__main__":下的的代码将会运行
    # 当该文件被当成模块运行时，if __name__ == "__main__":下的代码不会被运行
if __name__ == "__main__":
    main()
```
有没有觉得上面的函数传入的参数太多了呢？？  
的确很多，有56个参数。看得眼睛都疼。  
这种写法是为了什么呢？之前的可复用性在哪里呢？？  
再改写一次，代码如下：
```python
import requests     # requests是python的一个轻量级爬虫框架
from bs4 import BeautifulSoup as bs  # BeautifulSoup这个名字太长了，简写成bs

# 编码方式 通常情况下 二选一即可
# coding = 'utf-8'
coding = 'gbk'

# 根路径
base_url = 'https://www.gulongwang.com'

# 首页解析式
base_req = 'p a'

# 章节列表页解析式
chapter_req = '#right li a'

# 内容页开始解析式
req_start = 'div'

# 内容页结束解析式
req_end = 'nr_con'

# 是否为相对路径 是则填写True 不是填写 False

Yes = True
# Yes = False


# 打开网页函数
def get_response(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    response = requests.get(url, headers)
    #response.encoding = 'utf-8'
    response.encoding = coding
    return response

# 获取网页中a标签中的文本和链接信息
# 参数说明（顺序对应下面的参数位置）：
# 根路径（需要和相对路径进行拼接），需要解析的url、解析式、链接的键名、文本信息的键名、传入的字典
def get_text_and_link(base_url,url,req,link_name,text_name,items):
    response = get_response(url)
    soup = bs(response.text, 'lxml')
    #print(len(soup.select(req)))
    for item in soup.select(req):
        # 由于获取到的链接是相对路径，故此需要进行url拼接组成链接
        items[link_name] = base_url + item['href']
        items[text_name] = item.text
        yield items

# 绝对路径获取函数
def get_text_and_link_absolute(url,req,link_name,text_name,items):
    response = get_response(url)
    soup = bs(response.text, 'lxml')
    #print(len(soup.select(req)))
    for item in soup.select(req):
        # 由于获取到的链接是绝对路径，故此需要进行url拼接组成链接
        items[link_name] = item['href']
        items[text_name] = item.text
        yield items

# 获取内容函数
def get_content(url,req_start,req_end,items):
    response = get_response(url)

    # 把获取到的文本信息用html的解析器解析
    soup = bs(response.text, 'html.parser')
    # 通过传入的解析式解析小说正文，这里的写法最好用肉眼观察
    # 这里有两个解析式，是因为获取一大段内容需要 开始 和 结束 标记

    content = soup.find(req_start,class_=req_end).strings
    # 把书名、章节名、小说正文内容传入writeFile函数进行保存
    writeFile(items['book_name'],items['chapter_name'],content)

# 保存文件函数
def writeFile(book_name,title,content):
    # 把书名后面加上.txt保证文件是txt类型文件
    # 写入方式是 a 添加写法   w是覆盖写法  编码格式是utf-8
    with open(f'{book_name}.txt','a',encoding='utf-8')as txt_file:
        #设置文件编码，避免写入时乱码
        # 每一次写入章节名时进行换行
        txt_file.write('\n'+title+'\n')
        for line in content:
            #content是一个生成器，采用for循环逐次写入文件
            txt_file.write(line)
    print(f'{ title } 写入到《{ book_name }》.txt 完成')

# 主函数
def main():
    # 根url 根网址

    # 生成一个空字典，来接收内容
    items = {}
    # 获取书名的列表
    # 第一次从首页获取书的书名和书的链接
    # 函数传入的参数 根路径，首页的地址、解析式、赋予书的链接名的键名、赋予书名的键名、字典
    if Yes == True:

        book_links = get_text_and_link(base_url,base_url,base_req,'book_link','book_name',items)
        # 从书名的列表逐一获取出每一本书的书名和书的链接
        for item in book_links:
            # 第二次获取书的章节名和小说的正文链接
            # 函数传入的参数有跟路径、书的链接、章节列表的解析式、章节链接的键名、章节的名字、字典
            chapter = get_text_and_link(base_url,item['book_link'],chapter_req,'chapter_link','chapter_name',items)
            for item in chapter:
                # 打印每一章节的章节名和章节链接
                get_content(item['chapter_link'],'div','nr_con',items)
    else:
        book_links = get_text_and_link_absolute(base_url,base_req,'book_link','book_name',items)
        # 从书名的列表逐一获取出每一本书的书名和书的链接
        for item in book_links:
            # 第二次获取书的章节名和小说的正文链接
            # 函数传入的参数有 书的链接、章节列表的解析式、章节链接的键名、章节的名字、字典
            chapter = get_text_and_link_absolute(item['book_link'],chapter_req,'chapter_link','chapter_name',items)
            for item in chapter:
                # 打印每一章节的章节名和章节链接
                get_content(item['chapter_link'],req_start,req_end,items)

    # 当.py文件运行时，在if __name__ == "__main__":下的的代码将会运行
    # 当该文件被当成模块运行时，if __name__ == "__main__":下的代码不会被运行
if __name__ == "__main__":
    main()
```  
更难看了，对吧？？  
这样写还是为了**可复用性**。  
可复用性体现在哪里呢？？  
我们再找一个网页结构类似的小说网站。（三层结构：首页、章节列表页、小说正文页）   
举个例子，找个金庸的吧。`http://jinyong.zuopinj.com/`  
我们只需要修改上面代码中的网址、解析式、编码格式、是否为相对路径。  
就可以爬取了哟。如下所示：  
```python
# 编码方式 通常情况下 二选一即可
coding = 'utf-8'
#coding = 'gbk'


# 根路径
base_url = 'http://jinyong.zuopinj.com'

# 首页解析式
base_req = '#cols-1 h3 a'

# 章节列表页解析式
chapter_req = '.book_list a'

# 内容页开始解析式
req_start = 'div'

# 内容页结束解析式
req_end = 'contentbox'

# 是否为相对路径 是则填写True 不是填写 False

# Yes = True
Yes = False
```  
这个网站有一点需要注意，有一定的反爬措施，大家设一个休息时间即可。   
每爬取一个网页休息5秒到10秒即可。  
利用time模块的sleep方法。python文档上有写，自己去查。  
还有一点是，在上面的基础上把**base_url**改成`http://liangyusheng.zuopinj.com/`试试。这个网站的大多数作家的小说都可以爬下来哟。  
## 不足之处  
这个爬虫不足之处有以下几点：
- 当发生错误，断电断网后，不能从上一次结束的地方开始爬，只会从头再来。  
- 爬取速度太慢了，这是单进程爬虫，只能打开网页，然后获取玩所有正文内容并保存后才能进行下一个网址的爬取。  

## 进阶方向  
之后我们会采取**scrapy**包进行爬取。它自带有异步处理的方法。爬取速度会提高很大的幅度。  
不过，在介绍scrapy前，继续用requests爬取一个淘宝商品页面来讲一下，网站对爬虫的处理和识别。  
