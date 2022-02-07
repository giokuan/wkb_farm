from wkbfarm import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QFileDialog
from wkbfarm import Ui_MainWindow

#class Ui_MainClear(object)

def open_window(self):
        
    self.window =QtWidgets.QMainWindow()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self.window)
    MainWindow.close()

    # self.next()
    self.window.show()



