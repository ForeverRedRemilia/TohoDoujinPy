# 浏览器请求头信息
headers = {
    "Host": "exhentai.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    #"Referer": "https://exhentai.org/?f_cats=761&f_search=parody%3Atouhou_project+character%3AMarisa_Kirisame&advsearch=1&f_sname=on&f_stags=on&f_sh=on&f_spf=&f_spt=",
    "Referer": "",
    "Cookie": "ipb_member_id=1838963; ipb_pass_hash=4620a8f43eedbf611ef866f0ced267d4; igneous=af81e450f; sk=547jkxp2r2bpsm401qza9k0rkajc; u=1838963-0-539k0n29hm9",
    "Upgrade-Insecure-Requests": "1"
}

# 代理设置
proxy = '127.0.0.1:10809'  # 本地代理
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

# 暂停时间设置
# 左闭区间（单位秒)
lTime = 3
# 右闭区间（单位秒）
rTime = 6
