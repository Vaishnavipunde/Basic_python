

#zip fun!!!!imp!!!!!!!!
names=["mama","dada"]
info=[1,2]
for n,i in zip(names,info):
    print(n,i)

#ignor extra element in zip fun
names=["mama","dada","kaka"]
info=[1,2]
for n,i in zip(names,info):
    print(n,i)

#zip longest for printing extra element
from itertools import zip_longest
names=["mama","dada","kaka"]
info=[1,2]
for n,i in zip_longest(names,info):
    print(n,i)

#instead none use fill value
from itertools import zip_longest
names=["mama","dada","kaka","baba"]
info=[1,2]
for n,i in zip_longest(names,info,fillvalue=0):
    print(n,i)
