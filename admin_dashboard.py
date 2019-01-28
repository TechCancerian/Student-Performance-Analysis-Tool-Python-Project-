import sys
import datetime
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import openpyxl
sns.set(style="darkgrid")

try:
    from Tkinter import *
    from Tkinter import filedialog
    from Tkinter import messagebox
except ImportError:
    from tkinter import *
    from tkinter import filedialog
    from tkinter import messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global data
    data = StringVar()
    global summary
    summary=StringVar()
    global timestamp
    timestamp=StringVar()
    global img1
    img1="./graph1.png"
    global img2
    img2="./graph2.png"
    
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    set_Tk_var()
    top = ADMIN_DASHBOARD (root)
    init(root, top)
    root.mainloop()

w = None
def create_ADMIN_DASHBOARD(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = ADMIN_DASHBOARD (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_ADMIN_DASHBOARD():
    root.destroy()


def texttospeechdata():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(data.get())
    engine.setProperty('rate',100)  #100 words per minute
    engine.setProperty('volume',0.9)
    engine.runAndWait()

def texttospeechsum():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(summary.get())
    engine.setProperty('rate',100)  #100 words per minute
    engine.setProperty('volume',0.9)
    engine.runAndWait()

def addnew():
    root=Tk()
    # define Labels
    l1 = Label(root, text='Roll No')
    l1.grid(row=0, column=0)

    l2 = Label(root, text='Name')
    l2.grid(row=0, column=2)

    l3 = Label(root, text='Section')
    l3.grid(row=1, column=0)

    l4 = Label(root, text='ADBMS')
    l4.grid(row=1, column=2)
    
    l5 = Label(root, text='DS')
    l5.grid(row=2, column=0)

    l6 = Label(root, text='Python')
    l6.grid(row=2, column=2)
    

    # define Entries
    rollno_text=StringVar()
    e1=Entry(root,textvariable=rollno_text)
    e1.grid(row=0, column=1)

    name_text=StringVar()
    e2=Entry(root,textvariable=name_text)
    e2.grid(row=0, column=3)

    section_text=StringVar()
    e3=Entry(root,textvariable=section_text)
    e3.grid(row=1, column=1)

    adbms_text=StringVar()
    e4=Entry(root,textvariable=adbms_text)
    e4.grid(row=1, column=3)
    
    ds_text=StringVar()
    e5=Entry(root,textvariable=ds_text)
    e5.grid(row=2, column=1)
    
    python_text=StringVar()
    e6=Entry(root,textvariable=python_text)
    e6.grid(row=2, column=3)

    def returning():
            rollno,name,section,adbms,ds,python=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()
            row=[rollno,name,section,adbms,ds,python]
            try:
                with open(filename,'r') as file1:
                    existingLines = [line for line in csv.reader(file1, delimiter=',')]
                with open(filename,'a',newline='') as file2:
                    reader2 = csv.writer(file2,delimiter=',')
                    cnt=1
                    for line in existingLines:
                        if row[0] in line:
                            data.set('Record already exists')
                            cnt=0
                            break
                        else:
                            continue
                    if cnt==1:
                        reader2.writerow(row)
                if(cnt==1):
                    df=pd.read_csv(filename,encoding="ISO-8859-1",index_col="Rollno")
                    viewall()
                    sales_report = pd.pivot_table(df, index=["Section"], values=["ADBMS", "Python","DS"],\
                                  aggfunc=[np.max, np.min], fill_value=0)
                    val=str(sales_report)+"\n\n\n"+str(df.describe().round(2))
                    summary.set(val)
                    timestamp.set(datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp()).isoformat())
                    graph1=sns.lmplot('ADBMS', 'Python', data=df,\
                    hue='Section', fit_reg=False,palette="Set1",markers=["o","+","*"],height=3,aspect=1.7)
                    plt.savefig('graph1.png')
                    plt.close()
                    fig, ax = plt.subplots()
                    fig.set_size_inches(6, 3.5)
                    graph2=sns.boxplot(data=df,width=0.2,ax=ax);
                    plt.savefig('graph2.png')
                    plt.close()
                    img1="./graph1.png"
                    img2="./graph2.png"
                    setimg1()
                    setimg2()
                    messagebox.showinfo("Message", "1 Record Added!")
            except (NameError , FileNotFoundError):
                data.set("Please select a file first")
                messagebox.showerror("Error", "Select a file first!")
            root.destroy()
    
    #button
    B = Button(root, text ="OK",width=12, command = returning)
    B.grid(row=3, column=2)
     
def delete():
        root=Tk()
        #define Labels
        l1 = Label(root, text='Roll No')
        l1.grid(row=0, column=0)

    # define Entries
        rollno_text=StringVar()
        e1=Entry(root,textvariable=rollno_text)
        e1.grid(row=0, column=1)


        def returning():
            rollno=e1.get()
            row=[rollno]
            try:
                with open(filename,'r') as file1:
                    existingLines = [line for line in csv.reader(file1, delimiter=',')]
                with open(filename,'w',newline='') as file2:
                    reader2 = csv.writer(file2,delimiter=',')
                    cnt=1
                    for line in existingLines:
                        if row[0] in line:
                            cnt=0
                            continue
                        else:
                            reader2.writerow(line)
                if cnt==1:
                    data.set("Record does not exists")
                else:
                    df=pd.read_csv(filename,encoding="ISO-8859-1",index_col="Rollno")
                    viewall()
                    sales_report = pd.pivot_table(df, index=["Section"], values=["ADBMS", "Python","DS"],\
                                    aggfunc=[np.max, np.min], fill_value=0)
                    val=str(sales_report)+"\n\n\n"+str(df.describe().round(2))
                    summary.set(val)
                    timestamp.set(datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp()).isoformat())
                    graph1=sns.lmplot('ADBMS', 'Python', data=df,\
                    hue='Section', fit_reg=False,palette="Set1",markers=["o","+","*"],height=3,aspect=1.7)
                    plt.savefig('graph1.png')
                    plt.close()
                    fig, ax = plt.subplots()
                    fig.set_size_inches(6, 3.5)
                    graph2=sns.boxplot(data=df,width=0.2,ax=ax);
                    plt.savefig('graph2.png')
                    plt.close()
                    img1="./graph1.png"
                    img2="./graph2.png"
                    setimg1()
                    setimg2()
                    messagebox.showinfo("Message", "1 Record Deleted!")

            except (NameError,FileNotFoundError):
                data.set("Please select a file first")
                messagebox.showerror("Error", "Select a file first!")
            root.destroy()
    
    #button
        B = Button(root, text ="OK",width=12, command = returning)
        B.grid(row=0, column=2)
        root.mainloop()

