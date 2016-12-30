# Python While 循环语句

# While in list use pop
print("# While in list use pop")
numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)     # 偶数
    else:
        odd.append(number)      # 奇数
print(numbers)
print(even)
print(odd)
print()

print("# Normal While")
count = 0
while (count < 5):
    print("The count is:", count)
    count += 1
print()

# Continue 和 break 用法
print("# Continue 和 break 用法")
i = 1
while i< 10:
    i+=1
    if i%2 >0:  # 非双数时跳过输出
        continue
    print(i, end="|")  # 输出双数 2|4|6|8|10|
print()

i = 1
while 1:
    print(i, end="|") # 输出 1|2|3|4|5|
    i += 1;
    if i > 5:
        break
print()

# 无限循环
# print("# 无限循环")
# var = 1
# while var == 1:
#     num = input("Enter a number:")
#     print("You entered: ", num)
# print("Good Bye!")

# 循环使用else语句
print("# 循环使用else语句")
count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")
print()

# 简单语句组
# print("# 简单语句组")
# flag = 1
# while(flag) : print("Givin flag is really true!")
# print("Good Bye!")
# print()
