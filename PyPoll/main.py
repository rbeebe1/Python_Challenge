# This code will analyze election results and return Total Votes, 
# Candidates and their total votes/percentages, and the Winner

import csv

filePath = "Resources/election_data.csv"

totalVotes = 0
uniqueCandidates = {}
percentageOfVotes = []

# Open csv file
with open(filePath, "r", encoding = "UTF-8") as handler:
    csvreader = csv.reader(handler)
    next(csvreader)
    # Count the number of columns in totalVotes 
    for col in csvreader:
        totalVotes += 1
        # If candidate name not already in list, add to the list
        if col[2] not in uniqueCandidates:
            # Key = Value
            uniqueCandidates[col[2]] = 1
        else: 
            uniqueCandidates[col[2]] += 1

    # Get candidate with most number of votes
    max_key = max(uniqueCandidates, key = uniqueCandidates.get)

    # Print
    print("Election Results"
          "\n-------------------------"
          f"\nTotal Votes: {totalVotes}"
          "\n-------------------------")
    for key,value in uniqueCandidates.items():
        print(f"{key} : {round((value/totalVotes)*100, 3)}% ({value})")    
    print("-------------------------"
          f"\nWinner: {max_key}"
          "\n-------------------------")

# Save to text file
txt_file_path = "Analysis/PyPoll_Analysis.txt"

with open(txt_file_path, 'w') as txt:
    print("Election Results"
          "\n-------------------------"
          f"\nTotal Votes: {totalVotes}"
          "\n-------------------------", file = txt)
    for key,value in uniqueCandidates.items():
        print(f"{key} : {round((value/totalVotes)*100, 3)}% ({value})", file = txt)    
    print("-------------------------"
          f"\nWinner: {max_key}"
          "\n-------------------------", file = txt)