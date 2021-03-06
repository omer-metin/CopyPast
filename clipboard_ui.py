# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(450, 430)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 451, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(30, 30, 30, 30)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")

        self.label_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_1)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clipboard"))
        self.label_1.setText(_translate("MainWindow", "1:"))
        self.label_2.setText(_translate("MainWindow", "2:"))
        self.label_3.setText(_translate("MainWindow", "3:"))
        self.label_4.setText(_translate("MainWindow", "4:"))
        self.label_5.setText(_translate("MainWindow", "5:"))
        self.label_6.setText(_translate("MainWindow", "6:"))
        self.label_7.setText(_translate("MainWindow", "7:"))
        self.label_8.setText(_translate("MainWindow", "8:"))
        self.label_9.setText(_translate("MainWindow", "9:"))
