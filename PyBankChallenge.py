import csv

filePath = "Resources/budget_data.csv"

numberOfMonths = []
profitLoss = []
profitLossDifferences = []

# Open csv file
with open(filePath, "r", encoding = "UTF-8") as handler:
    csvreader = csv.reader(handler)
    next(csvreader)

    # Create lists to contain all months and all profit/losses
    for row in csvreader:
        numberOfMonths.append(row[0])
        profitLoss.append(int(row[1]))

    # Get the difference in Profit Loss by subtracting the new value by old value
    for i in range(1, len(profitLoss)):
        profitLossDifferences.append(profitLoss[i] - profitLoss[i - 1])

# Calculate the total # of Months by getting the length of the list of months
monthCount = len(numberOfMonths)


totalProfitLoss = sum(profitLoss)

# Calculate the Profit/Loss Average, Min, and Max
profitLossAvg = round(sum(profitLossDifferences)/len(profitLossDifferences), 2)
profitLossMax = max(profitLossDifferences)
profitLossMin = min(profitLossDifferences)

# Find the corresponding Month for Min and Max
maxMonth = (numberOfMonths[profitLossDifferences.index(profitLossMax)  + 1])
minMonth = (numberOfMonths[profitLossDifferences.index(profitLossMin)  + 1])

# Print full analysis
analysis = (f"Financial Analysis"
"\n----------------------------"
f"\nTotal Months: {monthCount}"
f"\nTotal: ${totalProfitLoss}"
f"\nAverage Change: ${profitLossAvg}"
f"\nGreatest Increase in Profits: {maxMonth} (${profitLossMax})"
f"\nGreatest Decrease in Profits: {minMonth} (${profitLossMin})")

print(analysis)

txt_file_path = "Analysis/PyBank_Analysis.txt"

with open(txt_file_path, 'w') as txt:
    txt.write(analysis)