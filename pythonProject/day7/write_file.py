# # 打开一个文件如果直接使用open内建函数，需要手动调用close关闭文件
# # 那么使用with上下文管理器就可以不需要手动关闭文件
# with open("ryans2.txt", "w", encoding="utf-8") as file2:
#     file2.write("qwer\nasdf\nzxcv")
#
# # 当使用w写入的模式打开文件的时候，如果文件不存在，那么会新建文件
# # 如果文件存在，会覆盖原来的内容
# with open("ryans2.txt", "w", encoding="utf-8") as file2:
#     file2.write("hahaha")
#
# # 当使用r读取的模式打开文件的时候，如果文件不存在，那么程序会报错
# # 当使用r读取的模式，默认可以不传递实参r
# with open("ryans3.txt", "r", encoding="utf-8") as file2:
#     file2.read() # FileNotFoundError: [Errno 2] No such file or directory: 'ryans3.txt'

with open("/Users/ryanshang/dev/seleniumstudy/seleniumstudy/pom.xml", "rb") as file2:
    print(file2.read())