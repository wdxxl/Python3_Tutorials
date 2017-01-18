import re

print("# 检索和替换")

phone = "2004-959-559 #这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "",phone)
print("电话号码：", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码：", num)

print()

print("#repl 参数是一个函数")
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
print()

# re.I 使匹配对大小写不敏感
# re.L 做本地化识别（locale-aware）匹配
# re.M 多行匹配, 影响
# re.S 使匹配包括换行在内的所有字符
# re.U 根据Unicode字符集解析字符, 这个标志影响 \w \W \b \B
# re.X 该标志通过给予你更灵活的格式以便你奖正则表达式写的更易于理解
