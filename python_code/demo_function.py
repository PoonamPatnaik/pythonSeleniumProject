# Create a Greeting function
# Objective: Create a function that greets the user.
#
# Instructions:
#
# Write a function called GreetUser that takes a single argument username.
#
# The function should print "Hello, [username]! Welcome to the Python course."
#
# Call the function with username "John".
#
# Expected Output:
#
# Hello, John! Welcome to the Python course.

def Greeting(name):
    print("Hello, " + name + "!" + " Welcome to the Python course.")
Greeting(name="Rahul")


# Average Calculator
# Objective: Calculate the average of three numbers.
#
# Instructions:
#
# Create a function called CalculateAverage that takes three parameters: num1, num2, and num3.
#
# Use the numbers 10,20,30 as input to functions
#
# The function should return the average of these three numbers.
#
# Expected Output:
#
# The average of 10, 20, and 30 is 20.0

def CalculateAverage(num1,num2,num3):
    return (num1+num2+num3)/3
var_av = CalculateAverage(10,20,30)
print("The average of 10, 20, and 30 is ".format(),var_av)


