
# 导入 socket, sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
# 设置端口
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port)) # TypeError: connect() takes exactly one argument (2 given)

# 接收小于1024字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))