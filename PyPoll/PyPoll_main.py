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

#set empty lists for vote %s and candidate data
votePerc = []
candidateData = []

#cycle through candidate list and calculate % of votes per candidate
for i in range(len(candidates)):
    #add vote % to list
    votePerc.append(election[candidates[i]] / totalVotes)

    #format votePerc as %
    votePerc[i] = format(votePerc[i], ".3%")

    #add candidate data to list
    candidateData.append(f"{candidates[i]}: {votePerc[i]} ({election[candidates[i]]}) \n")

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
print("---------------- \n")
for i in range(len(candidates)):
    print(f"{candidateData[i]}")
print("----------------")
print(f"Winner: {winningCandidate}")

#write text doc with results
electionDocument = open('election_results.txt','w')
electionDocument.write(f"""Election Results 
---------------- 
Total Votes: {totalVotes} 
---------------- \n""") 
electionDocument.writelines(candidateData)
electionDocument.write(f"""---------------- 
Winner: {winningCandidate}""")
electionDocument.close()