# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(394, 359)
        self.label = QtWidgets.QLabel(menu_window)
        self.label.setGeometry(QtCore.QRect(92, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(menu_window)
        self.widget.setGeometry(QtCore.QRect(80, 110, 241, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_multiplication = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_multiplication.setFont(font)
        self.btn_multiplication.setObjectName("btn_multiplication")
        self.verticalLayout.addWidget(self.btn_multiplication)
        self.btn_addition = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_addition.setFont(font)
        self.btn_addition.setObjectName("btn_addition")
        self.verticalLayout.addWidget(self.btn_addition)
        self.btn_back_main = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_back_main.setFont(font)
        self.btn_back_main.setObjectName("btn_back_main")
        self.verticalLayout.addWidget(self.btn_back_main)

        self.retranslateUi(menu_window)
        self.btn_back_main.clicked.connect(menu_window.close)
        self.btn_addition.clicked.connect(menu_window.close)
        self.btn_multiplication.clicked.connect(menu_window.close)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "Form"))
        self.label.setText(_translate("menu_window", "    菜单"))
        self.btn_multiplication.setText(_translate("menu_window", "乘法练习"))
        self.btn_addition.setText(_translate("menu_window", "加法练习"))
        self.btn_back_main.setText(_translate("menu_window", "返回主页面"))