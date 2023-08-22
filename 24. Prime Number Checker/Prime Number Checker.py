# Method One
def prime_checker1(number):
    if number % 1 == 0 and number % number == 0:
        if number % 2 == 0:
            print("it's not a prime number")
        elif number % 3 == 0:
            print("it's not a prime number")
        elif number % 5 == 0:
            print("it's not a prime number")
        elif number % 7 == 0:
            print("it's not a prime number")
        elif number % 11 == 0:
            print("it's not a prime number")
        else:
            print("It's a prime number")

# Method Two
def prime_checker2(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:
            is_Prime = False
    if is_Prime:
        print("It's a prime number")
    else:
        print("it's not a prime number")

n = int(input("Check this number: "))
prime_checker1(number=n)
prime_checker2(number=n)
