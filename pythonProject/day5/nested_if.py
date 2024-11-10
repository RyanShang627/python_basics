import random
# 要求用户输入一个1,5之间的整数值
# 电脑随机生成一个1,5之间的整数值
# 然后比较大小，输出结果

# 使用random模块调用randint方法生成范围之内的随机整数
computer_num = random.randint(1, 5) # 左闭右闭的区间，包含开始和结束的范围值
# print(computer_num)

user_num = eval(input("请输入一个数字(1-5之间的整数): "))
if 1 <= user_num <= 5:
    print(f"您输入的数值是: {user_num}, 符合范围")
    # 比较大小，输出结果
    if user_num > computer_num:
        print(f"用户输入的值为: {user_num}, 电脑的值: {computer_num}")
        print("用户胜利！")
    elif user_num == computer_num:
        print(f"用户输入的值为: {user_num}, 电脑的值: {computer_num}")
        print("平局！")
    else:
        print(f"用户输入的值为: {user_num}, 电脑的值: {computer_num}")
        print("电脑胜利！")
else:
    print(f"您输入的数值是: {user_num}, 不符合范围")