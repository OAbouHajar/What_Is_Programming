name = input("please enter your name ")
age = input("please enter your age ")
is_student = input("please confirm if you are a student (True/False) ")

#test age int
if int(age) >= 18:
    print("you are an adult")

#test name vowel str
if "o" in name:
    print("vowel o")
elif "a" in name:
    print("vowel a")
else:
    print("no vowel")

#test student bool
if is_student == 'True':
    print("it's great to be a student!")