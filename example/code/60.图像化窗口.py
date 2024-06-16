#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/13 22:46
# @Author  : 刘双喜
# @File    : 60.图像化窗口.py
# @Description : 添加描述
import time
import tkinter as tk

# 创建一个新的窗口
window = tk.Tk()
window.title('这是标题')
window.geometry('300x1000')

# 创建变量
var_str1 = tk.StringVar()
var_str1.set('显示')
var_str2 = tk.StringVar()
var_str2.set('显示2')

# 创建一个标签
label_1 = tk.Label(window, text="这是一个标签", bg='green', font=('Arial', 12), width=12, height=2, )
label_1.pack()
label_2 = tk.Label(window, textvariable=var_str2, bg='green', font=('Arial', 12), width=12, height=2, )
label_2.pack()
label_3 = tk.Label(window, text='标签3', bg='green', font=('Arial', 12), width=12, height=2, )
label_3.pack()

# 创建一个文本
text_1 = tk.Text(window, background='yellow', height=2)
text_1.pack()

# 创建一个文本框
entry = tk.Entry(window, show='*', background='red')
entry.pack()


def insert_in():
    data = entry.get()
    text_1.insert('insert', data)


def insert_end():
    data = entry.get()
    text_1.insert('end', data)


def insert_xy():
    data = entry.get()
    text_1.insert(1.2, data)


def print_select():
    data = listbox.get(listbox.curselection())
    var_str2.set(data)


# 创建一个按钮
show = False


def hit_me():
    global show
    if show is False:
        show = True
        var_str1.set('不显示')
    else:
        show = False
        var_str1.set('显示')


button_1 = tk.Button(window, width=15, height=2, textvariable=var_str1, command=hit_me)
button_1.pack()

button_2 = tk.Button(window, width=15, height=2, text='插入', command=insert_in)
button_2.pack()
button_3 = tk.Button(window, width=15, height=2, text='追加', command=insert_end)
button_3.pack()
button_4 = tk.Button(window, width=15, height=2, text='追加xy', command=insert_xy)
button_4.pack()
button_5 = tk.Button(window, width=15, height=2, text='打印', command=print_select)
button_5.pack()

# 创建一个列表框
var_str3 = tk.StringVar()
var_str3.set((11, 22, 33, 44))
listbox = tk.Listbox(window, listvariable=var_str3)
for i, v in enumerate([1, 2, 3, 4], 1):
    listbox.insert(i, f"选项{v}")
listbox.insert('end', "选项最后")
listbox.pack()

# 选项
var_str4 = tk.StringVar()
var_str4.set('选项')


def selection():
    # 给标签赋赋值, 标签不能有text
    label_3.config(text='select' + var_str4.get())
    var_str2.set('select' + var_str4.get())


# 给变量v4 赋值AB
select_1 = tk.Radiobutton(window, text='OptionA', variable=var_str4, value='A', command=selection)
select_1.pack()
select_2 = tk.Radiobutton(window, text='OptionB', variable=var_str4, value='B', command=selection)
select_2.pack()

# 多选
var_int5 = tk.IntVar()
var_int6 = tk.IntVar()


def selection_2():
    if var_int5.get() == 1 and var_int6.get() == 0:
        label_3.config(text=f'I L PY')
    elif var_int5.get() == 0 and var_int6.get() == 1:
        label_3.config(text='I L C')
    elif var_int5.get() == 1 and var_int6.get() == 1:
        label_3.config(text='I L Both')
    else:
        label_3.config(text='I N L Both')


check_button_1 = tk.Checkbutton(window, text='Python', variable=var_int5, onvalue=1, offvalue=0, command=selection_2)
check_button_2 = tk.Checkbutton(window, text='C', variable=var_int6, onvalue=1, offvalue=0, command=selection_2)
check_button_1.pack()
check_button_2.pack()

# 图片
canvas = tk.Canvas(window, bg='blue', height=200, width=200)
img_file = tk.PhotoImage(file='..\\data\\60.tk\\1.png')
img = canvas.create_image(10, 10, anchor='nw', image=img_file)
x0, y0, x1, y1 = 50, 50, 80, 80
arc = canvas.create_arc(x0,y0,x1,y1, start=0, extent=180) # 扇形
rect = canvas.create_rectangle(150,150, 100+20, 100+40) # 长方形，起点坐标和终点坐标
canvas.pack()

def move():
    canvas.move(rect, 1,2)
button_6 = tk.Button(window, text='Move', command=move)
button_6.pack()

# 菜单
label_4 = tk.Label(window, text='标签4', bg='red')
label_4.pack()
count = 1
def do_job():
    global count
    label_4.config(text=f'do count={count}')
    count += 1

menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)  # tearoff=1,显示虚线，可以移动菜单
menubar.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='New', command=do_job)
file_menu.add_command(label='Find', command=do_job)
file_menu.add_separator()  # 分割线
file_menu.add_command(label='Exit', command=window.quit)

sub_menu = tk.Menu(file_menu, tearoff=0)
window.config(menu=menubar)
file_menu.add_cascade(label='Edit', menu=sub_menu, underline=0)
sub_menu.add_command(label='Name', command=do_job)

# 运行主循环
window.mainloop()
