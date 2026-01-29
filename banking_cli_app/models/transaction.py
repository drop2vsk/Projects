from datetime import datetime


class Transaction():
    def __init__(self,txn_type,amount,balance_after):
        self.txn_type = txn_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()