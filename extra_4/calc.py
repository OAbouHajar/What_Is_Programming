# 2 user input ( firs number ) (second number)
# 5 if stat 
# if ()
    # Add + 
    # Sub - 
    # Mul * 
    # Div / 
    # Pow **
# 1 output result 


# print("Hello To calc program!", end="*\n")
# print("\tThis program takes two input\t & \tprint the result out")
# print("\tafter choosing the operation")

print('''Hello To calc program!
This program takes two input & print the result out
after choosing the operation
''')

#  10 + 10 
# int()

user_operation = ''


# user input for number 1 and number 2
# to help confirm the input
# print(num1, type(num1))
# print(num2, type(num2))
while True:
    num1 = input("Please Enter the first number ")
    num2 = input('Please Enter the second number ')

    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        user_operation = input('Please Enter the operation ')
        print('****STAGE 2 *****')

        if user_operation == '+':
            print("The result is: ", num1 + num2)
        elif user_operation == '-':
            print("The result is: ", num1 - num2)
        elif user_operation == '*':
            print("The result is: ", num1 * num2)
        elif user_operation == '/' and num2 != int('0'):
            print("The result is: ", num1 / num2)
        elif user_operation == '**':
            print("The result is: ", num1 ** num2)
        else :
            print("Operation not correct")
    else: 
        print('Number 1 and Number 2 should be a digit')

    print('***** END ******')



# AND TRUE && TRUE == TRUE
# OR TRUE && FALSE == TRUE