# 使用while和for循环分别输出1 2 4 5 6 8 10

list1 = [1, 2, 4, 5, 6, 8, 10]

# for循环输出
for num in list1:
    print(num, end=' ')
else:
    print('\n成功用for循环遍历列表')

# while循环输出
i = 0
while i < len(list1):
    print(list1[i], end=' ')
    i += 1
else:
    print('\n成功用while循环遍历列表')