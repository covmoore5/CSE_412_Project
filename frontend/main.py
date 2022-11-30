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

### FUNCTIONS

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

def findPresc():
    listbox3.delete(0, END)
    rows = qs.find_patient_presc(medNameEntry3.get())
    for row in rows:
        listbox3.insert(END, row[0])

def getAllPatients():
    listbox4.delete(0, END)
    rows = qs.get_all_patients()
    listbox4.insert(0, "NAME \t NUMBER")
    for row in rows:
        temp = "{0}, \t {1}".format(row[0],row[1])
        listbox4.insert(END, temp)

def getMedsWithInd():
    listbox5.delete(0, END)
    rows = qs.get_med_with_ind(medNameEntry5.get())
    for row in rows:
        listbox5.insert(END, row[0])
        

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
lookupIndBtn = Button(frame, text="Find Indications", command=findIndication).grid(column=2, row=5)

scroll2 = Scrollbar(frame, width=10)
listbox2=Listbox(frame, background="Blue", fg="white",selectbackground="Red", yscrollcommand=scroll2, width=50)
scroll2.config( command = listbox.yview)

scroll2.grid(column=2, row=6)
listbox2.grid(column=0, row=6, columnspan=3)


### CODE FOR GETTING PATIENT PRESCRIPTIONS
medNameEntry3 = Entry(frame)
prescriptionTitle = Label(frame, text="Find a Patient's Prescriptions").grid(column=1, row=7)
medNameLbl3 = Label(frame, text="Enter a Patient Name:").grid(column=0, row=8)

medNameEntry3.grid(column=1, row=8)
lookupPrescBtn = Button(frame, text="Find Patient's Prescriptions", command=findPresc).grid(column=2, row=8)

scroll3 = Scrollbar(frame, width=10)
listbox3=Listbox(frame, background="Blue", fg="white",selectbackground="Red", yscrollcommand=scroll3, width=50)
scroll3.config( command = listbox3.yview)

scroll3.grid(column=2, row=9)
listbox3.grid(column=0, row=9, columnspan=3)


### CODE FOR GETTING PATIENT NAMES AND PHONE NUMBERS
medNameEntry4 = Entry(frame)
patientTitle = Label(frame, text="Get Patient Names and Patient ID").grid(column=4, row=0)
medNameLbl4 = Label(frame, text="Enter Admin Password:").grid(column=3, row=1)

medNameEntry4.grid(column=4, row=1)
lookupPatBtn = Button(frame, text="Get Patients", command=getAllPatients).grid(column=5, row=1)

scroll4 = Scrollbar(frame, width=10)
listbox4=Listbox(frame, background="Blue", fg="white",selectbackground="Red", yscrollcommand=scroll4, width=50)
scroll4.config( command = listbox4.yview)

scroll4.grid(column=6, row=2)
listbox4.grid(column=3, row=2, columnspan=3)

### CODE FOR GETTING ALL MEDICINE WITH SAME INDICAITON

medNameEntry5 = Entry(frame)
indTitle = Label(frame, text="Find Medication with the same Indication").grid(column=4, row=4)
medNameLbl5 = Label(frame, text="Enter Indication:").grid(column=3, row=5)

medNameEntry5.grid(column=4, row=5)
lookupIndBtn = Button(frame, text="Get Medicines", command=getMedsWithInd).grid(column=5, row=5)

scroll5 = Scrollbar(frame, width=10)
listbox5=Listbox(frame, background="Blue", fg="white",selectbackground="Red", yscrollcommand=scroll5, width=50)
scroll5.config( command = listbox5.yview)

scroll5.grid(column=6, row=6)
listbox5.grid(column=3, row=6, columnspan=3)


root.mainloop()


    