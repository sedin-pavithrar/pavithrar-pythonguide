from typing import Optional, List, Dict, Deque
from dataclasses import dataclass
from collections import deque

# A dataclass automatically creates
# __init__()
# __repr__()


@dataclass
class Transaction:
    type:    str # CR/DR
    amount:  float
    balance: float
    note:    Optional[str] = None 

#  Suppose you deposit ₹2000.

# Transaction object become

# Transaction(
#     type="CR",
#     amount=2000,
#     balance=7000,
#     note=None
# )


class BankAccount:
    def __init__(self, 
                holder:str,
                acc_num:str,
                balance:float=0.0) -> None:

        if balance < 0:
            raise ValueError("Opening balance cannot be negative.") 
        
        self.holder: str = holder
        self.acc_num: str = acc_num
        self._balance: float = balance
        self.transactions: Deque[Transaction] = deque(maxlen = 5)

    def _add_transaction(
            self,
            txn_type:str,
            amount:float,
            note:Optional[str] = None) -> None:
        
        transaction = Transaction(
            type = txn_type,
            amount=amount,
            balance= self._balance,
            note = note )
        
        self.transactions.append(transaction)
        
    def deposit(self, amount:float) -> None:
        if not self._amount_check(amount):
            return
        
        self._balance += amount
        self._add_transaction("CR",amount)

        print(f"Deposited Rs.{amount:,.2f}")
        return 


    def withdraw(self, amount:float) -> bool: 
        if not self._amount_check(amount):
            return False
        if not self._balance_check(amount):
            return False
        
        self._balance -= amount
        self._add_transaction("DR",amount)

        print(f"Withdrawn Rs.{amount:.2f}")
        return True
    

    @property
    def balance(self) -> float:
        return self._balance

    def transfer(
        self,
        amount: float,
        target_account: Optional["BankAccount"] = None
    ) -> bool:

        if target_account is None:
            print("Please provide a target account.")
            return False

        if self is target_account:
            print("Cannot transfer to the same account.")
            return False

        if not self._amount_check(amount):
            return False

        if not self._balance_check(amount):
            return False

        self._balance -= amount
        self._add_transaction(
            "DR",
            amount,
            f"Transfer to {target_account.holder}"
        )

        target_account._balance += amount
        
        target_account._add_transaction(
            "CR",
            amount,
            f"Transfer from {self.holder}"
        )

        print(
            f"Transferred Rs.{amount:,.2f} "
            f"to {target_account.holder}"
        )

        return True

    def mini_statement(self) -> List[str]: 
        statement:List[str] = []

        for tx in self.transactions:
            line = (
                f"{tx.type}"
                f":₹{tx.amount:.2f} " 
                f"Balance:₹{tx.balance:.2f}"
            )
            if tx.note:
                line += f" ({tx.note})"
            statement.append(line)

        return statement
    
    def __str__(self) -> str:
        return (
            f"Account Holder: {self.holder} | "
            f"Account Number: {self.acc_num} | "
            f"Balance: Rs.{self._balance:,.2f}"
        )

    def _amount_check(self, amount: float) -> bool:

        if amount <= 0:
            print("Amount must be greater than 0.")
            return False
        return True

    def _balance_check(self, amount: float) -> bool:

        if amount > self._balance:
            print("Insufficient balance.")
            return False
        return True
    
def main() -> None:

    accounts: Dict[str, BankAccount] = {} 

    acc1 = BankAccount("Rahul", "HDFC001", 5000.0)
    acc2 = BankAccount("Priya", "SBI001", 3000.0)

    accounts[acc1.acc_num] = acc1
    accounts[acc2.acc_num] = acc2

    acc1.deposit(2000.0)
    acc1.withdraw(1000.0)
    acc1.transfer(2000.0, acc2)

    print("\n", acc1)

    print("\n----- ACC1 MINI STATEMENT -----")
    for record in acc1.mini_statement():
        print(record)

    print("\n----- ACC2 MINI STATEMENT -----")
    for record in acc2.mini_statement():
        print(record)

    print(f"\nCurrent Balance: Rs.{acc1.balance:.2f}")


if __name__ == "__main__":
    main()
