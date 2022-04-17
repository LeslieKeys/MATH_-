# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiplication.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

from PyQt5.QtWidgets import QMessageBox


class Ui_multiplication_window(object):

    def setupUi(self, multiplication_window):
        multiplication_window.setObjectName("multiplication_window")
        multiplication_window.resize(394, 138)
        self.btn_back_menu_1 = QtWidgets.QPushButton(multiplication_window)
        self.btn_back_menu_1.setGeometry(QtCore.QRect(260, 87, 116, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_back_menu_1.setFont(font)
        self.btn_back_menu_1.setObjectName("btn_back_menu_1")
        self.widget = QtWidgets.QWidget(multiplication_window)
        self.widget.setGeometry(QtCore.QRect(15, 80, 181, 51))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_answer_1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_answer_1.setFont(font)
        self.label_answer_1.setObjectName("label_answer_1")
        self.verticalLayout_3.addWidget(self.label_answer_1)
        self.txt_1 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txt_1.setFont(font)
        self.txt_1.setObjectName("txt_1")
        self.verticalLayout_3.addWidget(self.txt_1)
        self.widget1 = QtWidgets.QWidget(multiplication_window)
        self.widget1.setGeometry(QtCore.QRect(15, 10, 364, 64))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.number_a_1 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_a_1.setFont(font)
        self.number_a_1.setObjectName("number_a_1")
        self.verticalLayout.addWidget(self.number_a_1)
        self.number_b_1 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_b_1.setFont(font)
        self.number_b_1.setObjectName("number_b_1")
        self.verticalLayout.addWidget(self.number_b_1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_answer_1 = QtWidgets.QPushButton(self.widget1)
        self.btn_answer_1.setObjectName("btn_answer_1")
        self.verticalLayout_2.addWidget(self.btn_answer_1)
        self.btn_next_1 = QtWidgets.QPushButton(self.widget1)
        self.btn_next_1.setObjectName("btn_next_1")
        self.verticalLayout_2.addWidget(self.btn_next_1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.retranslateUi(multiplication_window)
        self.btn_back_menu_1.clicked.connect(multiplication_window.close)
        QtCore.QMetaObject.connectSlotsByName(multiplication_window)

    def retranslateUi(self, multiplication_window):
        _translate = QtCore.QCoreApplication.translate
        self.random_a_1 = random.randint(0, 10)
        self.random_b_1 = random.randint(10, 20)
        self.answer = self.random_a_1 * self.random_b_1
        self.number_a_1.setText(_translate("multiplication_window", "数字a:" + str(self.random_a_1)))
        self.number_b_1.setText(_translate("multiplication_window", "数字b:" + str(self.random_b_1)))
        self.btn_answer_1.clicked.connect(self.check_1)
        self.btn_next_1.setHidden(True)
        self.btn_answer_1.setHidden(False)
        multiplication_window.setWindowTitle(_translate("multiplication_window", "Form"))
        self.btn_back_menu_1.setText(_translate("multiplication_window", "返回菜单"))
        self.label_answer_1.setText(_translate("multiplication_window", "答案："))
        self.btn_answer_1.setText(_translate("multiplication_window", "提交"))
        self.btn_next_1.setText(_translate("multiplication_window", "下一题"))
        self.btn_next_1.clicked.connect(self.number)

    def number(self):
        _translate = QtCore.QCoreApplication.translate
        self.random_a_1 = random.randint(0, 10)
        self.random_b_1 = random.randint(10, 20)
        self.answer = self.random_a_1 * self.random_b_1
        self.number_a_1.setText(_translate("multiplication_window", "数字a:" + str(self.random_a_1)))
        self.number_b_1.setText(_translate("multiplication_window", "数字b:" + str(self.random_b_1)))
        self.btn_next_1.setHidden(True)
        self.btn_answer_1.setHidden(False)

    def check_1(self):
        result = self.txt_1.text()
        try:
            if int(result) == int(self.answer):
                msg_box_1 = QMessageBox(QMessageBox.Warning, '恭喜你', '回答正确')
                msg_box_1.exec_()
                self.txt_1.clear()
                self.btn_next_1.setHidden(False)
                self.btn_answer_1.setHidden(True)


            else:
                msg_box_2 = QMessageBox(QMessageBox.Warning, '糟糕', '答案是错的')
                msg_box_2.exec_()
                self.txt_1.clear()
        except :
            msg_box_3 = QMessageBox(QMessageBox.Warning, '错误!', '有错误发生！')
            msg_box_3.exec_()
            self.txt_1.clear()



