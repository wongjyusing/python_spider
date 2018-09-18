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
