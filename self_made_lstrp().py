#make a function that will find the first charactr in the inputted string
def custom_lstrip(s):
    start_index = 0
    
    # Finds the first non-space character
    while start_index < len(s) and s[start_index] == " ":
        start_index += 1

    #this returns for example s[2:] so the print will start at the letter that is in the start_index
    return s[start_index:]

#asks the user to input their name + some spaces before it
name = input("Please enter your full name and please add some space at front = ")

#print
result = custom_lstrip(name)
print(f"'{result}'") 
