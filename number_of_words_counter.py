#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

#the actual program
user_statement = input("Give me a statement to count the number of words in = ").split()
seperated_words = len(user_statement)

#print the total number of words in the string
print(seperated_words)
