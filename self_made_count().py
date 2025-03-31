#make a function that works just like count()
def custom_count(input_string, substring):
    count = 0
    index = 0
    
    while index <= len(input_string) - len(substring):
        if input_string[index:index + len(substring)] == substring:
            count += 1
        index += 1

    return count


#asks for user input

#print
