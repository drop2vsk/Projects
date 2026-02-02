from datetime import datetime


class Transaction():
    """
        Represents a single account transaction.

        :param txn_type: 'CR' or 'DR'
        :param amount: transaction amount (> 0)
        :param balance_after: balance after transaction
        """
    def __init__(self,txn_type,amount,balance_after):
        self.txn_type = txn_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()