#make a function that functions like center()
def custom_center(input_string, width):
    if len(input_string) >= width:
        return input_string
    
    total_spaces = width - len(input_string)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    return ' ' * left_spaces + input_string + ' ' * right_spaces

#enter user input
user_input = input("Enter a random word = ")
width = int(input("Enter your desired width for the string = "))

#print
