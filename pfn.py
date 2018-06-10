#perfectNumber
def pefn(n=int):
    temp=0
    res=0
    for i in range(1,n):
        temp=n%i
        if temp==0:
            res=res+i
        else: 
            pass
    return res
n=int(input("Enter the number you want to check"))
comp=0
pefn(n)
res=comp
if comp==0:
    print("The number is not perfect")
elif comp==n:
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")

    


    
            
        
        
