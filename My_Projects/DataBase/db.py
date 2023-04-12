import pymysql
from config import host, user, password, db_name, port

class DB():
    
    def __init__(self):
        self.connect()
        
        
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
            # print('Successfully connected...')
            # print("#" * 20)
            self.connect_status = 'connected'
        except Exception as ex:
            # print('Connection refused...')
            self.connect_status = 'disconnect'
            self.ex = ex
            # print(ex)
        
    
    def fetch_all(self):
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT * FROM user"
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print(ex)
            print('No connection...')
            pass        
    
    
    
            
db = DB()
print(db.connect_status)
print(db.fetch_all())
# print(db.connection)
# print(db.ex)
# print(type(db.ex))