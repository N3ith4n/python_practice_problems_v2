#makes a function that is like isupper()
def custom_is_upper(input_string):
    for character in input_string:
        if character.isalpha() and not ('A' <= character <= 'Z'):
            return False
    return True
  
#take user input
user_input = input("Input your name お願いします: ")

#print
