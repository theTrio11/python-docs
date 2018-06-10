#pass validation
s=str(input("Enter the password"))
le=len(s)
l=["@","&","$","-","*","^"]
for i in s:
    if not le>=8:
        print("Your password is not meet min length requirement")
        break
    elif not le<=20:
        print("Your password does not meet max length requirement")
        break
    elif not(s.isalpha()):
        
        if not(s.islower()):
            print("No lower characters")
        elif not(s.isupper()):
            print("No upper characters")
        
        print("Your password is not meeting alphabetic requirement")
        break
    elif not(s.isdigit()):
        print("Your password does not contain digit in it!")
        break
    elif not(i in l):
        print("Your password does not special characters!")
        break
    else:
        print("Welcome!")
        break

        
        
        
