class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def withdraw(self, amount, provide_pin):
        if provide_pin == self.__pin:
            print(f"correct pin")
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Amount withdrawn: {amount}")
            else:
                print(f"Insufficient balance")
        else:
            print(f"Incorrect PIN")

    def deposit(self, amount, provide_pin):
        if provide_pin == self.__pin:
            print(f"correct pin")
            self.__balance += amount
            print(f"Amount deposited: {amount}")
        else:
            print(f"Incorrect PIN. Transaction denied")

    def change_pin(self, provide_old_pin, new_pin):
        if provide_old_pin == self.__pin:
            self.__pin = new_pin
            print(f"PIN changed successfully")
        else:
            print(f"Incorrect old PIN. cannot change PIN")

    def check_balance(self, provide_pin):
        if provide_pin == self.__pin:
            print(f"Your balance is: {self.__balance}")
        else:
            print(f"Incorrect PIN. cannot show balance")

account_owner1 = ATM(15000, 12345)

# deposit money
account_owner1.deposit(12000, 12345)

# check balance
account_owner1.check_balance(12345)

# withdraw money
account_owner1.withdraw(5000, 12345)

# check balance
account_owner1.check_balance(12345)

account_owner1.change_pin(12345, 67891)

account_owner1.check_balance(12345)