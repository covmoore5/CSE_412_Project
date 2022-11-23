from tkinter import *
from tkinter import ttk
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(1, parent_path)

import queryScripts as qs


root = Tk()
root.title("Medicine App!")
frame = ttk.Frame(root, padding=50)
frame.grid()


def findSE():
    listbox.delete(0, END)
    rows = qs.find_ind_for_med(medNameEntry.get())
    for row in rows:
        print(row)
        listbox.insert(END, row[0])
        

### CODE FOR SIDE EFFECTS OF MEDICINE

medNameEntry = Entry(frame)
title = Label(frame, text="Find Side Effects of a Medicine").grid(column=1, row=0)
medNameLbl = Label(frame, text="Enter a Medicine Name:").grid(column=0, row=1)

medNameEntry.grid(column=1, row=1)
lookupSEBtn = Button(frame, text="Find Side Effects", command=findSE).grid(column=2, row=1)

scroll = Scrollbar(frame, width=10)
listbox=Listbox(frame, background="Blue", fg="white",selectbackground="Red", yscrollcommand=scroll, width=50)
scroll.config( command = listbox.yview)

scroll.grid(column=2, row=2)
listbox.grid(column=0, row=2, columnspan=3)


### CODE FOR INDICATIONS OF MEDICINE





root.mainloop()


    