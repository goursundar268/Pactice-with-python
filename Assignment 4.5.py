from tkinter import *
gour=Tk()
gour.title("My Application")
gour.geometry("250x350")
#gour.resizable(0,0)
gour.iconbitmap("cal_logo.ico")
#gour.configure(background="aqua")

exp= ""
def btn_click(num):
    global exp
    exp=exp+str(num)
    var.set(exp)

def equal():
    global exp
    exp=str(eval(exp))
    var.set(exp)


def clear():
    global exp
    var.set("")
    exp= ""

def backspace():
    global exp
    exp=exp[:len(exp)-1]
    var.set(exp)


var=StringVar()
A=Entry(gour,textvariable=var,bg="gray",width=19,font="normal")
A.place(x=21,y=4)

x=Frame(gour,height=300,width=300)
x.place(x=20,y=30)

#--------------------------------------------------------------------------1st rows

clear=Button(x,text="AC",height=2,width=4,font="normal",command=clear)
clear.grid(row=0,column=0)

a2=Button(x,text="%",height=2,width=4,font="normal",command=lambda:btn_click("%")).grid(row=0,column=1)

backspace=Button(x,text="⌫",height=2,width=4,font="normal",command=backspace).grid(row=0,column=2)

a4=Button(x,text="/",height=2,width=4,font="normal",command=lambda:btn_click("/")).grid(row=0,column=3)

#--------------------------------------------------------------------------2nd rows

b1=Button(x,text="7",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("7")).grid(row=1,column=0)

b2=Button(x,text="8",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("8")).grid(row=1,column=1)

b3=Button(x,text="9",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("9")).grid(row=1,column=2)

b4=Button(x,text="*",height=2,width=4,font="normal",command=lambda:btn_click("*")).grid(row=1,column=3)

#--------------------------------------------------------------------------3rd rows

c1=Button(x,text="4",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("4")).grid(row=2,column=0)

c2=Button(x,text="5",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("5")).grid(row=2,column=1)

c3=Button(x,text="6",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("6")).grid(row=2,column=2)

c4=Button(x,text="-",height=2,width=4,font="normal",command=lambda:btn_click("-")).grid(row=2,column=3)

#-------------------------------------------------------------------------4ed rows

d1=Button(x,text="1",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("1")).grid(row=3,column=0)

d2=Button(x,text="2",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("2")).grid(row=3,column=1)

d3=Button(x,text="3",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("3")).grid(row=3,column=2)

d4=Button(x,text="+",height=2,width=4,font="normal",command=lambda:btn_click("+")).grid(row=3,column=3)

#-------------------------------------------------------------------------4ed rows

e1=Button(x,text="00",height=2,width=4,font="normal",command=lambda:btn_click("00")).grid(row=4,column=0)

e2=Button(x,text="0",height=2,width=4,font="normal",bg="pink",command=lambda:btn_click("0")).grid(row=4,column=1)

e3=Button(x,text=".",height=2,width=4,font="normal",command=lambda:btn_click(".")).grid(row=4,column=2)

equal=Button(x,text="=",height=2,width=4,font="normal",command=equal).grid(row=4,column=3)

gour.mainloop() 