#make a function that works the same as title()
def custom_title(input_string):
    words = input_string.split()
    
    capitalized_words = [word[0].upper() + word[1:].lower() if len(word) > 0 else word for word in words]
  
    return ' '.join(capitalized_words)

#asks for user input
user_input = input("Give me a random sentence = ")

#print
