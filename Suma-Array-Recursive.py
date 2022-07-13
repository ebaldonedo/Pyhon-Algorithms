from array import array


def Suma_Array_Recursive(arr):
    if(len(arr)==0):
        return 0
    else:
        return arr[0]+ Suma_Array_Recursive(arr[1:])

sumArray=[1,2,3,4,5] 

print(Suma_Array_Recursive(sumArray) )