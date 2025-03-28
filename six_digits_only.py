#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

#asks for user input
user_number = input("Give me a number from 0-1000 = ")

#the actual program
fill = user_number.zfill(6)

#print
print(fill)
