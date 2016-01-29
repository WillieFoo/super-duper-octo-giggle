# coding=utf-8
__author__ = 'angellrp'

### 模块 ###
# import  引用某个模块
# from ... import  引用模块中指定的部分
# from ... import*  将模块中的所有内容全部引用



# 全局变量 和 局部变量
# money = 1000
#
# def printMoney():
#     global money #注释掉全局变量的引用定义后，报出UnboundLocalError错误
#     money = money + 1000
#
# print money
# printMoney()
# print money

# dir()函数  #将模块中定义过的命名排好序后输出
# import math
#
# print dir(math)


# globals()函数 和 locals()函数
# name = "Lily"
# age  = 18
# sex  = "F"
#
# def printFuncValName():
#     global name
#     global age
#     global sex
#     hobby = "playing basketball"
#     fansNum = 204
#     adds = "MillSion Street"
#     print globals()
#     print locals()
#
# printFuncValName()

# 导入自定义包/库
# import test
#
# test.first()
# test.second()
# test.third()



### 文件I/O ###
#1 读取键盘输入

# part1 #
# str1 = raw_input("Enter you input: ")  #将输入的字符原原本本输出
# print "what's you enter:", str1

# str2 = input("Enter you input: ")  #将输入的内容假设为有效的表达式,并进行运算
# print "what's you write: ", str2


# part2 #
# file = open("foo.txt", "wb") #没有时自动创建
#
# print "name of the txt:", file.name
# print "it's closed or not:", file.closed
# print "which mode is it:", file.mode
# print "softspace flag:", file.softspace
#
# file.write("Please put it in the plate!\nOK! i will do it soon.\n")
# file.close()
#
# file = open("foo.txt", "rb")
# print "The context is:\n", file.read()
# file.close()
#
# file = open("foo.txt", "r+")
# print "first read:", file.read(10)
# print "the current position:", file.tell() #指出光标所处于当前文件中的位置
# print "second read:", file.read()
# file.seek(0, 0) # 改变光标的位置,参数分别为:offset(偏移量)、from(起始位置)
# print "third read:", file.read()
# file.close()

# part3 #
import os

# filename = "/Users/angellrp/docs/pythonProjects/foo.txt"
#
# if os.path.exists(filename): # 判断文件是否存在
#     print "It's exists!"
# else:
#     print "I can't find it."

# if os.path.exists("too.txt"):
#     os.rename("too.txt", "foo.txt") # 重命名文件
#     Message = 'the "%s" file has rename.'
# else:
#     Message = 'the "%s" file can not be find!'
#
# print Message % "too.txt"

# file = open("ddt.txt", "w")
# file.close()
#
# if os.path.exists("ddt.txt"):
#     os.remove("ddt.txt") # 移除文件
#     print "I has remove it."
# else:
#     print "I can't find it."

# part4 #
# if os.path.exists("newDir"):
#     print "It has already exists."
#     print os.getcwd() #获取当前的工作目录
#     os.chdir("/Users/angellrp/docs/pythonProjects/python") #改变文件目录(文件夹)
#     print os.getcwd()
#     # if os.path.exists("/Users/angellrp/docs/pythonProjects/python"):
#     #     print "It has been removed."
#     #     os.rmdir("/Users/angellrp/docs/pythonProjects/python")
#     # else:
#     #     print "I can't find it."
#     # print os.getcwd()
#     # print "It has already exists."
# else:
#     print "create a new directory."
#     os.mkdir("newDir") #创建新的文件目录(文件夹),参数:path(路径)、mode(模式)


