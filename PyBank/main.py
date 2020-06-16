import pandas as pd
df = pd.read_csv("resources/budget_data.csv")

listdate = df['Date']
listprofit = df['Profit/Losses']
file = open("analysis/output.txt",'w')

# print(len(df))
# print(sum(listprofit))

change = []
for i in range(len(df)-1):
    # the first data has no value. (row 2 to the end of the data)
    change.append(listprofit[i+1] - listprofit[i])

# dataset should be "-1"
avechange = sum(change)/(len(df)-1)
# print(f'{avechange:.02f}')

maxvalue = max(change)
# print(maxvalue)

# first data should be ignored, starting from 2nd data
maxindex = change.index(max(change)) + 1
# print(listdate[maxindex + 1])

minvalue = min(change)
minindex = change.index(min(change)) + 1
# print(minvalue)
# print(listdate[minindex])


print ("Financial Analysis")
print ("----------------------")
print ("Total months: " + f'{len(df)}')
print ("Total: $" + f'{sum(listprofit)}')
print ("Average Change: $" + f'{avechange:.02f}')
print ("Greatest Increase in Profits: " + f'{listdate[maxindex]}' + f'(${maxvalue})')
print ("Greatest Decrease in Profits: " + f'{listdate[minindex]}' + f'(${minvalue})')

file.write("Financial Analysis")
file.write("\n----------------------")
file.write("\nTotal months: " + f'{len(df)}')
file.write("\nTotal: $" + f'{sum(listprofit)}')
file.write("\nAverage Change: $" + f'{avechange:.02f}')
file.write("\nGreatest Increase in Profits: " + f'{listdate[maxindex]}' + f'(${maxvalue})')
file.write("\nGreatest Decrease in Profits: " + f'{listdate[minindex]}' + f'(${minvalue})')