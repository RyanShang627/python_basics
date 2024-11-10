# 猜测汽车的价格，输出对应的称呼
price = eval(input("请输入小米su7的价格: "))
if price == 9.9:
    print("雷神")
elif price == 14.9:
    print("雷总")
elif price == 19.9:
    print("雷子")
elif price == 29.9:
    print("老雷")
else:
    print("输入的价格不在猜测范围之内")