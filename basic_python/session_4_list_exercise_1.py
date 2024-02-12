list1=[223,432,45,332,532,453,789]
#find maximaum
max(list1) 

#find minimum
min(list1) 

#Reverse the List
list1=["shekhar","sanket","shubham","ram","sham"]
new=list1[::-1]
print(new)

#Take 10 number in list and write program for serching
list1=[3,5,7,6,2,1,8,4,9,0]
ele=int(input("Enter number:"))
if ele in list1:
    print("number is Present")
else:
    print("Number is Absent")
    
#take Dublicate number and write code to find duplicat number
list1=[3,2,5,7,4,6,3,6,2,1,8,4,9,0]
d_list=[]

for i in list1:
    ct=list1.count(i)
    if ct !=1:
        if i not in d_list: 
            d_list.append(i)
print(d_list)

#Find vowels in list
list1=["A", "E", "I", "O", "U","S","X","H","A","O","V","A"]
count=0
for i in list1:
    if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        count=count+1
length=len(list1)
print(f"List length is {length} and Total Vowels :{count}")

#write python for adding all item of list
list1=[2,4,5,3,5,2]
sum=0
for i in list1:
    sum=sum+i
print(sum)


def sum_all(sum1):     #Using Function
    sum=0
    for i in sum1:
        sum=sum+i
    return sum

sum_all([2,3,5,3,2,6])
        
#write python for multi all list item
list1=[2,4,5,3,5,2]
mul=1
for i in list1:
    mul=mul*i
print(mul)

def mul_all(mul1):     #Using Function
    mul=1
    for i in mul1:
        mul=mul*i
    return mul
mul_all([2,3,5,3,2,6])

#write program for find big number in list
list1=[222,53,74,643,753,245]
print("largest number is :",max(list1))


def find_max(max1):   #using Function
    return max(max1)
find_max([22,32,53,64])

#write program for find small number in list
list1=[222,53,74,643,753,245]
print("largest number is :",min(list1))


def find_max(max1):   #using Function
    return min(max1)
find_max([22,32,53,64])

#write program to count the number of string which satisfies the condition that
#the string  leghth is 2 or more and the first and last char are same
list1=["abba","shas","1221","pawar"]
count=0
for i  in list1:
    if len(i)>2:
        if i[0]==i[-1]:
            count=count+1
print(count)

#write a python to get a list ,sorted in increasing order by the last element
# in each tuple from a given  list of non-empty tuple

def last(n):
    return n[-1]
    
def sort_list(tuples):
    result=sorted(tuples ,key=last)   #key-A Function to execute to decide the order.
    return result 
print(sort_list([(2,5),(1,2),(4,4),(2,3),(2,1)]))





sort_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
result=sorted(sort_list,key=lambda x:x[-1]) #key getting last iteam
print(result)
#[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#revmove duplicat item in list
list1=[26,86,35,26,10,35,12,20,10,26]     
for i in list1:
    total=list1.count(i)
    if total !=1:
        list1.remove(i)
print(list1)         #[86, 35, 12, 20, 10, 26]


list1=[26,86,35,26,10,35,12,20,10,26]
new_list=[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)       #[26, 86, 35, 10, 12, 20]



list1=[26,86,35,26,10,35,12,20,10,26]
set_list1=set(list1)
list2=list(set_list1)
print(list2)          #[35, 10, 12, 20, 86, 26]

#write program for copy list
original=[11,22,33,44,55]
copy=original           
print(copy)            #[11, 22, 33, 44, 55]


#write a program to find a string of word are larger than given number
word_len=[]
def long_word(n,str):
    
    txt=str.split(" ")
    for x in txt:
        if len(x) >=n:
            word_len.append(x)
long_word(3,"the quick brown fox jump")
print(word_len)


new=[]
long_list=("the quick brown fox jump")
txt=long_list.split(" ")
for x in txt:
    if len(x) >=3:
        new.append(x)
print(new)    

#write program for write commman item in two list

result=False
def common_data(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                result=True
                return result
print(common_data([11,22,33,44,55,66,77],[11,23,24,54,65,76,87]))

#write program for diffewnce between two list
list1=[1,3,5,6,7,9]
lsit2=[1,2,4,6,7,8]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
diff_total=diff1+diff2
print(diff_total)
            
#convert a list of characters into string
s=['a','p','p','s']
str1="".join(s)
print(str1)

#find the index of item
num=[10,20,30,40]
print(num.index(30))

#append one list into other list
num1=[1,0,2,9,3]
num2=[3,5,6,7,7]
num3=num1+num2
print(num3)
   