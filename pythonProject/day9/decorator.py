# # 用户进行账号的注册
# # 原来函数定义的功能没有对账号进行验证，现在需要增加额外的功能验证账号长度符合6-12位字符
# # 定义一个装饰器来完成账号长度的验证
# def check(func): # func接收被装饰的函数引用
#     def inner():
#         print("现在开始验证账号长度")
#         func()
#
#     return inner
#
#
# def username():
#     print(f"您输入的账号为: qewqeqr")
#
#
# username = check(username) # 16  ---- 4 ---- 9 ---- 16 username = inner
# username() # username() = inner() 17 --- 5 --- 6 --- 7 --- 12 --- 13 --- 7


# 正常购物流程需要先登录后添加商品到购物车，目前没有登陆也可以直接添加，添加登陆功能之后再购物
def check(func):  # 外面的函数有且只有一个形参，用来接收被装饰函数的引用
    def inner():
        print("开始进入登陆页面")
        print("开始输入账号密码")
        print("验证账号密码中...")
        print("登陆成功")
        print("可以进行正常购物")
        func()
    return inner  # 返回的函数引用千万不要加括号

def shopping():
    print("添加一辆小米su7到购物车")

# 装饰器的调用语法格式
# check执行完成之后：func接收被装饰的函数，返回里面函数的引用
shopping = check(shopping)
shopping()