def search():
    root=Tk()
    # define Labels
    l1 = Label(root, text='Roll No')
    l1.grid(row=0, column=0)

    l2 = Label(root, text='Name')
    l2.grid(row=0, column=2)

    l3 = Label(root, text='Section')
    l3.grid(row=1, column=0)

    l4 = Label(root, text='ADBMS')
    l4.grid(row=1, column=2)
    
    l5 = Label(root, text='DS')
    l5.grid(row=2, column=0)

    l6 = Label(root, text='Python')
    l6.grid(row=2, column=2)
    

    # define Entries
    rollno_text=StringVar()
    e1=Entry(root,textvariable=rollno_text)
    e1.grid(row=0, column=1)

    name_text=StringVar()
    e2=Entry(root,textvariable=name_text)
    e2.grid(row=0, column=3)

    section_text=StringVar()
    e3=Entry(root,textvariable=section_text)
    e3.grid(row=1, column=1)

    adbms_text=StringVar()
    e4=Entry(root,textvariable=adbms_text)
    e4.grid(row=1, column=3)
    
    ds_text=StringVar()
    e5=Entry(root,textvariable=ds_text)
    e5.grid(row=2, column=1)
    
    python_text=StringVar()
    e6=Entry(root,textvariable=python_text)
    e6.grid(row=2, column=3)

    def returning():
        rollno,name,section,adbms,ds,python=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()
        row=[rollno,name,section,adbms,ds,python]
        try:
            with open(filename,'r') as file1:
                existingLines = [line for line in csv.reader(file1, delimiter=',')]
                cnt=1
                rec=0
                findings=[]
                for line in existingLines:
                    if (row[0] in line) or (row[1] in line) or (row[2] in line) or (row[3]==line[3]) or (row[4]==line[4]) or (row[5]==line[5]):
                        cnt=0
                        findings.append(line)
                        rec=rec+1
                    else:
                        continue
            if cnt==1 or findings==[]:
                data.set("No record found")
            else:
                data.set('Rollno\tName\tSection\tADBMS\tDS\tPython\n')
                for i in findings:
                    data.set(data.get()+'\t'.join(i)+"\n")
                data.set(data.get()+"\n\n"+str(rec)+" record(s) found")
                    
        except (NameError , FileNotFoundError) as e:
            data.set("Please select a file first")
            messagebox.showerror("Error", "Select a file first!")
        root.destroy()
    #button
    B = Button(root, text ="OK",width=12, command = returning)
    B.grid(row=3, column=2)

