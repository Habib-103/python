# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import receipt, pricelist, setting, login, signup, homepage

class Ui_LoginPage(object):
    
    def __init__(self, window):
        self.window=window
        
    def login_open_signup(self):
        self.window.close()
        self.ui = signup.Ui_SignupPage(self.window)
        self.window = QtWidgets.QDialog()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def login_login(self):
        db = sqlite3.connect("db.FP.Python.db")
        name = self.signin_username.text()
        password = self.signin_password.text()
        result = db.execute('select * from users where username = ? and password = ?', (name, password))
        
        #userlogin check
        if (len(result.fetchall()) > 0) and name != "" and password != "":
            self.window.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = homepage.Ui_Homewindow(self.window)
            self.ui.setupUi(self.window)
            self.ui.information(self.signin_username.text(), self.signin_password.text())
            self.window.show()
        #admin login check
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Nando's Restaurant Management System")
            msg.setText("User doesn't exist!")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            
#################SWITCH to homepage function ######################################

    # def homepagewindow(self):
    #     self.window.close()
    #     from ui_folder.homepage import Ui_Homewindow
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_Homewindow(self.window)
    #     self.ui.setupUi(self.window)
    #     ###hides the previous window
    #     self.window.show()

    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(1271, 769)
        LoginPage.setStyleSheet("")
        self.icon = QtWidgets.QLabel(LoginPage)
        self.icon.setGeometry(QtCore.QRect(0, 110, 741, 561))
        self.icon.setStyleSheet("border-radius: 50%;")
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("../images/Restaurant-Management-page-BG-2.jpg"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.Background = QtWidgets.QLabel(LoginPage)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1271, 871))
        self.Background.setStyleSheet("")
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("../images/Untitled-1-01-01.jpg"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.signin_username = QtWidgets.QLineEdit(LoginPage)
        self.signin_username.setGeometry(QtCore.QRect(870, 410, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.signin_username.setFont(font)
        self.signin_username.setStyleSheet("background-color: white;\n"
"border: 3px solid #fdefe6;\n"
"border-radius: 25px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"font-color:gray;\n"
"")
        self.signin_username.setObjectName("signin_username")
        self.signin_password = QtWidgets.QLineEdit(LoginPage)
        self.signin_password.setGeometry(QtCore.QRect(870, 480, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.signin_password.setFont(font)
        self.signin_password.setStyleSheet("background-color: white;\n"
"border: 3px solid #fdefe6;\n"
"border-radius: 25px;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"font-color:gray;")
        self.signin_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signin_password.setObjectName("signin_password")
        self.signin_btn_login = QtWidgets.QPushButton(LoginPage)
        self.signin_btn_login.setGeometry(QtCore.QRect(1060, 580, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.signin_btn_login.setFont(font)
        self.signin_btn_login.setAutoFillBackground(False)
        self.signin_btn_login.setStyleSheet("QPushButton{\n"
"background-color: #fdefe6;\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-color:gray;\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fdefe6;\n"
"border-style:inset;\n"
"color: #fdefe6;\n"
"}\n"
"")
        self.signin_btn_login.setObjectName("signin_btn_login")
        self.signin_btn_signup = QtWidgets.QPushButton(LoginPage)
        self.signin_btn_signup.setGeometry(QtCore.QRect(870, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.signin_btn_signup.setFont(font)
        self.signin_btn_signup.setStyleSheet("QPushButton{\n"
"background-color: #fdefe6;\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-color:gray;\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #white;\n"
"border-style:inset;\n"
"color: #fdefe6;\n"
"}\n"
"\n"
"")
        self.signin_btn_signup.setObjectName("signin_btn_signup")
        self.login_background_4 = QtWidgets.QLabel(LoginPage)
        self.login_background_4.setGeometry(QtCore.QRect(0, 0, 1281, 111))
        self.login_background_4.setMouseTracking(True)
        self.login_background_4.setStyleSheet("background-color: #fbddd2;")
        self.login_background_4.setText("")
        self.login_background_4.setObjectName("login_background_4")
        self.login_background_5 = QtWidgets.QLabel(LoginPage)
        self.login_background_5.setGeometry(QtCore.QRect(-10, 670, 1281, 101))
        self.login_background_5.setMouseTracking(True)
        self.login_background_5.setStyleSheet("background-color: #fbddd2;")
        self.login_background_5.setText("")
        self.login_background_5.setObjectName("login_background_5")
        self.label_3 = QtWidgets.QLabel(LoginPage)
        self.label_3.setGeometry(QtCore.QRect(1060, 20, 161, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images/logo-01.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(LoginPage)
        self.label.setGeometry(QtCore.QRect(40, 30, 561, 41))
        self.label.setStyleSheet("font: 75 16pt \"Helvetica Rounded\";\n"
"color: #cd152d;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(LoginPage)
        self.label_4.setGeometry(QtCore.QRect(930, 210, 161, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../images/1-01.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Background.raise_()
        self.icon.raise_()
        self.signin_username.raise_()
        self.signin_password.raise_()
        self.signin_btn_login.raise_()
        self.signin_btn_signup.raise_()
        self.login_background_4.raise_()
        self.login_background_5.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.signin_btn_signup.clicked.connect(self.login_open_signup)
        self.signin_btn_login.clicked.connect(self.login_login)


        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Dialog"))
        self.signin_username.setPlaceholderText(_translate("LoginPage", "Username"))
        self.signin_password.setPlaceholderText(_translate("LoginPage", "Password"))
        self.signin_btn_login.setText(_translate("LoginPage", "Log in "))
        self.signin_btn_signup.setText(_translate("LoginPage", "Sign Up"))
        self.label.setText(_translate("LoginPage", "Nando\'s Restaurant Management System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QDialog()
    ui = Ui_LoginPage(LoginPage)
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())

