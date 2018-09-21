import os
import csv


csvbudget = os.path.join('Resources', 'budget_data.csv')
budgetoutput = os.path.join('analysis', 'financialSummary.txt')

with open(csvbudget,newline = '') as financialInfo:
    reader = csv.reader(financialInfo,delimiter = ",")
    
    header = next(reader)
    
    print(header)
         
    #bottomlines = list(reader)
    
    revenue = []
    date = []
    change = []

    for row in reader:  

        revenue.append(int(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print('-----------------------------')
    print('Total Months:', len(date))
    print('Total Revenue:', sum(revenue))
       
    
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])
             
    avgChange = sum(change)/len(change)
        
    maxChange = max(change)
        
    minChange = min(change) 
    maxChangeDate = str(date[change.index(max(change))])
    minChangeDate = str(date[change.index(min(change))])
    
    print('Average Revenue Change: $', round(avgChange))
    print(f'Greatest Increase in Revenue:, maxChangeDate,($,{maxChange})')
    print(f'Greatest Decrease in Revenue:, minChangeDate,($, {minChange})')

