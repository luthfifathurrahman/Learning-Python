total_even_number = 0
# Method One
for number in range(1, 101):
    if number % 2 == 0:
        total_even_number += number

total_even_number1 = 0
# Method Two
for number in range(2, 101, 2):
    total_even_number1 += number

print(total_even_number)
print(total_even_number1)