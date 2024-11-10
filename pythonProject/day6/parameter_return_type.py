# 定义一个函数：输入账号（字符串）和密码（整数），返回值：列表（字典）账号和密码

def login(username:str, password:int) -> list:
    return [username, password]

# 根据指定类型传递实参
print(login("天秋", 1887623)) # ['天秋', 1887623]

# 不按照指定类型传递实参
print(login(123, "666")) # 程序不会报错，但是会警告. [123, '666']
