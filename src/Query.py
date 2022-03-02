import requests
from lxml import etree
import random
import time
import datetime
import xlwt
import CharacterRomanizationList
import CharacterSChineseDic
import Config

# 注入罗马音List
rmList = CharacterRomanizationList.characterRomanizationList
# 注入简体中文字典
scDic = CharacterSChineseDic.characterSChineseDic
# 注入浏览器请求头部
headers = Config.headers
# 注入代理（如不需要可以去掉）
proxies = Config.proxies
# 注入暂停时间（用于反反爬虫机制）
lTime = Config.lTime
rTime = Config.rTime

i = 0
length = len(rmList)
# 创建人物——数量Dict，用于排序输出
characterNumDict = {}
# 存放出现过的数量值是否被用到
vlDic = {}
# 存放出现过的数量值的次数
vlCount = {}
while i < length:
    curCharacter = rmList[i]
    scCharacter = scDic[curCharacter]
    # 选好要查询的条件，点击查询，copy地址栏中的url，根据需求更改url，推荐选择Doujinshi、Manga、Non-H三个标签
    url = "https://.org/?f_cats=761&f_search=parody%3Atouhou_project+character%3A" + curCharacter + "&advsearch=1&f_sname=on&f_stags=on&f_sh=on&f_spf=&f_spt="
    # 更新请求头部中的Referer
    headers['Referer'] = url
    html = requests.get(url, headers=headers, proxies=proxies)
    etree_html = etree.HTML(html.text)
    content = etree_html.xpath('/html/body/div[2]/div[2]/p/text()')
    for each in content:
        each = each.replace('Showing ', '').replace(',', '').replace('results', '').replace(' ', '') \
            .replace('result', '')
        print(scCharacter + " : " + each)
        if each is None or each == '':
            print("连接丢失，即将重连...")
            i -= 1
        else:
            characterNumDict[curCharacter] = int(each)
            vlDic[each] = 'false'
            if each in vlCount.keys():
                vlCount[each] = vlCount[each] + 1
            else:
                vlCount[each] = 1
    # 随机暂停时间（秒）
    suspendTime = random.randint(lTime, rTime)
    print("随机暂停时间：%s秒，进度%s/%s" % (suspendTime, i + 1, length))
    time.sleep(suspendTime)
    i += 1
dictList = sorted(characterNumDict.items(), key=lambda d: d[1], reverse=False)

# 创建excel表格
wb = xlwt.Workbook()
ws = wb.add_sheet('Query')
ws.write(0, 0, 'name')
ws.write(0, 1, 'type')
ws.write(0, 2, 'value')
ws.write(0, 3, 'date')
# name的初始值
j = 0
# 单条数据的行数
cul = 0
# 初始化增加的天数
day = 0
# 排名
rank = len(vlCount) + 1
for key, value in dictList:
    j += 1
    curVl = vlDic[str(value)]
    if curVl == 'false':
        # 记录最早出现该值的排名
        vlDic[str(value)] = 'true'
        rank -= 1
        day += 1
    # 天数
    x = 0
    while cul < j * 20:
        cul += 1
        ws.write(cul, 0, scDic[key])
        ws.write(cul, 1, rank)
        ws.write(cul, 2, value)
        nowTime = (datetime.datetime.now() + datetime.timedelta(days=x + day)).strftime("%Y-%m-%d")
        ws.write(cul, 3, nowTime)
        x += 1
wb.save('result.xls')
