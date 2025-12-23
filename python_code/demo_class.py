# Understanding class creation in Python
# Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.
#
# Instructions:
#
# Create a class named BasicCalculator.
#
# Define a constructor that initializes two numbers. Use numbers 10 & 5
#
# Implement methods for:
#
# Addition
#
# Subtraction
#
# Multiplication
#
# Division
#
# Each method should return the result of the operation.
#
# Create an instance of the BasicCalculator class and demonstrate the functionality of each method.
#
# Example Output:
#
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0


class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def Addition(self):
        return self.num1 + self.num2

    def Subtraction(self):
        return self.num1 - self.num2
    def Multiplication(self):
        return self.num1 * self.num2
    def Division(self):
        return self.num1 / self.num2
BasicCalculator = BasicCalculator(10,5)
print("Addition:",BasicCalculator.Addition())
print("Subtraction:",BasicCalculator.Subtraction())
print("Multiplication:",BasicCalculator.Multiplication())
print("Division:",BasicCalculator.Division())