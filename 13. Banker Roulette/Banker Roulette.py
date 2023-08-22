# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. (, )\n")
names = names_string.split(", ")

# Select a name from the list at random.
randomizer = random.randint(0, len(names) - 1)
print(f"{names[randomizer]} is going to buy the meal today!")

# Alternatively, we can adopt this approach to simplify matters.
print(f"{random.choice(names)} is going to buy the meal today!")
