alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            shifting_index = alphabet.index(letter) + shift
            new_text += alphabet[shifting_index]
        else:
            new_text += letter
    print(f"The encoded text is {new_text}")

import Caesar_Logo
print(Caesar_Logo.logo)

is_over = False
while not is_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(text=text, shift=shift, direction=direction)
        restart = input("Type 'yes' to start again, type 'no' to end this Caesar Cipher.\n").lower()
        if restart == "no":
            is_over = True
            print("Thank You.")
    else:
        print("Please try again and choose either 'encode' or 'decode'.")