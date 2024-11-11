import time
now = time.strftime('%Y-%m-%d %H:%M:%S')
print(now)
# >>> 2021-04-21 13:50:06


# time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# >>> 2021-04-21 14:59:04
# time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# >>> Wed Apr 21 14:59:04 2021



import datetime
today = datetime.date.today()
# >>> 2021-04-21
yesterday = today - datetime.timedelta(days=1)
# >>> 2021-04-20
last_month = today.month - 1 if today.month - 1 else 12
# >>> 3



import time
import datetime
now = datetime.datetime.fromtimestamp(time.time())
# >>> 2021-04-21 13:56:07.508362


import calendar

cal = calendar.month(2021, 4)
print(cal)
# >>> cal
#
#      April 2021
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
# 5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30




# 计算两个日期之间相差的天数
from datetime import date

def main(year1, month1, day1, year2, month2, day2):
    years1 = date(year1,month1,day1)
    years2 = date(year2,month2,day2)
    day= abs(years1-years2).days
    return day

"""
时间日期格式化符号
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""

print(time.perf_counter())  # 返回系统运行时间
print(time.process_time())  # 返回进程运行时间



"""
import time

Functions:

sleep(2) -------- delay seconds
clock() --------- CPU time since process start    #python3.8 不在支持！
per_counter() --- CPU time since process start
——————————————————————————————————————————————
Methods:

time() -------- 1619162869.0196998    
localtime() --- 本地时间Tuple          
gmtime() ------ 国际标准时间Tuple      
ctime() --------- 'Fri Apr 23 15:42:41 2021'   
asctime() ----- 'Fri Apr 23 15:42:41 2021'
mktime() -------- 'TypeError'                   
strftime() ------ 'TypeError'
strptime() ------ 'TypeError'
--------------------------------------------------------------------------

time.strftime('%c') --------------------- 'Fri Apr 23 15:42:41 2021'
time.strftime('%Y-%m-%d %H:%M:%S.%p') --- '2021-04-23 16:23:17.PM'
time.strftime(%A %B') ------------------- 'Friday April'

---------------
-----------------------------------------------------------

localtime([seconds]) --> UTC Tuple ------------var: time.time()
gmtime([seconds]) -----> local time Tuple------var: time.time()
ctime([seconds]) ------> string ---------------var: time.time()
asctime([Tuple]) ------> string -------------- var: time.gmtime/localtime()
mktime(local time) ----> string -------------- var: time.localtime()
strptime(string,format) ----> Tuple ------var: time.ctime/asctime()

-------------------------------------------------------------------------------------------------------------

>>> time.localtime()
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=23, tm_hour=7, tm_min=28, tm_sec=6, tm_wday=4, tm_yday=113, tm_isdst=0)

>>> time.gmtime()
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=23, tm_hour=15, tm_min=28, tm_sec=59, tm_wday=4, tm_yday=113, tm_isdst=0)


start = time.perf_counter() --------- CPU time since process start
func()
end = time.perf_counter()
print('CPU执行用时: ', end - start)
"""