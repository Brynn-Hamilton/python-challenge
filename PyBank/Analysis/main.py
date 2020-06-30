# Import dependencies
import os
import csv
import sys

# Path to csvfile
csvpath = '..\\Resources\\budget_data.csv'

#Define variables
total_months = 0
revenue_net_total = 0
revenue_changes = []
month_count = []
greatest_increase_profit = 0
greatest_decrease_loss = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Open and read CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for row in csvreader:
        # Calculate Total # of Months and Net Total (Profit/Loss)
        total_months += 1
        revenue_net_total = revenue_net_total + int(row[1]) 
        
#       Calculate Greatest Increase/Decrease
        if int(row[1]) > greatest_increase_profit:
            greatest_increase_profit = int(row[1])
            greatest_increase_month = row[0]

        if int(row[1]) < greatest_decrease_loss:
            greatest_decrease_loss = int(row[1])
            greatest_decrease_month = row[0]

        # Calculate Average Change
        revenue_changes.append(int(row[1]))
        month_count.append(row[0])


# Calculate Total Revenue Change
average_change = sum(revenue_changes) / len(revenue_changes)

highest = max(revenue_changes)
lowest = min(revenue_changes)


# Generate and Print Final Analysis of Value Totals
print(f"Financial Analysis")
print(f"--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${revenue_net_total}")
print("Average Change: ${:.2f}".format(average_change))
print(f"Greatest Increase in Profits: {greatest_increase_month}, ${highest}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}, ${lowest}") 

#Print as text file
with open("output.txt", "w") as txt_file:
    sys.stdout = txt_file
    print(f"Financial Analysis")
    print(f"--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${revenue_net_total}")
    print("Average Change: ${:.2f}".format(average_change))
    print(f"Greatest Increase in Profits: {greatest_increase_month}, ${highest}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month}, ${lowest}")
   


