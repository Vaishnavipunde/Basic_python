#Set
#it not allowed duplicate elements
.............................................................................
basket={"apple","banana","orange","cheery","apple"}
print(basket)
#output:{'cheery', 'orange', 'banana', 'apple'} removing Duplicate

#Add element in set
basket.add("apricot")
print(basket)
 
#find Max and Min
num={143,543,753,654,876}
max(num)  #876
min(num) #143

#Removing item from set
basket={"apple","banana","orange","cheery","apple"}
basket.remove("apple")   #All apple are remove
basket.discard("cheery") 
 print(basket)
 
 .............................................................................
 
#Set Oprations
s1={"apple","orange","banana"}
s2={"lime","mango","banana","sp"}
#print("Union:",s1 | s2)
#print("interction:",s1 & s2)
print("Diffrennce:",s1 - s2)
...............................................................................
#Dictnary{"key":"value"}

capitals={"Maharashrta":"Mumbai",
          "Gujrat":"Ahemdbad",
          "UP":"Lakhnow",
          "Karnataka":"Banglore"
          }
print(capitals)

#Acces value
print(capitals["Maharashrta"])

#Adding New key-value
capitals["West_Bangal"]="Kolkata"
print(capitals)

#chaning value of key
capitals["Gujrat"]="Gadhinager"
print(capitals)

#Removing item
capitals.pop("Gujrat")  #using POP()
print(capitals)

del capitals["UP"]     #using DEl()
print(capitals)      

#itertaing item
capitals={"Maharashrta":"Mumbai",
          "Gujrat":"Ahemdbad",
          "UP":"Lakhnow",
          "Karnataka":"Banglore"
          }
for state in capitals:     
    print(state,end=" ")          #Acces Only key
    print(capitals[state])            #Accesing Value

for state in capitals:     
    print(state,end=",")          #Seprate by ','
    print(capitals[state])


#key,value and item
print(capitals.keys())         
print(capitals.values())
print(capitals.items())    

#Checking key is present or not
print("UP" in capitals)      #TRue
print("UP" not in capitals)    #false

#Dictnories value can be in tuple
seasons={"summer":("feb","march","aperl","may"),
         "Rainy":("june","july","Aug","Sept"),
         "Winter":("Oct","nov","Dec","jan")
         }
print(seasons)
print(seasons["summer"])
print(seasons["summer"][2])    #Accesssing 2 elemant from value

#Dictnorary Not allowed duplicat 
dict2={"Brand":"Maruti","Model":"Breeza","Year":2020,"Year":2021}
print(dict2)
#{'Brand': 'Maruti', 'Model': 'Breeza', 'Year': 2021}

#loop acces only key
for i in dict2:
    print(i,end=" ,")  #Acces key
    print(dict2[i])      #Use onrignal name of dict to access value\7
    
 
    