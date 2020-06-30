# Import dependencies
import os
import csv
import sys

# Path to CSV
csvpath = '..\\Resources\\election_data.csv'

# Define Variables
election_data = {}
candidate_vote_list = {}
total_votes = 0
winner = ""

# Open and read CSV
with open (csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    for row in csvreader:
        # Calculate total votes
        total_votes = total_votes + 1

        if str(row[2]) in election_data:

            # Calculate total number of votes cast per candidate
            election_data[row[2]] = election_data[row[2]] + 1
        else: 
            election_data[row[2]] = 1

# Calculate percentage of votes for each candidate
for vote_percentage in election_data:
    candidate_vote_list[vote_percentage] = (election_data[vote_percentage] / total_votes) * 100

# Calculate winner of election based on votes
winner = max(election_data, key= election_data.get)

# Print final results
print("Election Results")
print("--------------------")
print(f"Total Votes:{total_votes}")
print("--------------------")
# print list of candidates with vote percentage and total # of votes
for candidate_totals in election_data:
    message = str(candidate_totals) + \
        ":  {:.3f}".format(candidate_vote_list[candidate_totals]) + \
            "% " + "(" + str(election_data[candidate_totals]) + ")"
    print(message)
print("--------------------")

# print winning candidate/candidate with most votes
print(f"Winner: {winner}")
print("--------------------")

# Print to text file
with open("output.txt", "w") as txt_file:
    sys.stdout = txt_file

    # Print final results as text file
    print("Election Results")
    print("--------------------")
    print(f"Total Votes:{total_votes}")
    print("--------------------")
    # print list of candidates with vote percentage and total # of votes
    for candidate_totals in election_data:
        message = str(candidate_totals) + \
            ":  {:.3f}".format(candidate_vote_list[candidate_totals]) + \
                "% " + "(" + str(election_data[candidate_totals]) + ")"
        print(message)
    print("--------------------")

    # print winning candidate/candidate with most votes
    print(f"Winner: {winner}")
    print("--------------------")