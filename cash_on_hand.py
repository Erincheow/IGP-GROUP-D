# Import csv module
import csv
#Import os library
import os

def COH():
    """
    - function will determine whether the cash on hand across 5 Coh had surplus or deficit
    """
    #Use with open() and use os.path.join to join directory names to locate the files and read it
    with open(os.path.join("Csv folder", "Cash on Hand.csv"), "r") as file:
        # instantiate a reader object
        reader = list(csv.reader(file))  
        #Skip header
        reader = reader[1:]
    
    Coh = [] #Create an empty list to store the days and cash on hand values
    for i, row in enumerate(reader):
        Coh.append([]) 
        for element in row:
            Coh[i].append(int(element))
    #Create an variable with an empty string and name it "output"
    output = ""
    #To find the corresponding days with cash on hand deficit
    for i in range(1,len(Coh)):  
        if Coh[i-1][1] > Coh[i][1]:
            output += f"[CASH DEFICIT] DAY: {Coh[i][0]}, AMOUNT: USD{Coh[i-1][1] - Coh[i][1]}\n"
    #Check whether there is deficit for the corresponding days , if no cash deficit, will return cash surplus
    if output == "":
        return f"[CASH SURPLUS]CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    return output[:-1]



   