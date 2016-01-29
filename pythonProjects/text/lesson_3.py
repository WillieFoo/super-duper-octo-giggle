# coding=utf-8
import math

__author__ = 'angellrp'

### 数据类型 ###

#1 数字数据类型
#  不可改变,如果改变数字数据类型的数值,则需要重新分配存储空间
#  可以使用del语句删除一些数字的引用
#  Python数学函数

print abs(-10)    #内置函数
print math.fabs(-10)    #函数库中函数 [取绝对值]
print math.ceil(4.2)    #[向上取整]
print math.floor(4.8)   #[向下取整]
print max(2, 7, -4, 5, 1, 9, 6)    #内置函数 [获取序列最大值]
print min(2, 7, -4, 5, 1, 9, 6)    #内置函数 [获取序列最小值]
print math.modf(12.42)    #[分出整数和小数部分]
print math.pow(3, 2)    #[获取平方值]
print round(4.5)    #内置函数 [四舍五入]
print math.sqrt(9)    #[获取平方根]

print math.degrees(math.pi/2)  #弧度转角度
print math.radians(30)  #角度转弧度

print "============================"
#  Python随机数函数
import random


print random.choice(range(10))  #随机获取序列中的数值
print random.randrange(0, 21, 2)  #获取0~20中随机偶数
print random.random()  #随机生成一个实数,区间在[0 ~ 1]

#设置随机数种子
print random.seed(10)
print random.random()
print random.random()

print random.seed(10)
print random.random()
print random.random()

#将序列的元素随机排序
t = ["A", "B", "C", "D", "E"]
print t
random.shuffle(t)
print t
random.shuffle(t)
print t
print t

print random.uniform(10, 20)  #随机生成一个实数,区间在[10,20]

print random.sample(t, 3)  #从序列中随机获取指定数目的子序列
print random.sample(t, 3)



#2 字符串类型
#  python不支持单字符类型,所以单字符也算是字符串


#3 list列表类型

print "============================"
list1 = ["A", "B", "C", "D", "E"]
list2 = ["a", "b", "b", "c", "c"]

list1.append("F")  #在列表末尾添加新的对象
print list1

print list2.count("b")  #统计某个元素在列表中出现的次数
print list2.index("b")  #找出列表中第一个匹配项的索引

list1.insert(2, "G")  #将对象插入列表
print list1

list1.pop(1)  #移除列表中指定索引的元素,默认为末尾的元素
print list1

list2.remove("b")  #移除列表中匹配的第一个元素
print list2

list1.reverse()  #反向列表中元素
print list1

list1.sort()  #对原列表进行排序
print list1


#4 tuple元组类型
print "============================"

tuple1 = (1, 2, 4, 7, 3, 1)
tuple2 = ("a", "c", "f", "b", "g")

print cmp(tuple1, tuple2)  #比较两个元组的元素
print len(tuple1)  #计算列表的个数
print max(tuple1)  #返回元组的最大值
print min(tuple2)  #返回元组的最小值
print list(tuple1)  #将元组转换成列表
print tuple(list1)  #将列表转换成元组

#上述python函数也可适用于list列表


#5 dict字典类型

#  del()语句的使用
print "============================"

dict = {"name":"dict", "age":21, "sex":"F", "message":False}
print dict

del dict["name"]  #删除键为”name“的条目
print dict

dict.clear()  #清空字典
print dict

del dict  #删除字典 
print dict

#  不允许同一键出现两次,创建时如果同意键被赋值两次,后一个值才会被记住
#  键必须不可变,所以可用数,字符串或元组充当,所以用列表是不行的

#  内置函数
dict1 = {"name":"Adobe", "age":8}
dict2 = {"A":2, "B":5, "C":3, "D":4}
print cmp(dict1, dict2)
print len(dict1)
print str(dict2)

print type(dict1)  # 返回变量的数据类型
print type(list1)
print type(2)
print type("i am a man !")


#
dict = {"name":"Adobe", "age":8, "sex":"M", "A":1, "B":2, "C":3}
print dict
dict_c = dict.copy()  #复制字典到一个新的字典中
print dict_c
dict_c = dict_c.fromkeys(["www", "sss", "aaa", "fff", "yyy"], 10)  #将序列作为键，values作为默认值创建字典
print dict_c
print dict.get("name")  #获取相关键的值
print dict.get("D")
print dict.has_key("D")  #判断字典中是否有某个键
print dict.items()  #遍历字典中所有的键值对，并以序列的形式输出
print dict.keys()  #遍历字典中所有的键
print dict.values()  #遍历字典中所有的值
dict.setdefault("D", 4)  #添加新的键值对,默认值为None
print dict
dict_c.update(dict)  #更新字典1到字典2中(合并)
print dict_c

