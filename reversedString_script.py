# Python script to reverse a string entered by the user
string = input("Enter a string: ")
reversed = ""

for character in string:
    reversed = character + reversed


print(reversed)
