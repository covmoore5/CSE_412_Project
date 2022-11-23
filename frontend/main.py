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
    rows = qs.find_se_for_med(medNameEntry.get())
    for row in rows:
        listbox.insert(END, row[0])

def findIndication():
    listbox2.delete(0, END)
    rows = qs.find_ind_for_med(medNameEntry2.get())
    for row in rows:
        listbox2.insert(END, row[0])
        

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
medNameEntry2 = Entry(frame)
indicationTitle = Label(frame, text="Find Indications of a Medicine").grid(column=1, row=4)
medNameLbl2 = Label(frame, text="Enter a Medicine Name:").grid(column=0, row=5)

medNameEntry2.grid(column=1, row=5)
lookupIndBtn = Button(frame, text="Find Side Effects", command=findIndication).grid(column=2, row=5)

scroll2 = Scrollbar(frame, width=10)
listbox2=Listbox(frame, background="Blue", fg="white",selectbackground="Red", yscrollcommand=scroll2, width=50)
scroll2.config( command = listbox.yview)

scroll2.grid(column=2, row=6)
listbox2.grid(column=0, row=6, columnspan=3)




root.mainloop()


    