from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
from pass_ui import Ui_PassDialog
import os
import hashlib

class ChangePassword(QtWidgets.QDialog):
    def __init__(self):
        super(ChangePassword, self).__init__()
        self.ui = Ui_PassDialog()
        self.ui.setupUi(self)
        self.init_UI()
        
        
    def init_UI(self):
        self.ui.pushButton.clicked.connect(lambda: self.change_pass())
        pass
    
    
    def change_pass(self):
        if self.hash_pass(self.ui.old_pass.text())  == self.get_current_password():
            if self.ui.new_pass.text() != '':
                if self.ui.new_pass.text() == self.ui.pass_confirm.text():
                    self.write_new_pass(self.ui.new_pass.text())
                    self.show_info_message('Пароль змінено!')
                    self.close()
                    pass
                else:
                    self.show_warning_message('Паролі не співпадають!')
                # self.close()
                pass
            else:
                self.show_warning_message('Введіть новий пароль!')
            # self.close()
            pass
        else:
            self.show_warning_message('Невірно введений пароль!')
    
    
    def get_current_password(self):
        path = os.path.join(os.path.dirname(__file__), 'hash.txt')
        with open(path, 'r') as file:
            return file.read()
    
    
    def write_new_pass(self, pas):
        path = os.path.join(os.path.dirname(__file__), 'hash.txt')
        with open(path, 'w') as file:
            file.write(self.hash_pass(pas))
    
    
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
    application = ChangePassword()
    application.setFixedSize(346, 220)
    application.show()
    sys.exit(app.exec())