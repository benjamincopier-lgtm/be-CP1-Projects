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
new_phone= sphone[0:2]
print(new_phone)
old_phone= sphone[3:7]
print(old_phone)
snew_phone=str(new_phone)
print(snew_phone)
new_phone2= sphone[:6]
print(new_phone2)