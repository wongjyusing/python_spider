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

# 逐一打印出书名和链接
for book in booklist:
    booklink = book['href']  # 获取a标签中的href属性
    bookname = book.text     # 获取a标签中的文本信息
    print(bookname,booklink)
