num1 = input ('please enter the first number ')
num2 = input ('please enter the second number ')
operation = input ('please enter the operation ')

if num1.isdigit() and num2.isdigit():
    print ("first input: ", num1)
    print ("second input: ", num2)
    # eval is and evaluation function to the operation behavior  
    print ('operation result: ', eval(num1+(operation)+num2))
else:
    print ("please make sure to enter numbers for first number and second number")

print("** END **")