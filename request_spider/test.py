import requests     # requests是python的一个轻量级爬虫框架
from bs4 import BeautifulSoup as bs  # BeautifulSoup这个名字太长了，简写成bs

# 打开网页函数
def get_response(url):
    headers = {

'Host': 'www.25xz.com',
'Connection': 'keep-alive',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Referer': 'http://www.25xz.com/player/1.shtml',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'ASP.NET_SessionId=qhgwada3kxhnrckccypdxgah',
        }
    response = requests.get(url, headers)
    response.encoding = 'utf-8'
    #response.encoding = 'gbk'
    return response


def main():
    base_url = 'http://www.25xz.com/ajax/musicList.shtml@1'
    response = get_response(base_url)
    print(response.text)
    #soup = bs(response.text,'lxml')
    #print(soup.select('.play_musicname'))

if __name__ == '__main__':
    main()
