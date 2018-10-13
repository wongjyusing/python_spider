# tornado_base
这是tornado项目的基础配置。

# 启动项目
`python server.py`   

# 项目文件
```tree
├── applications.py     # 应用文件，用于添加数据库操作游标
├── config.py           # 项目主体配置，用于改变服务端口和静态模板文件的配置
├── README.md           # 说明书
├── server.py           # 项目启动文件，整合项目中的必要程式
├── static              # 静态文件目录，用于存放css、js、图片
├── templates           # 模板文件目录，用于存放html文件
│   └── home.html       # 演示用的html文件
├── urls.py             # 路由配置，分发路由
└── views               # 视图文件目录，存放视图文件，也可以理解为处理方法
    ├── index.py        # 视图处理逻辑文件，这里用来演示
    └── __init__.py     # 声明views目录是一个python包
```

# 使用方法
下载项目文件。  
`git clone https://github.com/wongjyusing/tornado_base.git`  
然后删除原来的git配置文件，在当前目录下执行下面的代码。   
`find . -name ".git" | xargs rm -Rf`  
重命名该目录,修改下面的new_name为你自己的项目名称。
`cd .. && sudo mv tornado_base/ new_name/`  

# 基于本项目基础开发的项目
[使用torndao作为服务器，tushare作为数据来源，Highcharts（js包）作为绘图工具。绘制股票K线图](https://github.com/wongjyusing/stock_k_line)（施工中)  
