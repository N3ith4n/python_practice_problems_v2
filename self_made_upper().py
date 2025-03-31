#makes a function like the upper() function
def custom_upper(input_string):
    uppercase_string = ""
    
    for character in input_string:
        if 'a' <= character <= 'z':
            uppercase_character = chr(ord(character) - 32)
            uppercase_string += uppercase_character
        else:
            uppercase_string += character
            
    return uppercase_string

#get user input
user_input = input("Give me your name: ")

#prints
result = custom_upper(user_input)
print(f"Here is the upper case version of your name: {result}")
