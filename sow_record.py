from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QFileDialog
import sys






class Ui_MainForm(object):

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setStyleSheet('QMessageBox {background-color: rgb(121,126, 129) }\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75);\
            border-radius: 5px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        mess.setWindowIcon(QtGui.QIcon('logo/ico_logo.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_() 

    def search(self): 
        """ return a person name or a chapter"""   
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "pigfarm"
            )
            mycursor = mydb.cursor()
            sow_id = self.id_edit.text()
            
            mycursor.execute("SELECT * FROM sow_performance WHERE sow_no = '"+sow_id+"' ");
            result = mycursor.fetchall()
          
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    def insert_data(self):
        """ Save the Sow information in the database"""

        parity_no = self.parity_edit.text()
        
        var_dob1 = self.date_of_breed1_dateEdit.date()
        dob1= var_dob1.toPyDate()
        
        boar1 = self.boar_no1_edit.text()
        
        var_dob2 = self.date_of_breed2_dateEdit.date()
        dob2= var_dob2.toPyDate()
        
        boar2 = self.boar_no2_edit.text()
        var_due_date = self.due_date_dateEdit.date()
        due_date=var_due_date.toPyDate()

        var_actual_farrow = self.actual_farrowing_dateEdit.date()
        actual_farrow = var_actual_farrow.toPyDate()

        born_alive = self.boarn_alive_edit.text()
        still_birth = self.still_birth_edit.text()
        mummified = self.mummified_edit.text()
        total_piglets = self.total_piglets_edit.text()
        
        var_date_wean = self.date_weaning_dateEdit.date()
        date_wean = var_date_wean.toPyDate()
        
        total_wean_piglets = self.total_wean_piglets_edit.text()
        sow_id = self.id_edit.text()
    
            

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="pigfarm")
       
        query=("INSERT INTO sow_performance (parity_no, dob1, boar_no1, dob2, boar_no2, \
            due_date, actual_farrowing, born_alive, still_birth, mummified, total_piglets,\
            date_wean, total_wean, sow_no) VALUES  (%s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)")
        cur=self.conn.cursor()
        data= cur.execute(query, (parity_no, str(dob1), boar1.upper(), str(dob2), boar2.upper(),\
                str(due_date), str(actual_farrow), born_alive, still_birth, mummified,\
                total_piglets, str(date_wean), total_wean_piglets, sow_id ))
        print(data)

        if (data):
            # msg=QMessageBox()
            if    parity_no == "":
                self.messageBox("Information", " Parity Field Cannot be empty!")
                return
            elif  len(boar1) == 0:
                self.messageBox("Information", " Please Enter a Boar id Cannot be empty!")
                return
           
           

            else:
                self.messageBox("WKB Piggery", " Sow Record Saved")
                self.conn.commit()
                #self.Savebutton.setEnabled(False)
                #self.addbuttom.setEnabled(True)
                # self.cancel()
                self.loadData()

    def loadData(self):
        """ load data in the table"""
        
        #row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "pigfarm"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM sow_performance ORDER BY parity_no ASC" )
            result = mycursor.fetchall()
            
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                  
        except mc.Error as e:
            print ("Error Occured")

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1431, 636)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 1411, 211))
        self.tableWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\
         stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        self.loadData()
        #self.search()
        self.tableWidget.verticalHeader().setVisible(False)


        ### FRAME ###
        self.breeding_frame = QtWidgets.QFrame(self.centralwidget)
        self.breeding_frame.setGeometry(QtCore.QRect(10, 260, 351, 251))
        self.breeding_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\
         stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.breeding_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.breeding_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.breeding_frame.setObjectName("breeding_frame")
        
        self.farrowing_frame = QtWidgets.QFrame(self.centralwidget)
        self.farrowing_frame.setGeometry(QtCore.QRect(370, 260, 351, 251))
        self.farrowing_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\
         stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.farrowing_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.farrowing_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.farrowing_frame.setObjectName("farrowing_frame")

        self.weaning_frame = QtWidgets.QFrame(self.centralwidget)
        self.weaning_frame.setGeometry(QtCore.QRect(730, 260, 361, 251))
        self.weaning_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\
         stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.weaning_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.weaning_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weaning_frame.setObjectName("weaning_frame")
        

        ### LABEL ###

        self.parity_label = QtWidgets.QLabel(self.breeding_frame)
        self.parity_label.setGeometry(QtCore.QRect(40, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.parity_label.setFont(font)
        self.parity_label.setObjectName("parity_label")
        self.parity_label.setStyleSheet("background-color: transparent")

        self.breeding_label = QtWidgets.QLabel(self.breeding_frame)
        self.breeding_label.setGeometry(QtCore.QRect(120, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(15)
        self.breeding_label.setFont(font)
        self.breeding_label.setObjectName("breeding_label")
        self.breeding_label.setStyleSheet("background-color: transparent")
        
        self.date_of_breed1_label = QtWidgets.QLabel(self.breeding_frame)
        self.date_of_breed1_label.setGeometry(QtCore.QRect(40, 80, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_of_breed1_label.setFont(font)
        self.date_of_breed1_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.date_of_breed1_label.setLineWidth(0)
        self.date_of_breed1_label.setObjectName("date_of_breed1_label")
        self.date_of_breed1_label.setStyleSheet("background-color: transparent")

        self.date_of_breed2_label = QtWidgets.QLabel(self.breeding_frame)
        self.date_of_breed2_label.setGeometry(QtCore.QRect(40, 140, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_of_breed2_label.setFont(font)
        self.date_of_breed2_label.setObjectName("date_of_breed2_label")
        self.date_of_breed2_label.setStyleSheet("background-color: transparent")

        self.boar_no1_label = QtWidgets.QLabel(self.breeding_frame)
        self.boar_no1_label.setGeometry(QtCore.QRect(40, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.boar_no1_label.setFont(font)
        self.boar_no1_label.setObjectName("boar_no1_label")
        self.boar_no1_label.setStyleSheet("background-color: transparent")

        self.boar_no2_label = QtWidgets.QLabel(self.breeding_frame)
        self.boar_no2_label.setGeometry(QtCore.QRect(40, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.boar_no2_label.setFont(font)
        self.boar_no2_label.setObjectName("boar_no2_label")
        self.boar_no2_label.setStyleSheet("background-color: transparent")

        self.due_date_label = QtWidgets.QLabel(self.breeding_frame)
        self.due_date_label.setGeometry(QtCore.QRect(40, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.due_date_label.setFont(font)
        self.due_date_label.setObjectName("due_date_label")
        self.due_date_label.setStyleSheet("background-color: transparent")

        self.farrowing_label = QtWidgets.QLabel(self.farrowing_frame)
        self.farrowing_label.setGeometry(QtCore.QRect(100, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(15)
        self.farrowing_label.setFont(font)
        self.farrowing_label.setStyleSheet("")
        self.farrowing_label.setObjectName("farrowing_label")
        self.farrowing_label.setStyleSheet("background-color: transparent")

        self.actual_farrowing_label = QtWidgets.QLabel(self.farrowing_frame)
        self.actual_farrowing_label.setGeometry(QtCore.QRect(20, 60, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.actual_farrowing_label.setFont(font)
        self.actual_farrowing_label.setStyleSheet("")
        self.actual_farrowing_label.setObjectName("actual_farrowing_label")
        self.actual_farrowing_label.setStyleSheet("background-color: transparent")

        self.born_alive_label = QtWidgets.QLabel(self.farrowing_frame)
        self.born_alive_label.setGeometry(QtCore.QRect(20, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.born_alive_label.setFont(font)
        self.born_alive_label.setObjectName("born_alive_label")
        self.born_alive_label.setStyleSheet("background-color: transparent")

        self.mummified_label = QtWidgets.QLabel(self.farrowing_frame)
        self.mummified_label.setGeometry(QtCore.QRect(20, 150, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.mummified_label.setFont(font)
        self.mummified_label.setObjectName("mummified_label")
        self.mummified_label.setStyleSheet("background-color: transparent")
        

        self.still_birth_label = QtWidgets.QLabel(self.farrowing_frame)
        self.still_birth_label.setGeometry(QtCore.QRect(20, 120, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.still_birth_label.setFont(font)
        self.still_birth_label.setStyleSheet("")
        self.still_birth_label.setObjectName("still_birth_label")
        self.still_birth_label.setStyleSheet("background-color: transparent")
     

        self.total_piglets_label = QtWidgets.QLabel(self.farrowing_frame)
        self.total_piglets_label.setGeometry(QtCore.QRect(20, 180, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.total_piglets_label.setFont(font)
        self.total_piglets_label.setAutoFillBackground(False)
        self.total_piglets_label.setStyleSheet("")
        self.total_piglets_label.setScaledContents(False)
        self.total_piglets_label.setObjectName("total_piglets_label")
        self.total_piglets_label.setStyleSheet("background-color: transparent")
    

        self.weaning_label = QtWidgets.QLabel(self.weaning_frame)
        self.weaning_label.setGeometry(QtCore.QRect(130, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(15)
        self.weaning_label.setFont(font)
        self.weaning_label.setObjectName("weaning_label")
        self.weaning_label.setStyleSheet("background-color: transparent")

        
        self.date_weaning_label = QtWidgets.QLabel(self.weaning_frame)
        self.date_weaning_label.setGeometry(QtCore.QRect(20, 60, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_weaning_label.setFont(font)
        self.date_weaning_label.setObjectName("date_weaning_label")
        self.date_weaning_label.setStyleSheet("background-color: transparent")

        self.total_wean_piglets_label = QtWidgets.QLabel(self.weaning_frame)
        self.total_wean_piglets_label.setGeometry(QtCore.QRect(20, 90, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.total_wean_piglets_label.setFont(font)
        self.total_wean_piglets_label.setObjectName("total_wean_piglets_label")
        self.total_wean_piglets_label.setStyleSheet("background-color: transparent")

        self.average_weight_label = QtWidgets.QLabel(self.weaning_frame)
        self.average_weight_label.setGeometry(QtCore.QRect(20, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.average_weight_label.setFont(font)
        self.average_weight_label.setObjectName("average_weight_label")
        self.average_weight_label.setStyleSheet("background-color: transparent")
        



        ### TEXTBOX AND DATE EDIT ###

        self.parity_edit = QtWidgets.QLineEdit(self.breeding_frame)
        self.parity_edit.setGeometry(QtCore.QRect(200, 50, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.parity_edit.setFont(font)
        self.parity_edit.setObjectName("parity_edit")
        
        self.date_of_breed1_dateEdit = QtWidgets.QDateEdit(self.breeding_frame)
        self.date_of_breed1_dateEdit.setGeometry(QtCore.QRect(200, 80, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_of_breed1_dateEdit.setFont(font)
        self.date_of_breed1_dateEdit.setObjectName("date_of_breed1_dateEdit")

        
        self.boar_no1_edit = QtWidgets.QLineEdit(self.breeding_frame)
        self.boar_no1_edit.setGeometry(QtCore.QRect(200, 110, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.boar_no1_edit.setFont(font)
        self.boar_no1_edit.setObjectName("boar_no1_edit")
        
        self.date_of_breed2_dateEdit = QtWidgets.QDateEdit(self.breeding_frame)
        self.date_of_breed2_dateEdit.setGeometry(QtCore.QRect(200, 140, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_of_breed2_dateEdit.setFont(font)
        self.date_of_breed2_dateEdit.setObjectName("date_of_breed2_dateEdit")
        
        self.boar_no2_edit = QtWidgets.QLineEdit(self.breeding_frame)
        self.boar_no2_edit.setGeometry(QtCore.QRect(200, 170, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.boar_no2_edit.setFont(font)
        self.boar_no2_edit.setObjectName("boar_no2_edit")
        
        self.due_date_dateEdit = QtWidgets.QDateEdit(self.breeding_frame)
        self.due_date_dateEdit.setGeometry(QtCore.QRect(200, 200, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.due_date_dateEdit.setFont(font)
        self.due_date_dateEdit.setObjectName("due_date_dateEdit")   
        
        self.boarn_alive_edit = QtWidgets.QLineEdit(self.farrowing_frame)
        self.boarn_alive_edit.setGeometry(QtCore.QRect(220, 90, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.boarn_alive_edit.setFont(font)
        self.boarn_alive_edit.setStyleSheet("")
        self.boarn_alive_edit.setObjectName("boarn_alive_edit")
        
        self.actual_farrowing_dateEdit = QtWidgets.QDateEdit(self.farrowing_frame)
        self.actual_farrowing_dateEdit.setGeometry(QtCore.QRect(220, 60, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.actual_farrowing_dateEdit.setFont(font)
        self.actual_farrowing_dateEdit.setObjectName("actual_farrowing_dateEdit")
        
        self.still_birth_edit = QtWidgets.QLineEdit(self.farrowing_frame)
        self.still_birth_edit.setGeometry(QtCore.QRect(220, 120, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.still_birth_edit.setFont(font)
        self.still_birth_edit.setObjectName("still_birth_edit")
        
        self.mummified_edit = QtWidgets.QLineEdit(self.farrowing_frame)
        self.mummified_edit.setGeometry(QtCore.QRect(220, 150, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.mummified_edit.setFont(font)
        self.mummified_edit.setObjectName("mummified_edit")
        
        self.total_piglets_edit = QtWidgets.QLineEdit(self.farrowing_frame)
        self.total_piglets_edit.setGeometry(QtCore.QRect(220, 180, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.total_piglets_edit.setFont(font)
        self.total_piglets_edit.setObjectName("total_piglets_edit")
        
        self.total_wean_piglets_edit = QtWidgets.QLineEdit(self.weaning_frame)
        self.total_wean_piglets_edit.setGeometry(QtCore.QRect(230, 90, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.total_wean_piglets_edit.setFont(font)
        self.total_wean_piglets_edit.setObjectName("total_wean_piglets_edit")
        
        self.date_weaning_dateEdit = QtWidgets.QDateEdit(self.weaning_frame)
        self.date_weaning_dateEdit.setGeometry(QtCore.QRect(230, 60, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_weaning_dateEdit.setFont(font)
        self.date_weaning_dateEdit.setObjectName("date_weaning_dateEdit")
        
        self.average_weight_edit = QtWidgets.QLineEdit(self.weaning_frame)
        self.average_weight_edit.setGeometry(QtCore.QRect(230, 120, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.average_weight_edit.setFont(font)
        self.average_weight_edit.setObjectName("average_weight_edit")
        
        
        ### BUTTONS ###
        self.add_record_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_record_button.setGeometry(QtCore.QRect(10, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.add_record_button.setFont(font)
        self.add_record_button.setObjectName("add_record_button")
    

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(190, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.insert_data)
        
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(920, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(730, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(370, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.edit_button.setFont(font)
        self.edit_button.setObjectName("edit_button")
        
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(550, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(0, 0, 1431, 611))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("logo/background.jpg"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        
        self.id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_edit.setGeometry(QtCore.QRect(20, 559, 71, 31))
        self.id_edit.setObjectName("id_edit")

        self.total_piglets_label.raise_()
        self.farrowing_label.raise_()
        self.actual_farrowing_label.raise_()
        self.boarn_alive_edit.raise_()
        self.born_alive_label.raise_()
        self.actual_farrowing_dateEdit.raise_()
        self.mummified_label.raise_()
        self.still_birth_label.raise_()
        self.still_birth_edit.raise_()
        self.mummified_edit.raise_()
        self.total_piglets_edit.raise_()
        
        self.label_background.raise_()
        self.tableWidget.raise_()
        self.breeding_frame.raise_()
        self.farrowing_frame.raise_()
        self.weaning_frame.raise_()
        self.add_record_button.raise_()
        self.save_button.raise_()
        self.exit_button.raise_()
        self.cancel_button.raise_()
        self.edit_button.raise_()
        self.clear_button.raise_()
        self.id_edit.raise_()
        
        MainForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Sow Performance Record"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainForm", "Parity No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainForm", "Date of Breed 1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainForm", "Boar No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainForm", "Date of Breed 2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainForm", "Boar No."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainForm", "Due Date"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainForm", "Actual Farrowing"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainForm", "Born Alive"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainForm", "Still Birth"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainForm", "Mummified"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainForm", "Total Piglets"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainForm", "Date Wean"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainForm", "Total Wean Piglets"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainForm", "Sow No."))
       

        self.breeding_label.setText(_translate("MainForm", "Breeding"))
        self.date_of_breed1_label.setText(_translate("MainForm", "Date of Breed:"))
        self.boar_no1_label.setText(_translate("MainForm", "Boar No."))
        self.boar_no2_label.setText(_translate("MainForm", "Boar No."))
        self.date_of_breed2_label.setText(_translate("MainForm", "Date of Breed:"))
        self.due_date_label.setText(_translate("MainForm", "Due Date:"))
        self.parity_label.setText(_translate("MainForm", "Parity No."))
        self.farrowing_label.setText(_translate("MainForm", "Farrowing"))
        self.actual_farrowing_label.setText(_translate("MainForm", "Actual Farrowing:"))
        self.born_alive_label.setText(_translate("MainForm", "Born Alive:"))
        self.mummified_label.setText(_translate("MainForm", "Mummified:"))
        self.still_birth_label.setText(_translate("MainForm", "Still Birth:"))
        self.total_piglets_label.setText(_translate("MainForm", "Total Piglets:"))
        self.weaning_label.setText(_translate("MainForm", "Weaning"))
        self.date_weaning_label.setText(_translate("MainForm", "Date Weaning:"))
        self.total_wean_piglets_label.setText(_translate("MainForm", "Total Wean Piglets:"))
        self.average_weight_label.setText(_translate("MainForm", "Average Weight:"))
        self.add_record_button.setText(_translate("MainForm", "ADD RECORD"))
        self.save_button.setText(_translate("MainForm", "SAVE"))
        self.exit_button.setText(_translate("MainForm", "EXIT"))
        self.cancel_button.setText(_translate("MainForm", "CANCEL"))
        self.edit_button.setText(_translate("MainForm", "EDIT"))
        self.clear_button.setText(_translate("MainForm", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())