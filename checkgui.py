# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkgui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 600, 480))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(610, 10, 181, 461))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.B_wechat = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_wechat.setFont(font)
        self.B_wechat.setObjectName("B_wechat")
        self.B_firefox = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_firefox.setFont(font)
        self.B_firefox.setObjectName("B_firefox")
        self.B_npcap = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_npcap.setFont(font)
        self.B_npcap.setObjectName("B_npcap")
        self.B_start = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_start.setFont(font)
        self.B_start.setObjectName("B_start")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.B_wechat.clicked.connect(MainWindow.wechat)
        self.B_firefox.clicked.connect(MainWindow.firefox)
        self.B_npcap.clicked.connect(MainWindow.npcap)
        self.B_start.clicked.connect(MainWindow.startdtj)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.B_wechat.setText(_translate("MainWindow", "安装微信"))
        self.B_firefox.setText(_translate("MainWindow", "安装火狐"))
        self.B_npcap.setText(_translate("MainWindow", "安装驱动"))
        self.B_start.setText(_translate("MainWindow", "启动答题"))

