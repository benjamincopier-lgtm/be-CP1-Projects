#benjamin copier, password strength checker

password= input("input your new password, it should have a capital letter, a number, and should be eight or more characters long: ")
password_caps_check=password.lower()
#print(password_caps_check)
if password != password_caps_check:
    true1=True
else:
    true1=False
    print("no capitals are in your password")
"""int_find_in_password1=password.find("1")
int_search1=int(int_find_in_password1)
int_find_in_password2=password.find("2")
int_search2=int(int_find_in_password2)
int_find_in_password3=password.find("3")
int_search3=int(int_find_in_password3)
int_find_in_password4=password.find("4")
int_search4=int(int_find_in_password4)
int_find_in_password5=password.find("5")
int_search5=int(int_find_in_password5)
int_find_in_password6=password.find("6")
int_search6=int(int_find_in_password6)
int_find_in_password7=password.find("7")
int_search7=int(int_find_in_password7)
int_find_in_password8=password.find("8")
int_search8=int(int_find_in_password8)
int_find_in_password9=password.find("9")
int_search9=int(int_find_in_password9)
int_find_in_password0=password.find("0")
int_search0=int(int_find_in_password0)
if int_search1>=0 or int_search2>=0 or int_search3>=0 or int_search4>=0 or int_search5>=0 or int_search6>=0 or int_search7>=0 or int_search8>=0 or int_search9>=0 or int_search0>=0:
    true2=True
    print("cheese")
else:
    True2=False
    print("you should have a number")"""
int_find_in_password1=password.find("1","2","3","4","5","6","7","8","9","0")
if int_find_in_password1 >= 0:
    print("true")
else:
    print("false")
password_length_check=len(password)
if password_length_check >= 8:
    true3=False
    print("2")
else:
    print("3")