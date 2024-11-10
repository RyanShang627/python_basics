# # 不可变的数据类型
# str1 = "abc"
# # 使用id()内建函数查看变量的内存地址
# print(hex(id(str1))) # 0x1048e8810
#
# # 修改变量的实际值
# str1 = str1.replace("b", "i")
# print(str1)
# print(hex(id(str1))) # 0x104969380. 实际数据被修改时，内存地址值也发生变化 => 那么就是不可变的数据类型

# # 可变数据类型
# list1 = [1, 2, 3]
# print(list1)
# print(hex(id(list1))) # 0x104feb740
# print("-" * 100)
# list1.append(6)
# print(list1) # [1, 2, 3, 6]
# print(hex(id(list1))) # 0x104feb740 实际数据被修改时，内存地址没变.

dict1 = {1 : 0, "1": 2, (1, 2): 12, [5, 6]: 999}
print(dict1)