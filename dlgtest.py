# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgtest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_test(object):
    def setupUi(self, Dialog_test):
        Dialog_test.setObjectName("Dialog_test")
        Dialog_test.resize(640, 480)
        self.label = QtWidgets.QLabel(Dialog_test)
        self.label.setGeometry(QtCore.QRect(50, 30, 54, 12))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog_test)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 60, 581, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 0, 1, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 1, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 1, 1, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog_test)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 260, 451, 201))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.Btn_quit = QtWidgets.QPushButton(Dialog_test)
        self.Btn_quit.setGeometry(QtCore.QRect(500, 410, 111, 41))
        self.Btn_quit.setObjectName("Btn_quit")
        self.Btn_next = QtWidgets.QPushButton(Dialog_test)
        self.Btn_next.setGeometry(QtCore.QRect(500, 270, 111, 41))
        self.Btn_next.setObjectName("Btn_next")
        self.Btn_last = QtWidgets.QPushButton(Dialog_test)
        self.Btn_last.setGeometry(QtCore.QRect(500, 340, 111, 41))
        self.Btn_last.setObjectName("Btn_last")

        self.retranslateUi(Dialog_test)
        self.Btn_quit.clicked.connect(Dialog_test.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_test)

    def retranslateUi(self, Dialog_test):
        _translate = QtCore.QCoreApplication.translate
        Dialog_test.setWindowTitle(_translate("Dialog_test", "单词测试"))
        self.label.setText(_translate("Dialog_test", "word"))
        self.Btn_quit.setText(_translate("Dialog_test", "退出"))
        self.Btn_next.setText(_translate("Dialog_test", "下一个"))
        self.Btn_last.setText(_translate("Dialog_test", "上一个"))

