# Create a GUI program for Calendar using python tkinter. 

from calendar import*
from tkinter import*
gour=Tk()
gour.title("Calender")
gour.geometry("200x300")
def show():
    m=int(mont.get())
    y=int(year.get())
    output.delete(0,0,END)
    output.insert(INSERT,month(y,m))

Label(gour,text="month:").pack()
mont=Spinbox(gour,from_=1,to=12)
mont.pack()
Label(gour,text="year:").pack()
year=Spinbox(gour,from_=1900,to=2100)
year.pack()

Button(gour,text="show",command=show).pack()
output=Text(gour,width=20,height=10,wrap=WORD)
output.pack()
gour.mainloop()


