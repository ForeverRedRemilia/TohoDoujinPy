import CharacterRomanizationList
import time

list1 = CharacterRomanizationList.characterRomanizationList
for i in range(len(list1)):
    print("序号：%s   值：%s" % (i+1, list1[i]))
    time.sleep(2)
