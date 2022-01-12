# Create a file with the User class, including the __init__ and make_deposit methods
# Add a make_withdrawal method to the User class
# Add a display_user_balance method to the User class
# Create 3 instances of the User class
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
# Have the second user make 2 deposits and 2 withdrawals and then display their balance
# Have the third user make 1 deposits and 3 withdrawals and then display their balance
# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances


class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        return f"User: {self.name}, Balance: {self.account_balance}"
        # print("running database")

    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        return self, user


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
nolan = User("Nolan Rangel", "test@gmail.com")


guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(100).transfer_money(50, nolan)
print(User.display_user_balance(guido))

monty.make_deposit(500).make_deposit(500).make_withdrawal(250).make_withdrawal(250)
print(User.display_user_balance(monty))


nolan.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)
print(User.display_user_balance(nolan))
