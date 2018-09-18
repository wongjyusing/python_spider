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
