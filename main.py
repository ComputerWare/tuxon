from tkinter import filedialog, Tk
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import webbrowser
import os

t = Tk()
t.title('Tuxon IDE')
t.geometry('802x430')
scrollbar = Scrollbar(t)
scrollbar.pack(side = RIGHT, fill = Y)
menubar = Menu(t)

# Functions
def open_file():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    global path1
    path1 = askopenfile(mode='r', filetypes = files, defaultextension = files)
    print(path1.name)
    opened_file = open(path1.name, 'r')
    wrrunFile = open('runFile.txt', 'w')
    if path1:
        content = opened_file.read()
        wrrunFile.write(path1.name)
        wrrunFile.close()
        inputtxt.insert(INSERT, content)
    
def new_window():
    os.system("./tuxon")
    
def new():
    global path1
    files = [('Python Files', '*.py')]
    path1 = asksaveasfile(filetypes = files, defaultextension = files)
    
def close_window():
    t.destroy()
    
def about():
    tkinter.messagebox.showinfo("About","Tuxon version: 1.1, Python version: 3, Developer email: evansergi851@outlook.com")
    
def preview():
    runfile = open('runFile.txt', 'r')
    if file:
        filerun = runfile.read()
        os.system("/bin/python3 "+filerun)
        runfile.close()
    
def savefile():
    global path1
    code = inputtxt.get(1.0, "end-1c")
    f = open(path1.name, 'w')
    if file:
        f.write(code)
    # close the file
    f.close()

def online_help():
    webbrowser.open('https://piware.w3spaces.com')
# Files Menu Bar
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = new)
file.add_command(label ='New Window', command = new_window)
file.add_separator()
file.add_command(label ='Save', command = savefile)
file.add_command(label ='Open', command = open_file)
file.add_separator()
file.add_command(label ='Quit', command = close_window)

# Run Menu Bar
run = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Run', menu = run)
run.add_command(label ='Run File', command = preview)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='About', command = about)
help_.add_command(label ='Help', command = online_help)
t.config(menu = menubar)

inputtxt = Text(t, height = None, width = None, bg = "white")
inputtxt.pack(expand=True, fill=BOTH)

scrollbar.config(command = inputtxt.yview)

t.mainloop()
