age = input("What is your current age? ")

age = int(age)
age_left = 90 - age
month_left = age_left * 12
week_left = age_left * 52
day_left = age_left * 365

print(f"You have {day_left} days, {week_left} weeks, and {month_left} months left.")