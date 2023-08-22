def greet():
    print("Hello")

greet()

# Function with an input
def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Luthfi")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Luthfi", "Indonesia")
greet_with("London", "John")
greet_with(location="London", name="Todd")