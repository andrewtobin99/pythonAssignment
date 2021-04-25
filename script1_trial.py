#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:07:30 2021

@author: andrewtobin
"""

import tkinter as tk    # from tkinter import Tk for Python 3.x
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd

window = tk.Tk()
greeting = tk.Label(text = "Welcome to File Selector")
greeting.pack()

def getFiles ():
    global df
    global import_file_path
    import_file_path = filedialog.askopenfilename( filetypes = (("csv Files", "*.csv"),("JSON Files", "*.json")))
    if import_file_path[-3:] == 'csv':
        df = pd.read_csv(import_file_path)
    elif import_file_path[-4:] == 'json':
        df = pd.read_json(import_file_path)
    else:
        print('Invalid file type')
    
browsebtn_Files = tk.Button(text='Import Files', command=getFiles, bg='green' ///////
                               , fg='black', 
                               font=('helvetica', 12, 'bold'))
browsebtn_Files.pack()

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application',
                                        'Are you sure you want to exit the application',
                                        icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
        
button1 = tk.Button (window, text='Exit Application',
                     command=ExitApplication,bg='brown',fg='black',
                     font = ('helvetica', 12, 'bold'))
button1.pack()
output_title = tk.Label(text = "Output")
output_title.pack()
output_frm = tk.Frame(relief = tk.SUNKEN, borderwidth=5)
output_frm.pack()
frame_lbl = tk.Label(master= output_frm, text = "import_file_path")
frame_lbl.pack()
window.mainloop()
