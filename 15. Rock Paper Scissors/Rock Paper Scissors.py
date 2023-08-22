import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

database = [rock, paper, scissors]

# User Choice
user_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors\n"))

# Computer Choice
comp_choice = random.randint(0, 2)

# Result
if ((user_choice == 0 and comp_choice == 2) or
        (user_choice == 2 and comp_choice == 1) or
        (user_choice == 1 and comp_choice == 0)):
    print(f"You choose:\n{database[user_choice]}")
    print(f"Computer choose:\n{database[comp_choice]}")
    print("You Win!")
elif ((user_choice == 2 and comp_choice == 0) or
      (user_choice == 1 and comp_choice == 2) or
      (user_choice == 0 and comp_choice == 1)):
    print(f"You choose:\n{database[user_choice]}")
    print(f"Computer choose:\n{database[comp_choice]}")
    print("You Lose")
elif comp_choice == user_choice:
    print(f"You choose:\n{database[user_choice]}")
    print(f"Computer choose:\n{database[comp_choice]}")
    print("Draw")
else:
    print("Start again and type 0 for rock, type 1 for paper, type 2 for scissors")