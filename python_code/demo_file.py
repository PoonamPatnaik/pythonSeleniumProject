# Read and Print File Contents
# Objective: Write a program to read the contents of a file and print it to the console.
#
# Instructions:
#
# Sample file file1.txt is provided with this assignment.
#
# Write a Python script that opens the file and reads all its contents.
#
# Print the entire content of the file.

reader = open("test.txt","r")

count = 0

with open("test.txt", "r") as file:
    lines = file.readlines()
    for line in file:
        count += 1
print(count)

lines.insert(count, "test 3" + "\n")

with open("test.txt", "w") as file:
     file.writelines(lines)

print(reader.read())


reader.close()