# 导入拷贝模块
import copy

# 准备一个数据：使用字典对应的值分别是可变和不可变的类型
dict1 = {'list_num': [1, 2, 3], 'num': 666}

print(dict1)

# 对字典进行浅拷贝
new_dict = copy.copy(dict1)
print(new_dict)
print('*' * 100)
# 字典浅拷贝完成之后，对原来数据进行修改之后，被浅拷贝的数据也发生修改
# 结论：对于可变的数据类型使用浅拷贝无效
dict1['list_num'].append(4)
print(dict1)
print(new_dict)
print('*' * 100)

# 对字典进行深拷贝
new_dict = copy.deepcopy(dict1)
print(new_dict)
print('*' * 100)
# 结论：对于可变的数据类型使用深拷贝,可以保证数据独立
dict1['list_num'].append(4)
print(dict1)
print(new_dict)