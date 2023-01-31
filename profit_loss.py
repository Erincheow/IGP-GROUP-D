from pathlib import Path
# Import csv module
import csv
file_path = Path.home()/"IGP"/"Python folder"/"Csv folder"/"Profit and Loss.csv"
# read the csv file to append NetProfit and cash on hand values from the csv.
with file_path.open(mode = "r",encoding = "UTF-8-sig", newline="") as csvfile:

# instantiate a reader object
    reader = list(csv.reader(csvfile,delimiter=",")) 
    reader = reader[1:]

def Profit():
    NetProfit= []
    for i, row in enumerate(reader):
        NetProfit.append([])
        for element in row:
            NetProfit[i].append(int(element))

    output = ""

    for i in range(1,len(NetProfit)):
        if NetProfit[i-1][4] > NetProfit[i][4]:
            output += f"[PROFIT DEFICIT] DAY: {NetProfit[i][0]}, AMOUNT: USD{NetProfit[i-1][4] - NetProfit[i][4]}\n"
    if output == "":
        return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY"
    return output[:-1]

