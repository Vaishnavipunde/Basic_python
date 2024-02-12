>>>>>>>>>>>>>>>>>>25/07/2023>>>>>>>>>>>>>>>>>
#functions

def prime_num(num):
    if (num>1):
        for i in range(2,num):
            if (num%i==0):
                print("its not a prime number!!")
                break
            else:
                print("its is a prime number!!!")
                break
    else:
        print("its not a prime number!!")
prime_num(1)




#write a program to check password
def checkpassword(password):
    has_upper=False
    has_lover=False
    has_number=False
    for ch in password:
        if ch >="A" and ch <="Z":
            has_upper=True
        elif ch >='a' and ch<='z':
            has_lover=True
        elif ch >="0" and ch <="9":
            has_number=True
    if len(password)>=8 and has_lover and has_upper and has_number:
        return True 
    else:
        return False

pa=input("Enter your password: ")
if checkpassword(pa):
    print("Strong Password")
else:
    print("Password is not strong")

 
................................................................
