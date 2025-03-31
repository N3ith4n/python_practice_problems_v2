#makes a function that is like islower()
def custom_is_lower(input_string):
    for character in input_string:
        if character.isalpha() and not ('a' <= character <= 'z'):
            return False
    return True
  
#take user input
user_input = input("Input your name お願いします = ")

#print
result = custom_is_lower(user_input)
print(f"Is your name all in lowercase? {result}")
