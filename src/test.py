import CharacterRomanizationList
import CharacterSChineseDic
import time
import xlwt

wb = xlwt.Workbook()
# 添加一个表
ws = wb.add_sheet('test')
# 3个参数分别为行号，列号，和内容
# 需要注意的是行号和列号都是从0开始的
ws.write(0, 0, 'Charactier')
ws.write(0, 1, 'Num')
list1 = CharacterRomanizationList.characterRomanizationList
dict1 = CharacterSChineseDic.characterSChineseDic
i = 0
while i < len(list1):
    print("序号：%s   值：%s" % (i + 1, dict1[list1[i]]))
    # ws.write(i + 1, 0, dict1[list1[i]])
    # time.sleep(2)
wb.save('test.xls')
