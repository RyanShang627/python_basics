# and关键字：只有两个条件同时满足最终结果才为真，其他情况都为假
print(1 == 1 and 1 == 2) # False
print(1 == 2 and 1 == 1) # False
print(1 == 3 and 1 == 2) # False
print(1 == 1 and 2 == 2) # True

# or 关键字: 2个条件只有一个满足最终结果都为真，只有两个条件都不满足才为假
print(1 == 1 or 1 == 2) # True
print(1 == 2 or 1 == 1) # True
print(1 == 1 or 2 == 2) # True
print(1 == 3 or 1 == 2) # False

# not 关键字：取反 => 真变假，假变真
print(not 1 == 2) # True
print(not 1 == 1) # False
