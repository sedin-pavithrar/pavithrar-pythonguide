# Currency Conversion: 
# You are building a currency converter for a travel app. Given an amount, a from_currency, and a to_currency, 
# convert the amount using fixed exchange rates (all relative to USD as base) and return a formatted result string. 
# The converter must also display what the same amount equals across all supported currencies. 
# Example 1 
# Input 
# amount = 100 
# from_currency = "USD" 
# to_currency = "INR" 
# Output 
# $100.00 USD → ₹8,450.00 INR 
# Rate: 1 USD = 84.5000 INR 
# Example 2 
# Input 
# amount = 5000 
# from_currency = "INR" 
# to_currency = "USD" 
# Output 
# ₹5,000.00 INR → $59.17 USD 
#Rate: 1 INR = 0.0118 USD 
# Example 3 — invalid input 
# Input 
# amount = 100 
# from_currency = "XYZ" 
# to_currency = "INR" 
# Output 
# "Error: 'XYZ' is not a 
# supported currency." 
# Constraints 
# 0 < amount <= 10,000,000 — amount is always a positive number 
# from_currency and to_currency are strings — validate against supported list 
# If either currency is unsupported, return an error string — do not crash 
# Output amounts must be rounded to 2 decimal places 
# Exchange rate in output must show 4 decimal places 
# from_currency == to_currency is valid — return the same amount with a note 



print("===== Currency Converter =====")

currencies = {
    "USD": 1,
    "INR": 84.5,
    "EUR": 0.87,
    "GBP": 0.75,
    "JPY": 154,
    "AED": 3.67,
    "CAD": 1.36
}
print()
for currency,amount in currencies.items():
    print(f"{currency} -> {amount}")

print("Enter the from currency and to currency to get converted ")
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
amount = float(input("Enter amount: "))

if amount <= 0 or amount > 10000000:
    print("Error: Amount must be between 0 and 10,000,000.")
    exit()

if from_currency not in currencies :
    print(f"Error: '{from_currency}' is not a supported currency.")

elif to_currency not in currencies:
    print(f"Error: '{to_currency}' is not a supported currency.")

else:

    if from_currency == to_currency:
        print(f"\n{amount:.2f} {from_currency} = {amount:.2f} {to_currency}")
        print("Note: Source and destination currencies are the same.")

    else:
        amount_in_usd = amount / currencies[from_currency]
        converted_amount = amount_in_usd * currencies[to_currency]

        exchange_rate = ( currencies[to_currency] / currencies[from_currency])

        print("\n----- Conversion Result -----")
        print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
        )

        print( f"Rate: 1 {from_currency} = {exchange_rate:.4f} {to_currency}"
        )
    print("\n ---- Equivalent in all currencies ----")
    amount_in_usd = amount / currencies[from_currency]
    for currency, rate in currencies.items():
        value = amount_in_usd * rate
        print(f"{currency}: {value:.2f}")

