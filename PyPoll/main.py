import os
import csv

# Set path for file
csvpath = os.path.join('Resources','election_data.csv')

# Open the CSV and skip header row
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

# Initial Variables
    total = 0

# A complete list of candidates who received votes
    candidates = {}

# Loop through CSV
    for row in csvreader:
    #The total number of votes cast
        total = total + 1

        if row[2] in candidates:
            a = candidates[row[2]]
            b = a + 1
            existing_candidate = {row[2]:b}
            candidates.update(existing_candidate)
            pass
        else:
            new_candidate = {row[2]:1}
            candidates.update(new_candidate)
            pass
            
    # Print results
    print(f"Election Results")
    print(f"---------------------------------------------")
    print(f"Total Votes: {total}")
    print(f"---------------------------------------------")
    # The total number of votes each candidate won
    for key, value in candidates.items():
        # The percentage of votes each candidate won
        percentage = value/total
        percentage = "{:.3%}".format(percentage)
        print(f"{key}: {percentage} ({value})")  
    print(f"---------------------------------------------")
    # The winner of the election based on popular vote.
    for key, value in candidates.items():
        winner = max(candidates.values())
        if value == winner:
            print(f"Winner: {key}")
    print(f"---------------------------------------------")

# Set path for file
txtpath = os.path.join('Analysis','output.txt')

# Open the txt and write results
with open(txtpath,"w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"---------------------------------------------\n")
    txt_file.write(f"Total Votes: {total}\n")
    txt_file.write(f"---------------------------------------------\n")
    # The total number of votes each candidate won
    for key, value in candidates.items():
        # The percentage of votes each candidate won
        percentage = value/total
        percentage = "{:.3%}".format(percentage)
        txt_file.write(f"{key}: {percentage} ({value})\n")  
    txt_file.write(f"---------------------------------------------\n")
    # The winner of the election based on popular vote.
    for key, value in candidates.items():
        winner = max(candidates.values())
        if value == winner:
            txt_file.write(f"Winner: {key}\n")
    txt_file.write(f"---------------------------------------------\n")