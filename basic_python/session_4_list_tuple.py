

#Python Collection type
..............................................................................
#tuple
#creating Tuple
tup1=(1,2,3,4,5)
print(tup1[0])
print(tup1[1])
print(tup1[3])
print(f"{tup1[4]}")


#tuple can use any type of data 
tup2=("sp",302,True,30.2)
print(tup2)

#Iterating over tuple
tup3=("apple","banana","plim","apple")
for x in tup3:
    print(x)

#-find length
len(tup3) #-find length----------------->4

#count the number of occerd
tup3.count("apple") #count the number of occerd---------------->2

#find out the index of value
tup3.index("apple")#find out the index of value----------------->0
tup3.index("plim")#find out the index of value----------------->2


#holyoython.com
#checking element exist
if "apple" in tup3:
    print("Present")
else:
    print("Apsent")

#nested tuple
Tuple1=(1,2,3,4,5)
Tuple2=("Sita","Ram")
Tuple3=(12,Tuple1,Tuple2,"Hello")
print(Tuple3)


...............................................................................
#list
#creating List
list1=["sita",123,"ram",40.3]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

#Nested list
list1=["hello",123,"Word"]
list2=["Sp",456]
list3=[1234,list1,list2,"Success"]
print(list3)

#Accesssing the element
list1[-1]               #Access last elament  [-4,-3,-2,-1]
list1[0]                #Access first elament [0,1,2,3,4]


list1=["john","shekhar","paul","ringo","George"]
print(list1[:])  #printing all lsit
print(list1[:3]) #printing first element
print(list1[1:]) #printing skip first element
print(list1[1:4]) #printing 1-4 element

#Add in list(in end)
list1.append("Sham")
print(list1)
#output-['john', 'shekhar', 'paul', 'ringo', 'George', 'Sham']

#Add two list
list1.extend(["Gita","Sanket"])
print(list1)
#output-['john', 'shekhar', 'paul', 'ringo', 'George', 'Sham', 'Gita', 'Sanket']

#insert into spcific location
list1=["john","shekhar","paul","ringo","George"]
list1.insert(3,"Pawar") #using insert() Function
print(list1)
#output-['john', 'shekhar', 'paul', 'Pawar', 'Shekhar', 'ringo', 'George', 'Sham', 'Sham', 'Gita', 'Sanket']


#list Concatanation
lit1=[1,2,3]
lit2=[7,8,9]
lit3=lit1+lit2
print(lit3)
#output-[1, 2, 3, 7, 8, 9]

#removing
list1=["mark","Sub","jason","howard"]
list1.remove("Sub")   #Using remove() function with name
print(list1)

list1.pop(1)   #Using POP() function with index
print(list1)




