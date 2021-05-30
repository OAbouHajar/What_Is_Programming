# if the input not a number  print(error)


grade = input("Enter your mark please! ")
grade_int = int(grade)

print("Your grade is :" , type(grade))
print("Your grade is :" , type(grade_int))



# 61
if grade_int >= 101:
    print("Out of the range!")
elif grade_int >= 70:
    print("A+")
elif grade_int >= 60:
    print("A")
elif (grade_int >= 40):
    print("B")
elif grade_int >= 0 :
    print("C")
else: 
    print("Less than zero not accepted ")



print("Program End")
