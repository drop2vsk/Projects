from models.user import User
from models.account import Account
class Bankservice():
    def __init__(self):
        self.accounts = {}
        self.users = {}
        self.current_user = None

    def _get_validated_account(self,account_number):
        if self.current_user is None:
            raise ValueError("User must logged in")
        if account_number not in self.accounts:
            raise ValueError("Account number is not exist")
        account = self.accounts[account_number]
        if account not in self.current_user.accounts:
            raise ValueError("This account number is not belongs to the current user")
        return account

    def create_user(self,user_name,password):
        if user_name in self.users:
            raise ValueError("User is already exists") 
        user = User(user_name,password)
        self.users[user_name] = user
        return user
    
    def user_login(self,user_name,password):
        if user_name not in self.users:
            raise ValueError ("User does not exist")
        user = self.users[user_name]
        if password != user.password:
            raise ValueError ("Wrong Password")
        self.current_user = user
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
        account = self._get_validated_account(account_number)
        return account.deposit(amount)
    
    def withdraw(self,account_number,amount):
        account = self._get_validated_account(account_number)
        return account.withdraw(amount)

    def user_logout(self):
        if self.current_user is None:
            raise ValueError("No user is currently logged in")
        self.current_user = None

    def get_account(self,account_number):
        account = self._get_validated_account(account_number)
        return account