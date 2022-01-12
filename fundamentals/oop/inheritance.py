# original non DRY code

class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    	self.is_roth = is_roth  

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    


# inherited code with super. Add BankAccount class in () behind RetirementAccount

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
    	super().__init__(int_rate, balance)	
        self.is_roth = is_roth	

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

