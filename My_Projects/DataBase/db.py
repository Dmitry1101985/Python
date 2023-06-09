import pymysql
from config import host, user, password, db_name, port
import hashlib
from warn_mes import WM
from PyQt5 import QtWidgets
import sys


class DB():
    
    def __init__(self):
        pass
    
    
    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            return True
        except Exception as ex:
            message = WM()
            message.set_text('Немає з`єднання з сервером!', str(ex))
            message.show()
            # print(f'No connection\n {ex}')
            return False
        
    
    def fetch_all(self):
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    query = "SELECT * FROM user"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    return rows
            except Exception as ex:
                message = WM()
                message.set_text('Немає з`єднання з таблицею даних!', str(ex))
                message.show()        
            self.close_connection()
    
    
    def get_password_by_login(self, login):
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    query = f"SELECT password FROM user WHERE login = '{login}'"
                    cursor.execute(query)
                    row = cursor.fetchone()
                    return row['password']
            except Exception as ex:
                message = WM()
                message.set_text('Помилка отримання даних!', str(ex))
                message.show()
            self.close_connection()
    
    
    def set_password_by_login(self, login, password):
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    password = self.hash_pass(password)
                    query = "UPDATE user SET `password` = %s  WHERE user.login = %s"
                    cursor.execute(query, (password, login))
                    self.connection.commit()
            except Exception as ex:
                message = WM()
                message.set_text('Помилка запису даних!', str(ex))
                message.show()
            self.close_connection()
    
    
    def insert_user(self, user):
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    password = self.hash_pass(user['password'])
                    login = user['login']
                    email = user['email']
                    name = user['name']
                    last_name = user['last_name']
                    is_approved = user['is_approved']
                    query = "INSERT INTO user (login, password, email, name, last_name, is_approved) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, (login, password, email, name, last_name, is_approved))
                    self.connection.commit()
            except Exception as ex:
                message = WM()
                message.set_text('Помилка запису даних!', str(ex))
                message.show()
            self.close_connection()
    
    
    def get_all_logins(self):
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    query = "SELECT login FROM user"
                    cursor.execute(query)
                    col = cursor.fetchall()
                    return col
            except Exception as ex:
                message = WM()
                message.set_text('Помилка отримання даних!', str(ex))
                message.show()
            self.close_connection()
    
    
    def get_user_by_login(self, login):
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    query = f"SELECT * FROM user WHERE login = '{login}'"
                    cursor.execute(query)
                    row = cursor.fetchall()
                    return row
            except Exception as ex:
                message = WM()
                message.set_text('Помилка отримання даних!', str(ex))
                message.show()
            self.close_connection()
    
    
    
    def hash_pass(self, pas):
        salt = '1101985'
        hashed_pas = hashlib.pbkdf2_hmac('sha256',pas.encode('utf-8'),salt.encode('utf-8'), 100000)
        return hashed_pas
    
    
    def close_connection(self):
        try:
            self.connection.close()
        except Exception as ex:
            pass
    
    
    def is_login_exist(self, login):
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    query = f"SELECT id FROM user WHERE login = '{login}'"
                    cursor.execute(query)
                    id = cursor.fetchone()
            except Exception as ex:
                message = WM()
                message.set_text('Помилка отримання даних!', str(ex))
                message.show()
            self.close_connection()
        
        if id == None:
            return False
        else:
            return True
    
    
    # def test(self):
    #     if self.hash_pass('8552') == self.get_password_by_login('admin'):
    #         print('YES')
    #     else:
    #         print('NO')
    #         print(self.hash_pass('8552'))


        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    db = DB()
    # print(db.get_user_by_login('admin'))
    sys.exit(app.exec())
            


