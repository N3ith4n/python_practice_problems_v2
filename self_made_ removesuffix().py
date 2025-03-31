#makes a def where it will check if the input ends with the suffix
def custom_removesuffix(user_input, suffix):
    if user_input.endswith(suffix):
        return user_input[:len(user_input) - len(suffix)]
    return user_input

#asks the user for input
random_word = input("Enter a random word = ")
suffix = input("Enter the suffix to remove = ")

#print
result = custom_removesuffix(random_word, suffix)
print(f"Here is your word minus the suffix you inputted = {result}")
