num1 = eval(input("请输入第一个数字："))
num2 = eval(input("请输入第二个数字："))
# 比较两个数字大小，输出最大值
print(num1 if num1 > num2 else num2)
# else 后面是判断条件不成立的结果