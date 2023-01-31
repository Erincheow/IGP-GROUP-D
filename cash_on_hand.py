from pathlib import Path
# Import csv module
import csv
file_path = Path.home()/"IGP"/"Python folder"/"Csv folder"/"Cash on Hand.csv"
# read the csv file to append days and cash on hand values from the csv.
with file_path.open(mode = "r",encoding = "UTF-8-sig", newline="") as csvfile:
        reader = list(csv.reader(csvfile,delimiter=","))
        reader = reader[1:]
# instantiate a reader object
def COH():
    Days= []
    for i, row in enumerate(reader):
        Days.append([])
        for element in row:
            Days[i].append(int(element))

    output = ""

    for i in range(1,len(Days)):  
        if Days[i-1][1] > Days[i][1]:
            output += f"[CASH DEFICIT] DAY: {Days[i][0]}, AMOUNT: USD{Days[i-1][1] - Days[i][1]}\n"
    if output == "":
        return f"[CASH SURPLUS]CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    return output[:-1]
    

   