# coding=utf-8
__author__ = 'angellrp'

### 运算符 ###

#1 算数运算符
#  + - * / 加减乘除
#  %  取模
#  ** 幂
#  // 取整

print '=========================='
print 5 % 2
print 5 ** 2
print 5 // 2

#2 比较运算符
#  < > <= >=
#  == 等于
#  != 不等于
#  <> 不等于

print '=========================='
print 5 == 2
print 5 != 2
print 5 <> 2

#3 赋值运算符
#  == += -= *= /= %= **= //=

print '=========================='
a, b = 2, 3
a += b
print a
a -= b
print a
a *= b
print a
a /= b
print a
a %= b
print a
a **= b
print a
a //= b
print a

#4 位运算符
# & | ^ ~ << >> 按位与运算符、按位或运算符、按位异或运算符、按位取反运算符、左移运算符、右移运算符

print '=========================='
a = 50    # 50 = 0011 0010
b = 22    # 22 = 0001 0110
          # a & b = 0001 0010
print a & b
          # a | b = 0011 0110
print a | b
          # a ^ b = 0010 0100
print a ^ b
          # ~a = 1100 1101
print ~a

#5 逻辑运算符
#  and or not 与,或,非

print '=========================='
a = 20
b = 'A'
c = False
d = True

print a and b   #与运算,结果取决于后者
print a and c
print b and a
print a or c    #或运算,结果取决于前者
print b or a
print not d     #非运算,结果相反

#6 成员运算符
#  in, not in

print '=========================='
L = ['one', 'two', '3']
if 'one' in L:
    print 'the L has "one"'
if 'three' not in L:
    print 'there are not three'

#7 身份运算符
# is, not is

print '=========================='
a = 20
b = 20

if a is b:
    print 'a is the same to b'
    print a

#  id()获取变量的引用
if id(a) == id(b):
    print 'a is the same to b'
    print id(a)


### 条件语句 ###
#  if 表达式1:
#      代码块1
#  elif 表达式1:
#      代码块2
#  else:
#      代码块3

print '=========================='
a = 10
b = 20
c = 30
if a > b:
    print 'a is greater than b'
elif a > c:
    print 'a is greater than c'
else:
    print 'a is less than b and c'

### 循环语句 ###

#1 while循环语句
#  while 表达式:
#      语句块1
#  else:
#      语句块2

#  else下的语句块会在循环结束时执行

print '=========================='
n = 1
while n < 10:
    n += 1
    print 'the number is:', n
else:
    print 'this is a line !!!'

# 无限循环
# while True:
#     num = raw_input("Enter a num you like:")
#     print 'the number you choose is:', num



#2 for循环语句
#  通常for语句是用来遍历某个组合中的元素的
#  for 元素 in 组合:
#      语句块

#  for 元素 in 组合:
#      语句块1
#  else:
#      语句块2

print '=========================='
for num in range(1, 20):
    if num == 1 or num == 2 or num == 3:
        print num, 'is a prime number!'
    else:
        for i in range(2, num):
            if num % i == 0:
                j = num / i
                print 'the factor number:', num, i, '*', j
                break
        else:
            print num, 'is a prime number!'

#3 循环嵌套
#  while语句和for语句也可以相互嵌套

#4 break语句:终止循环语句,跳出循环

print '=========================='
str = '000000001000'
var = ''
for letter in str:
    if letter == '1':
        break
    var += letter
print var

#5 continue语句:结束本次循环，进入下一次的循环

print '=========================='
str = '1020100102'
var = ''
for letter in str:
    if letter == '0':
        continue
    var += letter
print var

#6 pass语句:空语句,不做任何作用,一般用做占位语句

