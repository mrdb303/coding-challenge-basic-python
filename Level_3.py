# Coding challenge: Level 3 - Count characters in a string
#
# Create a function that counts the characters in the string;
# "Row Row Row Your Boat"
#
# The function should return a dictionary where the index is the 
# character and its value is the character count.
#
# For example {'R': 3, 'B':1}
# R is found in the string 3 times, B is found in the string 1 time and so on

sentence = "Row Row Row Your Boat"

def get_letter_dict(line):
    char_dict = {}
    for letter in line:
        if letter not in char_dict:
            char_dict.update( {letter : 1} )
        else:
            char_dict[letter] = char_dict[letter] + 1

    return char_dict


print("\nLetter distribution for string: " + sentence)
print(get_letter_dict(sentence))