
import json

data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

# 写入Json 数据
with open("data.json", "w") as f:
    json.dump(data, f)

# 读取数据
with open("data.json", "r") as f:
    data2 = json.load(f)

print(data2)