def update():
    root=Tk()
    # define Labels
    l1 = Label(root, text='Roll No')
    l1.grid(row=0, column=0)

    l2 = Label(root, text='Name')
    l2.grid(row=0, column=2)

    l3 = Label(root, text='Section')
    l3.grid(row=1, column=0)

    l4 = Label(root, text='ADBMS')
    l4.grid(row=1, column=2)
    
    l5 = Label(root, text='DS')
    l5.grid(row=2, column=0)

    l6 = Label(root, text='Python')
    l6.grid(row=2, column=2)
    

    # define Entries
    rollno_text=StringVar()
    e1=Entry(root,textvariable=rollno_text)
    e1.grid(row=0, column=1)

    name_text=StringVar()
    e2=Entry(root,textvariable=name_text)
    e2.grid(row=0, column=3)

    section_text=StringVar()
    e3=Entry(root,textvariable=section_text)
    e3.grid(row=1, column=1)

    adbms_text=StringVar()
    e4=Entry(root,textvariable=adbms_text)
    e4.grid(row=1, column=3)
    
    ds_text=StringVar()
    e5=Entry(root,textvariable=ds_text)
    e5.grid(row=2, column=1)
    
    python_text=StringVar()
    e6=Entry(root,textvariable=python_text)
    e6.grid(row=2, column=3)

    def returning():
        rollno,name,section,adbms,ds,python=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()
        row=[rollno,name,section,adbms,ds,python]
        try:
            with open(filename,'r') as file1:
                existingLines = [line for line in csv.reader(file1, delimiter=',')]
            with open(filename,'w',newline='') as file2:
                reader2 = csv.writer(file2,delimiter=',')
                cnt=1
                for line in existingLines:
                    if row[0] in line:
                        cnt=0
                        reader2.writerow(row)
                        continue
                    else:
                        reader2.writerow(line)
            if cnt==1:
                data.set("Record does not exists")
            else:
                df=pd.read_csv(filename,encoding="ISO-8859-1",index_col="Rollno")
                viewall()
                sales_report = pd.pivot_table(df, index=["Section"], values=["ADBMS", "Python","DS"],\
                                aggfunc=[np.max, np.min], fill_value=0)
                val=str(sales_report)+"\n\n\n"+str(df.describe().round(2))
                summary.set(val)
                timestamp.set(datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp()).isoformat())
                graph1=sns.lmplot('ADBMS', 'Python', data=df,\
                hue='Section', fit_reg=False,palette="Set1",markers=["o","+","*"],height=3,aspect=1.7)
                plt.savefig('graph1.png')
                plt.close()
                fig, ax = plt.subplots()
                fig.set_size_inches(6, 3.5)
                graph2=sns.boxplot(data=df,width=0.2,ax=ax);
                plt.savefig('graph2.png')
                plt.close()
                img1="./graph1.png"
                img2="./graph2.png"
                setimg1()
                setimg2()
                messagebox.showinfo("Message", "1 Record Updated!")
                    
        except (NameError , FileNotFoundError) as e:
            data.set("Please select a file first")
            messagebox.showerror("Error", "Select a file first!")
        root.destroy()
    
    #button
    B = Button(root, text ="OK",width=12, command = returning)
    B.grid(row=3, column=2)
    root.mainloop()

def viewall():
    try:
        data.set("")
        with open(filename,'r') as file1:
            existingLines = [line for line in csv.reader(file1, delimiter=',')]
            val=""
            for line in existingLines:
                data.set(data.get()+"\n"+'\t'.join(line))
    except (NameError,FileNotFoundError):
         data.set("Please select a file first")
         messagebox.showerror("Error", "Select a file first!")
       

def quit():
    destroy_ADMIN_DASHBOARD()


