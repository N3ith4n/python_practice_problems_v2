#make a function that functions just like capitalize()
def custom_capitalize(input_string):
    if len(input_string) == 0:
        return input_string
      
    return input_string[0].upper() + input_string[1:].lower()

#asks for user input
user_input = input("Enter a random word = ")

#print
