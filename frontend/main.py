from tkinter import *
from tkinter import ttk



root = Tk()
frame = ttk.Frame(root, padding=200)
frame.grid()

sideEffectsRes = Label(frame)
medNameEntry = Entry(frame)

def findSE():
    sideEffectsRes.config(text="Side Effects for {0} Found".format(medNameEntry.get()))

title = Label(frame, text="Medicine App!").grid(column=1, row=0)
medNameLbl = Label(frame, text="Enter a Medicine Name:").grid(column=0, row=1)

medNameEntry.grid(column=1, row=1)
lookupSEBtn = Button(frame, text="Enter to find Side Effects", command=findSE).grid(column=2, row=1)
sideEffectsRes.grid(column=0, row=2)

root.mainloop()


    