#make a function that works just liike rjust()
def custom_rjust(input_string, width):
    if len(input_string) >= width:
        return input_string
      
    spaces_to_add = width - len(input_string)
    
    return ' ' * spaces_to_add + input_string

#asks for user input
user_input = input("Enter a random word = ")
width = int(input("What is your desired string width? = "))

#print
result = custom_rjust(user_input, width)
print(f"Here is the adjusted string with your desired string width = '{result}'")
