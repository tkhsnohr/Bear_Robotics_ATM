from ATM import ATM
from Account import Account

if __name__ == "__main__":
    user_info = Account("Bear", "Robotics", "1234", "1234567890", 1000)
    atm = ATM(10000)

    transaction = True

    while transaction:
        user_input = input("1) Insert card\n0) End transaction\n")
        if user_input == "1":
            atm.insert_card()
            if atm.isCardInserted:
                sign_in_success = user_info.pin_number()
                if sign_in_success:
                    print(f"Hello {user_info.firstName} {user_info.lastName}.")
                    while transaction:
                        user_input = input("\n1) Select account\n0) End transaction\n")
                        if user_input == "1":
                            while transaction:
                                user_input = input(
                                    "\n1) See balance\n2) Deposit\n3) Withdraw\n0) End transaction\n"
                                )
                                if user_input == "1":
                                    user_info.see_balance()
                                elif user_input == "2":
                                    amount = int(input("Enter the deposit amount: "))
                                    user_info.deposit(amount)
                                elif user_input == "3":
                                    amount = int(input("Enter the deposit amount: "))
                                    user_info.withdraw(amount)
                                elif user_input == "0":
                                    transaction = False
                                    atm.end_transaction()
                                else:
                                    print(
                                        "\nInvalid input. Please enter a valid input.\n"
                                    )
                                    continue
                        elif user_input == "0":
                            transaction = False
                            atm.end_transaction()
                        else:
                            print("\nInvalid input. Please enter a valid input.\n")
                            continue

                else:
                    print("\nFailed to sign in. Ending transaction.\n")
                    transaction = False
                    atm.end_transaction()

        elif user_input == "0":
            transaction = False
            atm.end_transaction()

        else:
            print("\nInvalid input. Please enter a valid input.\n")
            continue
