from services.user import User
from datetime import datetime

class Bankservice():
    def __init__(self,customer_id,password):
        User.customer_id = customer_id
        User.password = password
        self.current_session = datetime.now()
