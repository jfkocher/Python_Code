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

window.geometry('450x200')

#window.configure(background = 'Gray64')

directory_base_check = '\\eccifs\home2$\jfkocher\home\Python Scripts\Practice\Practice Folder for Batch Production'

style = Style()
#style.layout()

lbl_description = Label(window, text='Enter the Directory and type of Data Request to create standard folders')
lbl_description.grid(column=0,row=0, columnspan = 2, pady = 5, sticky=W+E+N+S)

lbl_path = Label(window, text='Directory:').grid(row=2, sticky = E, pady = 20)
#lbl_path.grid(column=0,row=2, pady = 20)

directory_input = Entry(window,width=50)
directory_input.grid(column=1, row=2, sticky = W, padx = 5)


lbl_combo = Label(window, text='Data Request Type:').grid(row=4, sticky = W)
#lbl_combo.grid(column=0,row=4)
#Types of Data Requests
dr_type = Combobox(window)
dr_type['values']= ('External with DA','External without DA','Internal','Recurring Reporting')
dr_type.current(0) #set the selected item
dr_type.grid(column=1, row=4, sticky =W, padx = 5)

def print_text(input_text):
    lbl_display['text'] = input_text

def directory_create():
    dr_type_ans = dr_type.get()
    dir_ans = directory_input.get()

    #Create Error if Folder path does not match preferred
    if directory_base_check in dir_ans:
        pass
    else:
        print('Recheck Directory: Incorrect Directory')
        print_text('Recheck Directory: Incorrect Directory')



btn = Button(window, text="Create Folders",command=directory_create)
btn.grid(column=0, row=5, pady = 20)

lbl_display = Label(window, text = '')
lbl_display.grid(column = 1, row = 5, sticky=W+E+N+S, pady = 20, padx = 5)
lbl_display.configure(background = 'gray64')



#combo.get()

window.mainloop()
