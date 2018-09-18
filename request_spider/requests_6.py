import requests
import re
import json
import pandas
# 打开网页函数
def get_response(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
    response = requests.get(url, headers) # 加上浏览器头，以防被禁
    response.encoding = 'utf-8'      # 指定编码格式
    #response.encoding = 'gbk'      # 指定编码格式
    return response

def main():
    # 搜索的商品名
    commodity = '火鸡面'
    # 拼接url 生成商品搜索页
    base_url = f'https://s.taobao.com/search?q={ commodity }'
    # 打开该url获取内容
    response = get_response(base_url)
    # 由于 淘宝的数据是在 网页源代码中的第8个script语句中的第一段json数据中
    # 正常的话无法通过bs4、xpath等方式解析。
    # 只能通过正则来获取数据
    req = 'g_page_config = (.*?)g_srp_loadCss'
    # 由于re.findall方法获取到的是一个列表，所以需要取第一个元素，并把字符中的空格去掉
    items_list = re.findall(req,response.text,re.S)[0].strip()
    # items_list是一个字符串，由于结尾有个;  不符合json的格式要求，去掉它
    # 使用json中的load方法，转换成pyhton可操作的字典类型
    js = json.loads(items_list[:-1])
    jd = js['mods']['itemlist']['data']['auctions'] #.keys())
    # 使用pandas的数据呈现方法转化之前处理过的数据
    df = pandas.DataFrame(jd)
    # 在下面逐一输入键名进行观察需要的数据。用浏览器打开当前文件,进行筛选
    # 筛选完成后生成一个txt文件
    df[['category','raw_title','view_price','item_loc','view_sales']].to_html(f'{commodity}.html')






# 你这个问题结合这个文件来说吧
# 当你运行这个文件时，只会执行在if __name__ == "__main__":下面的main（）函数
# 当这个文件被作为模块调用时，则不会执行下面的main（）函数


if __name__ == "__main__":
    main()
