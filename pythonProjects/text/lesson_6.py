# coding=utf-8
__author__ = 'angellrp'

# from Tkinter import *

# from tkMessageBox import *

# def answer():
#
#     showerror("Answer", "Sorry, no answer available")
#
#
# def callback():
#
#     if askyesno('Verify', 'Really quit?'):
#
#         showwarning('Yes', 'Not yet implemented')
#
#     else:
#
#         showinfo('No', 'Quit has been cancelled')
#
#
# Button(text='Quit', command=callback).pack(fill=X)
#
# Button(text='Answer', command=answer).pack(fill=X)
#
# mainloop()


# import Tkinter
#
# root = Tkinter.Tk()
#
# Tkinter.Button(text = 'Quit').pack()
# Tkinter.Button(text = 'cancelled').pack()
# Tkinter.Button(text = 'OK').pack()
#
# root.mainloop()




### 创建查询窗口 ###
from Tkinter import *  #引用Tk模块
root = Tk()  #初始化Tk()

# [函数]
def sreach():
    print "What do you want to sreach ?"

def sure():
    print "Are you sure ?"

def clean():
    print "Clean it !"

def cancelled():
    print "It's cancelled !"



root.title("查询窗口")  #窗口标题
root.geometry('300x500')  #窗口大小
root.resizable(width = False, height = False)  #设置窗口长宽是否可以改变

# [标签]
label = Label(root, text = "ASCII码查询", bg = "white", font = ("Arial", 24), width = 10, height = 2)
label.pack()

# [矩形容器]
frame = Frame(root)

# left side
frame_l = Frame(frame)
Button(frame_l, text = "查询", command = sreach).pack(side = TOP)
Button(frame_l, text = "确定", command = sure).pack(side = BOTTOM)
frame_l.pack(side = LEFT)

# right side
frame_r = Frame(frame)
Button(frame_r, text = "清除", command = clean).pack(side = TOP)
Button(frame_r, text = "取消", command = cancelled).pack(side = BOTTOM)
frame_r.pack(side = RIGHT)

frame.pack()

# [单行文本框]
var1 = StringVar()
entryBox1 = Entry(root, textvariable = var1)
entryBox1.pack()

var2 = StringVar()
entryBox2 = Entry(root, textvariable = var2)
entryBox2.pack()

def copyText():
    if (var1.get() > 0):
        var2.set(var1.get())
    else:
        print "There are no Words !"

Button(root, text = "复制", command = copyText).pack()

# [多行文本框]

# text = Text(root)
# text.insert(1.0, "Dear Mother:\n")
# text.insert(END, "zzzzzzzzzzzzzzz\n")
# text.insert(END, "QQQQQQQQQQQQQQQ")
# text.pack()

# [列表框]

def showChose(event):
    varText.set(list.get(list.curselection()))
    print "What you choose is:", list.get(list.curselection())
varText = StringVar()

Entry(root, text = varText).pack()

var = StringVar()
list = Listbox(root, height = 5, listvariable = var)

list_item = ['A', 'B', 'C', 'F']
for item in list_item:
    list.insert(END, item)
list.delete(1, 2)

var.set(('Lily', 'Bob', 'Cheer', "Davie"))

list.bind('<ButtonRelease-1>', showChose)

list.pack()



root.mainloop()  #进入消息循环

