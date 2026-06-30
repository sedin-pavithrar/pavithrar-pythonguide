import os,sys
import json

def calculate_total(items,discount=0,tax=0.18):
    total=0
    for item in items :
        total=total+item["price"]*item["quantity"]
    if discount>0 :
        total=total-(total*discount/100)
    return round(total,2)

def apply_tax(total, tax=0.18):
    return round(total * (1 + tax), 2)


class Invoice:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def total(self):
        return calculate_total(self.items)
