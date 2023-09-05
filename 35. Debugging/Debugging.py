############DEBUGGING#####################

def my_function():
    for i in range(1, 20):
#   for i in range(1, 21):
        """The problem is in range(1, 20) it will never reach 20 because of this code. it is better to change it into range(1,21)"""
        if i == 20:
            print("You got it")
my_function()

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
# dice_num = randint(0, 5)
print(dice_imgs[dice_num])
# print(dice_imgs[dice_num - 1])
""" The problem is dice_imgs[dice_num], there will be an index error because dice_imgs start from 0 and finish at 5.
meanwhile the dice_num is starting from 1 until 6. So if you use dice_imgs[dice_num], there is a possibility that the code will call
dice_imgs[6]. that's why it should be dice_imgs[dice_num - 1]
OR
we can change randint(1, 6) into randint(0, 5)"""

year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
if year > 1980 and year < 1994:
    print("You are a millenial.")
# elif year >= 1994:
elif year > 1994:
  print("You are a Gen Z.")
"""
the problem is 1994 is not included in the if elif statement."""

age = input("How old are you?")
# age = int(input("How old are you?"))
if age > 18:
  # print(f"You can drive at age {age}.")
print("You can drive at age {age}.")
"""
the first error is in age variable, the output from 'age' variable is string, we need to change it to int.
the second error is the print code is not indented.
the third error is you need to put f-string to call age variable inside the print function"""

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
"""
the problem is lay on
word_per_page == int(input("Number of words per page: "))
do not use ==, it should be =."""

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    # b_list.append(new_item)
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
"""
the problem is
b_list.append(new_item)
it should indented, or put it inside the for loops. so it will append all the new_item in every loops.
"""