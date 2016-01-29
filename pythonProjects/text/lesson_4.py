# coding=utf-8
__author__ = 'angellrp'
import time

### 时间与日期 ###
#1 tick时间戳
print time.time()

#2 时间元组
print time.localtime(time.time())  #获取当前时间,返回元组

#3 格式化
print time.asctime(time.localtime(time.time()))  #获取格式化的时间

#4 日历
import calendar
print calendar.month(2015, 9)  #获取某年某月的日历

# Time模块的内置函数
print time.clock()  #用浮点数计算返回CPU当前时间,用来衡量不同程序的耗时。

time.sleep(1)  #推迟调用程序的运行,参数为秒(sec)

print time.clock()

# Calendar日历模块的内置函数
print calendar.calendar(2015, 1, 1, 5)  #返回一个多行字符串格式的某年年历

calendar.setfirstweekday(6)  #设置每个星期的第一天是星期几
print calendar.firstweekday()  #返回当前每个星期的第一天是星期几

print calendar.isleap(2015)  #返回是否是闰年


### 函数 ###

print "======================="
#1 必备参数
def printStr1(str):
    "输出任意传入的字符串"
    return str

print printStr1("this is printStr1!")
# print printStr1()  #不传入参数则会报错

#2 命名参数[与传参的顺序无关]
def printStr2(str, int):
    return int, str

print printStr2(int = 3, str = "this is printStr2!")

#3 缺省参数
def printStr3(name, age = 20):
    return name, age

print printStr3("function", 30)
print printStr3("function")

#4 可变参数
def printStr4(*values):
    for var in values:
        print var

printStr4(3, 1, 6, 2)
printStr4("str")

def printStr5(**args):
    return args.items()

print printStr5(a = 1, b = 2, c = 3)

#5 匿名函数
#  python使用lambda函数创建匿名函数
sum = lambda arg1, arg2:arg1 + arg2

print sum(10, 20)
