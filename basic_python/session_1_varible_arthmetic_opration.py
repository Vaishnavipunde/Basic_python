>>>>>>>>>>>>>>21/07/2023>>>>>>>>>>>>>

#input of user is defult String
age1=input("enter the age: ")
print(type(age1))
print(age1)

age2=input("enter the age: ")
print(type(age2))
print(age2)

age=age1+age2
print(age)

#typecasting-convert string to interger
age1=int(input("enter the age: "))
print(type(age1))
print(age1)

age2=int(input("enter the age: "))
print(type(age2))
print(age2)

age=age1+age2
print(age)

#IEEE 754 floting point number
exchange_rate=1.83
print(exchange_rate)
print(type(exchange_rate))

###################################################

int_value= 100
str_value='1.2'
float_value= float(int_value) #typecasting
print("int value converted into float:",float_value)
print(type(float_value))
float_value= float(str_value) #typecasting
print("int value converted into float:",float_value)
print(type(float_value))

#complex number

c1= 2
c2= 2j
print("c1:",c1,"c2:",c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#boolen number

all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

#we also convert string into boolean
status = bool(input("enter the value:"))
print(status)
print(type(status))

#Arthmetic opration
home =10
away =15

print(home+away)
print(type(home+away))

print(49*3)
print(type(49*3))

goals_for=10
goal_agins=7
print(goals_for-goal_agins)
#if we divide integer two number then result will be in  a flaot
print(100/7)
print(type(100/7))

#if we divide integer two number then result will be in  a int use //
print(100//7)
print(type(100//7))

#finding of reminder
print("modules division 100%3",100%3)
print(type(100%3))

#Power
a=3
b=5
print(3 ** 5)

#Asssigment Operators
x =1
x+=1   #has the same behavoir as x= x+1
 
#none value
winner = None 
print(winner is None)

winner = None 
print(winner is not None)

print(type(winner))

winner = True 
print(type(winner))

#indindation
num =10
if num >2:
    print("number is greater than 2")
    if num>5:
        print("number is greater than 5")
        if num>15:
            print("number is greater than 15")

num1=int(input("enter the number: "))
if num1 < 0:
    print("number is -ve")
else:   
    print("number is Positive")

