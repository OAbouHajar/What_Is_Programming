
# numbers = {
#   "osama": '083453641',
#   "jack": '083453641',
#   "sam": '083453641'
# }

# print(numbers.items())

# for k, v in numbers.items():
#     print("Name: ", k, "\tPhone number: ",v)



more = ''
numbers = dict()

while more != 'x': 
    name = input('Please enter the name: ')
    number = input('Please enter the number: ')
    # here we add to dict
    numbers[name] = number
    # here we tell the user the name was added
    print("***** your entry was added successfully *****")
    more = input("more contact Y, X to exit? ")

print_all = input('do you want to print the contact list? y or n ')

if (print_all == 'y'):
    for key,value in numbers.items():
        print('Name: ',key, '\tNumber:', value)
