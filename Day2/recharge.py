# Mobile Recharge Plan Selector: 
# Ask user for their budget and usage preference (calls / data / both). 
# Recommend the best recharge plan from 3 options and show what they save vs the next plan. 

# Enter your budget (₹): 300 
# Preference (calls/data/both): data 
# Best Plan: ₹239 — 1.5GB/day, 28 days 
# You save ₹61 vs the ₹299 plan. 
# Extra data vs ₹199 plan: +0.5GB/day 

print(" ====== Mobile Recharge Plan Selector ====== ")

print()

plans = {
    "calls": [
        {"price": 199, "data": 0.1, "validity": 28, "desc": "Unlimited calls, 100MB/day"},
        {"price": 239, "data": 0.3, "validity": 28, "desc": "Unlimited calls, 300MB/day"},
        {"price": 299, "data": 0.5, "validity": 56, "desc": "Unlimited calls, 500MB/day"}
    ],
    "data": [
        {"price": 199, "data": 1.0, "validity": 28, "desc": "1GB/day, 28 days, 100 mins/day calls"},
        {"price": 239, "data": 1.5, "validity": 28, "desc": "1.5GB/day, 28 days, Unlimited calls"},
        {"price": 299, "data": 2.0, "validity": 56, "desc": "2GB/day, 56 days, Unlimited calls"}
    ],
    "both": [
        {"price": 199, "data": 1.0, "validity": 28, "desc": "1GB/day, 28 days, Unlimited calls, 100 SMS/day"},
        {"price": 239, "data": 1.5, "validity": 28, "desc": "1.5GB/day, 28 days, Unlimited calls, 100 SMS/day"},
        {"price": 299, "data": 2.0, "validity": 56, "desc": "2GB/day, 56 days, Unlimited calls, 100 SMS/day"}
    ]
}

preference = input("Preference (calls/data/both):").lower()

if preference not in plans:
    print("Invalid preference")
else:
    selected_plan = plans[preference]

    print(" \n Available Plans:")
    for plan in selected_plan:
        print(f"₹{plan['price']} = {plan['desc']}")

    budget = int(input("\n Enter your budget ₹"))
    if budget < 199:
        print(f"No plans available for ₹{budget} \n Minimum budget needed:₹199")
    else:
        #Getting all best plan 
        affordable = [plan for plan in selected_plan if plan["price"] <= budget]

        if not affordable:
            print("No plans available ")

        else:
            #Highest price within budget
            best = affordable [-1]
    
            print("\n ---- Recommendation ---- ")
            print(f"Best Plan: ₹{best['price']} - {best['data']}GB/day, {best['validity']} days")


            #savings
            higher = [plan for plan in selected_plan if plan["price"] > best["price"]]
            
            if higher:
                next_plan = higher[0]
                print(f"You save ₹{next_plan['price'] - best['price']} vs ₹{next_plan['price']} plan")
            else:
                print ("You save ₹0")

             # previous plan
            lower = [plan for plan in selected_plan if plan["price"] < best["price"]]
            if lower:
                prev_plan = lower[-1]
                diff = best["data"] - prev_plan["data"]
                print(f"Extra data vs ₹{prev_plan['price']} plan: +{diff:.2f}GB/day")
            else:
                print("No lower plan to compare")

            

                



          
         







