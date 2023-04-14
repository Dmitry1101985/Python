
class User():
    
    def __init__(self) -> None:
        self.id = None
        self.login = None
        self.email = None
        self.name = None
        self.last_name = None
        self.is_approved = None
        
    
    def set_user(self, row) -> None:
        self.id = row[0]['id']
        self.login = row[0]['login']
        self.email = row[0]['email']
        self.name = row[0]['name']
        self.last_name = row[0]['last_name']
        self.is_approved = row[0]['is_approved']