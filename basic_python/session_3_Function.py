#>>>>>>>>>>>>>>>>>>25/07/2023>>>>>>>>>>>>>>>>>
#functions

def greet_user(): #function without argument
    print("Hello !!!!!!!!!!")
greet_user()    #function calling

..........................................................................    
    
def prime_num(num):  #function with argument
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
prime_num(11)   #Function calling

.........................................................................

def greet_user(user):
    print(f"HELLO {user}")  #f 

greet_user("BOSS")

..........................................................................
#positional Argument----------------use f
def animal(types,name):
    print(f"I have a {types}")
    print(f"I have a {types} and name is {name}")
animal("dog","moti")

def animal(types,name="sonya"): #defult value
    print(f"I have a {types}")
    print(f"I have a {types} and name is {name}")
animal("dog")

.........................................................................
.........................................................................
 

users=["admin","employee","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("Hello BOSS")
    elif user=="employee":
        print(f"Hello {user}") #------------------->
    elif user=="manager":
        print("Hello manager")
    elif user=="worker":
        print("Hello worker")
    else:
        print("Hello staff")
        
.........................................................................

adiectives=["orange","red","black","blue","fat","green","white"]
nonus=["apple","ball","goat","duck","cat","panda"]

import random
import string

adiective=random.choice(adiectives)
nonu=random.choice(nonus)
number=random.randrange(0,100)
special_char=random.choice(string.punctuation)

pas=adiective+nonu+special_char+str(number)
print(f"your password is :{pas}")

............................................................................


adiectives=["orange","red","black","blue","fat","green","white"]
nonus=["apple","ball","goat","duck","cat","panda"]

import random
import string
while True:
    adiective=random.choice(adiectives)
    nonu=random.choice(nonus)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    
    pas=adiective+nonu+special_char+str(number)
    print(f"your password is :{pas}\n")
    
    ch=input("create more password Y or N:\n")
    if ch=="y" or ch=="Y":
        continue
    else:
        break
........................................................................


print("Welcome To Piozza Hut!!!!!!!")
size=input("Plz Enter the size of pizza S,M,L:")

bill=0
if size=="S" or size=="M" or size=="L":
    add_pepperoni=input("You want to add Pepperoni Y or N:")
    add_cheese=input("ADD CHEESE Y or N:")
    if size=="S":
        print("Price of small size pizza is $15")
        bill=15
    elif size=="M":
        print("Price of M pizza is $20")
        bill=20
    elif size=="L":
        print("price of large pizza is $25")
        bill=25
    if add_pepperoni=="Y" or add_pepperoni=="y":
        if size=="S":
            bill=bill+2 
        else:
            bill=bill+3
    if add_cheese=="Y" or add_cheese=="y":
        bill=bill+1
        print(f"Your Pizza Bill is ${bill}")
else:
    print("Enter correct Size")
    