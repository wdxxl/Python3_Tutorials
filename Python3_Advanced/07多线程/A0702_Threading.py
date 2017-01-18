# 使用 threading 模块创建线程

import threading
import time
import sys

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程:", self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程:", self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
             sys.exit()
        time.sleep(delay)
        print("%s: %s" %(threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开始新线程
thread1.start()
thread2.start()

while thread2.isAlive():
    if not thread1.isAlive(): # 主要线程决定 次要线程死活
        if exitFlag == 0: exitFlag = 1
    pass
print("退出主线程")
