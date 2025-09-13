class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit_amount(self, amount):
        self.balance = self.balance + amount
        print(f"Amount deposited: {amount}")
    
    def withdraw_amount(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Amount withdrawn: {amount}")
        else:
            print(f"Insufficient balance")

    def transfer(self, amount, other_account):
        other_account.account_number = other_account
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transfered {amount} from {self.account_number} to {other_account.account_number}")
        else:
            print(f"Insufficient balance for transfer")
