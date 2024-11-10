# 输入对应的姓氏，匹配排名
name = input("请输入你的姓氏: ")

match name:
    case "李":
        print("您的姓氏排行第一")
    case "王":
        print("您的姓氏排行第二十六")
    case "张":
        print("您的姓氏排行第七十")
    case "雷":
        print("您的姓氏排行第八")