# Global Scope
x = 1

def test1():
  # Local Scope
  y = 2
  # can not call global scope in here, unless using global
  global x
  x += 10
  # can use global scope in local scope by calling it like this
  z = x + y
  print(f"enemies inside function: {x}")
  print(f"enemies inside function: {y}")
  print(f"enemies inside function: {z}")


# or there is this way without using global
def test2():
    return x + 1

test1()
print(f"enemies outside function: {x}")

test = test2()
print(test)
# can not call local scope outside

print(f"enemies inside function: {y}")

# Global Constant
"""Pro tips:
use global constant only for variable that you do not want to change
make it capitalize, so you know that it is a global constant and you can not change it
for example:"""

PI = 3.14
URL = "google.com"
