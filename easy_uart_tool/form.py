# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_serial_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_serial_button.setGeometry(QtCore.QRect(220, 250, 81, 23))
        self.open_serial_button.setObjectName("open_serial_button")
        self.search_com_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_com_button.setGeometry(QtCore.QRect(80, 50, 81, 23))
        self.search_com_button.setObjectName("search_com_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 50, 61, 21))
        self.label.setObjectName("label")
        self.comboBox_port = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_port.setGeometry(QtCore.QRect(230, 50, 341, 22))
        self.comboBox_port.setObjectName("comboBox_port")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 80, 131, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.clear_text_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_text_button.setGeometry(QtCore.QRect(220, 220, 81, 23))
        self.clear_text_button.setObjectName("clear_text_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_serial_button.setText(_translate("MainWindow", "打开串口"))
        self.search_com_button.setText(_translate("MainWindow", "扫描串口"))
        self.label.setText(_translate("MainWindow", "串口号"))
        self.clear_text_button.setText(_translate("MainWindow", "清空窗口"))
