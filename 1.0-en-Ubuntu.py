#coding=utf-8
import random
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Math Text")
window.geometry("500x300")
window.resizable(False,False) 

def callback():
    if messagebox.askokcancel("Mathematics training","Are you sure you want to exit?"):
        window.destroy()

def chenfa():
    global num
    global nextbtn1

    num=var1.get()
    try:
        if int(num)==a*b:
            messagebox.showinfo("Multiplication", "Congratulations, that's right! Try the next question！")
            nextbtn1.place(x=310,y=0)
            clicked1.place_forget()
            txt.delete(0, END)
        else:    
            messagebox.showinfo("Multiplication", "You are wrong")
            nextbtn1.place_forget()
            txt.delete(0, END)
    except:
        messagebox.showinfo("error!", "The format of the calculation result you entered is incorrect！")
        nextbtn1.place_forget()
        txt.delete(0, END)
def next1():
    global a
    global b
    global var1
    global txt
    global lbl1
    global lbl2
    global lbl3
    global exitmenu
    var1=tk.StringVar()
    a=random.randint(1,10) #随机数
    b=random.randint(10,20) #另一个随机数
    lbl1 = Label(window, text="How much is a*b？")
    lbl1.place(x=0,y=0)
    txt=tk.Entry(window,width=10,textvariable=var1,show=None)
    txt.place(x=175,y=0)
    lbl2 = Label(window,  text='a:%s'%a)
    lbl3 = Label(window, text='b:%s'%b)
    lbl2.place(x=0,y=20)
    lbl3.place(x=0,y=40)
    chenfa.place_forget()
    add.place_forget()
    nextbtn1.place_forget()
    exitmenu.place(x=190,y=240)
    clicked1.place(x=310,y=0)
def exitmenu():
    lbl1.place_forget()
    lbl2.place_forget()
    lbl3.place_forget()
    txt.place_forget()
    exitmenu.place_forget()
    nextbtn1.place_forget()
    nextbtn2.place_forget()
    clicked1.place_forget()
    clicked2.place_forget()
    add.place(x=169,y=50)
    chenfa.place(x=169,y=150)
    endbtn.place(x=0,y=240)
def openmenu():
    about.place_forget()
    add.place(x=169,y=50)
    chenfa.place(x=169,y=150)
    go.place_forget()
    endbtn.place(x=0,y=240)
def about():
    messagebox.showinfo("About", "Author:KEYS-ME\nVersion:1.0\nLanguage:en")
def jiafa():
    global var1
    global txt
    global nextbtn2
    global a
    global b
    global lbl1
    global lbl2
    global lbl3
    global exitmenu
    nextbtn2.place_forget()
    var1=tk.StringVar()
    add.place_forget()
    a=random.randint(1,1000) #随机数
    b=random.randint(1,1000) #另一个随机数
    lbl1 = Label(window, text="How much is a+b？")
    lbl1.place(x=0,y=0)
    txt=tk.Entry(window,width=10,textvariable=var1,show=None)
    txt.place(x=175,y=0)
    lbl2 = Label(window,text='a:%s'%a)
    lbl3 = Label(window,text='b:%s'%b)
    lbl2.place(x=0,y=20)
    lbl3.place(x=0,y=40)
    chenfa.place_forget()
    add.place_forget()
    clicked2.place(x=310,y=0)
    exitmenu.place(x=190,y=240)
def clickedadd():
    global num
    global nextbtn2
    num=var1.get()
    try:
        if int(num)==a+b:
            messagebox.showinfo("Addition operation", "Congratulations, that's right! Try the next question！")
            nextbtn2.place(x=310,y=0)
            clicked2.place_forget()
            txt.delete(0, END)
        else:    
            messagebox.showinfo("Addition operation", "You are wrong")
            nextbtn2.place_forget()
            txt.delete(0, END)
    except:
        messagebox.showinfo("error!", "The format of the calculation result you entered is incorrect！")
        nextbtn2.place_forget()
        txt.delete(0, END)


go = Button(window,text='start',font=('Arial,12'),compound="left",width=20,height=2,command=openmenu)
clicked1 = Button(window,text='check',font=('Arial,12'),compound="left",width=20,height=2,command=chenfa)
clicked2 = Button(window,text='check',font=('Arial,12'),compound="left",width=20,height=2,command=clickedadd)
endbtn = Button(window,text='exit',font=('Arial,12'),compound="left",width=20,height=2,command=callback)
nextbtn1 = Button(window,text='next',font=('Arial,12'),compound="left",width=20,height=2,command=next1)
nextbtn2 = Button(window,text='next',font=('Arial,12'),compound="left",width=20,height=2,command=jiafa)
add = Button(window,text='addition',font=('Arial,12'),compound="left",width=20,height=2,command=jiafa)
chenfa = Button(window,text='multiplication',font=('Arial,12'),compound="left",width=20,height=2,command=next1)
exitmenu = Button(window,text='back menu',font=('Arial,12'),compound="left",width=20,height=2,command=exitmenu)
about = Button(window,text='about',font=('Arinal,12'),compound="left",width=20,height=2,command=about)
go.place(x=150,y=110)
about.place(x=0,y=240)
window.protocol("WM_DELETE_WINDOW",callback)

window.mainloop()