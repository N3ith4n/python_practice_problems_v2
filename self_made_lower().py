#makes a function like the lower() function
def custom_lower(input_string):
    lowercase_string = ""
    
    for character in input_string:
        if 'A' <= character <= 'Z':
            lowercase_character = chr(ord(character) + 32)
            lowercase_string += lowercase_character
        else:
            lowercase_string += character
            
    return lowercase_string

#get user input
user_input = input("Give me your name: ")

#prints
result = custom_lower(user_input)
print(f"Here is the lower case version of your name: {result}")
