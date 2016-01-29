# coding=utf-8
__author__ = 'angellrp'

###正则表达式###
import re

## 匹配函数 ##
# re.match函数:尝试从字符串的起始位置匹配一个模式,成功返回一个匹配对象,如果不是起始位置匹配成功的话，返回none
# re.match(pattern, string, flags=0)
# pattern:  要匹配的正则表达式
# string:   被匹配的字符串
# flags:    标志位,用于控制正则表达式的匹配方式,如:是否区分大小写,多行匹配等等

# span()函数 返回一个tuple元组

print(re.match("www.baidu.com", "www.baidu.com").span())
print(re.match("www.baidu.com", "www.baidu.com"))
print(re.match("www", "www.baidu.com").span())
print(re.match("www", "www.baidu.com"))
print(re.match("com", "www.baidu.com"))

line = "Cats are smarter than dogs!"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print 'Group( ) = ', matchObj.group()
    print 'Group(1) = ', matchObj.group(1)
    print 'Group(2) = ', matchObj.group(2)
    print 'Group(1,2) = ', matchObj.group(1,2)
    print "Groups() = ", matchObj.groups()
else:
    print "No match!!!"

## 搜寻函数 ##
# re.search函数:扫描一遍字符串并返回第一个符合条件的匹配对象

print(re.search("www", "www.baidu.com").span())
print(re.search("com", "www.baidu.com").span())
