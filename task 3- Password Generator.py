import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    length = int(e.get())
    try:
        if length!='':
            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.sample(characters, length))
            label_output.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showwarning('WARNING!!','PLEASE ENTER THE LENGTH!!')
        print('no value added')
        
def copy_to_clipboard():
    password = label_output.cget("text").replace("Generated Password: ", "")
    if password:
        w.clipboard_clear()
        w.clipboard_append(password)
        w.update()
        messagebox.showinfo("Copied!", "Password copied to clipboard!")
        
#GUI
w=tk.Tk()
w.minsize(500,300)
w.title("PASSWORD GENERATOR")
tk.Label(w,text='PASSWORD GENERATOR',fg='blue',bd=5,bg='pink').grid(row=0,column=1)
tk.Label(w,text='ENTER PASSWORD LENGTH',padx=10,pady=5).grid(row=2,column=0)
e=tk.Entry(w)
e.grid(row=2,column=1)
tk.Button(w,text='COPY TO CLIPBOARD',fg='blue',command=copy_to_clipboard).grid(row=5,column=1)
tk.Button(w,text='Generate Password',fg='red',command=generate_password).grid(row=4,column=1)
label_output=tk.Label(w,text='')
label_output.grid(row=5,column=1)

w.mainloop()
