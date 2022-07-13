def FactorialRecursive(n):
    if(n==1):
        return n
    else:
       
        return (n*FactorialRecursive(n-1))

num=5
print("Factorial: ",num,"-->",FactorialRecursive(num))
