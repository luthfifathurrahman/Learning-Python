import database
import art
import random

"""import the database"""
data = database.data

def compare_a_b(account1, account2):
    print(f"Compare A: {account1['name']}, {account1['description']}, from {account1['country']}")
    print(art.vs)
    print(f"Against B: {account2['name']}, {account2['description']}, from {account2['country']}")

def game(data):
    accountA = random.choice(data)
    accountB = random.choice(data)
    if accountA == accountB:
        accountB = random.choice(data)
    print(art.logo)
    compare_a_b(account1=accountA, account2=accountB)
    game_over = False
    current_score = 0
    while not game_over:
        guess = input("Who has more follower? Type 'a' or 'b' or 'same': ").lower()
        if ((guess == "a" and accountA['follower_count'] > accountB['follower_count']) or
                (guess == "b" and accountB['follower_count'] > accountA['follower_count'])):
            accountA = accountB
            accountB = random.choice(data)
            print(art.logo)
            current_score += 1
            print(f"You're correct, your current score is {current_score}")
            compare_a_b(account1=accountA, account2=accountB)
        else:
            game_over = True
            print(art.logo)
            print(f"You're wrong, your final score is {current_score}")

game(data)