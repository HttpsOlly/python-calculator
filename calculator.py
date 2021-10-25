from tkinter import *

#Create Objects
root = Tk()

#Cosmetic Implementations
root.title("Simple Calculator")

box = Entry(root, width=30, borderwidth=5)
box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Functions
def numberclick(num):
    box.insert(END, num)

def equalsclick():
    second_num = box.get()
    box.delete(0, END)

    if operation == "addition":
        box.insert(0, first_num + int(second_num))

    if operation == "subtraction":
        box.insert(0, first_num - int(second_num))

    if operation == "multiplication":
        box.insert(0, first_num * int(second_num))

    if operation == "division":
        box.insert(0, first_num / int(second_num))
    
def clearclick():
    box.delete(0, END)

def addclick():
    f_num = box.get()
    global first_num
    global operation
    operation = "addition"
    first_num = int(f_num)
    box.delete(0, END)

def minusclick():
    f_num = box.get()
    global first_num
    global operation
    operation = "subtraction"
    first_num = int(f_num)
    box.delete(0, END)

def timesclick():
    f_num = box.get()
    global first_num
    global operation
    operation = "multiplication"
    first_num = int(f_num)
    box.delete(0, END)

def divideclick():
    f_num = box.get()
    global first_num
    global operation
    operation = "division"
    first_num = int(f_num)
    box.delete(0, END)

#Create Calc Buttons
number_1 = Button(root, text="1", padx=40, pady=20, command=lambda: numberclick(1))
number_2 = Button(root, text="2", padx=40, pady=20, command=lambda: numberclick(2))
number_3 = Button(root, text="3", padx=40, pady=20, command=lambda: numberclick(3))
number_4 = Button(root, text="4", padx=40, pady=20, command=lambda: numberclick(4))
number_5 = Button(root, text="5", padx=40, pady=20, command=lambda: numberclick(5))
number_6 = Button(root, text="6", padx=40, pady=20, command=lambda: numberclick(6))
number_7 = Button(root, text="7", padx=40, pady=20, command=lambda: numberclick(7))
number_8 = Button(root, text="8", padx=40, pady=20, command=lambda: numberclick(8))
number_9 = Button(root, text="9", padx=40, pady=20, command=lambda: numberclick(9))
number_0 = Button(root, text="0", padx=40, pady=20, command=lambda: numberclick(0))
equals   = Button(root, text="=", padx=40, pady=20, command=equalsclick)
clear    = Button(root, text="AC", padx=36, pady=20, command=clearclick)
addition = Button(root, text="+", padx=40, pady=20, command=addclick)
subtract = Button(root, text="–", padx=40, pady=20, command=minusclick)
multiply = Button(root, text="x", padx=40, pady=20, command=timesclick)
division = Button(root, text="÷", padx=40, pady=20, command=divideclick)
exit = Button(root, text="Exit Calculator", padx=40, pady=20, command=root.quit)

#Place Calc Buttons
number_7.grid(row=1, column=0)
number_8.grid(row=1, column=1)
number_9.grid(row=1, column=2)

number_4.grid(row=2, column=0)
number_5.grid(row=2, column=1)
number_6.grid(row=2, column=2)

number_1.grid(row=3, column=0)
number_2.grid(row=3, column=1)
number_3.grid(row=3, column=2)

number_0.grid(row=4, column=0)
equals.grid(row=4, column=1, columnspan=2)

clear.grid(row=5, column=0, rowspan=2)
addition.grid(row=5, column=1)
subtract.grid(row=5, column=2)

multiply.grid(row=6, column=1)
division.grid(row=6, column=2)

exit.grid(row=7, column=0, columnspan=3)

#Run Process
root.mainloop()