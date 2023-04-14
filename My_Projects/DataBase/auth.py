from PyQt5 import QtWidgets
import sys
import hashlib
from auth_ui import Ui_AuthDialog
from warn_mes import WM
from db import DB
from user import User


class Auth(QtWidgets.QDialog):
    def __init__(self):
        super(Auth, self).__init__()
        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)
        self.init_Ui()
        
        
    def init_Ui(self):
        self.ui.btnCancel.clicked.connect(lambda: self.close())
        self.ui.btnOk.clicked.connect(lambda: self.auth())
        self.indicate_connection()
        pass
    
    
    def hash_pass(self, pas):
        salt = '1101985'
        hashed_pas = hashlib.pbkdf2_hmac('sha256',pas.encode('utf-8'),salt.encode('utf-8'), 100000)
        return hashed_pas 
    
    
    def auth(self):
        
        if self.is_login_exists(self.trim_text(self.ui.login.text())):
            if self.is_password_correct(self.ui.password.text(), self.trim_text(self.ui.login.text())):
                user = User()
                db = DB()
                user.set_user(db.get_user_by_login(self.trim_text(self.ui.login.text())))
                if user.is_approved:
                    print('Go to MAIN')
                else:
                    message = WM()
                    message.set_text('Профіль не затверджений!', "Наразі адміністратор не затвердив Ваш профіль. Зачекайте, або зверніться до адміністратора...")
                    message.show()
                
            else:
                message = WM()
                message.set_text('Пароль не вірний!', 'При введенні пароля регістр має значення, але не мають значення пробіли до та після паролю.')
                message.show()
        else:
            message = WM()
            message.set_text('Такого логіна не існує!', 'При введенні логіна регістр, пробіли до та після логіну не мають значення.')
            message.show()
        
   
    
    
    def is_login_exists(self, login):
        is_exists = False
        db = DB()
        logins = db.get_all_logins()
        try:
            for row in logins:
                if row['login'] == login:
                    is_exists = True
        except Exception as ex:
            pass
        return is_exists
    
    
    
    def is_password_correct(self, password, login):
        db = DB()
        correct_pas = db.get_password_by_login(login)
        password = self.hash_pass(password.strip())
        if password == correct_pas:
            return True
        else:
            return False
    
    
    
    def indicate_connection(self):
        db = DB()
        if db.connect():
            self.ui.label_3.setText("Є з'єднання")
            self.ui.connection.setStyleSheet("background-color: green; border: solid 1px white; border-radius: 3px;")
        else:
            self.ui.label_3.setText("Немає з'єднання")
            self.ui.connection.setStyleSheet("background-color: red; border: solid 1px white; border-radius: 3px;")
        db.close_connection()
    
    
    
    def trim_text(self, text: str):
        return text.strip().lower()
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Auth()
    application.setFixedSize(380, 220)
    application.show()
    sys.exit(app.exec())