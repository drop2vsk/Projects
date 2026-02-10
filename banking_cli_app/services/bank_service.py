from models.user import User
class Bankservice():
    def __init__(self):
        self.users = {}
        self.current_user = None

    def create_user(self,user_name,password):
        if user_name in self.users:
            raise ValueError("User is already exists") 
        user = User(user_name,password)
        self.users[user_name]=user
        return user

    def create_account(self):
        pass
    def deposit(self,account_number,amount):
        pass
    def withdraw(self,account_number,amount):
        pass
    def user_login(self,user_name,password):
        pass
    def user_logout(self):
        pass
    def get_account(self,account_number):
        pass