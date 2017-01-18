
import socket
import sys

# 创建Socket对象
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口
serverSocket.bind((host, port)) # TypeError: bind() takes exactly one argument (2 given)

# 设置最大连接数 超过后排队
serverSocket.listen(5)

while True:
    # 建立客户端连接
    clientSocket,addr = serverSocket.accept() # 返回俩
    print("连接地址：%s" % str(addr))
    msg = "欢迎您访问菜鸟教程！"+"\r\n"
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()
