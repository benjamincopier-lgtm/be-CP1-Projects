#BC 1 factorial calculator

import math
while True:
    try:
        factorial=int(input("give me a number: "))
    except:
     print("not a number")
    else:
        break

print(factorial)
real_factorial=factorial+1
factorial_list=list(range(1,real_factorial))
print("the list of factorials is", *factorial_list)
factorial_multiplication=factorial
factorial_true_mult=factorial_multiplication
while factorial_true_mult > 1:
    factorial_true_mult-=1
    def multiplication(number):
        return number*factorial_true_mult#not a clue why this works, yay :O
    factorial_list.insert(factorial_true_mult,"*")
    all_factorials=list(map(multiplication,factorial_list))



print("the factorial of", factorial , "is", math.factorial(factorial), "because", *all_factorials, "=", math.factorial(factorial) )