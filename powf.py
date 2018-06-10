#calculatepower
def pow(b,p):
    r=1
    for i in range(1,p+1):
        r=b*r
    return r
b=int(input("Ente the base"))
p=int(input("Enter the power"))
pow(b,p)
print("The answer is=%d"%pow(b,p))
        
    
