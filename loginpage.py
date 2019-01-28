import sys
from backend import *
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import loginpage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    loginpage_support.set_Tk_var()
    top = LOGIN (root)
    loginpage_support.init(root, top)
    root.mainloop()

w = None
def create_LOGIN(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    loginpage_support.set_Tk_var()
    top = LOGIN (w)
    loginpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_LOGIN():
    global w
    w.destroy()
    w = None


class LOGIN:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {@Yu Gothic Medium} -size 12 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x475")
        top.title("LOGIN")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.25, rely=0.0, height=166, width=302)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="./projectimages/loginmain.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''LOGIN''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.158, rely=0.358, height=26, width=435)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#828282")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Welcome back ! Login to access SPAT''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.417, rely=0.484,height=34, relwidth=0.407)
        self.Entry1.configure(background="#f7f7f7")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=loginpage_support.Username)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.417, rely=0.611,height=34, relwidth=0.407)
        self.Entry2.configure(background="#f7f7f7")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(show="*")
        self.Entry2.configure(textvariable=loginpage_support.Password)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.217, rely=0.484, height=36, width=112)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Username''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.217, rely=0.611, height=36, width=108)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Password''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.2, rely=0.8, height=43, width=186)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#0c64e8")
        self.Button1.configure(command=loginpage_support.signin)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SIGN IN''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.575, rely=0.8, height=43, width=176)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#0c64e8")
        self.Button2.configure(command=loginpage_support.signup)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''SIGN UP''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.892, rely=0.0, height=53, width=56)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self._img2 = PhotoImage(file="./projectimages/camicon1.png")
        self.Button3.configure(image=self._img2)
        self.Button3.configure(pady="0")
        self.Button3.configure(relief=FLAT)
        self.Button3.configure(text='''Button''')
        self.Button3.configure(width=56)
        self.Button3.configure(command=loginpage_support.facerec)



if __name__ == '__main__':
    vp_start_gui()
