# http://www.runoob.com/python/python-modules.html


# 命名空间和作用域
Money = 2000
def AddMoney():
    global Money
    Money = Money + 1

print(Money)
AddMoney()
print(Money)

# dir() 函数
import math
content = dir(math)
print(content)

# Python中的包