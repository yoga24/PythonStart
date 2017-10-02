from tkinter import *


def print_name():
    print('My name is Yoga')


def say_hello(event):
    print('Helllooooooo')


root = Tk()
root.title('TKinter Root Title')
root.minsize(width=400, height=30)
root.resizable(width=False, height=False)

# Create label
my_label = Label(root, text='This is just random label')
my_label.pack()

# Button
my_button_1 = Button(root, text='PrintName', command=print_name)
my_button_2 = Button(root, text='SayHello')
my_button_2.bind('<Button-1>', say_hello)

my_button_1.pack(side=LEFT)
my_button_2.pack(side=LEFT)

root.mainloop()
