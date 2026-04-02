from services.bank_service import Bankservice

bank_service = Bankservice()
banking_portal = "============== Banking Portal =============="
banking_portal_end = "============================================"


def login_menu():
    print(banking_portal)
    print("1. Login")
    print("2. Create User")
    print("3. Exit")
    print(banking_portal_end)
    choice = input("Enter choise: ")
    return choice


def banking_menu():
    print(banking_portal)
    print("1. View Accounts")
    print("2. Account Details")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transaction History")
    print("6. Create Account")
    print("7. Logout")
    print(banking_portal_end)
    choice = input("Enter choise: ")
    return choice


while True:
    if bank_service.current_user is None:
        login_menu_option = login_menu()
        if login_menu_option == 1:
            user_name = input("Enter the Username: ")
            password = input("Enter Password: ")
            bank_service.user_login(user_name, password)
        elif login_menu_option == 2:
            user_name = input("Enter the Username: ")
            password = input("Enter Password: ")
            bank_service.create_user(user_name, password)
        elif login_menu_option == 3:
            break
