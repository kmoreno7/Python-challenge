import csv
import os

with open('election_data.csv') as csvfile:
    
    csvreader=csv.reader(csvfile) 
    header=next(csvreader) 
    
    #Prepare variables
    ballot_id=[]
    county=[]
    candidate=[]
    
    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        ballot_ids=row[0]
        countys=row[1]
        candidates=row[2]
        ballot_id.append(ballot_ids)
        county.append(countys)
        candidate.append(candidates)

    #The total number of votes cast
    total_votes=len(ballot_id)
    print(total_votes)
    
    #complete list of candidates who received votes

uni_candidates = []

for item in candidate: 
    if item not in uni_candidates: 
        uni_candidates.append(item) 

print("Unique elements of the list using append():\n")    
for item in uni_candidates: 
    print(item) 
#Begin data analysis 

#The percentage of votes each candidate won

count = 0 

for item in candidate:
    if item == 'Charles Casper Stockham' :
        count += 1 
        
print(count)

can_percent = round(count/total_votes *100, 2) 
print(can_percent)

count1 = 0 

for item in candidate:
    if item == 'Diana DeGette' :
        count1 += 1 
        
print(count1)
can1_percent = round(count1/total_votes *100, 2) 
print(can1_percent)

count2 = 0 

for item in candidate:
    if item == 'Raymon Anthony Doane' :
        count2 += 1 
        
print(count2)
can2_percent = round(count2/total_votes *100, 2) 
print(can2_percent)

analysis=f'\
  Election Results\n\
  -------------------------\n\
  Total Votes: {total_votes}\n\
  -------------------------\n\
  Charles Casper Stockham: {can_percent}% {count}\n\
  Diana DeGette: {can1_percent}% {count1}\n\
  Raymon Anthony Doane: {can2_percent}% {count2}\n\
  -------------------------\n\
  Winner: Diana DeGette\n\
  -------------------------\n'

print(analysis)

#Write into text file named election_data.txt

file1=open("election_data.txt","w") #Open or if file does not exist then create file named election_data.txt
file1.writelines(analysis) #Write analysis into election_data.txt
file1.close() #Close election_data.txt write mode
