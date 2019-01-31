# Student-Performance-Analysis-Tool-Python-Project-
A python gui based application for keeping track of student performances in the university

Project Title: Student Performance Analysis Tool

Introduction : "Student Performance Analysis Tool" provides us a simple interface for maintenance of student information. It can be used by educational institutes or colleges to maintain the records of students easily. Achieving this objective is difficult using a manual system as the information is scattered, can be redundant and collecting relevant information may be very time consuming. 
All these problems are solved using this project. Throughout the project the focus has been on presenting information in an easy and intelligible manner. The project is very useful for those who want to develop softwares /websites based on the same concept. The project provides facilities like online registration and profile creation of students thus reducing paperwork and automating the record generation process in an educational institution. Face recognition has also been implemented to provide more security and control and pandas and matplotlib have been used to analyse the data and conclude patterns from it.

### Technology Used: 

Python

#### Layout:
Login Page

![](https://i.ibb.co/qmHT1WH/loginpage.png)
 
 Admin Dashboard
 
![](https://i.ibb.co/DwmPmmj/dashboard.png)


#### Project Contents:

Files:

*	loginpage.py		: used for logging in
*	loginpage_support.py     : used for defining actions of         gui controls of our tkinter window 
* admin_dashboard.py       : our main window used for managing the student information and perform various operations like add record,     delete record, update record, search record etc.
*	backend.py			: used for establishing connectivity with mysql 
*	base.py			: used for face recognition
*	faces-train.py		: used for training data set used in face recognition

Folders:

*	_pycache_ 		: it consists of cache for our python files
*	cascades		: consists of cascades which are used in face recognition
*	images		: consists of images used in training our dataset for face recognition
*	lessons		: consists of filter-lesson,record video, timelapse etc
*	pickles		: consists of pickle file of our face-labels
*	projectimages	: consists of images used in our project
*	recognizers		: consists of our trained data set

Sample data files:

*	Book1.xlsx	: a sample excel file consisting of student data
*	Data.csv	: a sample excel file consisting of student data

Required Libraries and Dependencies:

Python 3.x , Xampp/wamp server is required to run this project. The Python executable should be in your default path, which the Python installer should have set.

Following modules should be installed:
1.	pymysql
2.	pandas
3.	numpy 
4.	matplotlib
5.	seaborn
6.	openpyxl
7.	pyttsx3
8.	pickle
9.	pillow
10.	cv2
Execute the following commands for installing cv2:
*	pip install opencv-python
* pip install opencv-contrib-python
11.	pytesseract (for image-to-text converter)
12.	create a database named “pythonidae” in xampp/wamp server
13.	create a table in the database named “logindetails” having the following structure:
Sql command: create table if not exists logindetails (username varchar(200) primary key, password varchar(200), role int(1))

![](https://i.ibb.co/SVYvXmX/sqlcommands.png)

#### FLOW DIAGRAM:

![](https://i.ibb.co/6tjKYQM/flow.png)

 
### Execution:

You have to execute the following command in anaconda prompt in order to execute the project:
python loginpage.py
then for first time sign up with a username and password while keeping xampp/wampp on and then login with your username and password

#### Made By:
Amanjot Singh(1610991092)

Ameesha(1610991094)

#### Acknowledgements

 visit https://youtu.be/PmZ29Vta7Vc for more information regarding face recognition system
