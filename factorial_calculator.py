#BC 1 factorial calculator

import math
def times(number):
    return number*2
factorial=int(input("give me a number: "))
print(factorial)
real_factorial=factorial+1
factorial_list=list(range(1,real_factorial))
print(*factorial_list)
set_factorial_list=set(factorial_list)
#int_factorial_list=int(*set_factorial_list)
factorial_multiplication=factorial
factorial_true_mult=factorial_multiplication-1
while factorial_true_mult > 1:
    factorial_true_mult-=1
    def multiplication(number):
        return number*factorial_true_mult

#steve=map(int_factorial_list*int_factorial_list)
print(factorial_true_mult)
all_factorials=map(multiplication,factorial_list)
print(all_factorials)

#print(math.factorial(5))