'''
The purpose of this python script is to produce a program, that when run, will provide two input options:
1. File path
2. Type of directory

One inputted, the program will create a directory with sub folders for data requests.
The best package to use may be Tkinter.
'''
from tkinter import *
from tkinter.ttk import *
import tkinter
import os

window = Tk()

window.title("Batch File")

window.geometry('500x200')

directory_base_check = '\\eccifs\home2$\jfkocher\home\Python Scripts\Practice\Practice Folder for Batch Production'

style = Style()
#style.layout()

lbl_description = Label(window, text='Enter the Directory and type of Data Request to create standard folders')
lbl_description.grid(column=1,row=0)

lbl_path = Label(window, text='Directory:')
lbl_path.grid(column=0,row=2)

directory_input = Entry(window,width=50)
directory_input.grid(column=1, row=2)


lbl_combo = Label(window, text='Data Request Type:')
lbl_combo.grid(column=0,row=4)
#Types of Data Requests
dr_type = Combobox(window)
dr_type['values']= ('External with DA','External without DA','Internal','Recurring Reporting')
dr_type.current(0) #set the selected item
dr_type.grid(column=1, row=4)


def directory_create():
    dr_type_ans = dr_type.get()
    dir_ans = directory_input.get()

    #Create Error if Folder path does not match preferred
    if directory_base_check in dir_ans:
    #Create the Directory
        os.chdir(dir_ans)
        os.mkdir("1_Input")
        os.mkdir("1_Input\\Matching")
        os.mkdir("2_Working")
        os.mkdir("3_Files_to_QA")
        os.mkdir("4_Final")
        os.mkdir("5_Deliverable")
    else:
        print('Recheck Directory: Incorrect Directory')



btn = Button(window, text="Create Folders",command=directory_create)
btn.grid(column=1, row=5)

#combo.get()

window.mainloop()

