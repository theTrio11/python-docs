#file1
i=input("Enter the file name you want to create")
j="y"
while j=="y":
    z=input("Enter your lines")
    f=open(i,"+a")
    f.write(z)
    f.close()
    j=input("Enter y to continue")
c=int(input("Enter your choice:1 for whole read\n2 for read 5 letters\n3 for read all lines"))
if c==1:
    f=open(i,"r")
    k=f.read()
    print(k)
    f.close
elif c==2:
    f=open(i,"r")
    l=f.read(5)
    print(l)
    f.close()
elif c==3:
    f=open(i,"r")
    m=f.readlines()
    print(m)
    f.close
else:
    print("Invalid choice")
with open 

