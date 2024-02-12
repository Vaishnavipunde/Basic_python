#>>>>>>>>>>>>>>>>>>>>>>>>>>26/07/2023>>>>>>>>>>>>>>>>>>>>>

#Passing Distnory
def user(first_name,last_name):
    person={"First_name":first_name,"last_name":last_name}
    return person
users=user("Shekhar","Pawar")
print(users)

#..............................................................................

#Passing List
def user(username):
    for name in username:
        mag=(f"Hello {name}")
        print(mag)
name_list=["Ram","sham","shita"]
User_list=["Shekhar","sanket"]
user(name_list)

#..............................................................................

#passing an Arbitary number of Arguments
def make_pizza(*topping):
    print(topping)
make_pizza("peppeoni")
make_pizza("cheese","green_peppers","mushrooms")


print("Your pizza with folling toppings:")
def make_pizza(*toppings):
    
    for topping in toppings:
        print(f"{topping}")
make_pizza("peppeoni")
make_pizza("cheese","green_peppers","mushrooms")


def make_pizza(size,*toppings):
    print(f"\nYour pizza with size {size} following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(14,"peppeoni")
make_pizza(12,"cheese","green_peppers","mushrooms") 

#...............................................................................

import pizza
pizza.make_pizza(14,"peppeoni")
pizza.make_pizza(12,"cheese","green_peppers","mushrooms") 

import pizza as p #Give name to Pizza in short-p
p.make_pizza(14,"peppeoni")
p.make_pizza(12,"cheese","green_peppers","mushrooms") 

from pizza import make_pizza  #importing only function
make_pizza(14,"peppeoni")
make_pizza(12,"cheese","green_peppers","mushrooms")


from pizza import*  #importing all function
make_pizza(14,"peppeoni")
make_pizza(12,"cheese","green_peppers","mushrooms")


from pizza import make_pizza as np #give name to function
np(14,"peppeoni")
np(12,"cheese","green_peppers","mushrooms")


#..............................................................................
scope of varible
#x=x+2
x=6
print(x)

.......................................................................
#lambda Function or Ananymous function 

#function_name= Lambda function_arguments : buciness logic
add= lambda a,b,c:a+b+c
add(8,9,6)

mutl= lambda a,b,c :a*b*c
mutl(2,3,4)

val=lambda *agr:sum(agr) #for multiple argumnets use*
val(3,4,5,6,2)
val(7,4,3)

def person(name,**data): #------------------------key-value---------------->
    print(name)
    print(data)
person(name="navin",plcae="mumbai",age=23,mob_no=108) 

#navin
#{'plcae': 'mumbai', 'age': 23, 'mob_no': 108}

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(f"{i}={j}")
person(name="navin",plcae="mumbai",age=23,mob_no=108) 
......................................................................

val=lambda **data:sum(data.values())
val(a=3,b=4,c=3,d=6)

max=lambda a,b: x if (a >b)
max(2,3)
#expected 'else' after 'if' expression

max=lambda a,b: x if (a >b) else b
max(3,2)


max=lambda a,b: a if (a >b) else b
max(4,3)

............................................................................
#Python Collection type


