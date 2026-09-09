#benjamin copier idiot proofing

name=input("what is your first name: ").strip().title()
print("hello " + name.strip().title())
while True:
    try:
        phone =int(input("what is your phone number: "))
        new_phone= phone.split(3)
        int(new_phone)
        new2_phone= " ".join()
        int(new2_phone)

    except:
     print("your phone number in numerical digits")
    else:
        break
