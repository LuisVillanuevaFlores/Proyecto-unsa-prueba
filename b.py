from a import sum
from a import multi

def sum_arr(arr):
    res = 0
    for i in range (len(arr)-1):
        res = res + sum (i,i+1)
    return res

def potencia (num,exp):
    if exp == 0:
        return 1
    return multi(num,potencia(num,exp-1))

a = potencia(3,7)
print(a)