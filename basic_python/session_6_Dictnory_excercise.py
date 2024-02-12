# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:37:25 2023

@author: shekhar
"""

#write a program form add key in dictneory
d ={1:2,33:44,34:65}
print(d)
d.update({44:65})
print("updated:",d)

d ={1:2,33:44,34:65}
print(d)
d[44]=65
print("updated:",d)

#concatenate the following dictnory to create new one
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={}
for i in (dic1,dic2):
    dic3.update(i)
print(dic3)

#check given key in dict or not
d={2:3,4:4,9:8,6:4}
num=int(input("enter key number:"))
if num in d:
    print("present")
else:
    print("absent")
    
#iterate dict in for loop
d={2:3,4:4,9:8,6:4}
for key,value in d.items():
    print(key,":",value)
    
for i in d:
    print(i,end=":")    #for key
    print(d[i])       #for value
    
    

