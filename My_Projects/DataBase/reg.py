from PyQt5 import QtWidgets
import sys
import hashlib
from warn_mes import WM
from db import DB
from reg_ui import Ui_RegDialog
import re
import dns.resolver


class Reg(QtWidgets.QDialog):
    def __init__(self):
        super(Reg, self).__init__()
        self.ui = Ui_RegDialog()
        self.ui.setupUi(self)
        self.init_Ui()
        
        
    def init_Ui(self):
        self.ui.btnCancel.clicked.connect(lambda: self.close())
        self.ui.btnOk.clicked.connect(lambda: self.check_data())
        pass
    
    
    def check_data(self):
        
        stage = 0
        mist = []
        
        if self.is_email_passed():
            self.change_label_color(self.ui.label_4, 'white')
            stage += 1
        else:
            mist.append('Невірний email')
            self.change_label_color(self.ui.label_4, 'red')
        
            
        if self.is_login_passed():
            self.change_label_color(self.ui.label, 'white')
            stage += 1
        else:
            mist.append('Невірний або зайнятий логін')
            self.change_label_color(self.ui.label, 'red')
        
        
        if self.is_password_passed():
            self.change_label_color(self.ui.label_2, 'white')
            stage += 1
        else:
            mist.append('Некоректний пароль')
            self.change_label_color(self.ui.label_2, 'red')
        
        
        if self.is_password_2_passed():
            self.change_label_color(self.ui.label_3, 'white')
            stage += 1
        else:
            mist.append('Перевірочний пароль не співпадає')
            self.change_label_color(self.ui.label_3, 'red')
        
        
        if self.is_name_passed():
            self.change_label_color(self.ui.label_5, 'white')
            stage += 1
        else:
            mist.append('Незаповнене ім`я')
            self.change_label_color(self.ui.label_5, 'red')
        
        
        if self.is_last_name_passed():
            self.change_label_color(self.ui.label_6, 'white')
            stage += 1
        else:
            mist.append('Незаповнене прізвище')
            self.change_label_color(self.ui.label_6, 'red')
            
            
        if stage == 6:
            user = {}
            user['login'] = self.ui.login.text().strip().lower()
            user['email'] = self.ui.email.text().strip()
            user['password'] = self.ui.password.text().strip()
            user['name'] = self.ui.name.text().strip()
            user['last_name'] = self.ui.last_name.text().strip()
            user['is_approved'] = False
            db = DB()
            db.insert_user(user)
            message = WM()
            message.set_text('Дані додано!', "Вам буде надано доступ коли адміністратор ухвалить Вашу заявку.")
            message.show()
            self.close()
        else:
            message = WM()
            message.set_text('Невірні дані!', "; ".join(mist))
            message.show()
  
        pass
    
    
    def is_name_passed(self):
        if self.ui.name.text().strip() != '':    
            return True
        else:
            return False
    
    
    def is_last_name_passed(self):
        if self.ui.last_name.text().strip() != '':    
            return True
        else:
            return False
    
    
    def is_password_2_passed(self):
        if self.ui.password.text().strip() == self.ui.password_2.text().strip():
            return True
        else:
            return False
    
    
    def is_password_passed(self):
        if self.ui.password.text().strip() != '':
            return True
        else: 
            return False
    
    
    def is_login_passed(self):
        if self.ui.login.text().strip().lower() != '' and self.is_login_new():    
            return True
        else:
            return False
     
    
    def is_login_new(self):
        is_new = True
        db = DB()
        logins = db.get_all_logins()
        try:
            for row in logins:
                if row['login'] == self.ui.login.text().strip().lower():
                    is_new = False
        except Exception as ex:
            pass
        return is_new
    
      
    def is_email_passed(self):
        if self.is_correct_email(self.ui.email.text().strip()) and self.is_valid_email(self.ui.email.text().strip()):
            return True
        else: 
            return False
      
    
    def is_correct_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
       
    
    def is_valid_email(self, email):
            # Разбиваем email на имя пользователя и домен
        parts = email.split('@')
        if len(parts) != 2:
            return False
        # Получаем MX-записи для домена
        domain = parts[1]
        try:
            answers = dns.resolver.resolve(domain, 'MX')
        except dns.resolver.NXDOMAIN:
            return False
        except dns.resolver.NoAnswer:
            return False
        except dns.resolver.NoNameservers:
            return False
        except:
            return False
        else:
            if answers.rrset is not None:
                return True
            else:
                return False
    
    
    def change_label_color(self, label, color):
        label.setStyleSheet(f"color: {color}; background-color: none; border: none;")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    reg = Reg()
    reg.setFixedSize(328, 494)
    reg.show()
    sys.exit(app.exec())