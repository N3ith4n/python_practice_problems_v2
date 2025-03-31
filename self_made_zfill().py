#make a function that works just like zfill()
def custom_zfill(input_string, width):
    if len(input_string) >= width:
        return input_string

    zeros_to_add = width - len(input_string)

    return '0' * zeros_to_add + input_string

#asks for user input
user_input = input("Enter a number = ")
width = int(input("What is your desired string width? = "))

#print
result = custom_zfill(user_input, width)
print(f"Here is your number with added zeroes up front to match the width you want = {result}")
