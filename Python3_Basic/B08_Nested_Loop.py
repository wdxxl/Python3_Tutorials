# 嵌套循环

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j):break  # 取模 - 返回除法的余数
        j+=1
    if(j> i/j): print(i,"是素数")
    i+=1

print("Good Bye!")
