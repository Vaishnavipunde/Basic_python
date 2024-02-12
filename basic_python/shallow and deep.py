# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 08:07:46 2023

@author: sai
"""

   
#shallow copy and deep copies!!!!!!!!!!!!!!!!!!!!!!IMP!!!!!!!!!!!!!!
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)
    

#shallow copy not chnage in list_a only list_b get change
import copy
list_a=[1,2,3,4,22]
list_b=copy.copy(list_a)
list_b[0]=-10
print(list_a)
print(list_b)

#shallow copy of level 2 list
import copy
list_a=[[1,2,3,4],[5,6,7,8]]
list_b=copy.copy(list_a)
list_b[0][0]=-10
print(list_a)
print(list_b)

#deep copy
import copy
list_a=[1,2,3,4,22]
list_b=copy.deepcopy(list_a)
list_b[0]=-10
print(list_a)
print(list_b)

import copy
list_a=[[1,2,3,4],[5,6,7,8]]
list_b=copy.deepcopy(list_a)
list_b[0][0]=-10
print(list_a)
print(list_b)
