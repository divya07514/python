class Account():

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance =  self.balance + amount
        print(f"Amount deposited is {amount}")

    def withdraw(self, amount):
        if not self.balance < amount:
            self.balance =  self.balance - amount
            print(f"Amount withdrawn is {amount}")
        else:
            print(f"Not Enough balance left. Current balance is {self.balance}")


    def __str__(self):
        return f"Balance is {self.balance}\n"


acc = Account("Divya", 100)
print(acc)

acc.deposit(100)
acc.deposit(300)
print(acc)

acc.withdraw(300)
print(acc)
acc.withdraw(600)


