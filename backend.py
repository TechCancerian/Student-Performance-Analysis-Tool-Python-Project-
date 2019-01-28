import pymysql as pm
try:
    from Tkinter import messagebox
except ImportError:
    from tkinter import messagebox
#---->>to connect to database

def connectdb():
    try:
        con = pm.connect(host='localhost', database='pythonidae',user='root',\
                         password='')
        cursor = con.cursor()
        query = 'create table if not exists logindetails(username varchar(200) primary key,password varchar(200), role int(1))'
        cursor.execute(query)
        con.commit()

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            messagebox.showerror("Error", e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

#--->>  to insert in the database         
def insert(username,password):
    try:
        con = pm.connect(host='localhost', database='pythonidae', \
                         user='root', password='')
        cursor = con.cursor()
        query = 'insert into logindetails values (%s, %s, 1)'
        data = (username, password)
        cursor.execute(query, data)
        con.commit()

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            messagebox.showerror("Error", e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

#--->> to search in database
def search(username,password):
    try:
        con = pm.connect(host='localhost', database='pythonidae', \
                         user='root', password='')
        cursor = con.cursor()
        query = 'select * from logindetails where username=%s AND password=%s'
        d = (username,password)
        cursor.execute(query, d)
        data = cursor.fetchall()
        return data

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            messagebox.showerror("Error", e)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
