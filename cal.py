#first program
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
print("for addition press 0,multiplication 1, division 2,subtration -")
z=str(input("Enter the operator"))
def switchd(arg):
    switcher={
        0: x+y,
        1: x*y,
        2: x/y,
        3: x-y,
        }
    return switcher.get(arg,"invalid operator")
print(switchd)

    
