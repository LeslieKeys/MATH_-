import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import main_1
import about
import menu
import multiplication
import addition





def about_page():
    w_about.setWindowTitle("关于")
    w_about.show()

def menu_page():
    w_menu.setWindowTitle("菜单")
    w_menu.show()

def multiplication_page():
    w_multiplication.setWindowTitle("乘法练习")
    w_multiplication.show()

def addition_page():
    w_addition.setWindowTitle("加法练习")
    w_addition.show()


def back_main_page():
    w_main.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w_main = QMainWindow()
    w_about = QMainWindow()
    w_menu = QMainWindow()
    w_multiplication = QMainWindow()
    w_addition = QMainWindow()
    ui_main = main_1.Ui_Math_Test()
    ui_main.setupUi(w_main)
    ui_about = about.Ui_about_window()
    ui_about.setupUi(w_about)
    ui_menu = menu.Ui_menu_window()
    ui_multiplication = multiplication.Ui_multiplication_window()
    ui_multiplication.setupUi(w_multiplication)
    ui_addition = addition.Ui_addition_window()
    ui_addition.setupUi(w_addition)
    ui_menu.setupUi(w_menu)
    w_main.setWindowTitle("数学测试")
    w_main.show()
    ui_main.btn_exit.clicked.connect(QCoreApplication.instance().quit)
    ui_main.btn_about.clicked.connect(about_page)
    ui_main.btn_menu.clicked.connect(menu_page)
    ui_menu.btn_back_main.clicked.connect(back_main_page)
    ui_menu.btn_multiplication.clicked.connect(multiplication_page)
    ui_multiplication.btn_back_menu_1.clicked.connect(menu_page)
    ui_menu.btn_addition.clicked.connect(addition_page)
    ui_addition.btn_back_menu_2.clicked.connect(menu_page)
    sys.exit(app.exec_())
