# sen = "welcome to our class on sunday."
# word = ''

# for char in sen:
#     if char != ' ' and char != '.': 
#         word += char
#     elif char == '.':
#         print(word)
#     else:
#         print(word)
#         word = ''



sen = "welcome to our class on sunday."
word = ''

for char in sen:
    if char != ' ' and char != '.': 
        word += char
    else:
        print(word)
        word = ''