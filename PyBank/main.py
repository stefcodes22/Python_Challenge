import os
import csv

#Variables
Months = []
Average_change = []
Profit_increase = 0
month_increase = ""
Profit_decrease = 0
month_decrease = ""
Total_months = 0
total_net = 0

csvpath = os.path.join ('Resources',"budget_data.csv")

# Reading the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  
    first_row = next(csvreader)
    Total_months += 1
    total_net = int(first_row[1])
    initial = int(first_row[1])

#Calculations   
    for Months in csvreader:
        Total_months += 1
        total_net = total_net + int(Months[1])
        prev_net = int(first_row[1])
       
        if Profit_increase < int(Months[1]):
            Profit_increase = int(Months[1]) 
            month_increase = Months[0]
        if Profit_decrease > int(Months[1]):
            Profit_decrease = int(Months[1])
            month_decrease = Months[0]

last_value = Months[1]
Average_change = round((int(last_value) - initial) / (Total_months-1), 2)

#Print to terminal

print("Financial Analysis")  
print("-----------------------------")     
print(f"Total months: {Total_months}")
print(f"Total: $ {total_net}")
print(f"The Average change: {Average_change}")
print(f"Greatest increase in profits: {month_increase} (${Profit_increase})")
print(f"Greatest decrease in profits: {month_decrease} (${Profit_decrease})")

#Print to text
file = ("Pybank_Analysis")
Analysistext = os.path.join('Analysis',file +".txt")
PyBank = open(Analysistext ,"w+")
PyBank.write("Financial Analysis \n") 
PyBank.write(f"Total months: {Total_months} \n") 
PyBank.write(f"Total: $ {total_net} \n")
PyBank.write(f"The Average change: {Average_change} \n")
PyBank.write(f"Greatest increase in profits: {month_increase} (${Profit_increase}) \n")
PyBank.write(f"Greatest decrease in profits: {month_decrease} (${Profit_decrease}) \n")