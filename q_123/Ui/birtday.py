# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'birthday.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BirthDayTableDialog99(object):
    def setupUi(self, BirthDayTableDialog99):
        BirthDayTableDialog99.setObjectName("BirthDayTableDialog99")
        BirthDayTableDialog99.resize(1180, 822)
        self.HeadLabel = QtWidgets.QLabel(BirthDayTableDialog99)
        self.HeadLabel.setGeometry(QtCore.QRect(850, 20, 121, 41))
        self.HeadLabel.setStyleSheet("font: 14pt \"Cantarell\";")
        self.HeadLabel.setObjectName("HeadLabel")
        self.familyLabel = QtWidgets.QLabel(BirthDayTableDialog99)
        self.familyLabel.setGeometry(QtCore.QRect(800, 710, 171, 41))
        self.familyLabel.setText("")
        self.familyLabel.setObjectName("familyLabel")
        self.tableWidget = QtWidgets.QTableWidget(BirthDayTableDialog99)
        self.tableWidget.setGeometry(QtCore.QRect(130, 70, 691, 681))
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.cancelPushButton = QtWidgets.QPushButton(BirthDayTableDialog99)
        self.cancelPushButton.setGeometry(QtCore.QRect(940, 130, 151, 41))
        self.cancelPushButton.setStyleSheet("border-radius:20px;\n"
"font: 12pt \"Cantarell\";\n"
"background-color: red;")
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.labelUser = QtWidgets.QLabel(BirthDayTableDialog99)
        self.labelUser.setGeometry(QtCore.QRect(980, 30, 171, 21))
        self.labelUser.setStyleSheet("font: 12pt \"Cantarell\";\n"
"color: rgb(18, 10, 255);")
        self.labelUser.setObjectName("labelUser")
        self.headLabe = QtWidgets.QLabel(BirthDayTableDialog99)
        self.headLabe.setGeometry(QtCore.QRect(280, 10, 511, 41))
        self.headLabe.setStyleSheet("font: 14pt \"Cantarell\";\n"
"font: 18pt \"Cantarell\";\n"
"color: rgb(43, 0, 255);")
        self.headLabe.setObjectName("headLabe")

        self.retranslateUi(BirthDayTableDialog99)
        QtCore.QMetaObject.connectSlotsByName(BirthDayTableDialog99)

    def retranslateUi(self, BirthDayTableDialog99):
        _translate = QtCore.QCoreApplication.translate
        BirthDayTableDialog99.setWindowTitle(_translate("BirthDayTableDialog99", "Dialog"))
        self.HeadLabel.setText(_translate("BirthDayTableDialog99", "Зашли как:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BirthDayTableDialog99", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BirthDayTableDialog99", "Телефон"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BirthDayTableDialog99", "Дата р."))
        self.cancelPushButton.setText(_translate("BirthDayTableDialog99", "назад"))
        self.labelUser.setText(_translate("BirthDayTableDialog99", "User"))
        self.headLabe.setText(_translate("BirthDayTableDialog99", "Дни рождения в этом месяце!!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BirthDayTableDialog99 = QtWidgets.QDialog()
    ui = Ui_BirthDayTableDialog99()
    ui.setupUi(BirthDayTableDialog99)
    BirthDayTableDialog99.show()
    sys.exit(app.exec_())
