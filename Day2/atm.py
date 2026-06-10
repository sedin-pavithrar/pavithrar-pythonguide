# ATM Machine:  
# Simulate a basic ATM. User enters a PIN (3 attempts max). 
# On success, show balance and let them withdraw/deposit. Block the card after 3 wrong PINs. 
# Welcome to PyBank ATM 
# Enter PIN: **** 
# > Balance: ₹12,500.00 
# > 1. Withdraw 2. Deposit 3. Exit 
# Enter choice: 1 
# Enter amount: 2000 
# > Withdrawn ₹2,000. New balance: ₹10,500.00 

balance = 20000.00
pin = 2505
attempts = 3

print("Welcome to PyBank ATM")

while attempts > 0:
    pin_input = int(input("Enter the PIN:"))
    
    if pin == pin_input:
        print("PIN verified")
        
        while True:
            print(f"Available Balance: {balance}")
            print("\nPlease Select which method you want to proceed\n")
            print("1.Withdraw\n2.Deposit \n3.Exit\n")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                withdraw_amnt = float(input("Enter amount to withdraw: "))
                if withdraw_amnt < 0 :
                    print("Enter amount greater than 0 ")
                
                if withdraw_amnt >= balance:
                    print("Balance Insufficient")
                    break
                else:
                    balance = balance-withdraw_amnt
                    print(f"Withdrawn amount {withdraw_amnt:.2f}. \n Available Balance : {balance:.2f}")
            elif choice == 2:
                deposit_amnt = float(input("Enter ammnt to deposit"))
                if deposit_amnt <= 0:
                    print("Invalid amount")
                else:
                    balance+=deposit_amnt
                    print(f"Available Balanc:{balance}")
            
            elif choice == 3:
                print("Thankyou for using PyBank ATM ")
                break


            else:
                print("Invalid choice")
        break
    else:
        attempts-=1
        print(f"Invalid pin {attempts} left ")

if attempts == 0:
    print("Card block due to 3 incorrect PIN attempts. Please reach the nearest Branch to reset your PIN")






