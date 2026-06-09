#Bill Splitter: Take a restaurant bill amount, number of people, and optional tip percentage as input.
# Calculate each person's share including tip, round to 2 decimal places, 
# print a formatted summary. 

bill_amount = float(input("Enter the bill amount: "))
people = int(input("Enter the no of people:"))
tip = input("Enter tip percentage (Press Enter if not required ) :")

if tip:
    tip_percentage = float(tip)
else:
    tip_percentage=0

tip_amnt = bill_amount * tip_percentage /100
total_amount = bill_amount + tip_amnt
share = round(total_amount/people ,2)

print(f"\nTotal Bill: ₹{total_amount: .2f}")
print(f"Each person split:₹{share: .2f}")

      


