import pandas as pd

# Open csv
df = pd.read_csv("resources/election_data.csv")

# get the data from each header
listid = df['Voter ID']
datacounty = df['County']
datacandidate =  df['Candidate']

# define a text file to export
file = open("analysis/voteresult.txt",'w')

# get unique value of county/candidate
listcounty = datacounty.unique()
listcandidate = datacandidate.unique()

# get the total number of votes
totalvote = len(df)
print('Election result')
file.write('Election result\n')
print('-----------------')
file.write('-----------------\n')
print (f'Total votes: {totalvote}')
file.write (f'Total votes: {totalvote}'+'\n')
print('-----------------')
file.write('-----------------'+'\n')

# use dictionary to count each candidate vote, create empty dictionary called count
count = {}

# set the number of each candidate as 0
for j in range(len(listcandidate)):
    count[listcandidate[j]] = 0

# for all data in candidate columns, repeating add 1 to vote number of each candidate
for candidate in datacandidate:
    count[candidate]+=1

# print all candidates vote information
for j in range(len(listcandidate)):
    print(f'{listcandidate[j]} : {count[listcandidate[j]]/totalvote*100:.02f}% ({count[listcandidate[j]]})')
    file.write(f'{listcandidate[j]} : {count[listcandidate[j]]/totalvote*100:.02f}% ({count[listcandidate[j]]})' +'\n')

# decide winner using max function to get the key of the candidate whose vote are the most
winner = max(count, key=count.get)
print('-----------------')
file.write('-----------------' + '\n')
print(f'Winner {winner}')
print('-----------------')
file.write(f'Winner {winner}'+ '\n')
file.write('-----------------'+ '\n')




