>>>>>>>>>>>>>>>>>>24/07/2023>>>>>>>>>>>>>>>>>

#elif condition
savings = float(input("enter the saving:"))
if savings == 0:
    print("there is no saving")
elif savings <500:
    print("Well Done")
elif savings <1000:
    print("that a tidy sum")
elif savings <10000:
    print("welcom sir!!!!")    
else:
    print("thank you!")

#while Loop
count=1
print("Starting")
while(count<=10):
    print(count)
    count=count+1  

#for loop
print("print out value in range")
for i in range(2,20):       #last number is not consider ex.20
    print(i)
print("Done")

#break 
print("only print code if all iteration completed")
num = int(input("enter the number:"))
for i in range(2,20):
    if i ==num:
        break              #break the statment
    print(i)
print("done")     

#anonymous varible
for _ in range(0,10):
    print(".",end="")
    print("")  #use to new line vertical :
   
for _ in range(0,10):
     print(".",end="") #use to horizontal .....
     
for i in range(0,6):
    if i ==num:
        break
    print(i,"",end="")
    print("done")   
    
#find odd number in give range
start,end=4,20
for i in range(start,end+1):
    
    #check  condition
    if i %2 !=0: #---------------------------------------------LOGIC >
        print(i,end="")


for i in range(1,21,2):

    print(i,end=" ")




#find even number in give range
start,end=4,20
for i in range(start,end+1):
    
    #check  condition
    if i %2 ==0: #---------------------------------------------LOGIC>
        print(i,end=" ")    
        

for i in range(2,21,2):

    print(i,end=" ")
    print(" ")

#Take input form user
start=int(input("enter the start number:"))
end=int(input("enter the end number:"))
for i in range(start,end+1):
    #condition
    if i%2 !=0:
        print(i,end=" ")
        
start=int(input("enter the stating number:"))
end=int(input("enter the ending number:"))
for i in range(start,end+1):
    #condition
    if i%2==0:
        print(i,end=" ")        
        
#Palindrom Number.............................................................       
num=int(input("enter the number:"))
temp=num
rev=0
while(num>0):
        digit=num%10
        rev=rev*10+digit
        num=num//10
if (temp==rev):
    print("Is Palindrom!!!!!!!!!!!!")
    print(rev)
else:
    print("It is not Palindrom!!!!!!!")
#.............................................................................
inputs=input("Enter the string:")
temp=inputs
rev=inputs[::-1]    
if (rev==temp):
    print("Is a palindrom string")
else:
    print("Not Palindrom")            
   

#prim Number.................................................................
num=int(input("Enter the number:"))
if num>1:
    
    for i in range(2,(num//2)+1):
        if num%i ==0:
            print("it not a prim")
            break
    else:
            print("it a prim number")
else:
    print("is not a prim number")  

................................................................................

num=int(input("Enter the number:"))
for i in range(2,num):
    if num%i==0:
        print("it a not prim number")
        break
    else:
        print("it a prim number")
        break


#leap Year..................................................................
Year=int(input("enter the year:"))
if(Year>0):
    if((Year % 400 == 0) or  (Year % 100 != 0) and  (Year % 4 == 0)):
        print("leap year")
    else:
        print("Not leap year")
        
#mario pyramid..............................................................
for i in range(7):
      for j in range(7):   
          print("*",end=" ")   
      print("")
      
      * * * * * * * 
      * * * * * * * 
      * * * * * * * 
      * * * * * * * 
      * * * * * * * 
      * * * * * * * 
      * * * * * * *
    
for i in range(7):
      for j in range(i+1):
          print("*",end=" ")
      print("")
      
      
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * * * 
      * * * * * * *
    

for i in range(7):
      for j in range(7-i):
          print("*",end=" ")
      print("")
      
      
      * * * * * * * 
      * * * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      *
     
#......................................................................
    
x,y,z=2,3,4
print(x)
print(y)    
print(z)     

#Global veribal.........................................................
x="Boss"
def my_function():
    print("I am",x)
my_function()

#Loacl veribal...........................................................
x="Boss"
def my_function():
    x="BigBoss"
    print("I am",x)
my_function()    

#Dictnory................................................................
x={"name":"shekhar","mobile":8308401920}
print(type(x))
print(x)58

........................................................................
str1="Hello"
str2=2
str3=str1+str2  #its show error

#Multiplue line Verible.................................................
x="""its is a python
python is very powerfull"""
print(x)
"""its is a python
python is very powerfull"""

#string opration..................................................
print(x[5:15])    """"s is a python"""         

print(x[0:15])    """its is a python"""

print(x[0:1])     """i"""

print(x[5:])
"""s a python
python is very powerfull"""

print(x[-9:0])
"""powerfull"""

print(x[-9:-1])
"""powerful"""

print(x.upper())
""" ITS IS A PYTHON
PYTHON IS VERY POWERFULL """

print(x.lower())
"""its is a python
python is very powerfull"""

print(x.split())
"""['its', 'is', 'a', 'python', 'python', 'is', 'very', 'powerfull']"""

print(x.strip( ))

print(x.replace("python", "java"))
"""its is a java
java is very powerfull"""

print(x.find("very")26
"""26"""

x="Hello Word"
print(x[::-1])
"""droW olleH"""

x="Hello Word"
print(x[::-2])
"""do le"""

print(x.find("Word"))
"""6"""

x="hello"
y="word"
print(x+" "+y)
"""hello word"""

x="hello"
y="word"
print(x+""+y)
"""helloword"""

#F string in python....................................................
x=24
print(f"My name Anthany and my age is {x}")

name="shekhar"
clas="Tycomp"
number=8308401920

print(f"My Name is {name}.I am study in{clas}.My mobile number is {number}")

"""My Name is shekhar.I am study inTycomp.My mobile number is8308401920"""
........................................................................
name="shekhar"
clas="Tycomp"
number=8308401920
my_order="My Name is {}.I am study in{}.My mobile number is {}"
print(my_order.format(name,clas,number))
.........................................................................
name="shekhar"
clas="Tycomp"
number=8308401920
my_self="My Name is {2}.I am study in{1}.My mobile number is {0}"
print(my_self.format(name,clas,number))
"""My Name is 8308401920.I am study inTycomp.My mobile number is shekhar"""
.............................................................................

print("This is fun fair and its got big \"round rigo\"")
"""This is fun fair and its got big "round rigo""""

.........................................................................
a=10
b=20 
print(a==b)
"""False"""
....................................................................
3*3+3/3-3
Out[140]: 7.0
