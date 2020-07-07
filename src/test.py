import requests
from lxml import etree

html = requests.get("https://thwiki.cc/%E5%AE%98%E6%96%B9%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8#.E4.B8.9C.E6.96.B9.E7.81.B5.E5.BC.82.E4.BC.A0")
# print(html.text)
etree_html = etree.HTML(html.text)
content = etree_html.xpath('/html/body/div[3]/div[3]/div[4]/div/div/ul/li/text()')
for each in content:
    each = each.replace('Showing ', '').replace(',', '').replace('results', '')
    print(each)