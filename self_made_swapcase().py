#make a function that functions just like swapcase()
def custom_swapcase(input_string):
    swapped_string = ""

    for character in input_string:
        if 'a' <= character <= 'z':
            swapped_string += character.upper() 
        elif 'A' <= character <= 'Z':
            swapped_string += character.lower()
        else:
            swapped_string += character

    return swapped_string

#ask for user input
user_input = input("Enter a random word or sentence = ")

#print
result = custom_swapcase(user_input)
print(f"This is the result of swapping all the cases on the word/sentence you gave = {result}")
