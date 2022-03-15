import os
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt
from pickle import TRUE
import sys
from tkinter import FALSE
from time import *  
from datetime import *
from matplotlib.pyplot import cla
from matplotlib.style import use
from matplotlib.widgets import Widget
import mysql.connector
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,QDialog)
from sympy import false, true
from dashbord7 import Ui_ParentalControle
from Admin_ui import Ui_ParentalControle
import time
from PyQt5 import QtWidgets
from datetime import datetime as dt
import ctypes, sys
from PyQt5.QtGui import QIcon
from time import sleep
from urllib.parse import urlparse
from pywinauto import Application


# function blocker to block the web site using file hosts in windows 10 
def blockeerr(url):
    if is_admin():
        while True:#while true for execute the code the whole time 
                if datetime(datetime.now().year,datetime.now().month,datetime.now().day,00)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,23):  
                    with open(host_path,"r+") as fileptr:
                        content = fileptr.read() 
                        if url in content:  
                            pass  
                        else:  
                            fileptr.write(ip_address+" "+url+"\n")
                else: 
                    with open(host_path,'r+') as file:
                        content = file.readlines(); 
                        print(content)
                        file.seek(0)
                        for line in content :
                            if url not in line :  
                                file.write(line)
                        file.truncate()  
                sleep(5)#ececute the code after any 5 seconds



#change the forma of url as a format that we want for return domaine name              
def parse(url):
        domain = url.split('/')[-1].split("-")
        print("www."+url.split("/")[0])
        for i in range(len(domain)):
            k=domain[i].split("%20")
        return "www."+url.split("/")[0]



#change the forma of url as a format that we want for return key words in the url
def parsekeyword(url):
        domain = url.split('/')[-1].split("-")
        for i in range(len(domain)):
            k=domain[i].split("%20")
        t=[]
        for i in range(len(domain)):
            t.append(domain[i].split("%20"))
        return t


#test if you are can exucute admin commands in windows 10 
def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


# connection database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
db_cursor= db_connection.cursor(buffered=True)
test = FALSE


host_path ='C:\Windows\System32\drivers\etc\hosts'#the path pf the hosts file in windows 10 
ip_address = '127.0.0.1'



