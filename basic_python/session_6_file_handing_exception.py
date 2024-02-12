# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:06:27 2023

@author: shekhar
"""
#Exception Handling

a=3
b=4
c=a+b
print(5/0)
try:
    print(5/0)
except ZeroDivisionError:
    print("Not Div by zero")

#file not found error
try:
    with open("sp.txt",encoding="utf-8") as file_object: 
        contents=file_object.read() #read() function :reading contents from file
    print(contents)
except FileNotFoundError:
    print("file not found")
