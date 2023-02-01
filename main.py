#Import the python files for cash_on_hand, overheads and profit_loss
from cash_on_hand import COH
from overheads import Overheads
from profit_loss import Profit

#Create 3 variables to store the three different functions
Overheads = Overheads()
COH = COH()
Profit= Profit()

#Use with to open the file and include the parameters (mode,encoding)
with open("Summary report.txt", "w") as file:
  #Use write() function to write into the txt file
  file.write(f"{Overheads}\n{COH}\n{Profit}")
file.close()
#Close the file


