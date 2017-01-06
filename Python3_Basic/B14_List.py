# http://www.runoob.com/python/python-lists.html

# 访问列表中的值
print("# 访问列表中的值")
list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,7]

print("list1[0] :",list1[0])
print("list2[1:5] :",list2[1:5])
print()

# 更新列表
print("# 更新列表")
list3 = ['physics','chemistry',1997,2000]
print("Value available at index 2:", list3[2])
list3[2] = 2001
print("New Value available at index 2:", list3[2])
print()

# 删除列表元素
print("# 删除列表元素")
list4 = ['physics','chemistry',1997,2000]
print(list4)
del list4[2]
print("After Deleting Value at index 2:", list4)
print()

# Python列表脚本操作符
print("# Python列表脚本操作符")
print(len([1,2,3]))
print([1,2,3]+[4,5,6])
print(["Hi!"]*4)
print(3 in [1,2,3])
for x in [1,2,3]:print(x, end=" ")
print()
print()

# Python列表截取
print("# Python列表截取")
L = ['spam','Spam','SPAM!']
print(L[2])
print(L[-2])
print(L[1:])
print()

# Python列表函数&方法
print("# Python列表函数&方法")
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [1,3,2]

print(len(list1))
print(max(list3))
print(min(list3))
aTuple = (123,'xyz','zara','abc')
alist = list(aTuple)
print(aTuple)
print(alist)

list1.append(4)
print(list1)
print("list1 中数字4 出现的次数：",list1.count(4))
list1.extend(list2)
print(list1)
print(list1.index(4))
list1.insert(4,7)
print(list1)

print(list1.pop())
print(list1)

list1.remove(3)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)
