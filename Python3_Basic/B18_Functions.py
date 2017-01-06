# http://www.runoob.com/python/python-functions.html
# Python 函数

# --------------------------------------------------
# 定义函数
def print_me(str):
    "打印传入的字符串到标准显示器上"
    print(str)
    return
# 调用函数
print_me("我要调用用户自定义函数！")
print_me("再次调用同一函数")
print()

# --------------------------------------------------
# 可写函数说明
def change_me(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print("函数内取值：", mylist)
    return
# 调用change_me函数
mylist = [10,20,30]
change_me(mylist)
print("函数外取值:", mylist)
print()
# --------------------------------------------------

# 参数
#     必备参数
#     关键字参数
#     默认参数
#     不定长参数
# --------------------------------------------------
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
# 调用printme函数
#printme()
#TypeError: printme() missing 1 required positional argument: 'str'
# --------------------------------------------------
# 调用printme函数
printme(str = "My String")
print()
# --------------------------------------------------
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name:",name)
    print("Age:",age)
    return
# 调用 printinfo 函数
printinfo(age = 50, name="miki")
print()
# --------------------------------------------------
def print_info(name, age=35):
    "打印任何传入的字符串"
    print("Name:",name)
    print("Age:",age)
    return
print_info(age = 50, name="miki")
print_info(name="miki")
# --------------------------------------------------
#     不定长参数
print("#    不定长参数")
def print_info_2(arg1, *var_tuple):
    "打印任何传入的参数"
    print("输出")
    print(arg1)
    for var in var_tuple:
        print(var, end=" ")
    return
print_info_2(10)
print_info_2(70, 60, 50)

# --------------------------------------------------
# 匿名函数
print("# 匿名函数")
#可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
#调用sum函数
print("相加后的值为：",sum(10,20))
print("相加后的值为：",sum(20,20))
print()

# ---------------------------------------------------
# return 语句
print("# return 语句")
#可写函数说明

#调用sum函数