import dataclasses

@dataclasses.dataclass
class Girl:
    # 定义数据类的实例属性必须要指定数据类型
    age = 18
    name = "刘亦菲"

    def show(self):
        print("开始表演节目")

g1 = Girl()
print(g1.name)
print(g1.age)

print(type(g1.name)) # 查看属性的值对应的数据类型
print(Girl.name)
print(Girl.age)