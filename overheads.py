# Import csv module
import csv
#Import os library
import os

def Overheads():
    """
    -function will determine which Overheads category have the highest overheads percentage
    """
   #Use with open() and use os.path.join to join directory names to locate the files and read it
    with open(os.path.join("Csv folder", "Overheads.csv"), "r") as file:
        # instantiate a reader object
        reader = list(csv.reader(file))  
        #Skip header
        reader = reader[1:]
        
    Numbers = [] #Create an empty list to store the overheads percentages
    Category = [] #Create an empty list to store the different overheads category
    #Use for loops to loop through the data 
    for row in reader:
        Numbers.append(float(row[1])) #Append overheads value and change the data to float()
        Category.append(row[0]) #Append the different overheads category

     #To find the cateogory of the corresponding maxmium overheads value 
    for i in range(0,len(Numbers)):    
        if Numbers[i] == max(Numbers):
            return f"[HIGHEST OVERHEADS] {Category[i]}: {max(Numbers)}%"






