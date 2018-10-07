import os
import csv

#set path to csv file
pyPoll_csv = os.path.join('election_data.csv')

#read the csv file
with open(pyPoll_csv, 'r') as pyPollData:
    electionData = csv.reader(pyPollData, delimiter=",")

    #skip the header
    next(electionData, None)

    #set totalVotes baseline to 0
    totalVotes = 0
    #set empty dictionary for candidates and vote count
    election = {}
    #set empty list for all candidates
    candidates = []

    #loop through rows/votes
    for vote in electionData:

        #running tally of votes
        totalVotes += 1

        #finds candidate in vote
        candidate = vote[2]

        #add candidate to election dictionary
        if not candidate in election:
            election[candidate] = 1
        #or add one to the candidate's vote count
        else:
            election[candidate] += 1

        #add candidate to list
        if not candidate in candidates:
            candidates.append(candidate)

#calculate % of votes per candidate            
votePerc0 = election[candidates[0]] / totalVotes
votePerc1 = election[candidates[1]] / totalVotes
votePerc2 = election[candidates[2]] / totalVotes
votePerc3 = election[candidates[3]] / totalVotes

#format votePercs as %
votePerc0 = format(votePerc0, ".3%")
votePerc1 = format(votePerc1, ".3%")
votePerc2 = format(votePerc2, ".3%")
votePerc3 = format(votePerc3, ".3%")

##determine winner
#set baseline for winning vote count and candidate
mostVotes = 0
winningCandidate = 0

for i in candidates:
    if election[i] > mostVotes:
        mostVotes = election[i]
        winningCandidate = i

#print results
print("Election Results")       
print("----------------")
print(f"Total Votes: {totalVotes}")
print("----------------")
print(f"{candidates[0]}: {votePerc0} ({election[candidates[0]]})")
print(f"{candidates[1]}: {votePerc1} ({election[candidates[1]]})")
print(f"{candidates[2]}: {votePerc2} ({election[candidates[2]]})")
print(f"{candidates[3]}: {votePerc3} ({election[candidates[3]]})")
print("----------------")
print(f"Winner: {winningCandidate}")

#write text doc with results
electionDocument = open('election_results.txt','w')
electionDocument.write(f"""Election Results 
---------------- 
Total Votes: {totalVotes} 
---------------- 
{candidates[0]}: {votePerc0} ({election[candidates[0]]}) 
{candidates[1]}: {votePerc1} ({election[candidates[1]]}) 
{candidates[2]}: {votePerc2} ({election[candidates[2]]}) 
{candidates[3]}: {votePerc3} ({election[candidates[3]]}) 
---------------- 
Winner: {winningCandidate}""")
electionDocument.close()