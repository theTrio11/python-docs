#declare alist and copy it into tabular form
l=[]
i=int(input("Enter the no of elements you want to enter in the list"))
print("Enter the elements")
k=1
while k<=i:
    x=input()
    l.append(x)
    k=k+1
f=open("naman.txt","+a")
s=str(l)
f.write(s)
f.close()

