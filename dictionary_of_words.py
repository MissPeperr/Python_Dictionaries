# PRACTICE: Dictionary of Words

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

word_definitions = {
    "code": "program instructions",
    "human": "a human being, especially a person as distinguished from an animal or (in science fiction) an alien",
}
"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["awesome"] = "The feeling of students when they are learning Python"
word_definitions["poop"] = "often used in my code when I test it"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(f'What\'s the word for "{word_definitions["code"]}"?')
print(f'What\'s the word for "{word_definitions["poop"]}"?')

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (key, value) in word_definitions.items():
    print(f'The definition of {key} is: {value}')