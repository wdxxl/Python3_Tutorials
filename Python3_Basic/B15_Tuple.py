# Python 元组
tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d"
tup4 = ()
tup5 = (50,)
tup6 = (60,)

# 访问元组
print("# 访问元组")
print(tup1[0])
print(tup2[1:4])
print()

# 修改元组
print("# 修改元组")
# tup1[0] = 12 # TypeError: 'tuple' object does not support item assignment
print(tup2 + tup3)

# 删除元组
print("# 删除元组")
print(tup1)
del tup1
# print(tup1) # NameError: name 'tup1' is not defined

# 无关闭分隔符
print("# 无关闭分隔符")
print('abc',-4.24e93, 18+6.6j, 'xyz')
x,y = 1,2
print("Value of x, y", x, y)