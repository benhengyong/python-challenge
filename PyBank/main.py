import os
import csv


budget_data = os.path.join("Resources","budget_data.csv") #set path for csvfile

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header=next(csv_reader) #passes over the first row, which is a header
    
    #initiliase all variables used
    month_count = 0
    total = 0
    profit = []
    profit_change = []
    average_profit_change=0
    greatest_increase = 0
    greatest_increase_position = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_position = 0
    greatest_increase_date = ""


    for row in csv_reader: #Reads the rows in budget_data
        profit.append(row[1]) #save profit values in a profit array
        month_count += 1 #Count the number of months 
        total = total + int(row[1]) #Sum the total profit/loss
        

for number in range(0, len(profit)): #Loop through the profit array
    if number != len(profit)-1: #Stop when the array reaches the end
        #Find the change in profit/loss between next row and current row
        profit_change.append(int(profit[number+1])-int(profit[number])) 
        #Use IF statements to find greatest increases, decrease and their profit values/positions
        if int(profit[number+1])-int(profit[number]) > greatest_increase:
            greatest_increase = int(profit[number+1])-int(profit[number])
            greatest_increase_position = int(profit[number+1])
        elif int(profit[number+1])-int(profit[number]) < greatest_decrease:
            greatest_decrease = int(profit[number+1])-int(profit[number])
            greatest_decrease_position = int(profit[number+1])

#Reopen file again so it reads from the start 
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header=next(csv_reader) #passes over the first row, which is a header

    #Go down the csvfile and find the dates that have the same profit values for greatest increase/decrease
    for row in csv_reader:
        if int(row[1]) == greatest_increase_position:
            greatest_increase_date = row[0]
        elif int(row[1]) == greatest_decrease_position:
            greatest_decrease_date = row[0]

    
for change in profit_change:
    average_profit_change += change #Sum all the changes in profit/loss

average_profit_change = average_profit_change/len(profit_change) #Calculate the average changes in profit/loss

#Print out all required information
print('Financial Analysis')
print('----------------------------')
print("Total Months:", month_count)
print(f'Total: ${total}')
print(f'Average Change: ${round(average_profit_change,2)}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

#Create file path to file that will be written to
output_path = os.path.join('analysis', 'financial analysis.txt')

#open the textfile and write the same information to text file
with open(output_path, 'w') as txt_file:
    txt_file.write('Financial Analysis \n')
    txt_file.write('---------------------------- \n')
    txt_file.writelines("Total Months:" +str(month_count)+"\n")
    txt_file.writelines(f'Total: ${total} \n')
    txt_file.writelines(f'Average Change: ${round(average_profit_change,2)} \n')
    txt_file.writelines(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}) \n')
    txt_file.writelines(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease}) \n')