# 通过使用while循环获取字符串中的每个元素
str1 = "oiuiod2sfudiosf2uysd2iog7w90890"
list1 = []
i = 0
print(len(str1))
while i < len(str1) - 1:
    list1.append(str1[i])
    i += 1
    if str1[i] == '2':
        continue
else:
    print(len(list1))
    print(list1)