import pandas as pd
df = pd.read_csv("resources/election_data.csv")
listid = df['Voter ID']
datacounty = df['County']
datacandidate =  df['Candidate']
file = open("analysis/voteresult.txt",'w')

listcounty = datacounty.unique()
listcandidate = datacandidate.unique()


totalvote = len(df)
print('Election result')
file.write('Election result\n')
print('-----------------')
file.write('-----------------\n')
print (f'Total votes: {totalvote}')
file.write (f'Total votes: {totalvote}'+'\n')
print('-----------------')
file.write('-----------------'+'\n')

count = {}
for j in range(len(listcandidate)):
    count[listcandidate[j]] = 0
for candidate in datacandidate:
    count[candidate]+=1

for j in range(len(listcandidate)):
    print(f'{listcandidate[j]} : {count[listcandidate[j]]/totalvote*100:.02f}% ({count[listcandidate[j]]})')
    file.write(f'{listcandidate[j]} : {count[listcandidate[j]]/totalvote*100:.02f}% ({count[listcandidate[j]]})' +'\n')

winner = max(count, key=count.get)
print('-----------------')
file.write('-----------------' + '\n')
print(f'Winner {winner}')
print('-----------------')
file.write(f'Winner {winner}'+ '\n')
file.write('-----------------'+ '\n')




