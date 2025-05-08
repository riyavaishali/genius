from tkinter import *
import random as r

def pass_generator():
    char='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*/'
    length=int(entry_length.get())
    password=r.sample(char,length)
    password="".join(password)
    display_entry.config(text=password)

root=Tk()
root.geometry("400x400")
root.title("Password Generator")

label_length=Label(root,text="Enter length")
label_length.grid(row=1,column=1)

entry_length=Entry(root)
entry_length.grid(row=1,column=2)

generate=Button(root,text="Generate",command=pass_generator)
generate.grid(row=3,column=2)

display_label=Label(root,text="Password")
display_label.grid(row=2,column=1)

display_entry=Label(root,text="None",bd=5)
display_entry.grid(row=2,column=2)

mainloop()