#make a function that will start reading the string from right to left and find the last character, thus removing the spaces at the end
def custom_rstrip(input_string):
    end_index = len(input_string) - 1

    while end_index >= 0 and input_string[end_index] == " ": 
        end_index -= 1
    
    return input_string[:end_index + 1]

#asks the user to input their name + some spaces after it
user_name = input("Please enter your full name and add some spaces at the end = ")

#print
result = custom_rstrip(user_name)
print(f"I removed the spaces at the end for you = '{result}'")
