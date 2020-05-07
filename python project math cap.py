from tkinter import *
import random
from tkinter import messagebox
obj=Tk()
obj.title("mathematical captcha")
obj.configure(bg="lavender")
fincap=0
def captcha():
    L=Label(compound=CENTER,text="MATHEMATICAL CAPTCHA",height=7,bg="thistle",fg="blue",font=("verdana",38,"bold italic")).pack(fill=X)
    l2=Label(text="prove that you are not a robot",anchor=CENTER,bg="thistle",fg="blue",font=("verdana",18,"bold italic")).pack(fill=X)

    def check():
        st=''
        sm=''
        inp=e1.get()
        global fincap
        print(type(inp))
        print(type(fincap),fincap)
        if(inp!=""):
            if (str(fincap) == inp):
                messagebox.showinfo("guide", "MATCHED")
                e1.delete(0,"end")
                obj.destroy()
            else:
                messagebox.showwarning("guide", "not a match")
                messagebox.showwarning("GUIDE","TRY AGAIN")
                e1.delete(0, "end")
                mainer()
        else:
            messagebox.showwarning("guide","empty")
    def mainer():
        st=''
        nums=[x for x in range(1,10)]
        num_1=random.choice(nums)
        num_2=random.choice(nums)
        global fincap
        fincap=num_1+num_2
        st=str(num_1)+'+'+str(num_2)
        la.config(text=st)

    objt = Frame(obj)
    objt.pack()
    la=Label(text="     ",bg="blue",fg="white",font=("verdana",28,"italic bold"))
    la.pack()
    e1 = Entry(obj, width=20, fg="black", font=("verdana", 28, "bold italic"))
    e1.pack()
    bu = Button(objt, text="refresh", command=mainer)
    bu.pack(side=LEFT)
    sub = Button(objt, text="submit", command=check)
    sub.pack(side=LEFT)
    mainer()


captcha()

obj.mainloop()
