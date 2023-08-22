print("Welcome to the tip calculator!!")
total_bill = float(input("What was the total bill?\n"))
tip_perc = int(input("What percentage tip would you like to give?\n"))
total_people = int(input("How many people to split the bill?\n"))

tip_perc /= 100
tips = total_bill * tip_perc
actual_bill = round((total_bill + tips) / total_people, 2)
final_bill = "{:.2f}".format(actual_bill)

print(f"Each person should pay: {final_bill}")