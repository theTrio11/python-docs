#smart cal
print("Enter choice : a=add,s=subtract,m=multiply,p=power,d=division")
c=str(input())
if c=="a":
    print("Enter the number")
    x=int(input())
    y=int(input())
    print("The sum is=",x+y)
elif c=="s":
    print("Enter the number")
    x=int(input())
    y=int(input())
    print("the subtracted ans is=",x-y)
elif c=="m":
    print("Enter the number")
    x=int(input())
    y=int(input())
    print("The product is=",x*y)
elif c=="p":
    print("Enter the number you want as a base")
    x=int(input())
    print("Enter the number you want as a power")
    y=int(input())
    print("The ans is=",x**y)
elif c=="d":
    print("Enter the number you want to divide")
    x=int(input())
    print("Enter the number you want as divsor")
    y=int(input())
    print("the ans is=",x/y)
else:
    print("Wrong choice")
    
,
