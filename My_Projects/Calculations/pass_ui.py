# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pass_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PassDialog(object):
    def setupUi(self, PassDialog):
        PassDialog.setObjectName("PassDialog")
        PassDialog.resize(346, 220)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/login_black_36dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PassDialog.setWindowIcon(icon)
        PassDialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 229, 127, 255), stop:1 rgba(0, 131, 68, 255))")
        self.label = QtWidgets.QLabel(PassDialog)
        self.label.setGeometry(QtCore.QRect(30, 25, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"background-color: none;\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PassDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 65, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"background-color: none;\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(PassDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 105, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;\n"
"background-color: none;\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.old_pass = QtWidgets.QLineEdit(PassDialog)
        self.old_pass.setGeometry(QtCore.QRect(180, 30, 130, 25))
        self.old_pass.setStyleSheet("background-color: rgba(255,255,255,20);\n"
"border: 2px solid rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.old_pass.setInputMask("")
        self.old_pass.setText("")
        self.old_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.old_pass.setObjectName("old_pass")
        self.new_pass = QtWidgets.QLineEdit(PassDialog)
        self.new_pass.setGeometry(QtCore.QRect(180, 70, 130, 25))
        self.new_pass.setStyleSheet("background-color: rgba(255,255,255,20);\n"
"border: 2px solid rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.new_pass.setInputMask("")
        self.new_pass.setText("")
        self.new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.new_pass.setObjectName("new_pass")
        self.pass_confirm = QtWidgets.QLineEdit(PassDialog)
        self.pass_confirm.setGeometry(QtCore.QRect(180, 110, 130, 25))
        self.pass_confirm.setStyleSheet("background-color: rgba(255,255,255,20);\n"
"border: 2px solid rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"color: white;\n"
"")
        self.pass_confirm.setInputMask("")
        self.pass_confirm.setText("")
        self.pass_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_confirm.setObjectName("pass_confirm")
        self.pushButton = QtWidgets.QPushButton(PassDialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 93, 28))
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: none;\n"
"border-radius: 9px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,55);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,95);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(PassDialog)
        QtCore.QMetaObject.connectSlotsByName(PassDialog)

    def retranslateUi(self, PassDialog):
        _translate = QtCore.QCoreApplication.translate
        PassDialog.setWindowTitle(_translate("PassDialog", "Зміна пароля"))
        self.label.setText(_translate("PassDialog", "Старий пароль:"))
        self.label_2.setText(_translate("PassDialog", "Новий пароль:"))
        self.label_3.setText(_translate("PassDialog", "Повторити пароль:"))
        self.pushButton.setText(_translate("PassDialog", "OK"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PassDialog = QtWidgets.QDialog()
    ui = Ui_PassDialog()
    ui.setupUi(PassDialog)
    PassDialog.show()
    sys.exit(app.exec_())