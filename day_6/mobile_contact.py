# empty dict to start the program
contacts = {}
# to start the loop
letter = ''

# 'a': [ahmad, amir, ana]


while letter != 'quit':
    letter = input('please enter the letter you want to create: ')
    name = input('please enter the name you want under this letter > ' + letter + ' <: ')

    if letter != 'quit':
        #         key      value
        #           a    :  Ahmad
        # contacts[letter] = name
        contacts[letter] = name 

    # now we print the contant of the dict
    print(contacts)