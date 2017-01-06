# http://www.runoob.com/python/python-date-time.html
import time
import calendar

ticks = time.time()
print(ticks)

# 获取当前时间
print("# 获取当前时间")
localtime = time.localtime(time.time())
print("本地时间为：", localtime)
print()
# time.struct_time(tm_year=2017, tm_mon=1, tm_mday=6, tm_hour=17, tm_min=21, tm_sec=20, tm_wday=4, tm_yday=6, tm_isdst=0)
# 序号	字段	值
# 0	4位数年	2008
# 1	月	1 到 12
# 2	日	1到31
# 3	小时	0到23
# 4	分钟	0到59
# 5	秒	0到61 (60或61 是闰秒)
# 6	一周的第几日	0到6 (0是周一)
# 7	一年的第几日	1到366 (儒略历)
# 8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜

# 获取格式化时间
print("# 获取格式化时间")
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为：", localtime)
print()

# 格式化日期
print("# 格式化日期")
# 格式化成 2017-01-06 17:26:54 形式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
# 格式化成 Fri Jan 06 17:28:48 2017 形式
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime(time.time())))
# 将格式字符串转换成时间戳 1483694928.0
a = "Fri Jan 06 17:28:48 2017"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
print()

# 获取某月日历
cal = calendar.month(2016,1)
print("输出2016年1月份的日历:")
print(cal)
print()
# Time 模块

# 日历 Calendar 模块