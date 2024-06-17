import os 
import csv
file_path= os.path.join("Resources\election_data.csv")
analysis_outcome= os.path.join("Analysis","election_results.txt")

votes= 0
canidates= []
canidate_votes= []


with open(file_path,"r") as file:
    csvreader= csv.reader(file)
    header= next(csvreader)


    for row in csvreader:
        votes = votes +1
        canidate = row[2]


        if canidate not in canidates:
            canidates.append(canidate)
            canidate_votes [canidate]+= 1
canidate_votes[canidate]+= 1

winner = ""
winner_votes = 0
output = []

votes = canidate_votes[canidate]
percentage = (votes / votes) * 100
output.append(f"{canidate}: {percentage:.3f}% ({votes})")

if votes > winner_votes:
        winner = canidate
        winner_votes = votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
for line in output:
    print(line)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

file.write("Election Results\n")
file.write("-------------------------\n")
file.write(f"Total Votes: {votes}\n")
file.write("-------------------------\n")
for line in output:
    file.write(f"{line}\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")


print("Results have been saved to election_results.txt file.")

