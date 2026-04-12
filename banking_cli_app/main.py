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
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None
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
    print(banking_portal_end, end="\n")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None
    return choice


def main():
    while True:
        if bank_service.current_user is None:
            login_menu_option = login_menu()
            if login_menu_option == 1:
                user_name = input("Enter the Username: ")
                password = input("Enter Password: ")
                try:
                    bank_service.user_login(user_name, password)
                    print(f"User {user_name} logged in successfully")
                    while bank_service.current_user is not None:
                        banking_menu_option = banking_menu()
                        if banking_menu_option == 1:
                            try:
                                current_user_details = bank_service.get_user_account()
                                print(current_user_details)
                            except ValueError as e:
                                print(e)
                        elif banking_menu_option == 2:
                            try:
                                current_user_account_details = (
                                    bank_service.get_account()
                                )
                                print(current_user_account_details)
                            except ValueError as e:
                                print(e)
                        elif banking_menu_option == 3:
                            try:
                                deposit = bank_service.deposit()
                                print(deposit)
                            except ValueError as e:
                                print(e)
                        elif banking_menu_option == 4:
                            try:
                                withdraw = bank_service.withdraw()
                                print(withdraw)
                            except ValueError as e:
                                print(e)
                        elif banking_menu_option == 5:
                            try:
                                transactions_history = bank_service.get_transactions()
                                print(transactions_history)
                            except ValueError as e:
                                print(e)
                        elif banking_menu_option == 6:
                            try:
                                create_account = bank_service.create_account()
                                print(create_account)
                            except ValueError as e:
                                print(e)
                        elif banking_menu_option == 7:
                            try:
                                bank_service.user_logout()
                                print("Logged out successfully")
                                break
                            except ValueError as e:
                                print(e)
                except ValueError as e:
                    print(e)
            elif login_menu_option == 2:
                user_name = input("Enter the Username: ")
                password = input("Enter Password: ")
                try:
                    bank_service.create_user(user_name, password)
                except ValueError as e:
                    print(e)
            elif login_menu_option == 3:
                break


if __name__ == "__main__":
    main()
