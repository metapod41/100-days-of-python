print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10 , 12 or 15 -> "))
people = int(input("How many people are there? "))
total_bill += total_bill*tip/100
to_pay = total_bill/people
print(f"Each person should pay : ${round(to_pay,2)}\n")
