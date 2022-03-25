import os
import csv

#Variables
candidatesvotes = {}
totalvotes = 0

file = os.path.join ('Resources',"election_data.csv")

# Reading the CSV
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)  
     
    for row in csv_reader:
        totalvotes += 1
        candidatename = row[2]
        if candidatename in candidatesvotes.keys():
            candidatesvotes[candidatename] += 1
        else:
            candidatesvotes[candidatename] = 1

winner = max(candidatesvotes,key=candidatesvotes.get)

#Print to terminal
print("Election Results")
print("-----------------------------") 
print(f"Total votes: {totalvotes}")
print("-----------------------------") 
for key, value in candidatesvotes.items():
    print(f"{key} : {value} ")
print("-----------------------------") 
print(f"The winner is: {winner}")
print("-----------------------------") 

#Print to text
file = ("Election_results")
Analysistext = os.path.join('analysis',file +".txt")
Pypoll = open(Analysistext ,"w+")
Pypoll.write("Election Results \n") 
Pypoll.write(f"Total votes: {totalvotes} \n")
for key, value in candidatesvotes.items():
    Pypoll.write(f"{key} : {value} \n") 
Pypoll.write(f"The winner is: {winner} \n")
 
