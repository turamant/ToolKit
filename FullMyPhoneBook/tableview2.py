# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableview2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableDialog2(object):
    def setupUi(self, TableDialog2):
        TableDialog2.setObjectName("TableDialog2")
        TableDialog2.resize(1180, 822)
        self.HeadLabel = QtWidgets.QLabel(TableDialog2)
        self.HeadLabel.setGeometry(QtCore.QRect(950, 20, 121, 21))
        self.HeadLabel.setStyleSheet("font: 14pt \"Cantarell\";")
        self.HeadLabel.setObjectName("HeadLabel")
        self.ABsearchPushButton_1 = QtWidgets.QPushButton(TableDialog2)
        self.ABsearchPushButton_1.setGeometry(QtCore.QRect(20, 20, 113, 36))
        self.ABsearchPushButton_1.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.ABsearchPushButton_1.setObjectName("ABsearchPushButton_1")
        self.nameLineEdit = QtWidgets.QLineEdit(TableDialog2)
        self.nameLineEdit.setGeometry(QtCore.QRect(920, 120, 221, 36))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.familyLabel = QtWidgets.QLabel(TableDialog2)
        self.familyLabel.setGeometry(QtCore.QRect(800, 710, 171, 41))
        self.familyLabel.setText("")
        self.familyLabel.setObjectName("familyLabel")
        self.selectTableWidget = QtWidgets.QTableWidget(TableDialog2)
        self.selectTableWidget.setGeometry(QtCore.QRect(140, 20, 701, 751))
        self.selectTableWidget.setRowCount(10000)
        self.selectTableWidget.setColumnCount(10)
        self.selectTableWidget.setObjectName("selectTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.selectTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectTableWidget.setHorizontalHeaderItem(4, item)
        self.nomerLineEdit = QtWidgets.QLineEdit(TableDialog2)
        self.nomerLineEdit.setGeometry(QtCore.QRect(920, 170, 221, 36))
        self.nomerLineEdit.setObjectName("nomerLineEdit")
        self.OPsearchPushButton_7 = QtWidgets.QPushButton(TableDialog2)
        self.OPsearchPushButton_7.setGeometry(QtCore.QRect(20, 260, 113, 36))
        self.OPsearchPushButton_7.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.OPsearchPushButton_7.setObjectName("OPsearchPushButton_7")
        self.GZIIsearchPushButton_4 = QtWidgets.QPushButton(TableDialog2)
        self.GZIIsearchPushButton_4.setGeometry(QtCore.QRect(20, 140, 113, 36))
        self.GZIIsearchPushButton_4.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.GZIIsearchPushButton_4.setObjectName("GZIIsearchPushButton_4")
        self.DEsearchPushButton_3 = QtWidgets.QPushButton(TableDialog2)
        self.DEsearchPushButton_3.setGeometry(QtCore.QRect(20, 100, 113, 36))
        self.DEsearchPushButton_3.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.DEsearchPushButton_3.setObjectName("DEsearchPushButton_3")
        self.VGsearchPushButton_2 = QtWidgets.QPushButton(TableDialog2)
        self.VGsearchPushButton_2.setGeometry(QtCore.QRect(20, 60, 113, 36))
        self.VGsearchPushButton_2.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.VGsearchPushButton_2.setObjectName("VGsearchPushButton_2")
        self.KLsearchPushButton_5 = QtWidgets.QPushButton(TableDialog2)
        self.KLsearchPushButton_5.setGeometry(QtCore.QRect(20, 180, 113, 36))
        self.KLsearchPushButton_5.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.KLsearchPushButton_5.setObjectName("KLsearchPushButton_5")
        self.MNsearchPushButton_6 = QtWidgets.QPushButton(TableDialog2)
        self.MNsearchPushButton_6.setGeometry(QtCore.QRect(20, 220, 113, 36))
        self.MNsearchPushButton_6.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.MNsearchPushButton_6.setObjectName("MNsearchPushButton_6")
        self.RSsearchPushButton_8 = QtWidgets.QPushButton(TableDialog2)
        self.RSsearchPushButton_8.setGeometry(QtCore.QRect(20, 300, 113, 36))
        self.RSsearchPushButton_8.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.RSsearchPushButton_8.setObjectName("RSsearchPushButton_8")
        self.TYsearchPushButton_9 = QtWidgets.QPushButton(TableDialog2)
        self.TYsearchPushButton_9.setGeometry(QtCore.QRect(20, 340, 113, 36))
        self.TYsearchPushButton_9.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.TYsearchPushButton_9.setObjectName("TYsearchPushButton_9")
        self.ZHSSsearchPushButton_11 = QtWidgets.QPushButton(TableDialog2)
        self.ZHSSsearchPushButton_11.setGeometry(QtCore.QRect(20, 420, 113, 36))
        self.ZHSSsearchPushButton_11.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.ZHSSsearchPushButton_11.setObjectName("ZHSSsearchPushButton_11")
        self.FHsearchPushButton_10 = QtWidgets.QPushButton(TableDialog2)
        self.FHsearchPushButton_10.setGeometry(QtCore.QRect(20, 380, 113, 36))
        self.FHsearchPushButton_10.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.FHsearchPushButton_10.setObjectName("FHsearchPushButton_10")
        self.YouYjasearchPushButton_13 = QtWidgets.QPushButton(TableDialog2)
        self.YouYjasearchPushButton_13.setGeometry(QtCore.QRect(20, 500, 113, 36))
        self.YouYjasearchPushButton_13.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.YouYjasearchPushButton_13.setObjectName("YouYjasearchPushButton_13")
        self.IEsearchPushButton_12 = QtWidgets.QPushButton(TableDialog2)
        self.IEsearchPushButton_12.setGeometry(QtCore.QRect(20, 460, 113, 36))
        self.IEsearchPushButton_12.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.IEsearchPushButton_12.setObjectName("IEsearchPushButton_12")
        self.addPushButton = QtWidgets.QPushButton(TableDialog2)
        self.addPushButton.setGeometry(QtCore.QRect(900, 380, 261, 36))
        self.addPushButton.setStyleSheet("font: 10pt \"Cantarell\";\n"
"color: rgb(0, 85, 0);")
        self.addPushButton.setObjectName("addPushButton")
        self.dayLineEdit = QtWidgets.QLineEdit(TableDialog2)
        self.dayLineEdit.setGeometry(QtCore.QRect(920, 220, 221, 36))
        self.dayLineEdit.setObjectName("dayLineEdit")
        self.monthLineEdit = QtWidgets.QLineEdit(TableDialog2)
        self.monthLineEdit.setGeometry(QtCore.QRect(920, 270, 221, 36))
        self.monthLineEdit.setObjectName("monthLineEdit")
        self.yearLineEdit = QtWidgets.QLineEdit(TableDialog2)
        self.yearLineEdit.setGeometry(QtCore.QRect(920, 320, 221, 36))
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.label = QtWidgets.QLabel(TableDialog2)
        self.label.setGeometry(QtCore.QRect(980, 50, 131, 21))
        self.label.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 12pt \"Cantarell\";")
        self.label.setObjectName("label")
        self.AZsearchPushButton_14 = QtWidgets.QPushButton(TableDialog2)
        self.AZsearchPushButton_14.setGeometry(QtCore.QRect(20, 540, 113, 36))
        self.AZsearchPushButton_14.setStyleSheet("selection-background-color: rgb(255, 7, 32);")
        self.AZsearchPushButton_14.setObjectName("AZsearchPushButton_14")
        self.updatePushButton = QtWidgets.QPushButton(TableDialog2)
        self.updatePushButton.setGeometry(QtCore.QRect(900, 420, 261, 36))
        self.updatePushButton.setStyleSheet("font: 10pt \"Cantarell\";\n"
"color: rgb(0, 85, 0);")
        self.updatePushButton.setObjectName("updatePushButton")
        self.deletePushButton = QtWidgets.QPushButton(TableDialog2)
        self.deletePushButton.setGeometry(QtCore.QRect(900, 460, 261, 36))
        self.deletePushButton.setStyleSheet("font: 10pt \"Cantarell\";\n"
"color: rgb(0, 85, 0);")
        self.deletePushButton.setObjectName("deletePushButton")

        self.retranslateUi(TableDialog2)
        QtCore.QMetaObject.connectSlotsByName(TableDialog2)

    def retranslateUi(self, TableDialog2):
        _translate = QtCore.QCoreApplication.translate
        TableDialog2.setWindowTitle(_translate("TableDialog2", "Dialog"))
        self.HeadLabel.setText(_translate("TableDialog2", "Зашли как"))
        self.ABsearchPushButton_1.setText(_translate("TableDialog2", "АБ"))
        self.nameLineEdit.setPlaceholderText(_translate("TableDialog2", "   Фамилия"))
        item = self.selectTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TableDialog2", "Фамилия"))
        item = self.selectTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TableDialog2", "Телефон"))
        item = self.selectTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TableDialog2", "Год р."))
        item = self.selectTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TableDialog2", "Месяц р."))
        item = self.selectTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TableDialog2", "День р."))
        self.nomerLineEdit.setPlaceholderText(_translate("TableDialog2", "   Номер телефона"))
        self.OPsearchPushButton_7.setText(_translate("TableDialog2", "ОП"))
        self.GZIIsearchPushButton_4.setText(_translate("TableDialog2", "ЖЗИЙ"))
        self.DEsearchPushButton_3.setText(_translate("TableDialog2", "ДЕ"))
        self.VGsearchPushButton_2.setText(_translate("TableDialog2", "ВГ"))
        self.KLsearchPushButton_5.setText(_translate("TableDialog2", "КЛ"))
        self.MNsearchPushButton_6.setText(_translate("TableDialog2", "МН"))
        self.RSsearchPushButton_8.setText(_translate("TableDialog2", "РС"))
        self.TYsearchPushButton_9.setText(_translate("TableDialog2", "ТУ"))
        self.ZHSSsearchPushButton_11.setText(_translate("TableDialog2", "ЦЧШЩ"))
        self.FHsearchPushButton_10.setText(_translate("TableDialog2", "ФХ"))
        self.YouYjasearchPushButton_13.setText(_translate("TableDialog2", "ЮЯ"))
        self.IEsearchPushButton_12.setText(_translate("TableDialog2", "ЪЫЬЭ"))
        self.addPushButton.setText(_translate("TableDialog2", "Добавить новый контакт"))
        self.dayLineEdit.setPlaceholderText(_translate("TableDialog2", "   День рождения"))
        self.monthLineEdit.setPlaceholderText(_translate("TableDialog2", "   Месяц рождения"))
        self.yearLineEdit.setPlaceholderText(_translate("TableDialog2", "   Год рождения"))
        self.label.setText(_translate("TableDialog2", "admin"))
        self.AZsearchPushButton_14.setText(_translate("TableDialog2", "A-Z"))
        self.updatePushButton.setText(_translate("TableDialog2", "Изменить данные контакта"))
        self.deletePushButton.setText(_translate("TableDialog2", "Удалить контакт"))
