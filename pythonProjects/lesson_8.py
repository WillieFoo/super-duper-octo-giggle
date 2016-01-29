__author__ = 'angellrp'
# coding=utf-8

###正则表达式###
import re

# re.match函数:尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话，返回none
# re.match(pattern, string, flags=0)
# pattern:  要匹配的正则表达式
# string:   被匹配的字符串
# flags:    标志位,用于控制正则表达式的匹配方式,如:是否区分大小写,多行匹配等等

print(re.match("www", "www.baidu.com").span())
print(re.match("com", "www.baidu.com").span())

