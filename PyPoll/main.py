import os
import csv

budget_data = os.path.join("Resources","election_data.csv") #set path for csvfile

#initialise variables 
total_votes = 0
charles_votes = 0
charles_percentage = 0
diana_votes = 0
diana_percentage = 0
raymon_votes = 0
raymon_percentage = 0
winner = ''

#open the csv file 
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header=next(csv_reader) #passes over the first row, which is a header

    #count the number of votes candidiates received
    for row in csv_reader:
        total_votes += 1
        if row[2] == 'Charles Casper Stockham':
            charles_votes += 1
        elif row[2] == 'Diana DeGette':
            diana_votes += 1
        elif row[2] == 'Raymon Anthony Doane':
            raymon_votes += 1

#calculate the percentages of each candidate
charles_percentage = charles_votes/total_votes      
diana_percentage = diana_votes/total_votes
raymon_percentage = raymon_votes/total_votes

#Determine who has the most votes, and is the winner
if charles_votes > diana_votes and charles_votes > raymon_votes:
    winner = 'Charles Casper Stockham'
elif diana_votes > charles_votes and diana_votes > raymon_votes:
    winner = 'Diana DeGette'
elif raymon_votes > charles_votes and raymon_votes > diana_votes:
    winner = 'Raymon Anthony Doane'

#print out to terminal the results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'Charles Casper Stockham: {charles_percentage:.3%} ({charles_votes})')
print(f'Diana DeGette: {diana_percentage:.3%} ({diana_votes})')
print(f'Raymon Anthony Doane: {raymon_percentage:.3%} ({raymon_votes})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

#Create file path to file that will be written to
output_path = os.path.join('analysis', 'financial analysis.txt')

#open the textfile and write the same information to text file
with open(output_path, 'w') as txt_file:
    txt_file.write('Election Results \n')
    txt_file.write('------------------------- \n')
    txt_file.writelines(f'Total Votes: {total_votes}\n')
    txt_file.writelines('-------------------------\n')
    txt_file.writelines(f'Charles Casper Stockham: {charles_percentage:.3%} ({charles_votes}) \n')
    txt_file.writelines(f'Diana DeGette: {diana_percentage:.3%} ({diana_votes}) \n')
    txt_file.writelines(f'Raymon Anthony Doane: {raymon_percentage:.3%} ({raymon_votes}) \n')
    txt_file.writelines('-------------------------\n')
    txt_file.writelines(f'Winner: {winner}\n')
    txt_file.writelines('-------------------------\n')