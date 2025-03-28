#make a function just like endswith
def custom_endswith(input_string, suffix):
    if len(input_string) < len(suffix):
        return False
    return input_string[-len(suffix):] == suffix

#asks for user input
user_input = input("Give me a random word =  ")
suffix = input("Enter the suffix to check = ")

#print
result = custom_endswith(user_input, suffix)
print(f"Does the word you gave ends with'{suffix}'? {result}!")
