import sys
from backend import *
import loginpage

try:
    from Tkinter import *
    from Tkinter import messagebox
except ImportError:
    from tkinter import *
    from tkinter import messagebox
    
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global Username
    global Password
    Username = StringVar()
    Password = StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def signin():
    data=search(Username.get(),Password.get())
    if data==():
        Username.set('')
        Password.set('')
        messagebox.showerror("Error", "Invalid Username or Password\nTry Again!!")
    else:
        destroy_window()
        import os
        os.system('python admin_dashboard.py')
        
def signup():
    user=Username.get()
    passw=Password.get()
    if user.strip()=='' or passw.strip=='':
        messagebox.showerror("Error", "Please fill username and password")
    else:
        data=insert(Username.get(),Password.get())

def facerec():
    destroy_window()
    import os
    os.system('python base.py')
    

if __name__ == '__main__':
    import loginpage
    loginpage.vp_start_gui()


