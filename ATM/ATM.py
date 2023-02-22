class ATM:
    def __init__(self, balance):
        self.isCardInserted = False
        self.balance = balance

    def insert_card(self):
        self.isCardInserted = True
        print("Card Inserted.")
        return

    def see_balance(self):
        print(f"{self.balance} in cashbin.")
        return

    def deposit(self, amount):
        self.balance += amount
        return

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance in cashbin.")
        else:
            self.balance -= amount
        return

    def end_transaction(self):
        self.isCardInserted = False
        print("Transaction ended.")
        return
