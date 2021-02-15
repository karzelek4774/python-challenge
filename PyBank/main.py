import os
import csv

# Set path for file
csvpath = os.path.join('Resources','budget_data.csv')

# Open the CSV and skip header row
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

# Initial Variables
    total = 0
    months = 0
    sum_change = 0
    previous = 0
    increase = 0
    decrease = 0

# Loop through CSV
    for row in csvreader:
    #The total number of months included in the dataset
        months = months + 1
    #The net total amount of "Profit/Losses" over the entire period
        total = total + float(row[1])
    #Calculate the changes in "Profit/Losses" over the entire period
        if months > 1:
            change = float(row[1]) - previous
            sum_change = sum_change + change
            #The greatest increase in profits (date and amount) over the entire period
            if change > increase:
                increase = change
                inc_month = row[0]
            #The greatest decrease in losses (date and amount) over the entire period    
            if change < decrease:
                decrease = change
                dec_month = row[0]
        previous = float(row[1])
    #Then find the average of those changes
    average = sum_change / (months - 1)

#Format to Currency
total = "${:.0f}".format(total)
average = "${:.2f}".format(average)
increase = "${:.0f}".format(increase)
decrease = "${:.0f}".format(decrease)
    
#Print results
print(f"Financial Analysis")
print(f"---------------------------------------------")
print(f"Total Months: {months}")
print(f"Total Profit: {total}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {inc_month} ({increase})")
print(f"Greatest Decrease in Profits: {dec_month} ({decrease})")

# Set path for file
txtpath = os.path.join('Analysis','output.txt')

# Open the txt and write results
with open(txtpath,"w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"---------------------------------------------\n")
    txt_file.write(f"Total Months: {months}\n")
    txt_file.write(f"Total Profit: {total}\n")
    txt_file.write(f"Average Change: {average}\n")
    txt_file.write(f"Greatest Increase in Profits: {inc_month} ({increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {dec_month} ({decrease})\n")