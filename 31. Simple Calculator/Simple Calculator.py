# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary
calc_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    import art
    print(art.logo)
    num1 = float(input("What is the first number: "))
    continue_calculation = False
    while not continue_calculation:
        symbol_calc = []
        for char in calc_operations:
            print(char)
            symbol_calc.append(char)
        operation = input("Pick an operation: ")
        if operation not in symbol_calc:
            operation = input("Sorry, you pick invalid operation, please provide the correct operation: ")
        num2 = float(input("What is the next number: "))
        function = calc_operations[operation]
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        want_another = False
        while not want_another:
            another_calculation = input(f"""\nType 'yes' to continue the calculation with {answer}.\nType 'no' to stop the calculation.\nType 'new' to start a new calculation.\nType here: """).lower()
            if another_calculation != "yes" and another_calculation != "no" and another_calculation != "new":
                another_calculation = input(f"""\nInvalid Answer.\nType 'yes' to continue the calculation with {answer}.\nType 'no' to stop the calculation.\nType 'new' to start a new calculation.\nType here: """).lower()
            if another_calculation == "yes":
                num1 = answer
                want_another = True
            elif another_calculation == "new":
                continue_calculation = True
                want_another = True
                calculator()
            elif another_calculation == "no":
                continue_calculation = True
                want_another = True
                print("Thank you for using this simple calculator program.")

calculator()