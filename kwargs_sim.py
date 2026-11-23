#kwargs and functions suck

def answer(**kwargs):
    print(**
          kwargs)


shalp= []
sed=True
while sed==True:
    steve=input("in order to do math you must choose a operation. multiply, divide, subtract, or/and add. or quit: ")
    if answer=="mult":
        shalp.append(steve)
        print("choose another or exit")
    elif steve=="add":
        shalp.append(steve)
        print("choose another or exit")
    elif steve=="subtract":
        shalp.append(steve)
        print("choose another or exit")
    elif steve=="divide":
        shalp.append(steve)
        print("choose another or exit")
    elif steve=="quit":
        break
print(*shalp)
answer(shalp)