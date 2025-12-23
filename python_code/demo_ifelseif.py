# Create a variable user and assign the value 16
#
# Use if-elif-else statements to print:
#
# "Good Morning" if the hour is between 5 and 11,
#
# "Good Afternoon" if the hour is between 12 and 17,
#
# "Good Evening" if the hour is between 18 and 21,
#
# "Good Night" for all other hours.
#
# Print "Greeting code has completed."
#
# Expected Output:
#
# For input 10:
#
# Good Morning
# Greeting code has completed.
# For input 15:
#
# Good Afternoon
# Greeting code has completed.

user = 16
if  5 <= user <=11:
     print("Good Morning")
     print("Greeting code has completed.")
elif 12 <= user <= 17 :
    print("Good Afternoon")
    print("Greeting code has completed.")

elif 18 <= user <= 21 :
    print("Good Evening")
    print("Greeting code has completed.")

else:
    print("Good Night")
    print("Greeting code has completed.")



