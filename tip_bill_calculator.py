print("Welcome to the tip calculator.")

# Step 1: Get inputs and convert to appropriate types
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 20, 30, or 50? "))
people = int(input("How many people to split the bill? "))

# Step 2: Calculate tip and total bill
tip_amount = (tip_percent / 100) * bill
total_bill = bill + tip_amount

# Step 3: Divide by number of people
amount_per_person = total_bill / people

# Step 4: Show result rounded to 2 decimal places
print(f"Each person should pay: ${amount_per_person:.2f}")
