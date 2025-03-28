#make a function that will find the first charactr in the inputted string
def custom_lstrip(s):
    start_index = 0
    
    while start_index < len(s) and s[start_index] == " ":
        start_index += 1
        
    return s[start_index:]

#asks the user to input their name + some spaces before it
name = input("Please enter your full name and please add some space at front = ")

#print
result = custom_lstrip(name)
print(f"I removed the spaces at front for you = {result}") 
