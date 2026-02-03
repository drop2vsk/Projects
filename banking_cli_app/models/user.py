class User():
    def __init__(self,customer_id,password):
        self.customer_id = customer_id
        self.password = password
        self.accounts = []