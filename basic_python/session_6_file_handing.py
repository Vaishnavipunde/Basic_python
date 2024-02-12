#>>>>>>>>>>>>>>>>>>>>>>>>>>>>28/07/2023>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#File Handing

#READ FUNCTION
with open("pi_digits.txt") as file_object: 
    contents=file_object.read() #read() function :reading contents from file
print(contents)

with open("pi_digits.txt") as file_object:  #Reative Path
    contents=file_object.read() 
print(contents.rstrip())        #Removing extra line in out put

file_path="C:/1-python/pi_digits.txt"   #Absolute path
with open(file_path) as file_object:
    contents=file_object.read()
print(contents)

#Reading line by line
file_path="C:/1-python/pi_digits.txt"   #Absolute path
with open(file_path) as file_object:
    for line in file_object:
        print(line)

file_path="C:/1-python/pi_digits.txt"   #Absolute path
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())         #removing space between line


#working with file        
with open("pi_digits.txt") as file_object:
    lines = file_object.readlines()
    pi_string=""
    for line in lines:
        pi_string=pi_string+line.rstrip()
        
        print(pi_string)
        print(len(pi_string))
    
#writing Opration
with open("programming.txt","w") as file_object:
    file_object.write("i love india")
    
#writting multiple line
with open("programming.txt","w") as file_object:
    file_object.write("i love programing")
    file_object.write("i love creating new game")
    
with open("programming.txt","w") as file_object:
    file_object.write("i love programing\n")
    file_object.write("i love creating new game\n")
    
#appending to a file - #file data can't be change
with open("programming.txt","a") as file_object:   #open with append 
    file_object.write("i also love finding menaing in large dtaset\n")
    file_object.write("i love creating apps that can run in a browser\n")



 
