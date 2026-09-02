#benjamin copier, average grade.


while True:
    try:
        grade_1 =float(input("first period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_1)
while True:
    try:
        grade_2 =float(input("second period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_2)
while True:
    try:
        grade_3 =float(input("third period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_3)
while True:
    try:
        grade_4 =float(input("fourth period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_4)
while True:
    try:
        grade_5 =float(input("fith period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_5 )
while True:
    try:
        grade_6 =float(input("sixth period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_6)
while True:
    try:
        grade_7 =float(input("seventh period grade: "))
    except:
     print("not a number")
    else:
        break
print(grade_7)
total_numb= grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + grade_6 + grade_7
average_grade= float( total_numb/7)
print("unrounded grade" , average_grade)
rounded_grades= round(average_grade,2)
print("the rounded grade is" ,rounded_grades)