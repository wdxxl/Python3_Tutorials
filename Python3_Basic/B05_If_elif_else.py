# Python 条件语句
# Chinese http://www.runoob.com/python/python-if-statement.html

# if 基本用法
print("# if 基本用法")
flag = False
name = 'luren'
if name == 'python':
    flag = True
    print('Welcome Boss')
else:
    print(name)
print()

# elif 用法
print("# elif 用法")
num = 5
if num == 3:            # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:                   # 条件均不成立时输出
    print('roadman')

print()

# if语句多个条件
print("# if语句多个条件")
num = 9
if num >=0 and num <=10:
    print('hello')

num = 10
if num < 0 and num > 10:
    print('hello')
else:
    print("undefine")

num = 8
if (num >= 0 and num <=5) or (num >=10 and num<=15):
    print('hello')
else:
    print("undefine")
print()

# if 简单语句组
print("# if 简单语句组")
var = 100
if(var == 100): print("变量var的值为100")
print("good bye!")

