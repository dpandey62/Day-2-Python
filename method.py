from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("ADD")
root.geometry("500x500")
root.resizable(width=False, height=False)
B1 = Button(root, text = "BUTTON 1")
B1.place(relx = 1,x=0, y=0, anchor=NE)
L = Label(root, text = "LABEL 1")
L.place(anchor = NW)
B2 = Button(root, text = "BUTTON 2")
B2.place(relx = 0.5, rely = 0.5, anchor=CENTER)
root .mainloop()