# Import csv module
import csv
#Import os library
import os

def Profit():
    """
    -function will determine whether the net profit across 5 days had surplus or deficit
    """
    #Use with open() and use os.path.join to join directory names to locate the files and read it
    with open(os.path.join("Csv folder", "Profit and Loss.csv"), "r") as file:
        # instantiate a reader object
        reader = list(csv.reader(file))  
        #Skip header
        reader = reader[1:]
    NetProfit= [] #Create an enpty list to store the NetProfit values
    #Use the enumerate() function to generate both the index and value
    for i, row in enumerate(reader):
        NetProfit.append([]) 
        for element in row:
            NetProfit[i].append(int(element)) #Append the NetProfit values and change the data to integers

    #Create an variable with an empty string and name it "output"
    output = "" 
    #To find the corresponding days with profit surplus or deficit
    for i in range(1,len(NetProfit)):
        #Compare the netprofit of current day to previous day
        if NetProfit[i-1][4] > NetProfit[i][4]:
            output += f"[PROFIT DEFICIT] DAY: {NetProfit[i][0]}, AMOUNT: USD{NetProfit[i-1][4] - NetProfit[i][4]}\n"
    #Check whether there is deficit for the corresponding days , if no cash deficit, will return cash surplus
    if output == "":
        return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY"
    return output[:-1] 

