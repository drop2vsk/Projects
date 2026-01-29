from transaction import Transaction
from datetime import datetime


class Account():
    def __init__(self,account_number,balance = 0.0):
        self.account_number = account_number
        self.balance = balance
        self.last_activity = datetime.now()
        self.transactions = []


    def deposit(self,amount):
        """
        Credits the given amount to the account.

        Rules:
        - Amount must be greater than zero
        - Creates a CR transaction with timestamp
        - Updates account balance and last activity time

        Raises:
        - ValueError if amount is invalid
        """
        if amount <= 0:
            raise ValueError("Amount should be greater than zero")
        self.balance += amount
        self.last_activity = datetime.now()

        transaction = Transaction(txn_type='CR',amount=amount,balance_after=self.balance)
        self.transactions.append(transaction)
        return transaction

    def withdraw(self,amount):
        """
        Docstring for withdraw
        
        :param self: Description
        :param amount: Amount needs to enter
        """
        pass