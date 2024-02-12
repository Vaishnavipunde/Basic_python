


#all() for checking values are true or not if  we give 0 it show useless 
lst=[2,3,1,5,-3]
if all(lst):
    print("all values are true")
else:
    print("useless")
_________________________________________________-

lst=[2,3,1,5,-3,0]
if all(lst):
    print("all values are true")
else:
    print("useless")

#if any non zero value is present it print success .if all zero in list then print non success
lst=[2,0,0,0]
if any(lst):
    print("success")
else:
    print("not success")
_____________________________________________
lst=[0,0,0]
if any(lst):
    print("success")
else:
    print("not success")

#count() used for counting purpose,counter start from zero
from itertools import count
counter=count()
print(next(counter))
print(next(counter))

#strating counter from one
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))

#cycle() used for reapeated method
import itertools
s=["a","b","c"]
for n in itertools.cycle(s):
    print(n)

#repeat() used for repeat several times
from itertools import repeat
for m in repeat("hello vaishnavi",times=6):
  print(m)


#combinations
from itertools import combinations
players=["hello","gello","mello","apple","orange","flower"]
for m in combinations(players, 2):
    print(m)


#permutations
from itertools import permutations
pl=["john","johny","marry","carry","sorry"]
for m in permutations(pl,3):
    print(m)


#product
from itertools import product
a=["vaishnavi","vishwajit"]
b=["vaibhavi","rajdeep"]
for x in product(a,b):
    print(x)
    
#filter
age=[12,55,20]    
adult=filter(lambda age:age>18,age)
print([age for age in adult])
    
   #0r   
age=[12,55,20]    
adult=list(filter(lambda age:age>18,age))
adult
   
_______________________________________________________________________________________________________________
# create iterator from several iterators in sequence and display the type and element of new iterator 
#chain itertool  for list
from itertools import chain
def chain_fun(l1,l2,l3):
    return chain(l1,l2,l3)
result=chain_fun([1,2,3],["a","b","c"],[22,33,1,2,7])
print("type of new iterator")
print(type(result))
print("element of new iterator")
for i in result:
    print(i,end=" ")

#chain itertool for tuple
from itertools import chain
def chain_fun(l1,l2,l3):
    return chain(l1,l2,l3)
result=chain_fun((1,2,3),("a","b","c"),(22,33,1,2,7))
print("type of new iterator")
print(type(result))
print("element of new iterator")
for i in result:
    print(i)

# create running product of element in an iterator
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
result=running_product([1,2,3,4])
print("running product of list")
for i in result:
    print(i)


#in tuple
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
result=running_product((1,2,3,4))
print("running product of list")
for i in result:
    print(i)


#construct infinite iterator that return evenly spaced values starting with specified number and step
import itertools as it
start=10
step=1
print("starting number is",start,"step is",step)
mycounter=it.count(start,step)
print("said fun print never ending items")
for i in mycounter:
    print(i)
    
    
#generate infinite cycle of element from iterable
#in list form
import itertools as it
def fun(iter):
  return it.cycle(iter) 
result=fun(["a","b","c"])
print("infinite cycle")
for i in result:
    print(i)

#in string form
result=fun("hi")
for i in result:
    print(i)

#to make an iterator that drops element from iterable as soon as an element is a positive number
import itertools as it
def fun(nums):
    return it.dropwhile(lambda x:x<0,nums)
nums=[-1,-2,-3,1,0,8]
print("original list",nums)
result=fun(nums)
print("drop element from iterable when positive number arise ",list(result))
for i in result:
    print(i)


