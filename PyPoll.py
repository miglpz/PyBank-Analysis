import os
import csv

election = os.path.join("Resources" "election_data.csv")

candidates = []
votes_count = []
votes_percent = []
votes_total = 0

with open(election, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        votes_total += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes.append(1)
        else:
            index = candidates.index(row[2])
            votes_count[index] += 1

    for votes in votes_count:
        percentage = (votes/votes_total) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        votes_percent.append(percentage)

    winner = max(votes_count)
    index = votes_count.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print(f"Total Votes: {str(votes_total)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(votes_percent[i])} ({str(votes_count[i])})")
print(f"Winner: {winning_candidate}")

