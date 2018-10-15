import requests
import re
import json
import pandas
# 打开网页函数
def get_response(url,commodity,today_time):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'cookie': 'xxxx',# cookie就不提供了，注意里面的 isg 参数  （需要你点击搜索栏后才会显示真正的参数）
        }
    params = {
        'q': commodity,
        'imgfile': {
                    'js': '1',
                    },
        'stats_click': {
            'search_radio_all':'1',
            'initiative_id': f'staobaoz_{ today_time }', # 注意这里需要修改一下时间
            'ie': 'utf8',
                }
            }
    response = requests.get(url, headers=headers,params=params) # 加上浏览器头，以防被禁
    response.encoding = 'utf-8'      # 指定编码格式
    #response.encoding = 'gbk'      # 指定编码格式
    return response
    #OPlCFG6GXQsCAdoP6nmnEljY
def main():
    # 搜索的商品名
    commodity = 'python书籍'
    # 填写 20181009 类型的时间格式
    today_time = '20181010'
    base_url = f'https://s.taobao.com/search?q={ commodity }&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_{today_time}&ie=utf8'
    print(base_url)
    response = get_response(base_url,commodity,today_time)
    print(response.text)
    req = 'g_page_config = (.*?)g_srp_loadCss'

    items_list = re.findall(req,response.text,re.S)[0].strip()

    js = json.loads(items_list[:-1])
    jd = js['mods']['itemlist']['data']['auctions'] #.keys())
    df = pandas.DataFrame(jd)
    df[['category','raw_title','view_price','item_loc','view_sales']].to_html(f'{commodity}.html')



if __name__ == "__main__":
    main()
