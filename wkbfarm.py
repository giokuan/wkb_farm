from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QFileDialog
import sys


class Ui_MainWindow(object):

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


    def exit_app(self):
        """ close or exit the app"""
        msg=QMessageBox()
        msg.setStyleSheet('QMessageBox {background-color: rgb(121,126, 129)}\
            QPushButton{color: white; font-size: 16px; background-color: transparent; \
            border-radius: 5px; padding: 10px; text-align: center;}QPushButton:hover{color: rgb(0, 0, 0);}') 
        msg.setWindowIcon(QtGui.QIcon('logo/wkb_pig_logo.ico'))
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you wan't to Exit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec_()
        if res == QMessageBox.Ok:  
            sys.exit()
        if res == QMessageBox.Cancel:
            pass


    def insert_data(self):
        """ Save the Sow information in the database"""

        ear_tag=self.ear_tag_number_edit.text()
        ear_notch=self.ear_notch_edit.text()
        if len(ear_notch) == 0:
            self.messageBox("Information", " Ear Notch Cannot be empty!")
            return        
        try:
            ear_notch=int(self.ear_notch_edit.text())
        except ValueError:
            self.messageBox("Information", " integer only!")
            return
            

        sex=self.sex_edit.text()
        breed=self.breed_edit.text()
        dob=self.date_of_birth_edit.date()
        var_date = dob.toPyDate()

        sire=self.sire_edit.text()
        dam=self.dam_edit.text()
        origin=self.origin_edit.text()
        #print(type(ear_notch))
            

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="pigfarm")
       
        query=("INSERT INTO pig_record (ear_tag_no, ear_notch, sex, breed, dob, sire, dam, origin) VALUES  (%s,%s, %s, %s, %s, %s, %s, %s)")
        cur=self.conn.cursor()
        data= cur.execute(query, (ear_tag.upper(),int(ear_notch),sex.upper(),breed.upper(),var_date,sire.upper(),dam.upper(),origin.upper()))
        

        if (data):
            # msg=QMessageBox()
            if    len(ear_tag) == 0:
                self.messageBox("Information", " Ear Tag Cannot be empty!")
                return
            elif  len(str(ear_notch)) == 0:
                self.messageBox("Information", " Ear Notch Cannot be empty!")
                return
            elif  len(sex)  == 0:
                self.messageBox("Information", " Sex Cannot be empty!")
                return
            elif  len(breed) == 0:
                self.messageBox("Information", " Breed Cannot be empty!")
                return
            # elif  len(dob)== 0:
            #     self.messageBox("Information", " Date of Birth Cannot be empty!")
            #     return
            elif  len(sire)== 0:
                self.messageBox("Information", " Sire Cannot be empty!")
                return
            elif  len(dam)== 0:
                self.messageBox("Information", " Dam Cannot be empty!")
                return
            elif  len(origin)== 0:
                self.messageBox("Information", " Origin Cannot be empty!")
                return
           

            else:
                self.messageBox("WKB Piggery", " Sow Record Saved")
                self.conn.commit()
                #self.Savebutton.setEnabled(False)
                #self.addbuttom.setEnabled(True)
                # self.cancel()
                self.loadData()

    def update(self):
        
        sow_id1 = self.sow_no_edit.text()
        # print(sow_id)
        ear_tag1=self.ear_tag_number_edit.text()
        ear_notch1=self.ear_notch_edit.text()
        if len(ear_notch1) == 0:
            self.messageBox("Information", " Ear Notch Cannot be empty!")
            return        
        try:
            ear_notch1=int(self.ear_notch_edit.text())
        except ValueError:
            self.messageBox("Information", " integer only!")
            return
            
        sex1=self.sex_edit.text()
        breed1=self.breed_edit.text()
        dob1=self.date_of_birth_edit.date()
        var_date = dob1.toPyDate()

        sire1=self.sire_edit.text()
        dam1=self.dam_edit.text()
        origin1=self.origin_edit.text()
        
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="pigfarm")
        cur=self.conn.cursor()

        sql = "UPDATE pig_record SET ear_tag_no = '"+ ear_tag1.upper() +"', ear_notch = '" + str(ear_notch1) + "', sex = '" + sex1.upper() + "', breed= '" + breed1.upper()\
                + "', dob = '" + str(var_date) + "', sire = '" + sire1.upper()+ "', dam = '" + dam1.upper() + "', origin = '" + origin1.upper() + "'= '%s' WHERE sow_no = '"+sow_id1+"' "
        
        if (sql):
            #msg=QMessageBox()
            if    len(ear_tag1) == 0:
                self.messageBox("Information", " Ear Tag Cannot be empty!")
                return
            elif  len(sex1) == 0:
                self.messageBox("Information", " Sex Cannot be empty!")
                return
            elif  len(breed1)  == 0:
                self.messageBox("Information", " Breed Cannot be empty!")
                return
            elif  len(sire1) == 0:
                self.messageBox("Information", " Sire Cannot be empty!")
                return
            elif  len(dam1)== 0:
                self.messageBox("Information", " Dam Cannot be empty!")
                return
            elif  len(origin1)== 0:
                self.messageBox("Information", " Origin Cannot be empty!")
                return
                

            else:
                cur.execute(sql)
                self.messageBox("WKB Piggery", " Sow Record Data Updated")
                self.conn.commit()
                self.loadData()
                #self.cell_click_disabledTextbox()


    def add_sow(self):
        # self.update_button.show()
        
        self.ear_tag_number_edit.setEnabled(True)
        self.ear_notch_edit.setEnabled(True)
        self.sex_edit.setEnabled(True)
        self.breed_edit.setEnabled(True)
        self.date_of_birth_edit.setEnabled(True)
        self.sire_edit.setEnabled(True)
        self.dam_edit.setEnabled(True)
        self.origin_edit.setEnabled(True)
        self.cancel_button.setEnabled(True)
        self.save_button.setEnabled(True)


    def edit(self):
        self.update_button.show()
        self.edit_button.hide()
        self.ear_tag_number_edit.setEnabled(True)
        self.ear_notch_edit.setEnabled(True)
        self.sex_edit.setEnabled(True)
        self.breed_edit.setEnabled(True)
        self.date_of_birth_edit.setEnabled(True)
        self.sire_edit.setEnabled(True)
        self.dam_edit.setEnabled(True)
        self.origin_edit.setEnabled(True)
        self.cancel_button.setEnabled(True)
        self.save_button.setEnabled(False)



    def cancel(self):
        # self.update_button.hide()
        # self.edit_button.setEnabled(False)
        self.ear_tag_number_edit.setEnabled(False)
        self.ear_notch_edit.setEnabled(False)
        self.sex_edit.setEnabled(False)
        self.breed_edit.setEnabled(False)
        self.date_of_birth_edit.setEnabled(False)
        self.sire_edit.setEnabled(False)
        self.dam_edit.setEnabled(False)
        self.origin_edit.setEnabled(False)
        self.cancel_button.setEnabled(False)
        self.save_button.setEnabled(False)

        self.refresh()

        
        self.edit_button.show()
        self.edit_button.setEnabled(False)
        self.update_button.hide()

        

    def refresh(self):
        self.sow_no_edit.clear()
        self.ear_tag_number_edit.clear()
        self.ear_notch_edit.clear()
        self.sex_edit.clear()
        self.breed_edit.clear()
        self.date_of_birth_edit.clear()
        self.sire_edit.clear()
        self.dam_edit.clear()
        self.origin_edit.clear()
        self.edit_button.setEnabled(False)
        self.save_button.setEnabled(False)

        self.loadData()





    def loadData(self):
        """ load data in the table"""
        
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "pigfarm"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM pig_record ORDER BY sow_no ASC" )
            result = mycursor.fetchall()
            
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    def cell_click(self,columnCount,rowCount):
        """ Give you the specific information of particular Sow when you clicked the
        the Sow ID field """

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="pigfarm")
        cur=self.conn.cursor()
        item = self.tableWidget.selectedItems()
        i = (item[0].text())
        if rowCount != (0):
            return

        else:
            cur.execute ("SELECT * from pig_record WHERE sow_no=" +str(i))
            col = cur.fetchone()
            #print (row)           
            ear_tag_number = col[1]
            ear_notch = col[2]
            sex = col[3]
            breed = col [4]
            dob = col[5]
            sire = col[6]
            dam = col[7]
            origin = col[8]
           
        self.sow_no_edit.setText(i)
        self.ear_tag_number_edit.setText(ear_tag_number)
        self.ear_notch_edit.setText(str(ear_notch))
        self.sex_edit.setText(sex)
        self.breed_edit.setText(breed)
        self.date_of_birth_edit.setDate(dob)
        self.sire_edit.setText(sire)
        self.dam_edit.setText(dam)
        self.origin_edit.setText(origin)

        if self.sow_no_edit.text() != 0:
            self.edit_button.setEnabled(True)
        else:
            return

        #self.cancel()

        
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 791)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/wkb_pig_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        
        ### TEXTBOX ###
        self.sow_no_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sow_no_edit.setGeometry(QtCore.QRect(150, 530, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.sow_no_edit.setFont(font)
        self.sow_no_edit.setObjectName("sow_no_edit")
        self.sow_no_edit.setEnabled(False)
        
        self.ear_tag_number_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ear_tag_number_edit.setGeometry(QtCore.QRect(150, 560, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.ear_tag_number_edit.setFont(font)
        self.ear_tag_number_edit.setObjectName("ear_tag_number_edit")
        self.ear_tag_number_edit.setEnabled(False)

        self.ear_notch_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ear_notch_edit.setGeometry(QtCore.QRect(150, 590, 113, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.ear_notch_edit.setFont(font)
        self.ear_notch_edit.setObjectName("ear_notch_edit")
        self.ear_notch_edit.setEnabled(False)

        self.sex_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sex_edit.setGeometry(QtCore.QRect(370, 530, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.sex_edit.setFont(font)
        self.sex_edit.setObjectName("sex_edit")
        self.sex_edit.setEnabled(False)

        self.breed_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.breed_edit.setGeometry(QtCore.QRect(370, 560, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.breed_edit.setFont(font)
        self.breed_edit.setObjectName("breed_edit")
        self.breed_edit.setEnabled(False)

        self.date_of_birth_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.date_of_birth_edit.setGeometry(QtCore.QRect(440, 590, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_of_birth_edit.setFont(font)
        self.date_of_birth_edit.setObjectName("date_of_birth_edit")
        self.date_of_birth_edit.setEnabled(False)

        self.sire_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sire_edit.setGeometry(QtCore.QRect(650, 530, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.sire_edit.setFont(font)
        self.sire_edit.setObjectName("sire_edit")
        self.sire_edit.setEnabled(False)

        self.dam_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.dam_edit.setGeometry(QtCore.QRect(650, 560, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.dam_edit.setFont(font)
        self.dam_edit.setObjectName("dam_edit")
        self.dam_edit.setEnabled(False)

        self.origin_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.origin_edit.setGeometry(QtCore.QRect(650, 590, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.origin_edit.setFont(font)
        self.origin_edit.setObjectName("origin_edit")
        self.origin_edit.setEnabled(False)
        

        
        ## LABEL ###
        self.sow_number_label = QtWidgets.QLabel(self.centralwidget)
        self.sow_number_label.setGeometry(QtCore.QRect(30, 530, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.sow_number_label.setFont(font)
        self.sow_number_label.setObjectName("sow_number_label")
         
        self.ear_tag_number_label = QtWidgets.QLabel(self.centralwidget)
        self.ear_tag_number_label.setGeometry(QtCore.QRect(30, 560, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.ear_tag_number_label.setFont(font)
        self.ear_tag_number_label.setObjectName("ear_tag_number_label") 
        
        self.ear_notch_label = QtWidgets.QLabel(self.centralwidget)
        self.ear_notch_label.setGeometry(QtCore.QRect(30, 590, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.ear_notch_label.setFont(font)
        self.ear_notch_label.setObjectName("ear_notch_label")

        self.sex_label = QtWidgets.QLabel(self.centralwidget)
        self.sex_label.setGeometry(QtCore.QRect(290, 530, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")

        self.breed_label = QtWidgets.QLabel(self.centralwidget)
        self.breed_label.setGeometry(QtCore.QRect(290, 560, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.breed_label.setFont(font)
        self.breed_label.setObjectName("breed_label")
        
        self.date_of_birth_label = QtWidgets.QLabel(self.centralwidget)
        self.date_of_birth_label.setGeometry(QtCore.QRect(290, 590, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.date_of_birth_label.setFont(font)
        self.date_of_birth_label.setObjectName("date_of_birth_label")
        
        self.sire_label = QtWidgets.QLabel(self.centralwidget)
        self.sire_label.setGeometry(QtCore.QRect(580, 530, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.sire_label.setFont(font)
        self.sire_label.setObjectName("sire_label")
        
        self.dam_label = QtWidgets.QLabel(self.centralwidget)
        self.dam_label.setGeometry(QtCore.QRect(580, 560, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.dam_label.setFont(font)
        self.dam_label.setObjectName("dam_label")
                
        self.origin_label = QtWidgets.QLabel(self.centralwidget)
        self.origin_label.setGeometry(QtCore.QRect(580, 590, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.origin_label.setFont(font)
        self.origin_label.setObjectName("origin_label")
        
        
        
        ### SEARCH ###
        self.frame_search = QtWidgets.QFrame(self.centralwidget)
        self.frame_search.setGeometry(QtCore.QRect(840, 530, 151, 80))
        self.frame_search.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search.setObjectName("frame_search")
        
        self.search_edit = QtWidgets.QLineEdit(self.frame_search)
        self.search_edit.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(12)
        self.search_edit.setFont(font)
        self.search_edit.setObjectName("search_edit")
        
        self.search_button = QtWidgets.QPushButton(self.frame_search)
        self.search_button.setGeometry(QtCore.QRect(10, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.search_button.setObjectName("search_button")
        
        
        ### BUTTONS ###
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(30, 650, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_sow)
        
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(210, 650, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.insert_data)
        self.save_button.setEnabled(False)
        
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(390, 650, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.update_button.setFont(font)
        self.update_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.update_button.setObjectName("update_button")
        self.update_button.clicked.connect(self.update)
        self.update_button.hide()

        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(390, 650, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.edit_button.setFont(font)
        self.edit_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.edit_button.setObjectName("edit_button")
        self.edit_button.clicked.connect(self.edit)
        self.edit_button.setEnabled(False)

        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(570, 650, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(self.cancel)
        self.cancel_button.setEnabled(False)

        
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(30, 710, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.refresh_button.setFont(font)
        self.refresh_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.clicked.connect(self.refresh)
        
        self.view_records_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_records_button.setGeometry(QtCore.QRect(210, 710, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.view_records_button.setFont(font)
        self.view_records_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.view_records_button.setObjectName("view_records_button")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(390, 710, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("background-color: rgb(121,126, 129);")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.exit_app)
        
        
        ### TABLE ###
        self.frame_table = QtWidgets.QFrame(self.centralwidget)
        self.frame_table.setGeometry(QtCore.QRect(30, 170, 961, 331))
        self.frame_table.setStyleSheet("")
        self.frame_table.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame_table)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 921, 291))
        self.tableWidget.setMaximumSize(QtCore.QSize(921, 16777215))
        self.tableWidget.setStyleSheet("background-color: transparent;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gunship Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.loadData()
        self.tableWidget.cellClicked.connect(self.cell_click)
        self.tableWidget.verticalHeader().setVisible(False)
        
        
        
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(60, 30, 921, 121))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo/wkbfarmlogo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        
        self.frame_logo = QtWidgets.QFrame(self.centralwidget)
        self.frame_logo.setGeometry(QtCore.QRect(30, 20, 961, 141))
        self.frame_logo.setStyleSheet("")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(0, 0, 1021, 771))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("logo/background.jpg"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        self.label_background.raise_()
        
        self.frame_logo.raise_()
        self.frame_table.raise_()
        self.frame_search.raise_()
        self.sow_no_edit.raise_()
        self.sow_number_label.raise_()
        self.ear_tag_number_edit.raise_()
        self.ear_tag_number_label.raise_()
        self.ear_notch_edit.raise_()
        self.ear_notch_label.raise_()
        self.date_of_birth_label.raise_()
        self.date_of_birth_edit.raise_()
        self.dam_edit.raise_()
        self.dam_label.raise_()
        self.sire_edit.raise_()
        self.sire_label.raise_()
        self.origin_edit.raise_()
        self.origin_label.raise_()
        self.sex_edit.raise_()
        self.sex_label.raise_()
        self.breed_edit.raise_()
        self.breed_label.raise_()
        self.add_button.raise_()
        self.save_button.raise_()
        self.update_button.raise_()
        self.edit_button.raise_()
        self.cancel_button.raise_()
        self.refresh_button.raise_()
        self.view_records_button.raise_()
        self.exit_button.raise_()
        self.label_logo.raise_()
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WKB Piggery Farm"))
        self.sow_number_label.setText(_translate("MainWindow", "Sow No."))
        self.ear_tag_number_label.setText(_translate("MainWindow", "Ear Tag No."))
        self.ear_notch_label.setText(_translate("MainWindow", "Ear Notch:"))
        self.date_of_birth_label.setText(_translate("MainWindow", "Date of Birth:"))
        self.dam_label.setText(_translate("MainWindow", "Dam:"))
        self.sire_label.setText(_translate("MainWindow", "Sire:"))
        self.origin_label.setText(_translate("MainWindow", "Origin:"))
        self.sex_label.setText(_translate("MainWindow", "Sex:"))
        self.breed_label.setText(_translate("MainWindow", "Breed:"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.edit_button.setText(_translate("MainWindow", "Edit"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))
        self.view_records_button.setText(_translate("MainWindow", "View Records"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sow No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ear Tag No."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ear Notch"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DOB"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sex"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Breed"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sire"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Dam"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Origin"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
