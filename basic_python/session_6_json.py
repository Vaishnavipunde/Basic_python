# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:55:13 2023

@author: shekhar
"""

import json
number=[2,3,5,2,5] 
file_name="number.json"
with open(file_name,"w") as f:
    json.dump(number,f)



import json
username=input("Enter name:")
file_name="username.json"
with open(file_name,"w") as f:
    json.dump(username,f)

import json
username=input("Enter name:")
file_name="username.json"
with open(file_name,"w") as f:
    json.dump(username,f)             #dump ---- enter in file
print(f"hello {username}")


import json
file_name="username.json"
with open(file_name) as f:
    username=json.load(f)           #load----------- acces data from file
print(f"welcome back {username}")


filename="username.json"
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("enter your name:")
    with open(filename,"w") as f:
        json.dump(username,f)
        print(f"we remender you when you come back,{username}")
else:
    print(f"welcome back,{username}")