# dictionary
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again."
}

# how to call an item from dictionary
print(programming_dictionary["Bug"])

# adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# creating an empty dictionary
empty_dictionary = {}

# edit an item in a dictionary
programming_dictionary["Bug"] = "an insect"
print(programming_dictionary)

# how to loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)