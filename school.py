#create your school result
class school:
    c=0
    sname=input("Enter the primary subject of the student")
    def _init_(s,name,sname,marks,e,cm,h):
        s.name=name
        s.e=e
        s.cm=cm
        s.h=h
        school.c+=1
    def insert(s,s.name):
        e=int(input("Enter the marks of english of %s student"%(s.sname)))
        cm=int(input("Enter the marks of computer of %s student"%(s.sname)))
        h=int(input("Enter the marks of hindi of %s student"%(s.sname)))
    def disp(s,s.name):
        print("The marks of%s student in english is %d"%(s.sname,s.e))
        print("The marks of%s student in computer is %d"%(s.sname,s.cm))
        print("The marks of%s student in hindi is %d"%(s.sname,s.h))
    print("total students are=",c)
if sname=="science":
    name=input("enter the name of the student")
    s=school.insert(name)
    
    

        
        
