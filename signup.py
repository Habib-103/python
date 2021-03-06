# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import login

class Ui_SignupPage(object):
    def __init__(self,window):
        self.window=window
        
    
    def signup_signup(self):
        db = sqlite3.connect("db.FP.Python.db")
        db.execute('''create table IF NOT EXISTS users(
            id integer primary key AUTOINCREMENT,
            email varchar(30) not null,
            username varchar(50) not null,
            password varchar(30) not null,
            confirm_password varchar(30) not null)''')
        
        name = self.signup_username.text()
        email = self.signup_email.text()
        password = self.signup_password.text()
        repassword = self.signup_repassword.text()
        
        if name=="":
            msg = QMessageBox()
            msg.setWindowTitle("Nando's Restaurant Management System")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif email == "":
            msg = QMessageBox()
            msg.setWindowTitle("Nando's Restaurant Management System")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif password == "":
            msg = QMessageBox()
            msg.setWindowTitle("Nando's Restaurant Management System")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif repassword == "":
            msg = QMessageBox()
            msg.setWindowTitle("Nando's Restaurant Management System")
            msg.setText("Please fill in all the information")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif password != repassword:
            msg=QMessageBox()
            msg.setWindowTitle("Nando's Restaurant Management System")
            msg.setText("Passwords Much Match!")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
    
        else:
            db.execute("insert into users(email,username, password,confirm_password) values(?, ?, ?,?)",
                         (email, name, password, repassword))
            db.commit()
            self.signup_login()
            db.close()
    
    def signup_login(self):
        self.window.close()
        
        self.window = QtWidgets.QDialog()
        self.ui = login.Ui_LoginPage(self.window)
        self.ui.setupUi(self.window)
        ###hides the previous window
        self.window.show()
        
        SignupPage.hide()
        

            
    def setupUi(self, SignupPage):
        SignupPage.setObjectName("SignupPage")
        SignupPage.resize(1219, 691)
        SignupPage.setStyleSheet("")
        self.signup_email = QtWidgets.QLineEdit(SignupPage)
        self.signup_email.setGeometry(QtCore.QRect(840, 320, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.signup_email.setFont(font)
        self.signup_email.setStyleSheet("background-color: white;\n"
        "border: 3px solid #fdefe6;\n"
        "border-radius: 25px;\n"
        "padding: 10px;\n"
        "font-size: 15px;\n"
        "font-color:gray;\n"
        "")
        self.signup_email.setText("")
        self.signup_email.setObjectName("signup_email")
        self.signup_btn_signup = QtWidgets.QPushButton(SignupPage)
        self.signup_btn_signup.setGeometry(QtCore.QRect(940, 560, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.signup_btn_signup.setFont(font)
        self.signup_btn_signup.setStyleSheet("QPushButton{\n"
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
        self.signup_btn_signup.setObjectName("signup_btn_signup")
        self.label = QtWidgets.QLabel(SignupPage)
        self.label.setGeometry(QtCore.QRect(0, 0, 1261, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/Untitled-1-01-01.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.signup_password = QtWidgets.QLineEdit(SignupPage)
        self.signup_password.setGeometry(QtCore.QRect(840, 440, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.signup_password.setFont(font)
        self.signup_password.setStyleSheet("background-color: white;\n"
        "border: 3px solid #fdefe6;\n"
        "border-radius: 25px;\n"
        "padding: 10px;\n"
        "font-size: 15px;\n"
        "font-color:gray;\n"
        "")
        self.signup_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_password.setObjectName("signup_password")
        self.signup_username = QtWidgets.QLineEdit(SignupPage)
        self.signup_username.setGeometry(QtCore.QRect(840, 380, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.signup_username.setFont(font)
        self.signup_username.setStyleSheet("background-color: white;\n"
        "border: 3px solid #fdefe6;\n"
        "border-radius: 25px;\n"
        "padding: 10px;\n"
        "font-size: 15px;\n"
        "font-color:gray;\n"
        "")
        self.signup_username.setObjectName("signup_username")
        self.signup_repassword = QtWidgets.QLineEdit(SignupPage)
        self.signup_repassword.setGeometry(QtCore.QRect(840, 500, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.signup_repassword.setFont(font)
        self.signup_repassword.setStyleSheet("background-color: white;\n"
        "border: 3px solid #fdefe6;\n"
        "border-radius: 25px;\n"
        "padding: 10px;\n"
        "font-size: 15px;\n"
        "font-color:gray;\n"
        "")
        self.signup_repassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_repassword.setObjectName("signup_repassword")
        self.icon = QtWidgets.QLabel(SignupPage)
        self.icon.setGeometry(QtCore.QRect(-10, 130, 861, 501))
        self.icon.setStyleSheet("border-radius: 50%;")
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("../images/res-01.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.login_background_4 = QtWidgets.QLabel(SignupPage)
        self.login_background_4.setGeometry(QtCore.QRect(0, 0, 1281, 141))
        self.login_background_4.setMouseTracking(True)
        self.login_background_4.setStyleSheet("background-color: #fbddd2;")
        self.login_background_4.setText("")
        self.login_background_4.setObjectName("login_background_4")
        self.label_3 = QtWidgets.QLabel(SignupPage)
        self.label_3.setGeometry(QtCore.QRect(910, 10, 211, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images/logo-01.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.login_background_5 = QtWidgets.QLabel(SignupPage)
        self.login_background_5.setGeometry(QtCore.QRect(-10, 620, 1281, 141))
        self.login_background_5.setMouseTracking(True)
        self.login_background_5.setStyleSheet("background-color: #fbddd2;")
        self.login_background_5.setText("")
        self.login_background_5.setObjectName("login_background_5")
        self.label_4 = QtWidgets.QLabel(SignupPage)
        self.label_4.setGeometry(QtCore.QRect(910, 160, 161, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../images/1-01.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.signup_email.raise_()
        self.signup_username.raise_()
        self.signup_password.raise_()
        self.signup_repassword.raise_()
        self.signup_btn_signup.raise_()
        self.icon.raise_()
        self.login_background_4.raise_()
        self.label_3.raise_()
        self.login_background_5.raise_()
        self.label_4.raise_()
        self.signup_btn_signup.clicked.connect(self.signup_signup)

        self.retranslateUi(SignupPage)
        QtCore.QMetaObject.connectSlotsByName(SignupPage)

    def retranslateUi(self, SignupPage):
        _translate = QtCore.QCoreApplication.translate
        SignupPage.setWindowTitle(_translate("SignupPage", "Dialog"))
        self.signup_email.setPlaceholderText(_translate("SignupPage", "Email Address"))
        self.signup_btn_signup.setText(_translate("SignupPage", "Sign Up"))
        self.signup_password.setPlaceholderText(_translate("SignupPage", "Password"))
        self.signup_username.setPlaceholderText(_translate("SignupPage", "Username"))
        self.signup_repassword.setPlaceholderText(_translate("SignupPage", "Confirm Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupPage = QtWidgets.QDialog()
    ui = Ui_SignupPage(SignupPage)
    ui.setupUi(SignupPage)
    SignupPage.show()
    sys.exit(app.exec_())
