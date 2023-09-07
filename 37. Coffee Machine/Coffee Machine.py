from art import logo


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def resources_check(coffee_ingredients):
    # TODO 4: Check resources sufficient
    """Return True if out of resources"""
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            return True


def coin_paid():
    # TODO 5: Process coins.
    """Return he total amount of coins inserted into the machine."""
    print("Please insert coins.")
    coin_inserted = int(input("How many quarters? ")) * 0.25
    coin_inserted += int(input("How many dimes? ")) * 0.1
    coin_inserted += int(input("How many nickles? ")) * 0.05
    coin_inserted += int(input("How many pennies? ")) * 0.01
    return coin_inserted


def process(coffee):
    """Verify the sum of coins inserted to determine if it meets the cost of the selected coffee.
    If it is sufficient,proceed with the coffee preparation process."""
    coffee_water = MENU[coffee]["ingredients"]["water"]
    coffee_milk = MENU[coffee]["ingredients"]["milk"]
    coffee_gram = MENU[coffee]["ingredients"]["coffee"]
    coffee_cost = MENU[coffee]["cost"]
    paid = coin_paid()
    # TODO 6: Check transaction successful?
    if paid < coffee_cost:
        print("Sorry that's not enough money. Money refunded")
    else:
        # TODO 7: Make Coffee
        resources['water'] -= coffee_water
        resources['milk'] -= coffee_milk
        resources['coffee'] -= coffee_gram
        if paid == coffee_cost:
            resources["money"] = paid
            print(f"Here is your {coffee}, Enjoy! ☕")
        elif paid > coffee_cost:
            resources["money"] += coffee_cost
            change = paid - coffee_cost
            final_change = "{:.2f}".format(change)
            print(f"Here is your {coffee}, Enjoy! ☕")
            print(f"Here is ${final_change} dollars in change")


def coffee_machine():
    """Main function for the coffee machine"""
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”
    coffee_machine_on = True
    while coffee_machine_on:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
        if prompt == "off":
            coffee_machine_on = False
            print("Thank you for using the machine.")
        # TODO 3: Print report. When the user enters “report” to the prompt, it shows the current resource values.
        elif prompt == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}gram\nMoney: ${resources['money']}")
        else:
            if resources_check(MENU[prompt]["ingredients"]):
                for item in MENU[prompt]["ingredients"]:
                    if MENU[prompt]["ingredients"][item] > resources[item]:
                        print(f"Sorry there is not enough {item}. Kindly reach out to the administrator.")
                        coffee_machine_on = False
            else:
                process(prompt)


print(logo)
coffee_machine()
