print('testing function')
def greet(name):
  """Greets a person by name."""
  print("Hello, " + name + "!")

# Calling the function
greet("Alice")
print('Testing class and its function\n------------------------------\n------------------------------')
class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

# Creating an instance of the Calculator class
calc = Calculator()

# Using the methods
result1 = calc.add(10, 5)
result2 = calc.subtract(15, 7)

print("Addition:", result1)
print("Subtraction:", result2)