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
