
lower = int(input("输入区间最小的值:"))
upper = int(input("输入区间最大的值:"))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
           print(num)

# 只有For循环正常退出时才会执行Else语句(不是由break结束循环)
# 当循环是由break语句中断时，else就不被执行。
# 请查看 代码 01_For_Break_Else.py
