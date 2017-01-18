
import re

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print("matchObj.group(): ",searchObj.group())
    print("matchObj.group(1): ",searchObj.group(1))
    print("matchObj.group(2): ",searchObj.group(2))
else:
    print("No Match!!")
print()

# Match 与 Search的区别
print("# Match 与 Search的区别")
searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print("searchObj.group(): ",searchObj.group())
else:
    print("No Search Result!!")

matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print("matchObj.group(): ",matchObj.group())
else:
    print("No Match!!")

print("re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；")
print("re.search匹配整个字符串，直到找到一个匹配")
