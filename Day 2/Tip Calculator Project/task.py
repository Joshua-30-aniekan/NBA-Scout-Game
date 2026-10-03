print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much percentage tip would you like to give? 10,12 or 15?"))
people = int(input("how many people to split the bill?"))
amount = (bill + (tip/100) * bill) / people
final_amount = round(amount, 3)
print(f"Each person would pay: ${final_amount}")