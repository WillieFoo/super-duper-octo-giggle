# coding = utf-8
# -*- coding: UTF-8 -*-
__author__ = 'angellrp'

### 中文编码 ###

#1 文档中有涉及到中文的,一律在文件头添加 # coding = utf-8 或 # -*- coding: UTF-8 -*-

#2 python 3.x 版本默认使用utf-8编码，所以不必手动添加

print '======================='
print '你好，世界'


### 多行语句 ###

#1 python中一般以换行作为一段语句的结束,但我们可以使用斜杆(\)表示多行显示:

#2 如果语句中含有{}、[]或()则不需要使用斜杆

print '======================='
item_one = 1
item_two = 2
item_three = 3

test = item_one + \
    item_two + \
    item_three

print test

days = {"Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"}

print days

### 注释 ###

#1 语句注释可使用字符'#'

#2 多行注释可使用三单引号(''') 或 三双引号(""")

'''
多行注释！！！
多行注释！！！
多行注释！！！
多行注释！！！
'''

### 多变量赋值 ###

print '======================='
a = b = c = 1

A, B, C = 4, 'yes', 2.02

print a, b, c , A, B, C

### del关键字 ###

#1 使用del关键字删除变量的引用

print '======================='
num1 = 1
num2 = 2

del num1
#del num1, num2

# print num1 # 出错,找不到相应的定义

print num2

### Python字符串 ###

#1 顺序和倒序:
    # 顺序:从左到右索引默认0开始的，最大范围是字符串长度少1
    # 倒序:从右到左索引默认-1开始，最大范围是字符串的开头

print '======================='
str = 'i am a superman !'

# 切片(包含下限，不包含上限)
print str[0:9]
print str[0:-1]
print str[-5:]

#2 ‘+’为字符串的连接符，‘*’为字符串的重复符

print str + ' ' + str

print (str + ' ') * 3

### Python列表 和 Python元组 ###

#1 同字符串一样，具有相同特性

#2 列表使用‘[]’表示，元组使用‘()’表示,
#  列表中的元素可变(动态),元组中的元素不可变(静态)
#  同为有序组合

print '======================='
list = ['one', 2, 'two', True]
tinyList = ['Bob', 'Mary']

print list

print list[:]
print list[-3:-2]

print list + tinyList
print tinyList * 2

tuple = ('A', 'B', 'C')
tinyTuple = ('a', 'b', 'c')

print tuple[1:3]
print tuple[-2:-1]

print tuple +tinyTuple
print tuple * 2


### Python字典 ###

#1 字典是无序的组合,与有序的列表不同

#2 字典使用大括号‘{}’表示

print '======================='
dict = {'one':1, 2:'two', 'tree':'green'}
tinyDict = {}
tinyDict['name'] = "Jack"
tinyDict['score'] = 92

print dict

print dict['one']

print dict[2]

print tinyDict.keys()

print tinyDict.values()














