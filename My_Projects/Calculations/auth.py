from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import os
import hashlib
from auth_ui import Ui_AuthDialog
from main import Calc


class Auth(QtWidgets.QDialog):
    def __init__(self):
        super(Auth, self).__init__()
        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)
        self.init_Ui()
        
        
    def init_Ui(self):
        self.ui.pushButton.clicked.connect(lambda: self.auth())
        pass
    
    
    def auth(self):
        if self.hash_pass(self.ui.old_pass.text()) == self.get_current_password():
            self.show_info_message('Добрий день, \n Олександра Володимирівна!')
            self.close()
            calc = Calc()
            calc.show()
        else:
            self.show_warning_message('Неправильний пароль!')
    
    
    def get_current_password(self):
        path = os.path.join(os.path.dirname(__file__), 'hash.txt')
        with open(path, 'r') as file:
            return file.read()
        
        
    def hash_pass(self, pas):
        salt = '1101985'
        hashed_pas = hashlib.pbkdf2_hmac('sha256',pas.encode('utf-8'),salt.encode('utf-8'), 100000)
        return str(hashed_pas)
    
    
    def show_warning_message(self, str):
        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)
        message.setWindowTitle('AHTUNG!')
        message.setText(str)
        message.addButton(QMessageBox.Ok)
        result = message.exec_()        
    
    
    def show_info_message(self, str):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle('NICE!')
        message.setText(str)
        message.addButton(QMessageBox.Ok)
        result = message.exec_()
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Auth()
    application.setFixedSize(300, 200)
    application.show()
    sys.exit(app.exec())