#class admin 
class Admin2(QMainWindow,Ui_ParentalControle):
    def __init__(self) :#consturctor
        QMainWindow.__init__(self)
        uic.loadUi("Admin_ui.ui", self)
        self.btn_page_1.clicked.connect(self.page1)
        self.login_btn.clicked.connect(self.login)
        self.btn_page_2.clicked.connect(self.page2)
        self.btn_page_3.clicked.connect(self.page3)
        self.registerregister_btn.clicked.connect(self.register)
        self.ajouterfisbtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.ajouterfilspage))
        self.webblockerbtn.clicked.connect(self.keywordblocker)
        self.listefilsbtn .clicked.connect(self.listefilsfunction)
        self.historiquebtn.clicked.connect(self.historique)
        self.listeblanchebtn.clicked.connect(self.webblockerpagefonctionwhiteliste)
        self.pushButton_2.clicked.connect(self.ajoutermotcle)
        self.ajouterbtn.clicked.connect(self.ajouterfils)
        self.urlblachebtn.clicked.connect(self.ajouterlisteblache)
        self.pushButton.clicked.connect(self.blocker)
        self.pushButton_3.clicked.connect(self.logout)
        if db_connection.is_connected() == False:
                db_connection.connect()
        db_connection.commit()



        # fill the content of tables 
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        queryf = "select * from  filsa where email = '%s'"%self.emailtext.text()
        q = "select * from  adultea where email = '%s'"%self.emailtext.text()
        que = "select * from WhiteListe where email ='%s'"%self.emailtext.text()
        qu = "select * from BlackListe where email ='%s'"%self.emailtext.text()
        try:
            db_cursor.execute(queryf)
            td = db_cursor.fetchall()
            db_cursor.execute(q)
            tda = db_cursor.fetchall()
            db_cursor.execute(que)
            tdaa = db_cursor.fetchall()
            db_cursor.execute(qu)
            blacklistet = db_cursor.fetchall()
            i=0
            j=len(td)
            k=0
            l=0
            self.tableWidget.setRowCount(len(td)+len(tda))
            for t in td:
                self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(t[0]))
                self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(t[1]))
                self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(str(t[2])))
                i=i+1
            for ta in tda:
                self.tableWidget.setItem(j,0,QtWidgets.QTableWidgetItem(ta[0]))
                self.tableWidget.setItem(j,1,QtWidgets.QTableWidgetItem(ta[1]))
                self.tableWidget.setItem(j,2,QtWidgets.QTableWidgetItem(str(ta[2])))
                j=j+1
            self.tablelisteblanche.setRowCount(len(tdaa))
            for t in tdaa:
                self.tablelisteblanche.setItem(k,0,QtWidgets.QTableWidgetItem(t[0]))
                k=k+1
            self.tableWidget_4.setRowCount(len(blacklistet))
            for ts in blacklistet:
                self.tableWidget_4.setItem(l,0,QtWidgets.QTableWidgetItem("kjfkkg"))
                self.tableWidget_4.setItem(l,1,QtWidgets.QTableWidgetItem(str(ts[1])))
                self.tableWidget_4.setItem(l,2,QtWidgets.QTableWidgetItem(str(ts[2])))
                l=l+1
            db_connection.commit()
        except:
            db_connection.rollback()
            db_connection.close()



    # open the the black list and key word page 
    def keywordblocker(self):
        self.stackedWidget_2.setCurrentWidget(self.webblockerpage)
        qu = "select * from BlackListe where email ='%s'"%self.emailtext.text()
        try:
            db_cursor.execute(qu)
            blacklistet = db_cursor.fetchall()
            l=0
            self.tableWidget_4.setRowCount(len(blacklistet))
            for ts in blacklistet:
                self.tableWidget_4.setItem(l,0,QtWidgets.QTableWidgetItem(ts[0]))
                self.tableWidget_4.setItem(l,1,QtWidgets.QTableWidgetItem(str(ts[1])))
                self.tableWidget_4.setItem(l,2,QtWidgets.QTableWidgetItem(str(ts[2])))
                l=l+1
            db_connection.commit()
        except:
            db_connection.rollback()
            db_connection.close()
        while True:#repet while the window is active the track the child browsing activities 
            # get the url from the current window in the browser chrome
            app = Application(backend='uia')
            app.connect(title_re=".*Chrome.*")
            dlg = app.top_window()
            url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
            # print(url)
            # parse(url)
            # data base connecxion
            if db_connection.is_connected() == False:
                db_connection.connect()
            db_connection.commit()
            db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
            queryf = "select * from Motcle where email = '%s'"%self.emailtext.text()
            try:
                db_cursor.execute(queryf)
                td = db_cursor.fetchall()
                for t in td:
                    for j in len (parsekeyword(url)):
                        if(t[0]==parse(url)[j]):#if the url doesn't exist in the white liste then block it 
                            # call for the  blockeerr function 
                            blockeerr(url)
                db_connection.commit()
            except:
                db_connection.rollback()
                db_connection.close()
            sleep(5)#execute the code after any 5 seconds



    def webblockerpagefonctionwhiteliste(self):#function of  the white liste 
        self.stackedWidget_2.setCurrentWidget(self.Listeblanche)
        if db_connection.is_connected() == False:
                db_connection.connect()
        db_connection.commit()
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        queryf = "select * from WhiteListe where email ='%s'"%self.emailtext.text()
        try:
            db_cursor.execute(queryf)
            td = db_cursor.fetchall()
            i=0
            self.tablelisteblanche.setRowCount(len(td))
            for t in td:
                self.tablelisteblanche.setItem(i,0,QtWidgets.QTableWidgetItem(t[0]))
                i=i+1
            db_connection.commit()
        except:
            db_connection.rollback()
            db_connection.close() 
        while True:#repet while the window is active the track the child browsing activities 
            # get the url from the current window in the browser chrome
            app = Application(backend='uia')
            app.connect(title_re=".*Chrome.*")
            dlg = app.top_window()
            url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
            # print(url)
            # parse(url)
            # data base connecxion
            if db_connection.is_connected() == False:
                db_connection.connect()
            db_connection.commit()
            db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
            queryf = "select * from WhiteListe  where email = '%s'"%self.emailtext.text()
            try:
                db_cursor.execute(queryf)
                td = db_cursor.fetchall()
                for t in td:
                    if(t[0]==parse(url)):#if the url doesn't exist in the white liste then block it 
                        # call for the  blockeerr function 
                        blockeerr(url)
                db_connection.commit()
            except:
                db_connection.rollback()
                db_connection.close()
            sleep(5)#execute the code after any 5 seconds



    # analyse historique and show the statistic of database        
    def analyze(self,results):
        plt.bar(range(len(results)), results.values(), align='edge')
        plt.xticks(rotation=45)
        plt.xticks(range(len(results)), results.keys())
        plt.show()
        for site, count in results.items():
                print(site, count)  # Interact with Bank Database
        self.tableWidget_3.setRowCount(len(results))
        i=0
        for t ,c in results.items():
            self.tableWidget_3.setItem(i,0,QtWidgets.QTableWidgetItem(t))
            self.tableWidget_3.setItem(i,1,QtWidgets.QTableWidgetItem(str(c)))
            i=i+1

    #show history interface         
    def historique(self):
        self.stackedWidget_2.setCurrentWidget(self.Historique)
        #path to user's history database (Chrome)
        data_path = "C:/Users/dell/AppData/Local/Google/Chrome/User Data/Default"
        files = os.listdir(data_path)

        history_db = os.path.join(data_path, 'history')

        #querying the db
        c = sqlite3.connect(history_db)
        cursor = c.cursor()
        select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
        cursor.execute(select_statement)

        results = cursor.fetchall() #tuple

        sites_count = {} #dict makes iterations easier :D

        for url, count in results:
                url = parse(url)
                if url in sites_count:
                    sites_count[url] += 1
                else:
                    sites_count[url] = 1

        sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

        self.analyze (sites_count_sorted)


    #log out    
    def logout(self):
        self.stackedWidget.setCurrentWidget(self.page_1) 


    #add key words to the database 
    def ajoutermotcle(self):
        motcle=self.lineEdit.text()
        if db_connection.is_connected() == False:
                db_connection.connect()
        db_connection.commit()
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        db_cursor.execute("create table if not exists Motcle(motcle VARCHAR(30) ,email VARCHAR(30), FOREIGN KEY (email) REFERENCES admina(email));")
        db_connection.commit()
        if motcle == "":
            QMessageBox.information(self,'information',"Please Enter mot cle",QMessageBox.Ok)
            return
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        query = "INSERT INTO Motcle(motcle,email) VALUES ('%s','%s')"%(motcle,self.emailtext.text())
        try:
            db_cursor.execute(query)
            QMessageBox.information(self,'Information', "Data inserted Successfully",QMessageBox.Ok)
            db_connection.commit()
        except:
            QMessageBox.information(self,'Information', "Data insertion failed!!!",QMessageBox.Ok)
            db_connection.rollback()
            db_connection.close() 
           
    
    #show the list of your children 
    def listefilsfunction(self):
        self.stackedWidget_2.setCurrentWidget(self.Listefils)
        if db_connection.is_connected() == False:
                db_connection.connect()
        db_connection.commit()
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        queryf = "select * from  filsa where email = '%s'"%self.emailtext.text()
        q = "select * from  adultea where email = '%s'"%self.emailtext.text()
        try:
            db_cursor.execute(queryf)
            td = db_cursor.fetchall()
            db_cursor.execute(q)
            tda = db_cursor.fetchall()
            i=0
            j=len(td)
            self.tableWidget.setRowCount(len(td)+len(tda))
            for t in td:
                self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(t[0]))
                self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(t[1]))
                self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(str(t[2])))
                i=i+1
            for ta in tda:
                self.tableWidget.setItem(j,0,QtWidgets.QTableWidgetItem(ta[0]))
                self.tableWidget.setItem(j,1,QtWidgets.QTableWidgetItem(ta[1]))
                self.tableWidget.setItem(j,2,QtWidgets.QTableWidgetItem(str(ta[2])))
                j=j+1
            db_connection.commit()
        except:
            db_connection.rollback()
            db_connection.close()


    def listeblache(self):
        if db_connection.is_connected() == False:
                db_connection.connect()
        db_connection.commit()
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        queryf = "select * from WhiteListe where email ='%s'"%self.emailtext.text()
        try:
            db_cursor.execute(queryf)
            td = db_cursor.fetchall()
            i=0
            self.tablelisteblanche.setRowCount(len(td))
            for t in td:
                self.tablelisteblanche.setItem(i,0,QtWidgets.QTableWidgetItem(t[0]))
                i=i+1
            db_connection.commit()
        except:
            db_connection.rollback()
            db_connection.close()



    # add the white liste to database 
    def ajouterlisteblache(self):
        urlblache=self.definirurlblanche.text()
        if db_connection.is_connected() == False:
                db_connection.connect()
       # executing cursor with execute method and pass SQL query
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS Parentalcontrole")  # Create a Database Named Bank
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
       # creating required tables
        db_cursor.execute("create table if not exists WhiteListe(url VARCHAR(30),email VARCHAR(30), FOREIGN KEY (email) REFERENCES admina(email));")
        db_connection.commit()
        if urlblache == "":
            QMessageBox.information(self,'information',"Please Enter url",QMessageBox.Ok)
            return
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        queryf = "INSERT INTO WhiteListe(url,email) VALUES ('%s','%s')"%(urlblache,self.emailtext.text())
        try:
            db_cursor.execute(queryf)
            QMessageBox.information(self,'Information', "Data inserted Successfully",QMessageBox.Ok)
            db_connection.commit()
        except:
            QMessageBox.information(self,'Information', "Data insertion failed!!!",QMessageBox.Ok)
            db_connection.rollback()
            db_connection.close() 



    # add the sites to be blocked in the database
    def blocker(self):
        if is_admin():#if you are an admin then you can execute the comand admin in the windows 10
            url = self.url.text()
            date_d = self.date_d.text()
            date_f = self.date_f.text()
            if db_connection.is_connected() == False:
                db_connection.connect()
            # executing cursor with execute method and pass SQL query
            db_cursor.execute("CREATE DATABASE IF NOT EXISTS Parentalcontrole")  # Create a Database Named Bank
            db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
            # creating required tables
            db_cursor.execute("create table if not exists BlackListe(url VARCHAR(30) ,date_d int,date_f int,email VARCHAR(30), FOREIGN KEY (email) REFERENCES admina(email));")
            db_connection.commit()
            if url == "":
                QMessageBox.information(self,'information',"Please Enter url",QMessageBox.Ok)
                return
            if date_d == "":
                QMessageBox.information(self,'information',"Please Enter date debut",QMessageBox.Ok)
                return
            if date_f == "":
                QMessageBox.information(self,'information',"Please Enter date fin",QMessageBox.Ok)
                return
            # set the period when the children can use the sites 
            # if the site in this period the child can't open the site in the browser chrome  
            if datetime(datetime.now().year,datetime.now().month,datetime.now().day,int(date_d))<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,int(date_f)):  
                with open(host_path,"r+") as fileptr:
                    content = fileptr.read() 
                    if url in content:  
                        pass  
                    else:  
                        fileptr.write(ip_address+" "+url+"\n")
            else: # if the site not in the period ,delete the site in the hosts file and 
                # unblock the site to be acces by th child 
                with open(host_path,'r+') as file:
                    content = file.readlines(); 
                    print(content)
                    file.seek(0)
                    for line in content :
                        if url not in line :  
                            file.write(line)
                    file.truncate()  
            db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
            queryf = "INSERT INTO BlackListe(url,date_d,date_f,email) VALUES ('%s','%s','%s','%s')"%(url,date_d,date_f,self.emailtext.text())
            try:
                db_cursor.execute(queryf)
                QMessageBox.information(self,'Information', "Data inserted Successfully",QMessageBox.Ok)
                db_connection.commit()
            except:
                QMessageBox.information(self,'Information', "Data insertion failed!!!",QMessageBox.Ok)
                db_connection.rollback()
                db_connection.close() 
        else:#you can't execute the command admin in the windows 10
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



    # function to add the children to the database
    def ajouterfils(self):
        if db_connection.is_connected() == False:
           db_connection.connect()
       # executing cursor with execute method and pass SQL query
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS Parentalcontrole")  # Create a Database Named Bank
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
       # creating required tables
        db_cursor.execute("create table if not exists filsa(nom VARCHAR(30) ,prenom VARCHAR(30), age int ,email varchar(30),FOREIGN KEY (email) REFERENCES admina(email));")
        db_cursor.execute("create table if not exists adultea(nom VARCHAR(30) ,prenom VARCHAR(30), age int,email varchar(30),FOREIGN KEY (email) REFERENCES admina(email));")
        db_connection.commit()
        nom=self.nomfilstext.text()
        prenom=self.prenomtext.text()
        age=self.agetext.text()
        if nom == "":
           QMessageBox.information(self,'information',"Please Enter User nom",QMessageBox.Ok)
           return
        if prenom == "":
           QMessageBox.information( self,'information',"Please Enter User prenon",QMessageBox.Ok)
           return
        if age == "":
           QMessageBox.information(self,'information',"Please Enter User age",QMessageBox.Ok)
           return
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        queryf = "INSERT INTO filsa(nom,prenom,age,email) VALUES ('%s','%s','%s','%s')"%(nom,prenom,age,self.emailtext.text())
        queryA = "INSERT INTO adultea(nom,prenom,age,email) VALUES ('%s','%s','%s','%s')"%(nom,prenom,age,self.emailtext.text())
        try:
            if(int(age)>18):
                db_cursor.execute(queryA)
                QMessageBox.information(self,'Information', "Data inserted Successfully",QMessageBox.Ok)
                db_connection.commit()
            else:
                db_cursor.execute(queryf)
                QMessageBox.information(self,'Information', "Data inserted Successfully",QMessageBox.Ok)
                db_connection.commit()
        except:
            QMessageBox.information(self,'Information', "Data insertion failed!!!",QMessageBox.Ok)
            db_connection.rollback()
            db_connection.close()



    #the menu page
    def page3(self):
        if(test==TRUE):
            self.stackedWidget.setCurrentWidget(self.page_3)
        else:
             QMessageBox.warning(self, "Login first", "go to login", QMessageBox.Ok)


    #the register page
    def page2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)


    # the login page 
    def page1(self):
        self.stackedWidget.setCurrentWidget(self.page_1)


    #function register    
    def register(self):
        if db_connection.is_connected()== False:
             db_connection.connect()
        # executing cursor with execute method and pass SQL query
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS Parentalcontrole")  # Create a Database Named AradhanaBank
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
       # creating required tables
        db_cursor.execute("Create table if not exists admina(email VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30))")

        db_connection.commit()
        email = self.registeremailtext.text() 
        Em=email # Retrieving entered user id
        pwd = self.registerpasswordtest.text()
        # Retrieving entered password
        if email == "":
           QMessageBox.information(self,'information',"Please Enter User email",QMessageBox.Ok)
           return
        if pwd == "":
           QMessageBox.information( self,'information',"Please Enter Password",QMessageBox.Ok)
           return
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
        query = "INSERT INTO admina(email,password) VALUES ('%s','%s')"%(email,pwd)
        try:
            db_cursor.execute(query)
            QMessageBox.information(self,'Information', "Data inserted Successfully",QMessageBox.Ok)
            db_connection.commit()
        except:
            QMessageBox.information(self,'Information', "Data insertion failed!!!",QMessageBox.Ok)
            db_connection.rollback()
            db_connection.close()


    #function login        
    def login(self):
        if db_connection.is_connected() == False:
           db_connection.connect()
       # executing cursor with execute method and pass SQL query
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS Parentalcontrole")  # Create a Database Named Bank
        db_cursor.execute("use Parentalcontrole")  # Interact with Bank Database
       # creating required tables
        db_cursor.execute("create table if not exists admina(email VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30));")
        db_connection.commit()
        try :
            user_name = self.emailtext.text()
            password = self.passwordtest.text()
            if user_name == "" and password == "":
                QMessageBox.warning(self, "Login", "Fill in the data", QMessageBox.Ok)
            else:
                query ="SELECT * FROM admina WHERE email = '" + user_name + "' AND password = '" + password + "'"
                db_cursor.execute(query)
                rowcount = db_cursor.rowcount
                print(db_cursor.rowcount)
                if db_cursor.rowcount == 1:
                    QMessageBox.question(self, 'Login Successful', 'Correct username and password', QMessageBox.Ok)
                    self.stackedWidget.setCurrentWidget(self.page_3)
                else:
                    QMessageBox.warning(self, "Login Incorrect", "Incorrect user or password", QMessageBox.Ok)
        except:
             db_connection.disconnect()

# main 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('image.png'))  
    window = Admin2()
    window.show()
    app.exec_()