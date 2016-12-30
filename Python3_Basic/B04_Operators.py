# 运算符
# English http://www.w3resource.com/python/python-operators.php
# Chinese http://www.runoob.com/python/python-operators.html
print("# 运算符 Python Arithmetic Operators")
x , y = 14, 5
print("Addition: X + Y = %s" %( x + y ))           # Addition: X + Y = 19 	加 - 两个对象相加
print("Subtraction: X - Y = %s" %( x - y ))        # Subtraction: X - Y = 9 减 - 得到负数或是一个数减去另一个数
print("Multiplication: X * Y = %s" %( x * y ))     # Multiplication: X * Y = 70 乘 - 两个数相乘或是返回一个被重复若干次的字符串
print("Division: X / Y = %s" %( x / y ))            # Division: X / Y = 2.8    除 - x除以y
print("Exponent: X ** Y = %s" %( x ** y ))          # Exponent: X ** Y = 537824   幂 - 返回x的y次幂
print("Floor Division: X // Y = %s" %( x // y ))   # Floor Division: X // Y = 2 取整除 - 返回商的整数部分
print("Modulus: X mod Y = %s" %(x % y))                  # Modulus: X % Y = 4 取模 - 返回除法的余数
print()

print("# 比较运算符 Python Comparison Operators")
print("X[%d] == Y[%d] %s" %( x,y,x == y ))          # X[14] == Y[5] False
print("X[%d] != Y[%d] %s" %( x,y, x != y ))         # X[14] != Y[5] True  (Python 3.3 不支持不等于用 <>)
print("X[%d] > Y[%d] %s" %( x,y, x > y ))           # X[14] > Y[5] True
print("X[%d] < Y[%d] %s" %( x,y, x < y ))           # X[14] < Y[5] False
print("X[%d] >= Y[%d] %s" %( x,y, x >= y ))         # X[14] >= Y[5] True
print("X[%d] <= Y[%d] %s" %( x,y, x <= y ))         # X[14] <= Y[5] False
print()

print("# 逻辑运算符 Python Logical Operators")
print("(X>10 AND Y>10) %s" %(x>10 and y>10))            # (X>10 and Y>10) False
print("(X>10 OR Y>10) %s" %(x>10 or y>10))              #(X>10 or Y>10) True
print("NOT (X>10 AND Y>10) %s" %(not(x>10 and y>10))) #not (X>10 and Y>10) True
print()

print("# 赋值运算符 Python Assignment Operators")
x,y=12,7
x+=y; print("X+=Y, X=%s" %(x))
x-=y; print("X-=Y, X=%s" %(x))
x*=y; print("X*=Y, X=%s" %(x))
x/=y; print("X/=Y, X=%s" %(x))
x%=y; print("X%%=Y, X=%s" %(x))
x**=y; print("X**=Y, X=%s" %(x))
x//=y; print("X//=Y, X=%s" %(x))
print()

print("# 位运算符 Python Bitwise Operators")
a = 60          # 60 = 0011 1100
b = 13          # 13 = 0000 1101
print("a = %s [bin = %s], b = %s [bin %s]" %(a, bin(a), b, bin(b))) # a = 60 [bin = 0b111100], b = 13 [bin 0b1101]
#按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print("a & b = %s [bin %s]"%(a&b, bin(a&b))) # a & b = 12 [bin 0b1100]
#按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
print("a | b = %s [bin %s]"%(a|b, bin(a|b))) # a | b = 61 [bin 0b111101]
#按位异或运算符：当两对应的二进位相异时，结果为1
print("a ^ b = %s [bin %s]"%(a^b, bin(a^b))) # a ^ b = 49 [bin 0b110001]
#按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
print("~a = %s [bin %s]"%(~a, bin(~a))) # ~a = -61 [bin -0b111101]
#左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
print("a << 2 = %s [bin %s]"%(a<<2, bin(a<<2))) # a << 2 = 240 [bin 0b11110000]
#右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
print("a >> 2 = %s [bin %s]"%(a>>2, bin(a>>2))) # a >> 2 = 15 [bin 0b1111]
print()

print("# 成员运算符")
a = 10
b = 20
list = [1,2,3,4,5]

if(a in list):
    print("变量a %s 在给定的列表list%s中"%(a,list))
else:
    print("变量a %s 不在给定的列表list %s中"%(a,list))
# 变量a 10 不在给定的列表list [1, 2, 3, 4, 5]中
if(b not in list):
    print("变量b %s 不在给定的列表list%s中"%(b,list))
else:
    print("变量b %s 在给定的列表list %s中"%(b,list))
# 变量b 20 不在给定的列表list[1, 2, 3, 4, 5]中
a = 2
if(a in list):
    print("变量a %s 在给定的列表list%s中"%(a,list))
else:
    print("变量a %s 不在给定的列表list %s中"%(a,list))
# 变量a 2 在给定的列表list[1, 2, 3, 4, 5]中
print()

print("# 身份运算符")
a = 20
b = 20
print("a和b 有相同的标识 a is b [%s]"%(a is b))
print("a和b 有相同的标识 id(a) == id(b) [%s]"%(id(a) == id(b)))
b = 30
print("a和b 有相同的标识 a is b [%s]"%(a is b))
print("a和b 有相同的标识 a is not b [%s]"%(a is not b))
print()

print("# 运算符优先级")
a = 20; b = 10; c = 15; d = 5; e = 0
print("(a + b) * c / d = %s "%((a + b) * c / d)) # (a + b) * c / d = 90.0
print("((a + b) * c) / d = %s "%(((a + b) * c) / d)) # ((a + b) * c) / d = 90.0
print("(a + b) * (c / d) = %s "%((a + b) * (c / d))) # (a + b) * (c / d) = 90.0
print(" a + b * c / d = %s "%(a + b * c / d)) # a + b * c / d = 50.0
