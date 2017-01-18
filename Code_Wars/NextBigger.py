from functools import reduce

'''
编写一个函数，接受一个正整数作为输入，然后输出由相同数字组成的下一个更大的数：
    next_bigger(12)==21
    next_bigger(513)==531
    next_bigger(2017)==2071
如果找不到由相同数字组成的更大整数，则返回-1：
    next_bigger(9)==-1
    next_bigger(111)==-1
    next_bigger(531)==-1
code wars 链接，不要偷看答案啊
http://www.codewars.com/kata/55983863da40caa2c900004e
'''
def next_bigger(number):
    t = [int(n) for n in str(number)]

    i = len(t) - 2
    while i >= 0 and t[i] >= t[i+1]: i -= 1
    if i == -1: return -1

    j = len(t) - 1
    while j > i and t[i] >= t[j]: j -= 1
    if j != i: t[i],t[j] = t[j], t[i]

    ints = t[0:i+1] + t[i+1:][::-1]
    return reduce(lambda x, y: x*10 + y, ints)

print(next_bigger(2134))
# print(next_bigger(4321))
# print(next_bigger(1234))
# print(next_bigger(12))
# print(next_bigger(513))
# print(next_bigger(2017))
# print(next_bigger(9))
# print(next_bigger(111))
# print(next_bigger(531))
