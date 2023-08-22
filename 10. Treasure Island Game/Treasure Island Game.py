print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Phase One
phase1 = input("Where would you like to go? To the left, to the right, or somewhere else?\n").lower()
if phase1 == "left":
    # Phase Two
    phase2 = input("A river lies ahead of you. Do you wish to swim across, wait, or choose a different direction?\n").lower()
    if phase2 == "wait":
        # Phase Three
        phase3 = input("Congratulations, you've advanced to the next phase. You're presented with several doors. Which color door would you like to select? Red, blue, yellow, or something else?\n").lower()
        if phase3 == "yellow":
            print("""Congratulations, You Have WON This Game! 🎉🎉🎉""")
        elif phase3 == "red":
            print("Snap! A fire suddenly ignites. You find yourself engulfed by the flames. The Game is Over")
        elif phase3 == "blue":
            print("""                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                     (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
What's that? Is it a crocodile? Oh no! The beast is drawing near to you. You get devoured by the crocodile. The game has come to an end.""")
        else:
            print("I'm sorry, but you've chosen the wrong door. The game is over.")
    else:
        print("I'm sorry, but you've been attacked by a trout. The game is over.")
else:
    print("You are falling into a hole, and it's Game Over.")