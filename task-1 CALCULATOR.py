import tkinter as tk
from tkinter import messagebox
w=tk.Tk()
w.title("CALCULATOR")
w.minsize(300,300)
tk.Label(w,text="CALCULATOR",fg='blue',font=("Verdana", 12,"bold")).grid(row=0,column=1)

def add():
    a=int(e1.get())
    b=int(e2.get())
    ans=a+b
    r.delete(0,tk.END)
    r.insert(0,ans)

def sub():
    a=int(e1.get())
    b=int(e2.get())
    ans=a-b
    r.delete(0,tk.END)
    r.insert(0,ans)

def multi():
    a=int(e1.get())
    b=int(e2.get())
    ans=a*b
    r.delete(0,tk.END)
    r.insert(0,ans)

def div():
    a=int(e1.get())
    b=int(e2.get())
    if b!=0:
        ans=a/b
        r.delete(0,tk.END)
        r.insert(0,ans)
    else:
        messagebox.showerror("ERROR"," 0 CANNOT BE A DENOMINATOR")

#GUI
v1=tk.Label(w,text='value 1').grid(row=2,column=0)
e1=tk.Entry(w)
e1.grid(row=2,column=1)

v2=tk.Label(w,text='value 2').grid(row=3,column=0)
e2=tk.Entry(w)
e2.grid(row=3,column=1)

f=tk.Frame(w)
tk.Button(f,text='+',bd=5,bg='green',fg='white',command=add).grid(row=4,column=0)
tk.Button(f,text='-',bd=5,bg='green',fg='white',command=sub).grid(row=4,column=1)
tk.Button(f,text='*',bd=5,bg='green',fg='white',command=multi).grid(row=4,column=2)
tk.Button(f,text='/',bd=5,bg='green',fg='white',command=div).grid(row=4,column=3)
f.grid(row=5,column=1)

tk.Label(w,text='RESULT').grid(row=6,column=0)
r=tk.Entry(w)
r.grid(row=6,column=1)
w.mainloop()
