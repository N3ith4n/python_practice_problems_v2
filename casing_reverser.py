#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

#asks the user for their full name
user_name = input("What is your full name? = ")

#empty string where the changed characters will be stored
reversed = " "

#loop that will check each character and manually change their casing
for a in user_name:
    reversed += a.swapcase()

#print the empty list
print(reversed)
