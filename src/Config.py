# 以下示例是用 Firefox 79 访问得到的请求头信息，可直接从浏览器控制台——网络中截取
headers = {
    "Host": "exhentai.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    # Referer与url一致即可
    "Referer": "",
    # Cookie是核心参数一定要有
    "Cookie": "",
    "Upgrade-Insecure-Requests": "1"
}

# 代理设置
proxy = '127.0.0.1:10809'  # 本地代理 可以更换成自己的
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

# 暂停时间设置
# 左闭区间（单位秒)
lTime = 3
# 右闭区间（单位秒）
rTime = 6
