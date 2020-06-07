# -*- coding: utf-8 -*-

# Form implementation generated from reading rpi1 file '1.rpi1'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
#import edge_ui_11
import time

class First_UI(QMainWindow):
    def __init__(self):
        super(First_UI, self).__init__()
        self.setupUi()
    
    
    def setupUi(self):
        self.setObjectName("Welcome~")
        self.resize(450, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Welcome_banner = QtWidgets.QLabel(self.centralwidget)
        self.Welcome_banner.setGeometry(QtCore.QRect(40, 20, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(48)
        self.Welcome_banner.setFont(font)
        self.Welcome_banner.setObjectName("Welcome_banner")

        #valueChanged = pyqtSignal()
        self.btn = QPushButton('Login', self)
        self.btn.setGeometry(330, 100, 100, 60)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.slot_btn_function)
 
        self.Discount = QtWidgets.QLabel(self.centralwidget)
        self.Discount.setGeometry(QtCore.QRect(30, 160, 400, 400))
        self.Discount.setText("")
        self.Discount.setPixmap(QtGui.QPixmap("./dis.jpg"))
        self.Discount.setScaledContents(True)
        self.Discount.setObjectName("Discount")

#        self.slot_btn_function()
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Welcome_banner.setText(_translate("MainWindow", "Welcome!"))

##    def login(self):
##        self.switch_window.emit()

    def slot_btn_function(self):
        self.hide()

        detect_person = True # face recognition here
        
        if not detect_person:
            from Edge_register import ui_1_1
            self.s = ui_1_1()
            self.s.show()
        else:
            #print("here")
            
            from Menu import ui_Menu
            self.s = ui_Menu()
            self.s.show()

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = First_UI()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()

##class UI_1_1(QMainWindow):
##    def __init__(self):
##        super(UI_1_1, self).__init__()
##        self.init_ui()
## 
##    def init_ui(self):
##        self.centralwidget = QtWidgets.QWidget(self)
##        self.centralwidget.setObjectName("centralwidget")
##        self.resize(450, 600)
##        self.setWindowTitle('New User')
##
##        self._banner = QtWidgets.QLabel(self)
##        self._banner.setGeometry(70, 20, 301, 111)
##        font = QtGui.QFont()
##        font.setFamily("Comic Sans MS")
##        font.setPointSize(48)
##        self._banner.setFont(font)
##        self._banner.setObjectName("_banner")
##        self._banner.show()
##        _translate = QtCore.QCoreApplication.translate
##        self._banner.setText(_translate("MainWindow", "New User"))
##        
##        self.btn = QPushButton('Register', self)
##        self.btn.setGeometry(120, 170, 221, 131)
##        font = QtGui.QFont()
##        font.setFamily("Comic Sans MS")
##        font.setPointSize(36)
##        self.btn.setFont(font)
##        self.btn.clicked.connect(self.slot_btn1_function)
##
##        self.btn2 = QPushButton('Quit', self)
##        self.btn2.setGeometry(120, 350, 221, 131)
##        font = QtGui.QFont()
##        font.setFamily("Comic Sans MS")
##        font.setPointSize(36)
##        self.btn2.setFont(font)
##        self.btn2.clicked.connect(self.slot_btn2_function)
##
##        self.setCentralWidget(self.centralwidget)
##        self.statusbar = QtWidgets.QStatusBar(self)
##        self.statusbar.setObjectName("statusbar")
##        self.setStatusBar(self.statusbar)
##        
##
##
##        #self.retranslateUi(self)
##        QtCore.QMetaObject.connectSlotsByName(self)
##
##    def slot_btn1_function(self):
##        self.hide()
##        self.f = First_UI()
##        self.f.show()
## 
##    def slot_btn2_function(self):
##        self.hide()
##        from Bye import BYE
##        self.f = BYE()
##        self.f.show()

##class Bye(QMainWindow):
##    def __init__(self):
##        super(Bye, self).__init__()
##        self.init_ui()
## 
##    def init_ui(self):
##        self.centralwidget = QtWidgets.QWidget(self)
##        self.centralwidget.setObjectName("centralwidget")
##        self.resize(450, 600)
##        self.setWindowTitle('Bye~')
##
##        self._banner = QtWidgets.QLabel(self)
##        self._banner.setGeometry(70, 20, 301, 111)
##        font = QtGui.QFont()
##        font.setFamily("Comic Sans MS")
##        font.setPointSize(48)
##        self._banner.setFont(font)
##        self._banner.setObjectName("_banner")
##        self._banner.show()
##        _translate = QtCore.QCoreApplication.translate
##        self._banner.setText(_translate("MainWindow", "Bye~"))
##        
##        self.btn = QPushButton('Return Main', self)
##        self.btn.setGeometry(50, 170, 300, 131)
##        font = QtGui.QFont()
##        font.setFamily("Comic Sans MS")
##        font.setPointSize(36)
##        self.btn.setFont(font)
##        self.btn.clicked.connect(self.slot_btn1_function)
##
##        self.setCentralWidget(self.centralwidget)
##        self.statusbar = QtWidgets.QStatusBar(self)
##        self.statusbar.setObjectName("statusbar")
##        self.setStatusBar(self.statusbar)
##        
##        QtCore.QMetaObject.connectSlotsByName(self)
##
##    def slot_btn1_function(self):
##        self.hide()
##        self.f = First_UI()
##        self.f.show()



   











