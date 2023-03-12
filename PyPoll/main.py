import csv

file = "PyPoll/Resources/election_data.csv"

vote_count = 0
candidates = {}

with open(file) as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")
    header = next(election_data)

    for row in election_data:
        if row[2] not in candidates:
            candidates[row[2]] = 0

        candidates[row[2]] = candidates[row[2]] + 1

        vote_count+= 1

print("Election Results")
print("--------------------")
print("Total Votes: " + str(vote_count))
print("--------------------")
for key in candidates:
    print(f"{key}: {str(round(candidates[key]/vote_count * 100, 3))}% ({candidates[key]})")
print("--------------------")
print("Winner: " + max(candidates, key=candidates.get))
print("--------------------")

write_path = "PyPoll/analysis/election_result.txt"
with open(write_path, 'w') as f: 
    f.write("Election Results\n")
    f.write("--------------------\n")
    f.write("Total Votes: " + str(vote_count))
    f.write("\n--------------------")
    for key in candidates:
        f.write(f"\n{key}: {str(round(candidates[key]/vote_count * 100, 3))}% ({candidates[key]})")
    f.write("\n--------------------")
    f.write("\nWinner: " + max(candidates, key=candidates.get))
    f.write("\n--------------------")
