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
        