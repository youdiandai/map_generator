# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\hello.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(964, 663)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(790, 600, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 26pt \"SimSun-ExtB\";")
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(0, 0, 1221, 661))
        self.listView.setStyleSheet("background-image:url(:/fm.jpg)")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "开始"))
import sds_qrc
