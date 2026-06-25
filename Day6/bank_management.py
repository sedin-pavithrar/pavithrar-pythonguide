# Bank Account Management 
# OOP foundation: BankAccount class with __init__, deposit(), withdraw(), get_balance(), mini_statement(), and __str__. 
# Stores the last 5 transactions as a list of dicts recording type 
# (CR/DR), amount, and running balance. __str__ returns a one-line summary. 
# This exact pattern is  used in every fintech backend.
# Problem
# BankAccount class with deposit, withdraw, balance, and mini statement of last 5 transactions.
# Constraints
# • deposit() rejects 0 or negative
# • withdraw() cannot exceed balance
# • transactions stores last 5 only
# Bonus: Add transfer(amount, target_account) between two BankAccount objects.

from collections import deque


class BankAccount:
    def __init__(self, holder: str, acc_num: str, balance: float = 0):

        if balance < 0:
          raise ValueError("Opening balance cannot be negative.")
        
        self.holder = holder
        self.acc_num = acc_num
        self._balance = balance
        self.transactions = deque(maxlen=5) # used deque to take last 5 trans


    def _add_transaction(self, txn_type: str, amount: float):
        transaction = {
            "type": txn_type,
            "amount": amount,
            "balance": self._balance
        }

        self.transactions.append(transaction)


    def deposit(self, amount: float) -> None:
        if not self._amount_check(amount):
            return

        self._balance += amount
        self._add_transaction("CR", amount)

        print(f"Deposited Rs.{amount:,.2f}")
        

    def withdraw(self, amount: float) -> None:

        if not self._amount_check(amount):
            return 

        if not self._balance_check(amount):
            return

        self._balance -= amount
        self._add_transaction("DR", amount)

        print(f"Withdrawn Rs.{amount:,.2f}")

    #Read only property
    @property
    def balance(self) :
        return self._balance


    def transfer(self, amount: float, target_account:"BankAccount" = None) -> None:
         #isinstance(object, class_or_tuple) 
         # object → the value or variable you want to check
         # class_or_tuple → a class/type or a tuple of classes/types

         if target_account is None:
          print("Please provide a target account.")
          return
         
         if not isinstance(target_account, BankAccount): 
          print("Invalid target account.")
          return
          
         if self is target_account:
            print("Cannot transfer to the same account.")
            return

         if not self._amount_check(amount):
            return 

         if not self._balance_check(amount):
            return
        
         self._balance -= amount
         self._add_transaction("DR", amount)

         target_account._balance += amount
         target_account._add_transaction("CR", amount)

         print(
            f"Transferred Rs.{amount:,.2f} "
            f"to {target_account.holder}"
        )


    def mini_statement(self) -> None:
        print("\n----- MINI STATEMENT -----")

        if not self.transactions:
            print("No transactions available.")
        else:
            for txn in self.transactions:
                if txn["type"] == "CR":
                    sign = "+"
                else:
                    sign = "-"
                
                print(f'{txn["type"]} {sign}Rs.{txn["amount"]:.2f} Balance: Rs.{txn["balance"]:.2f}')

        print(f"\nCurrent Balance: Rs.{self._balance:.2f}")

    def __str__(self) -> str:
        return (
            f"Account Holder: {self.holder} | Account Number: {self.acc_num} | Balance: Rs.{self._balance:,.2f}")
    
    
    def _amount_check(self,amount:float) -> bool:
        if amount <= 0:
            print("Amount must be greater than 0.")
            return False
        return True
    
    def _balance_check(self,amount:float) -> bool:
         if amount > self._balance:
            print("Insufficient balance.")
            return False
         return True

        
    
def main():
    acc1 = BankAccount("Rahul", "HDFC001", 5000)
    acc2 = BankAccount("Priya", "SBI001", 3000)
    acc1.deposit(2000)
    acc1.withdraw(10000)
    
    print(acc1)
    acc1.transfer(5000,acc2)

    acc1.mini_statement()

    print()
    acc2.mini_statement()

    print(acc1.balance)

    print(type(acc2)) # checck type of instance

if __name__ =="__main__":
    main()




# isinstance() : "Is this object an instance of this class or type?"

# isinstance(object, classinfo)
# object → the value you want to check
# classinfo → a class, type, or a tuple of classes/types

# It returns:

# True if the object belongs to that type (or a subclass)
# False otherwise

# print(isinstance(10, int))
# # True

# print(isinstance("hello", str))
# # True

# print(isinstance([1, 2, 3], list))
# # True

# print(isinstance(3.14, int))
# # False

# isinstance() vs type()

# You might think this is the same:

# type(x) == int

# But isinstance() is more flexible because it supports inheritance.

# If you pass something else:

# acc1.transfer(1000, "Priya")

# then:target_account = "Priya"

# and: isinstance(target_account, BankAccount)

# becomes: isinstance("Priya", BankAccount)

# Python checks:

# Was "Priya" created from BankAccount?

# No—it was created from str.

# So the result is: False

# When you write:

# acc2 = BankAccount("Priya", "SBI001", 3000)

# Python does two things:

# It creates a new object in memory.
# It attaches that object to the BankAccount class.

# You can think of it like this:

# acc2 ─────► object
#              │
#              └── created by BankAccount

# Python stores the object's type automatically.

# You can see it yourself:

# print(type(acc2))

# Output:

# <class '__main__.BankAccount'>

# So when you call:

# isinstance(acc2, BankAccount)

# Python checks:

# "Was this object created from BankAccount or one of its subclasses?"

# Since acc2 was created using:

# BankAccount(...)

# the answer is yes, so it returns:

# True