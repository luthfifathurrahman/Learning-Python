# Library
import art
import random

def deal_card(card, list):
    first_draw = random.choice(card)
    second_draw = random.choice(card)
    list.append(first_draw)
    list.append(second_draw)
    return list

def draw_one_card(card, list):
    draw_one = random.choice(card)
    list.append(draw_one)
    return list

def calculate_card(list):
    score = sum(list)
    if len(list) == 2 and score > 21 and 11 in list:
        list.remove(11)
        list.append(1)
        score = sum(list)
        return score
    return score

def compare(player_score, computer_score, computer_list):
    if player_score > 21:  # if player's score is more than 21, the player lose
        print("Too Bad, you lose. Your score is more than 21.\n")
        blackjack()
    elif computer_score > player_score:  # if the dealer's score is greater than player's score, the player lose the game
        print(f"\nThe dealer's cards: {computer_list}.\nThe dealer's score: {computer_score}, your score: {player_score}.\nSorry, you lose. Better luck next time!\n")
        blackjack()
    elif computer_score < player_score:  # if the dealer's score is less than player's score, the player win the game
        print(f"\nThe dealer's cards: {computer_list}.\nThe dealer's score: {computer_score}, your score: {player_score}.\nCongratulations!! you win!\n")
        blackjack()
    elif computer_score == player_score:  # otherwise it is a draw
        print(f"\nThe dealer's cards: {computer_list}.\nThe dealer's score: {computer_score}, your score: {player_score}.\nNot Bad, you Draw!\n")
        blackjack()

def blackjack():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card_list = []
    computer_card_list = []
    is_play = False
    while not is_play:
        play_or_not = input("Type 'yes' if you want to play Blackjack.\nType 'no' if you do not want to play.\nType Here: ").lower()
        if play_or_not != "yes" and play_or_not != "no":
            # Invalid answer
            play_or_not = input("\nYou provide an invalid answer.\nType 'yes' if you want to play Blackjack.\nType 'no' if you do not want to play.\nType Here: ").lower()
        if play_or_not == "yes":
            # Want to play the game
            print(art.logo)

            # The rules of this blackjack
            rules = """\nHere is The Rules of This Blackjack:
            1. The deck is unlimited in size.
            2. There are no jokers.
            3. The Jack/Queen/King all count as 10.
            4. The Ace count as 11.
            5. The cards have equal probability of being drawn.
            6. Cards are not removed from the deck as they are drawn.
            7. The computer is the dealer."""
            print(rules)

            # Creating a program that randomly selects two card for the player.
            deal_card(card=deck, list=player_card_list)
            player_score = calculate_card(player_card_list)
            print(f"\nYour cards: {player_card_list}, current score: {player_score}")

            # Creating a function that randomly selects one card for the dealer.
            deal_card(card=deck, list=computer_card_list)
            computer_score = calculate_card(computer_card_list)
            print(f"\nThe dealer's cards: {player_card_list[0]}")

            player_less_than_21 = False
            while not player_less_than_21:
                if player_score > 21:
                    player_less_than_21 = True
                    print("Too Bad, you lose. Your score is more than 21.\n")
                    blackjack()
                elif player_score == 21:
                    player_less_than_21 = True
                    print("!!!!BLACKJACK!!!!\n")
                    blackjack()
                elif player_score < 21:
                # if player_score < 21:
                    more_card = False  # Flag if player input wrong answer on another_card
                    while not more_card:
                        # Asking whether the player want to draw more card or pass
                        another_card = input("\nType 'yes' to get another card.\nType 'no' if you want to pass.\nType Here: ")
                        if another_card != "yes" and another_card != "no":  # if the player input an invalid answer
                            # Asked again whether the player want to draw more card or pass
                            another_card = input("\nType 'yes' to get another card.\nType 'no' if you want to pass.\nType Here: ")
                        if another_card == "yes":  # if the player type 'yes'
                            draw_one_card(card=deck, list=player_card_list)
                            player_score = calculate_card(player_card_list)
                            print(f"\nYour cards: {player_card_list}, current score: {player_score}")
                            more_card = True
                        elif another_card == "no":  # if the player type 'no' and have a score more than 21.
                            compare(player_score, computer_score, computer_card_list)
            is_play = True
        elif play_or_not == "no":
            # Do not want to play the game
            print(f"Okay, Thank you, Have a Nice Day!\n")
            is_play = True
            blackjack()

blackjack()