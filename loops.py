#loops
print("Enter the number of numbers")
x=int(input())
l1=[]
y=0
print("Enter the numbers")
while y<x:
    i=int(input())
    j=0
    l1.append(i)
    j=j+1
    y=y+1
print("list=",l1)
print("The new order is ")
l1.reverse()
print(l1)
    
