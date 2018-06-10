#count repeated words in a file
l=[]
count=0
f=open("naman.txt","+r")
l=f.read()
i=1
while i<=len(l):
    k="l.pop(i)"
    m="l.pop(i+1)"
    if k==m:
        count=count+1
print(count)
    
        

