#make a function that works just like index()
def custom_index(input_string, substring):
    for i in range(len(input_string) - len(substring) + 1):
        if input_string[i:i + len(substring)] == substring:
            return i
    raise ValueError(f"'{substring}' not found in string")

#asks for user input
user_string = input("Enter a string = ")
substring = input("Enter the substring to find = ")

#print

