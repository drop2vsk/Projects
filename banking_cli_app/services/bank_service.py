from models.user import User
from models.account import Account
class Bankservice():
    def __init__(self):
        self.accounts = {}
        self.users = {}
        self.current_user = None

    def create_user(self,user_name,password):
        if user_name in self.users:
            raise ValueError("User is already exists") 
        user = User(user_name,password)
        self.users[user_name] = user
        return user

    def create_account(self,account_number):
        if self.current_user is None:
            raise ValueError("User must logged in to create an account")
        if account_number in self.accounts:
            raise ValueError("account_number is already exists") 
        account = Account(account_number)
        self.current_user.accounts.append(account)
        self.accounts[account_number] = account
        return account


    def deposit(self,account_number,amount):
        pass
    def withdraw(self,account_number,amount):
        pass
    def user_login(self,user_name,password):
        if user_name not in self.users:
            raise ValueError ("User does not exist")
        user = self.users[user_name]
        if password != user.password:
            raise ValueError ("Wrong Password")
        self.current_user = user
        return user
    def user_logout(self):
        pass
    def get_account(self,account_number):
        pass