import requests
import re
import json
import pandas
# 打开网页函数
def get_response(url):
    headers = {
        'Host': 'www.stats.gov.cn',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Upgrade-Insecure-Requests': 1,
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',

}
    Cookie = 'AD_RS_COOKIE=20081946; _trs_uv=jmh0xxqq_6_jnbe; _trs_ua_s_1=jmh2f3zr_6_p1q'
    response = requests.get(url, headers) # 加上浏览器头，以防被禁
    response.encoding = 'utf-8'      # 指定编码格式
    #response.encoding = 'gbk'      # 指定编码格式
    return response


def main():
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
    res = get_response(base_url)
    print(res.text)



if __name__ == '__main__':
    main()
