# Train Ticket Fare Calculator: 

# Take passenger age, class (Sleeper/3AC/2AC), and distance (km). 
# Apply senior citizen discount (60+), children's fare (under 12), and calculate GST.
#  Print a ticket summary. 
# Passenger name: Rahul 
# Age: 63 | Class: 3AC | Distance: 850 km 
# Base fare: ₹1,105.00 
# Sr. discount: - ₹110.50 (10%) 
# GST (5%): + ₹49.73 
# Total: ₹1,044.23 
# "Booking confirmed for Rahul — Bon voyage!" 


print("=====Train Ticket Fare Calculator=====")

name = input("Enter passenger name:")
age = int(input("Enter your age:"))

classes = {
    1:{"name" : "Sleeper" , "rate":1.0},
    2:{"name" : "2AC" , "rate":1.3},
    3:{"name" : "3AC", "rate":1.6}
}

print("Select which class you have to travel \n 1.Sleeper\n 2.2AC\n 3.3AC \n")
sl_class = int(input("Enter your choice:"))
distance = int(input("Enter distance(km):"))

if sl_class not in classes:
    print("Invalid class selected")
    exit()

class_name = classes[sl_class]["name"]
rate_per_km = classes[sl_class]["rate"]

base_fare = distance * rate_per_km

discount = 0

if age < 12:
    discount = base_fare * 0.10
    discount_type = "Child discount"

elif age >= 60:
    discount = base_fare * 0.10
    discount_type = "Sr.discount"

else:
    discount_type = "No discount"

fare_after_dis = base_fare - discount 
gst = fare_after_dis*0.05
total = fare_after_dis + gst

print("\n -----Ticket Summary-----")

print(f"Passenger Name:{name}")
print(f"Age:{age} | Class: {class_name} | Distance:{distance} km")
print(f"Base Fare : ₹{base_fare:.2f}")

if discount > 0:
    print(f"{discount_type}: - ₹{discount:.2f} ")
else:
    print(f"{discount_type}: ₹0.00")

print(f"GST (5%): + ₹{gst:.2f}")
print(f"Total Fare: ₹{total:.2f}")

print(f'\n Booking confirmed for {name} — Bon voyage!')






