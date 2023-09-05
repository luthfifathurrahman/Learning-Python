import random
import art

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

def guessing(attempt):
    random_number = random.randint(1, 100)
    print(f"\npst! Correct Answer: {random_number}")
    print(f"Your Attempt: {attempt}")
    game_over = False
    while not game_over:
        if attempt > 0:
            guess_number = int(input("Make a guess: "))
            if guess_number == random_number:
                game_over = True
                print("\nCongratulations!! You Got It!!\n")
                play_again()
            elif guess_number > random_number:
                attempt -= 1
                print(f"\nToo High.\nGuess Again.\nYour Attempt: {attempt}")
            elif guess_number < random_number:
                attempt -= 1
                print(f"\nToo Low.\nGuess Again\nYour Attempt: {attempt}")
        elif attempt == 0:
            game_over = True
            print("\nToo Bad, You don't have any attempts.\nGAME OVER.\n")
            play_again()

def number_guessing():
    difficulty_correct = False
    while not difficulty_correct:
        difficulty = input("""Welcome to The Number Guessing Game!\nI'm thinking of a number between 1 to 100.\nChoose a difficulty. Type 'easy' or 'hard': """).lower()
        if difficulty != "easy" and difficulty != "hard":
            difficulty = input("Invalid Input.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            guessing(attempt=EASY_ATTEMPT)
            difficulty_correct = True
        elif difficulty == "hard":
            guessing(attempt=HARD_ATTEMPT)
            difficulty_correct = True

def play_again():
    is_again = False
    while not is_again:
        again = input("""Do you want to play again? Type 'yes' or 'no': """).lower()
        if again != 'yes' and again != 'no':
            again = input("""Invalid input. Type 'yes' or 'no': """).lower()
        if again == 'yes':
            is_again = True
            print(art.logo)
            number_guessing()
        elif again == 'no':
            print("Thank you for playing the game")
            is_again = True

print(art.logo)
number_guessing()