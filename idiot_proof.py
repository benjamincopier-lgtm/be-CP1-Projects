#benjamin copier idiot proofing

name=input("what is your first name: ").strip().title()
print("hello " + name.strip().title())
while True:
    try:
        phone =int(input("what is your phone number: "))
    except:
     print("your phone number in numerical digits")
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
print("your phone number is " + new_phone+"-"+new_phone2+"-"+new_phone3)
