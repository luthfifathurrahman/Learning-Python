print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
lower_case_name = name.lower()

#Count letter T
T = lower_case_name.count("t")

#Count letter R
R = lower_case_name.count("r")

#Count letter U
U = lower_case_name.count("u")

#Count letter E
E = lower_case_name.count("e")

#Count letter L
L = lower_case_name.count("l")

#Count letter O
O = lower_case_name.count("o")

#Count letter V
V = lower_case_name.count("v")

#Calculate
TRUE = (T + R + U + E)
LOVE = (L + O + V + E)
Score = int(str(TRUE) + str(LOVE))

if (Score < 10) or (Score > 90):
    print(f"Your score is {Score}, you go together like coke and mentos.")
elif (Score >= 40) and (Score <= 50):
    print(f"Your score is {Score}, you are alright together.")
else:
    print(f"Your score is {Score}.")