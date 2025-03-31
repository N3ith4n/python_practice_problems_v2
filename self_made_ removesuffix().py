#makes a def where it will check if the input ends with the suffix
def custom_removesuffix(user_input, suffix):
    if user_input.endswith(suffix):
        return user_input[:len(user_input) - len(suffix)]
    return user_input

#asks the user for input

#print
