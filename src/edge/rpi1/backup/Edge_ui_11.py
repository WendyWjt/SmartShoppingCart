# -*- coding: utf-8 -*-

# Form implementation generated from reading rpi1 file '1.1.rpi1'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

from Main import First_UI

import time


class ui_1_1(QMainWindow):
    def __init__(self):
        super(ui_1_1, self).__init__()
        self.init_ui()
 
    def init_ui(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.resize(450, 600)
        self.setWindowTitle('New User')

        self._banner = QtWidgets.QLabel(self)
        self._banner.setGeometry(70, 20, 301, 111)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(48)
        self._banner.setFont(font)
        self._banner.setObjectName("_banner")
        self._banner.show()
        _translate = QtCore.QCoreApplication.translate
        self._banner.setText(_translate("MainWindow", "New User"))
        
        self.btn = QPushButton('Register', self)
        self.btn.setGeometry(120, 170, 221, 131)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(36)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.slot_btn1_function)

        self.btn2 = QPushButton('Quit', self)
        self.btn2.setGeometry(120, 350, 221, 131)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.clicked.connect(self.slot_btn2_function)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        


        #self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def slot_btn1_function(self):
        self.hide()
        self.f = First_UI()
        self.f.show()
 
    def slot_btn2_function(self):
        self.hide()
        from Bye import BYE
        self.f = BYE()
        self.f.show()


