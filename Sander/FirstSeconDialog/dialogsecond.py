# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogsecond.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSecond(object):
    def setupUi(self, DialogSecond):
        DialogSecond.setObjectName("DialogSecond")
        DialogSecond.resize(400, 278)
        self.pushButtonSecond = QtWidgets.QPushButton(DialogSecond)
        self.pushButtonSecond.setGeometry(QtCore.QRect(92, 145, 261, 91))
        self.pushButtonSecond.setObjectName("pushButtonSecond")
        self.labelSecond = QtWidgets.QLabel(DialogSecond)
        self.labelSecond.setGeometry(QtCore.QRect(100, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelSecond.setFont(font)
        self.labelSecond.setObjectName("labelSecond")

        self.retranslateUi(DialogSecond)
        QtCore.QMetaObject.connectSlotsByName(DialogSecond)

    def retranslateUi(self, DialogSecond):
        _translate = QtCore.QCoreApplication.translate
        DialogSecond.setWindowTitle(_translate("DialogSecond", "Dialog"))
        self.pushButtonSecond.setText(_translate("DialogSecond", "Вернутся назад в первое окно"))
        self.labelSecond.setText(_translate("DialogSecond", "Второе окно"))