def browsefunc():
    try:
        global filename
        filename = filedialog.askopenfilename(filetypes=[("CSV files","*.csv"),("Excel file","*.xlsx"),("Excel file", "*.xls")])
        if ".xlsx" in str(filename) or ".xls" in str(filename):   
            wb = openpyxl.load_workbook(filename)
            sh = wb.active
            with open('test.csv', 'w',newline="") as f:  
                c = csv.writer(f)
                for r in sh.rows:
                    c.writerow([cell.value for cell in r])
            filename="test.csv"
        df=pd.read_csv(filename,encoding="ISO-8859-1",index_col="Rollno",error_bad_lines=False)
        #print(df)
        viewall()
        sales_report = pd.pivot_table(df, index=["Section"], values=["ADBMS", "Python","DS"],\
                                      aggfunc=[np.max, np.min], fill_value=0)
        val=str(sales_report)+"\n\n\n"+str(df.describe().round(2))
        summary.set(val)
        timestamp.set(datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp()).isoformat())
        graph1=sns.lmplot('ADBMS', 'Python', data=df,\
        hue='Section', fit_reg=False,palette="Set1",markers=["o","+","*"],height=3,aspect=1.7)
        plt.savefig('graph1.png')
        plt.close()
        fig, ax = plt.subplots()
        fig.set_size_inches(6, 3.5)
        graph2=sns.boxplot(data=df,width=0.2,ax=ax);
        plt.savefig('graph2.png')
        plt.close()
        img1="./graph1.png"
        img2="./graph2.png"
        setimg1()
        setimg2()
    except (NameError,FileNotFoundError):
        data.set("Please select a file first")
        messagebox.showerror("Error", "Select a file first!")
    root.mainloop()

    
    
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


