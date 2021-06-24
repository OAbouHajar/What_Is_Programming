from datetime import datetime

# while loop to print while the i is less than 10

# i = 0
# # infinity loop - very bad code written:
# while i < 10:
#     print(i)


# i = 1 
# while i <= 10:
#     print(i)
#     i += 1

# takes the users names and exit when we enter x as an input
name = input("please enter the name: ")
num = 0

while name != 'x':
    print('Hello ',name)    
    num += 1
    print("you are in queue position: ", num)
    now = datetime.now()    
    print("time", now)
    name = input("please enter the name: ")
    
    

print("you are out")