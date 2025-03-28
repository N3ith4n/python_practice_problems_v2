#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#the actual program
user_name = input("What is your full name? = ").title().split()
pascal_case_name = ''.join(word.title() for word in user_name)

#print
print(f"Here is your name in Pascal Case = {pascal_case_name}")
