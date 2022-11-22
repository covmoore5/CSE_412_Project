from tkinter import *
from tkinter import ttk
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(1, parent_path)

import queryScripts as qs


root = Tk()
frame = ttk.Frame(root, padding=50)
frame.grid()

sideEffectsRes = Label(frame, height = 100, width = 52)
medNameEntry = Entry(frame)


def findSE():
    rows = qs.find_ind_for_med(medNameEntry.get())
    temp = ""
    for row in rows:
        temp += row[0] + "\n"
    sideEffectsRes.config(text=temp)

title = Label(frame, text="Medicine App!").grid(column=1, row=0)
medNameLbl = Label(frame, text="Enter a Medicine Name:").grid(column=0, row=1)

medNameEntry.grid(column=1, row=1)
lookupSEBtn = Button(frame, text="Enter to find Side Effects", command=findSE).grid(column=2, row=1)
sideEffectsRes.grid(column=0, row=2)

root.mainloop()


    