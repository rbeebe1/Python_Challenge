import csv

filePath = "Resources/election_data.csv"

totalVotes = 0
uniqueCandidates = {}
percentageOfVotes = []

# Open csv file
with open(filePath, "r", encoding = "UTF-8") as handler:
    csvreader = csv.reader(handler)
    next(csvreader)

    for col in csvreader:
        totalVotes += 1
        if col[2] not in uniqueCandidates:
            # Key = Value
            uniqueCandidates[col[2]] = 1
        else: 
            uniqueCandidates[col[2]] += 1

    for key,value in uniqueCandidates.items():
        percentageOfVotes.append(round(((value/totalVotes)*100), 3))


    max_key = max(uniqueCandidates, key = uniqueCandidates.get)

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