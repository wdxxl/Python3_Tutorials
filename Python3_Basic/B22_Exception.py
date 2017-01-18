# http://www.runoob.com/python/python-exceptions.html

# try-except-else语句
try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("IOError: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
# chmod  -w testfile

# try-finally 语句
try:
    fh = open("testfile","w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("文件关闭")
        fh.close()
except IOError:
    print("IOError: 没有找到文件或读取文件失败")