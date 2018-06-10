#strings
print("Enter the Two strings")
s1=str(input())
s2=str(input())
l1=len(s1)
l2=len(s2)
if l1>l2:
    print("String 1 is longer than string 2")
    s1=s1.upper()
elif l2>l1:
    print("String 2 is longer than string1")
else:
    print("The twoi Strings are of Same length")

    
