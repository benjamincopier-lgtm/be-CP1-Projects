#benjamin copier user sing in

username= ("stungbyawasp8000times")
password=("codz0mbiesareawsome")
inputed_username= input("input your username: ")
inputed_password= input("input your password: ")
if username==inputed_username:
    print("correct username")
    if password==inputed_password:
        print("you logged in.")
    else:
        print("wrong password")
else:
    print("wrong username")