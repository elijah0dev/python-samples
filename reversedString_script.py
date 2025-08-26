string = input("Enter a string: ")
reversed = ""

for character in string:
    reversed = character + reversed

print(reversed)