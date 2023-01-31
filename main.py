from pathlib import Path
from cash_on_hand import COH
from overheads import Overheads
from profit_loss import Profit
# instantiate an file path object to home directory
home = Path.home()
#create a new file_path and extend it to 'IGP' and create a new file 'final_report.txt'
file_path = home/"IGP"/"Final report.txt" 
# print(file_path.exists()) # Check the file exists before proceeding to open file
 
Overheads = Overheads() 
COH = COH()
Profit= Profit()
#Use with to open the file and include the parameters (mode,encoding)
with file_path.open(mode= "w", encoding= "UTF-8") as file:
    #Write the values
    file.write(f"{Overheads}\n{COH}\n{Profit}")

file.close() #Close the file


