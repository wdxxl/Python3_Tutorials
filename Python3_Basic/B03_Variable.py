# 变量赋值
print("# 变量赋值")
counter = 100 #赋值整型变量
miles = 1000.0 #浮点数
name = "Wdxxl" #字符串
print("Counter: %d, Miles: %f, Name: %s" % (counter, miles, name))
print()

# 多个变量赋值
print("# 多个变量赋值")
a = b = c = 1
print("A: %d, B: %d, C: %d" % (a,b,c))
a,b,c = 1,2,"Wdxxl"
print("A: %d, B: %d, C: %s" % (a,b,c))
print()

# Python字符串
print("# Python字符串")
string = "Hello World!"
print(string)              # 输出完整字符串
print(string[0])           # 输出字符串中的第一个字符
print(string[2:5])         # 输出字符串中第三个至第五个之间的字符串
print(string[2:])          # 输出从第三个字符开始的字符串
print(string * 2)          # 输出字符串两次
print(string + "TEST")    # 输出连接的字符串
print()

# Python列表
print("# Python列表")
list = ['runoob', 786, 2.23, 'Wdxxl', 70.2]
tinylist = [123, 'king']
print(list)             # 输出完整列表
print(list[0])          # 输出列表的第一个元素
print(list[-2])         # 输出列表的倒数第二个元素
print(list[1:3])        # 输出第二个至第三个的元素 前闭后开
print(list[2:])         # 输出从第三个开始至列表末尾的所有元素
print(tinylist*2)       # 输出列表两次
print(list + tinylist)  # 打印组合的列表
print()

# Python元组
print("# Python元组 - 元组不能二次赋值，相当于只读列表")
tuple = ('runoob', 786, 2.23, 'Wdxxl', 70.2)
tinytuple = (123, 'king')
print(tuple)              # 输出完整元组
print(tuple[0])           # 输出元组的第一个元素
print(tuple[-2])          # 输出元组的倒数第二个元素
print(tuple[1:3])         # 输出第二个至第三个的元素 前闭后开
print(tuple[2:])          # 输出从第三个开始至列表末尾的所有元素
print(tinytuple*2)        # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组
print()

# Python元组 & 列表赋值 状况
print("# Python元组 & 列表赋值 状况")
tuple2 = ('runoob', 786, 2.23, 'Wdxxl', 70.2)
list2 = ['runoob', 786, 2.23, 'Wdxxl', 70.2]
#tuple2[2] = 1000 # 元组中是非法应用
#TypeError: 'tuple' object does not support item assignment
list2[2] = 1000  # 列表中是合法应用
print()

# Python元字典
print("# Python元字典")
dict ={}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'wdxxl', 'code': 6734, 'dept':'sales'}
print(dict['one'])      # 输出键为'one' 的值
#print(dict['two'])      KeyError: 'two'
print(dict[2])           # 输出键为 2 的值
print(tinydict)          # 输出完整的字典
print(tinydict.keys())   # 输出所有键
print(tinydict.values()) # 输出所有值
print()

# Python数据类型转换
print("# 数据类型转换")
print("#   int 函数能做的")
print("#     1) 把符合数字格式的数字型字符串转换成整数")
print("#     2) 把浮点数转换成整数，但是只是简单的取整，而非四舍五入")
print(int("124"))
print(int(124.56))
print(int(-124.36))
#print(int("124.56")) # ValueError: invalid literal for int() with base 10: '124.56'
#print(int("12a")) #ValueError: invalid literal for int() with base 10: '12a'

print("# 数据类型转换")
print("#   float 函数将整数和字符串转换成浮点数")
print(float("124"))
print(float("123.45"))
print(float("-123.6"))
#print(float("123v")) # ValueError: could not convert string to float: '123v'

print("# 数据类型转换")
print("#   str 函数将数字转成字符")
print(str(124.4))
#print(str(123.a)) #SyntaxError: invalid syntax
print(str("-123.45"))
print(str('ddd'))
print(str(-124.3))

#TODO with others
