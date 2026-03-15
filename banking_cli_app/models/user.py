class User():
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        """List of Account objects belonging to this user
        Example: [<Account object account_number=1001>,<Account object account_number=1005>]
        """
        self.accounts = []