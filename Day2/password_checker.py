# Password Strength Checker: 
# Take a password as input. Check for length ≥8, uppercase, lowercase, digit, and special character. 
# Show a strength score (Weak / Medium / Strong) with tips to improve. 

# Enter password: Hello@123 
# Length: OK Upper: OK Lower: OK 
# Digit: OK Special: OK 
# Strength: Strong (5/5) 
# "Your password is secure!" 

print("------Password Strength Checker------")

password = input("Enter your Password: ")

length = len(password) >= 8
upper_case = False
lower_case = False
digit = False
special_char = False

for ch in password:
    if ch.isupper():
        upper_case = True
    elif ch.islower():
        lower_case = True
    elif ch.isdigit():
        digit = True
    else:
        special_char = True

# if length:
#     score+=1
# if upper_case:
#     score+=1
# if lower_case:
#     score+=1
# if digit:
#     score+=1
# if special_char:
#     score+=1

score = 0
checks = {
    "Length": length,
    "UpperCase": upper_case,
    "LowerCase": lower_case,
    "Digit": digit,
    "Special Character": special_char
}
score = sum(checks.values())

for item, status in checks.items():
    print(f"{item}: {'OK' if status else 'Missing'}")

print("\n Password Strength score ")

# if score <= 2:
#     strength = "Weak"
# elif score <= 4:
#     strength = "Medium"
# else:
#     strength = "Strong"

strength = ("Weak" if score <= 2 
            else "Medium" if score <= 4 
            else "Strong"
)

print(f"\nYour password  is : {strength} ({score}/5)")
    
if strength == "Strong":
    print("Your password is secure!")
else:
    print("Tips to improve:")
    tips = {
    "Use at least 8 characters": length,
    "Add an uppercase letter": upper_case,
    "Add a lowercase letter": lower_case,
    "Add a digit": digit,
    "Add a special character": special_char
}
    for tip, status in tips.items():
        if not status:
            print("-", tip)









