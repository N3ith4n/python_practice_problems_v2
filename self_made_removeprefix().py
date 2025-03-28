#makes a def where it will check if the input starts with the prefix
def custom_removeprefix(user_input, prefix):
    if user_input.startswith(prefix):
        return user_input[len(prefix):]
    return user_input

#asks the user for input
random_word = input("Enter a random word: ")
prefix = input("Enter the prefix to remove: ")

#print
result = custom_removeprefix(random_word, prefix)
print(f"'{result}'")
