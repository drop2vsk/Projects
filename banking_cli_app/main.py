from services.bank_service import Bankservice

bank_service = Bankservice()
banking_portal = '============== Banking Portal =============='
banking_portal_end = '============================================'

def login_menu():
        print(banking_portal)
        print('1. Login')
        print('2. Create User')
        print('3. Exit')
        print(banking_portal_end)
        choice = input("Enter choise: ")
        return choice

def banking_menu():
        print(banking_portal)
        print('1. View Accounts')
        print('2. Account Details')
        print('3. Deposit')
        print('4. Withdraw')
        print('5. Transaction History')
        print('6. Create Account')
        print('7. Logout')
        print(banking_portal_end)
        choice = input("Enter choise: ")
        return choice

while True:
    if bank_service.current_user is None:
