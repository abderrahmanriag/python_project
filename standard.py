from tkinter import *
import math
root = Tk()
root.title('Calculator')
button_bg = "black"
button_fg = "white"
button_op_bg='gray20'
button_op_fg='white'
backround_color="black"
label_bg="black"; label_fg="white"
FONT=("Courier",15)
FONT_Lable=("Arial", 15)
FONT_ENTRY=("Courier",7)
root.configure(background=backround_color)
def create():
    row0 = 0;row1 = 1;row2 = 2;row3=3;row4 = 4;row5 = 5;row6 = 6
    l=Label(root, text="Standard",font=FONT_Lable, fg=label_fg, bg=label_bg)
    l.grid(row=row0, column=0, columnspan=2)
    e = Entry(root, width=45, borderwidth=2, bg="white", fg="black")
    e.grid(row=row1, column=0, columnspan=4, padx=10, pady=10)
    e.insert(0, 0)
    r=1
    def button_click(number):
        current=e.get()
        e.delete(0, END)
        if current==r:
            if number == ".":
                e.insert(0, "0" + str(number))
            else:
                e.insert(0, number)
        if current!=r:
            if number == ".":
                e.insert(0, str(current) + str(number))
            else:
                if current == "0":
                    e.insert(0, number)
                else:
                    e.insert(0, str(current) + str(number))
    def button_equal():
        second_number=e.get()
        e.delete(0, END)
        if op=='addition':
            result = float(second_number) + f_num
            if result - math.floor(result) == 0:
                e.insert(0, math.floor(result))
            else:
                e.insert(0, result)
        if op =="substraction":
            result = f_num - float(second_number)
            if result-math.floor(result)==0:
                e.insert(0, math.floor(result))
            else:
                e.insert(0, result)
        if op =="mul":
            result = float(second_number) * f_num
            if result - math.floor(result) == 0:
                e.insert(0, math.floor(result))
            else:
                e.insert(0, result)
        if op =="divition":
            result = f_num / float(second_number)
            if result - math.floor(result) == 0:
                e.insert(0, math.floor(result))
            else:
                e.insert(0, result)
    def button_add():
        first_number=e.get()
        global f_num
        f_num=float(first_number)
        e.delete(0, END)
        operation="addition"
        global op
        op=operation
    def button_sub():
        first_number=e.get()
        global f_num
        f_num=float(first_number)
        e.delete(0, END)
        operation="substraction"
        global op
        op=operation
    def button_div():
        first_number=e.get()
        global f_num
        f_num=float(first_number)
        e.delete(0, END)
        operation="divition"
        global op
        op=operation
    def button_mul():
        first_number=e.get()
        global f_num
        f_num=float(first_number)
        e.delete(0, END)
        operation="mul"
        global op
        op=operation
    def button_clear():
        e.delete(0, END)
        e.insert(0, 0)
    def button_back():
        lenght=len(e.get())
        if lenght==1:
            button_clear()
        else:
            e.delete(lenght-1, END)
    xnumber=23; y=20
    one=Button(root,font=FONT, text="1", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(1))
    two=Button(root, font=FONT, text="2", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(2))
    three=Button(root, font=FONT, text="3", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(3))
    four=Button(root, font=FONT,text="4", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(4))
    five=Button(root, font=FONT,text="5", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(5))
    six=Button(root, font=FONT,text="6", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(6))
    seven=Button(root, font=FONT,text="7", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(7))
    eight=Button(root, font=FONT,text="8", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(8))
    nine=Button(root, font=FONT,text="9", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(9))
    zero=Button(root, font=FONT,text="0", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click(0))
    point=Button(root, font=FONT,text=".", padx=xnumber, pady=y, bg=button_bg, fg=button_fg, command=lambda:button_click("."))
    add=Button(root, font=FONT,text="+", padx=xnumber, pady=y, bg=button_op_bg, fg=button_op_fg, command=button_add)
    sub = Button(root,font=FONT, text="-", padx=xnumber, pady=y, bg=button_op_bg, fg=button_op_fg, command=button_sub)
    divide = Button(root, font=FONT,text="/", padx=xnumber, pady=y, bg=button_op_bg, fg=button_op_fg, command=button_div)
    multiply=Button(root, font=FONT,text="X", padx=xnumber, pady=y, bg=button_op_bg, fg=button_op_fg, command=button_mul)
    clear = Button(root,font=FONT, text="C", padx=60, pady=y, bg='gray20', fg='white', command=button_clear)
    back=Button(root, font=FONT, text='D', padx=xnumber, pady=y, bg='gray20', fg='white', command=button_back)
    equal = Button(root, font=FONT,text="=", padx=60, pady=y, bg="red4", fg=button_fg, command=button_equal)
    one.grid(row=row5)
    two.grid(row=row5, column=1)
    three.grid(row=row5, column=2)
    add.grid(row=row5, column=3)
    four.grid(row=row4)
    five.grid(row=row4, column=1)
    six.grid(row=row4, column=2)
    sub.grid(row=row4, column=3)
    seven.grid(row=row3)
    eight.grid(row=row3, column=1)
    nine.grid(row=row3, column=2)
    multiply.grid(row=row3, column=3)
    clear.grid(row=row2, columnspan=2)
    back.grid(row=row2, column=2)
    divide.grid(row=row2, column=3)
    equal.grid(row=row6, column=2, columnspan=2)
    zero.grid(row=row6)
    point.grid(row=row6, column=1)
create()
root.mainloop()