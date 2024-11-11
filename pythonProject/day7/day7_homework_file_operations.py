"""
练习文件操作：创建/读取/修改/重命名/删除文件以及文件夹
"""
import os
import shutil
# 创建一个文件夹
os.mkdir("homework_os")

# 在"homework_os"文件夹下面创建若干文件
# 注意：如果这个目录文件夹不存在，则创建文件会失败
with open("./homework_os/a.txt", "w", encoding="utf-8") as file_a:
    file_a.write("This is file a. This is a text file.")
with open("./homework_os/b.md", "w", encoding="utf-8") as file_b:
    file_b.write("This is file b. This is a markdown file.")
with open("./homework_os/c.xml", "w", encoding="utf-8") as file_c:
    file_c.write("This is file c. This is a xml file.")
#
# # 重命名
# os.rename("./homework_os/a.txt", "./homework_os/a1.txt")
# # 复制
# os.
# # 获取当前我所在的模块的目录的路径信息
cur_dir = os.getcwd()
print(f"current directory is: {cur_dir}") # /Users/ryanshang/Dev/mashang/python_study/python_basics/pythonProject/day7
# # 删除文件夹
# os.rmdir("123")
# 作业：
# 删除一个有内容的文件夹： homework_os，必须先删除文件夹里面的内容文件，才能删除空文件
# 获取文件夹的列表文件
# file_list = os.listdir("homework_os")
# print(f"file list is {file_list}")
# # 返回的数据内容格式列表，可以通过遍历列表获取每个文件的名字+路径信息，进行remove删除
# for file in file_list:
#     # 注意：文件名只要不在当前目录，都需要加入路径信息，才能定位操作
#     os.remove(cur_dir + "/homework_os/" + file)
# else:
#     os.rmdir("homework_os")
shutil.rmtree("homework_os")
# 删除文件
# os.remove("ryans_new_name.txt")

