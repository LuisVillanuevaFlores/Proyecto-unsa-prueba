from a import sum

def sum_arr(arr):
    res = 0
    for i in range (len(arr)-1):
        res = res + sum (i,i+1)
    return res