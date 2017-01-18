# https://segmentfault.com/a/1190000007214571
# Python语法糖——遍历列表时删除元素

# 错误1
lst = [1,1,0,2,0,0,8,3,0,2,5,0,2,6]
for item in lst:
    if item == 0:
        lst.remove(item)
print(lst)
# [1, 1, 2, 8, 3, 2, 5, 0, 2, 6]

# 错误2
# for item in range(len(lst)):
#     if lst[item] == 0: # IndexError: list index out of range
#         del lst[item]
# print(lst)

lst = [1,1,0,2,0,0,8,3,0,2,5,0,2,6]
# 方法1 == Filter
lst1 = filter(lambda x: x!=0, lst)
print(list(lst1)) # <filter object at 0x1022443c8>

# 方法2 == 列表解析
lst2 = [x for x in lst if x != 0]
print(lst2)

# 方法3 == 遍历拷贝的list，操作原始的list
for item in lst[:]:
    if item == 0:
        lst.remove(item)
print(lst)


# 方法4 == 用while循环来搞定，每次循环都会判断0 是否在列表中
lst = [1,1,0,2,0,0,8,3,0,2,5,0,2,6]
while 0 in lst:
    lst.remove(0)
print(lst)

# 方法5 ==  倒序循环遍历
lst = [1,1,0,2,0,0,8,3,0,2,5,0,2,6]
for item in range(len(lst)-1, -1, -1):
    if lst[item] == 0:
        del lst[item]
print(lst)

# 推荐使用Filter
