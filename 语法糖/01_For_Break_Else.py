# https://segmentfault.com/a/1190000004903355
# Python语法糖——for/else循环语句里的break

for i in range(5):
    if i == 1:
        print("in for")
else:
    print("in else")
print("after for-loop")
# in for
# in else
# after for-loop

for i in range(5):
    if i == 1:
        print("in for")
        break
else:
    print("in else")
print("after for-loop")
# in for
# after for-loop

# 只有For循环正常退出时才会执行Else语句(不是由break结束循环)
# 当循环是由break语句中断时，else就不被执行。

found = False
for i in range(5):
    if i == 1:
        found = True
        print("in for")
        break
if not found:
    print("not found")
print("after for-loop")
# in for
# after for-loop
