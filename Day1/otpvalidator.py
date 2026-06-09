import random 

otp = random.randint(100000,999999)
print("OTP:",otp)

attempts = 3

for i in range(attempts):
    input_otp = int(input("Enter OTP:"))

    if input_otp == otp:
        print("OTP verified")
        break
    else:
        remaining = attempts -i -1
        if remaining > 0 :
            print(f"Invalid OTP.{remaining} attempts left")
        else:
            print("Account Locked.Try after sometime")




