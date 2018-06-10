class emp:
    c=0
    def _init_(s,name,role,salary):
        s.name=name
        s.role=role
        s.salary=salary
        emp.c+=1
    def display(s):
        print("%s,%s,%d"%(s.name,s.role,s.salary))
e1=emp("naman","ceo",99999999999)
e1.display()
