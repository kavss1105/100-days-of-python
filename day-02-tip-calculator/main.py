print("Welcome to the Tip Calculator")
a = float(input("What was the total bill amount ? ₹"))
b = float(input("How much tip would you like to give? 10, 15 or 20? "))
c = float(input("How many people to split the bill? "))
tip = (a * b) / 100
print(tip)
bill = tip + a
print(bill)
each_person = bill / c 
print(f"Each person should pay: ₹{round(each_person, 2)}")