Day 9  —  Assignment 1
Fully Type-Annotated Banking API
Real-world App
FastAPI / Django typed backend
Overview
Rewrites BankAccount using the typing module:
Optional[str], List[Transaction], Dict[str, BankAccount], and Callable[[Transaction], None].
 @dataclass auto-generates __init__ and __repr__ for Transaction. 
 mypy catches type errors statically before runtime.
 Type annotations are now required in all production Python at Google, Meta, and Stripe.
Problem
Rewrite BankAccount from Day 6 with full type annotations.
Use @dataclass for Transaction. 
Run mypy until zero errors.
Type Reference
Annotation
Meaning
Example
Optional[str]      str or None          def find(id: Optional[str])
List[Transaction]  list of Transaction  transactions: List[Transaction]
Dict[str,float]    dict str to float    rates: Dict[str,float]
-> None            returns nothing      def log(...) -> None:
Starter Code
from typing import Optional, List, Dict
from dataclasses import dataclass
@dataclass
class Transaction:
    type:    str
    amount:  float
    balance: float
    note:    Optional[str] = None
class BankAccount:
    def __init__(self, holder:str, acc_num:str, balance:float=0.0) -> None: 
    def deposit(self, amount:float) -> None: ...
    def withdraw(self, amount:float) -> bool: ...
    def mini_statement(self) -> List[str]: ...
Constraints
•  Every function has return type annotation
•  Every parameter annotated
•  @dataclass for Transaction
•  Run mypy -- fix until 0 errors