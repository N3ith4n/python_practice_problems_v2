#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#the actual program
user_name = input("What is your full name? (input it in incorrect casing please) = ")
snake_case_name = '_'.join(word.lower() for word in user_name.split())

#print
print(f"Here is your name in snake_case = {snake_case_name}")

