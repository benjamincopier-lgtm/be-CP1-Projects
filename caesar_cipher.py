#ben copier caesar cipher
steve6=0
steve=input("do you want to encrypt or to decrypt: ")
if steve=="encrypt":
    steve2=input("what do you want to encrypt")
    steve3=0
    steve4=len(steve2)-1
    while steve3 != steve4:
        steve3+=1
        steve5=(steve2[steve3])
        while steve6 !=28:
            alphabet=("abcdefghigklmnopqrstuvwxyz")
            steve5