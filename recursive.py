def SumaRecursiva(n):
    if(n==1):
        
        return n
    else:
        
        return (n+ SumaRecursiva(n-1))

   
print(SumaRecursiva(5))


