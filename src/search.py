import requests
from lxml import etree

cookie = {
    #"ipb_member_id": "1838963",
    #"ipb_pass_hash": "4620a8f43eedbf611ef866f0ced267d4"
    # "igneous": "af81e450f"
}

proxy = '127.0.0.1:10809'  # 本地代理
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
html = requests.get("https://exhentai.org/?f_cats=761&f_search=remilia", cookies=cookie, proxies=proxies)
# print(html.text)
etree_html = etree.HTML(html.text)
content = etree_html.xpath('/html/body/div[2]/div[2]/p/text()')
for each in content:
    each = each.replace('Showing ', '').replace(',', '').replace('results', '')
    print(each)
