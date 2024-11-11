# 使用内建函数open()
file_1 = open("ryans.txt", "r", encoding="utf-8")
# # 一次性读取文件的所有内容read()
# content = file_1.read()
# print(content)
# print(type(content))  # <class 'str'>

# 一次性读取所有的内容，但是一行一行的读取方式，返回一个列表，每一个元素是每一行内容
# print(file_1.readlines())
# print(len(file_1.readlines()))
# content_list = file_1.readlines()
# list1 = []
# for i in content_list:
#     list1.append(i.strip())
# else:
#     print(list1)

# 每次读取一行的内容
print(file_1.readline())
print(file_1.readline())
print(file_1.readline())

file_1.close()