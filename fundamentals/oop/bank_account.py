class BankAccount:

#     accounts = []

    def __init__(self, balance = 0, int_rate = .01):
        self.balance = balance
        self.int_rate = int_rate
        # BankAccount.accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")

    def display_account_info(self):
        return f"Balance: {self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    # @classmethod
    # def print_all_accounts(cls):
    #         for account in cls.accounts:
    #                 account.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(balance=0,int_rate=.01)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def transfer_money(self, amount, user):
        self.account.withdrawal(amount)
        user.account.deposit(amount)
        return self, user

    def display_user_balance(self):
        # print(self.account.balance)
        return f"User: {self.name}, Balance: {self.account.balance}"




guido = User("Guido van Rossum")
monty = User("Monty Python")
nolan = User("Nolan Rangel")


# guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(100)
# print(User.display_user_balance(guido))

# monty.make_deposit(500).make_deposit(500).make_withdrawal(250).make_withdrawal(250).transfer_money(200, nolan)
# print(User.display_user_balance(monty))


# nolan.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)
# print(User.display_user_balance(nolan))


# ANSWER

class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        return f"{self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02,1000),
            "savings" : BankAccount(.05,3000)
        }
        

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


adrien = User("Adrien")

adrien.account['checking'].deposit(100)
adrien.display_user_balance()



