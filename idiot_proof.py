#benjamin copier idiot proofing

name=input(f"what is your first name: ").strip().title()
print("hello " + name.strip().title())
while True:
    try:
        phone =int(input(f"what is your phone number: "))
    except:
     print(f"your phone number in numerical digits")
    else:
        break
sphone=str(phone)
print(sphone)
new_phone= str(sphone[0:3])
print(new_phone)
new_phone2= str(sphone[3:6])
print(new_phone2)
new_phone3= str(sphone[6:10])
print(new_phone3)
print(f"your phone number is " + new_phone+"-"+new_phone2+"-"+new_phone3)
while True:
    try:
        grade_1 =float(input(f"first period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_1)
while True:
    try:
        grade_2 =float(input(f"second period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_2)
while True:
    try:
        grade_3 =float(input(f"third period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_3)
while True:
    try:
        grade_4 =float(input(f"fourth period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_4)
while True:
    try:
        grade_5 =float(input(f"fith period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_5 )
while True:
    try:
        grade_6 =float(input(f"sixth period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_6)
while True:
    try:
        grade_7 =float(input(f"seventh period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_7)
total_numb= grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + grade_6 + grade_7
average_grade= float( total_numb/7)
print(f"unrounded grade" , average_grade)
rounded_grades= round(average_grade,1)
print("the rounded grade is" ,rounded_grades)