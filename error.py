#program to accept zero division error and value error while making a simple cvalculator
def cal():
    x=int(input("Enter the first digit"))
    y=int(input("Enter the second digit"))
    print("The sum is:",x+y)
    print("The difference is:",x-y)
    print("The product is:",x*y)
    print("The dision will give:",x/y)
    k=input("do you want to use the calculator")
    while k=="y":
        try:
          cal()
        except (ZeroDivisionError,ValueError) as e:
          print("Oops you have entered wrong data or dividing by zero")
          print("Retry!")
          k=input("do you want to use the calculator")
          cal()
    print("Thank You")
    
try:
    cal()
except (ZeroDivisionError,ValueError) as e:
    cal()



    
    
