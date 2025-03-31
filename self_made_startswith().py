#make a function just like startswith
def custom_startswith(input_string, prefix):
    if len(input_string) < len(prefix):
        return False
    return input_string[:len(prefix)] == prefix

#asks for user input
user_input = input("Give me a random word =  ")
prefix = input("Enter the prefix to check = ")

#print
result = custom_startswith(user_input, prefix)
print(f"Does the word you gave starts with'{prefix}'? {result}!")
