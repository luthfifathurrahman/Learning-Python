print("Welcome to the Roller Coaster!!!")

# Asking the customer's height to allow whether they can enter the roller coaster
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the roller coaster")
    # Asking how old the customer to decide the ticket price
    age = int(input("How old are you?\n"))
    if age < 12:
        bill = 5
        print("Children Ticket is $5")
    elif age <= 18:
        bill = 7
        print("Teenager Ticket is $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You got a free ticket.")
    else:
        bill = 12
        print("Adult Ticket is $12.")

    # Asking whether the customer want a photo or not
    photo = input("Do you want a photo? Y or N?\n")
    if photo == "Y":
        bill += 3
        print(f"The amount of bill you need to pay is ${bill}")

else:
    print("You can not ride the roller coaster, sorry.")