class ADMIN_DASHBOARD:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000' 
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9'  
        _ana2color = '#d9d9d9'  
        font10 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1135x849")
        top.title("ADMIN DASHBOARD")
        top.configure(background="#d88674")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Button1 = Button(top)
        self.Button1.place(relx=0.018, rely=0.035, height=163, width=176)
        self.Button1.configure(activebackground="#d88674")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d88674")
        self.Button1.configure(command=viewall)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="./projectimages/viewall1.png")
        self.Button1.configure(image=self._img1)
        self.Button1.configure(overrelief="flat")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief=FLAT)
        self.Button1.configure(text='''Button''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.194, rely=0.035, height=163, width=176)
        self.Button2.configure(activebackground="#d88674")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d88674")
        self.Button2.configure(command=addnew)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self._img2 = PhotoImage(file="./projectimages/addrecord.png")
        self.Button2.configure(image=self._img2)
        self.Button2.configure(pady="0")
        self.Button2.configure(relief=FLAT)
        self.Button2.configure(text='''Button''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.203, rely=0.306, height=163, width=176)
        self.Button3.configure(activebackground="#d88674")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d88674")
        self.Button3.configure(command=update)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self._img3 = PhotoImage(file="./projectimages/updateuser.png")
        self.Button3.configure(image=self._img3)
        self.Button3.configure(pady="0")
        self.Button3.configure(relief=FLAT)
        self.Button3.configure(text='''Button''')

        self.Button4 = Button(top)
        self.Button4.place(relx=0.018, rely=0.306, height=163, width=176)
        self.Button4.configure(activebackground="#d88674")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d88674")
        self.Button4.configure(command=delete)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self._img4 = PhotoImage(file="./projectimages/removeuser.png")
        self.Button4.configure(image=self._img4)
        self.Button4.configure(pady="0")
        self.Button4.configure(relief=FLAT)
        self.Button4.configure(text='''Button''')

        self.Button5 = Button(top)
        self.Button5.place(relx=0.018, rely=0.577, height=163, width=176)
        self.Button5.configure(activebackground="#d88674")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d88674")
        self.Button5.configure(command=search)
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self._img5 = PhotoImage(file="./projectimages/searchuser.png")
        self.Button5.configure(image=self._img5)
        self.Button5.configure(pady="0")
        self.Button5.configure(relief=FLAT)
        self.Button5.configure(text='''Button''')

        self.Button6 = Button(top)
        self.Button6.place(relx=0.211, rely=0.577, height=163, width=176)
        self.Button6.configure(activebackground="#d88674")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d88674")
        self.Button6.configure(command=quit)
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self._img6 = PhotoImage(file="./projectimages/exit.png")
        self.Button6.configure(image=self._img6)
        self.Button6.configure(pady="0")
        self.Button6.configure(relief=FLAT)
        self.Button6.configure(text='''Button''')

        self.Label1 = Label(top)
        self.Label1.place(relx=0.044, rely=0.236, height=26, width=117)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d88674")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''View All Records''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.22, rely=0.236, height=26, width=119)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d88674")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Add New Record''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.048, rely=0.506, height=26, width=101)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d88674")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Delete Record''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.229, rely=0.506, height=26, width=106)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d88674")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Update Record''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.048, rely=0.777, height=26, width=101)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d88674")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#ffffff")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Search Record''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.273, rely=0.777, height=26, width=30)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d88674")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#ffffff")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Exit''')

        self.Button7 = Button(top)
        self.Button7.place(relx=0.106, rely=0.836, height=53, width=205)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#21405b")
        self.Button7.configure(command=browsefunc)
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font9)
        self.Button7.configure(foreground="#ffffff")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="#000000")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''BROWSE''')

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.432, rely=0.035, relheight=0.896
                , relwidth=0.532)
        self.TNotebook1.configure(width=604)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Data",compound="left",underline="-1",)
        self.TNotebook1_t0.configure(background="#ffffff")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Summary Report", compound="left"
                ,underline="-1", )
        self.TNotebook1_t1.configure(background="#ffffff")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Graphs",compound="none",underline="-1",)
        self.TNotebook1_t2.configure(background="#ffffff")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.TLabel1 = ttk.Label(self.TNotebook1_t0)
        self.TLabel1.place(relx=0.017, rely=0.014, height=664, width=575)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(anchor=NW)
        self.TLabel1.configure(justify=LEFT)
        self.TLabel1.configure(textvariable=data)

        self.Button8 = Button(self.TNotebook1_t0)
        self.Button8.place(relx=0.4, rely=0.945, height=33, width=146)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#7f91e8")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Text to Speech''')
        self.Button8.configure(command=texttospeechdata)

        self.TLabel2 = ttk.Label(self.TNotebook1_t1)
        self.TLabel2.place(relx=0.017, rely=0.014, height=534, width=575)
        self.TLabel2.configure(background="#ffffff")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(font=font10)
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(anchor=NW)
        self.TLabel2.configure(width=575)
        self.TLabel2.configure(textvariable=summary)

        self.Button9 = Button(self.TNotebook1_t1)
        self.Button9.place(relx=0.4, rely=0.945, height=33, width=126)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#7f91e8")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Text to Speech''')
        self.Button9.configure(command=texttospeechsum)

        self.Label7 = Label(self.TNotebook1_t1)
        self.Label7.place(relx=0.017, rely=0.767, height=106, width=582)
        self.Label7.configure(anchor=NE)
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font10)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(width=582)
        self.Label7.configure(textvariable=timestamp)

        self.Labelframe1 = LabelFrame(self.TNotebook1_t2)
        self.Labelframe1.place(relx=0.017, rely=0.027, relheight=0.432
                , relwidth=0.967)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Graph 1''')
        self.Labelframe1.configure(background="#ffffff")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=580)

        self.Label8 = Label(self.Labelframe1)
        self.Label8.place(relx=0.017, rely=0.063, height=286, width=552
                , bordermode='ignore')
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        global setimg1
        def setimg1():
            self._img7 = PhotoImage(file=img1)
            self.Label8.configure(image=self._img7)
        setimg1()
        self.Label8.configure(width=552)

        self.Labelframe2 = LabelFrame(self.TNotebook1_t2)
        self.Labelframe2.place(relx=0.017, rely=0.479, relheight=0.5
                , relwidth=0.967)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Graph 2''')
        self.Labelframe2.configure(background="#ffffff")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")
        self.Labelframe2.configure(width=580)

        self.Label9 = Label(self.Labelframe2)
        self.Label9.place(relx=0.017, rely=0.055, height=336, width=552
                , bordermode='ignore')
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        global setimg2
        def setimg2():
            self._img8 = PhotoImage(file=img2)
            self.Label9.configure(image=self._img8)
        setimg2()
        self.Label9.configure(width=552)


if __name__ == '__main__':
    vp_start_gui()
    



    



