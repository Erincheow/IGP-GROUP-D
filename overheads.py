from pathlib import Path
# Import csv module
import csv
file_path = Path.home()/"IGP"/"Python folder"/"Csv folder"/"Overheads.csv"
# read the csv file to append NetProfit and cash on hand values from the csv.
with file_path.open(mode = "r",encoding = "UTF-8-sig", newline="") as csvfile:

# instantiate a reader object
    reader = list(csv.reader(csvfile,delimiter=",")) 
    reader = reader[1:]

def Overheads():
    Numbers = []
    Category = []
    for row in reader:
        Numbers.append(float(row[1]))
        Category.append(row[0])
    for i in range(0,len(Numbers)):    
        if Numbers[i] == max(Numbers):
            return f"[HIGHEST OVERHEADS] {Category[i]}: {max(Numbers)}%"
        




