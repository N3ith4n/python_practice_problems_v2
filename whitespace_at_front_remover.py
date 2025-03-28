#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

#asks for user input
user_name = input("Please give me your name and add some space at front too = ")

#the actual program
changed = user_name.lstrip()

#print
print(changed)
