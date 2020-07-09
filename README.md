# TohoDoujinPy
# 成果展示：https://www.bilibili.com/video/bv1QV41167jp
该项目为数据后端（爬虫端），数据前端我使用的是Jannchie的开源可视化项目，在github上也能找到

拉到Pycharm下即可，需要把pyvenv.cfg中的home改为你自己本机的python目录

在Config.py中有浏览器请求头信息的说明，需要先登录表站才能拿到Cookie。

Cookie是必备的！！其他头部信息越完整被反爬的概率就越小，如果请求头只有Cookie的话爬两下你的IP就会面临1~24小时的封锁

部分人物因为一个结果都没有所以被注释，减少防反爬等待时间

会在将来的版本中加入网络异常处理的机制
