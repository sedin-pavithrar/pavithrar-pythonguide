#Shopping Cart Calculator: Store products as a dictionary (name → price). 
# Let the user add items to a cart list, apply a 10% discount if total exceeds ₹1000, and
#  print an itemised bill with final amount. 

products = {
    1: ("Laptop",500000),
    2: ("Mouse",1000),
    3: ("Airpods",120000),
    4: ("Keyboard",2000) }

cart = []
print("Available Products")
for pid,(item,price) in products.items():
    print(f"{pid}.{item}-₹{price}")

while True:
    choice = int(input("\nEnter product num to add to cart "))

    if choice == 0:
        break

    if choice in products:
        cart.append(choice)
        print(f"{products[choice][0]} added to cart")
    else:
        print("Invalid product number")

total = 0
print("\n Bill")

for item in cart:
    name,price = products[item]
    total+=price
    print(f"{name:<15} ₹{price}")

discount = 0
if total > 1000:
    discount = total * 0.10

final_price = total-discount

print(f"Total Amount :₹{total}")
print(f"Discount(10%) :₹{discount:.2f}")
print(f"Final Amount : ₹{final_price:.2f}") 
