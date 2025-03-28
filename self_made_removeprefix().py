#makes a def where it will check if the input starts with the prefix
def custom_removeprefix(user_input, prefix):
    if user_input.startswith(prefix):  #this checks if the the string starts with a prefix
        return user_input[len(prefix):]  #uses slicing to remove the prefix
    return user_input  #returns the original string if no prefix is found

#asks the user for input
random_word = input("Enter a random word: ")
prefix = input("Enter the prefix to remove: ")

#print
result = custom_removeprefix(random_word, prefix)
print(f"'{result}'")  # Shows the result after removing the prefix
