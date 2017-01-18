# http://www.runoob.com/python/python-files-io.html

# 打印到屏幕
print("# 打印到屏幕")
print("Python 是一个非常棒的语言，不是吗？")
print()

# 读取键盘输入
# raw_input 这个3.2之后就被废掉了
#   http://stackoverflow.com/questions/10885537/raw-input-has-been-eliminated-from-python-3-2
# input
print("# 读取键盘输入")
str = input("请输入：")
print("你输入的内容是：", str)
print()

# eval(input())
# [x*5 for x in range(2,10,2)]
# [10, 20, 30, 40]
print("# 读取键盘输入")
str = eval(input("请输入："))
print("你输入的内容是：", str)
print()

# File 打开和关闭文件
fo = open("foo.txt", "w+")
print("文件名：", fo.name)
print("是否已关闭：", fo.closed)
print("访问模式：", fo.mode)

counter = fo.write("www.runoob.com!\nVery good site!\n");
print("输入字符数：",counter)
fo.close()
print("是否已关闭：", fo.closed)
print()



fo = open("foo.txt", "r+")
print("文件名：", fo.name)
print("是否已关闭：", fo.closed)
print("访问模式：", fo.mode)
str = fo.read(10)
print("读取的文件内容：",str)
fo.close()
print("是否已关闭：", fo.closed)
print()

# 文件定位
## 打开一个文件
print("# 文件定位")
fo2 = open("foo.txt", "r+")
str2 = fo2.read(16)
print("读取的字符串是：", str2)
## 查找当前位置
position = fo2.tell()
print("当前文件位置：",position)
## 把指针再次重新定位到文件开头
position = fo2.seek(0,0);
str2 = fo2.read(16)
print("读取的字符串是：", str2)
## 关闭打开的文件
fo2.close()
print()

# 文件重命名和删除
import os
## 重命名文件foo.txt 为 foo2.txt
os.rename("foo.txt","foo2.txt")
## 删除一个已经存在的文件foo2.txt
os.remove("foo2.txt")

# 目录
# 创建目录test
os.mkdir("test")
os.rmdir("test")
## 给出当前的目录
import os
print(os.getcwd())
