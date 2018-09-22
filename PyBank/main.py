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
       
    
    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])
             
    avgChange = sum(change)/len(change)
        
    maxChange = max(change)
        
    minChange = min(change) 
    maxChangeDate = str(date[change.index(max(change))])
    minChangeDate = str(date[change.index(min(change))])
    
    output=(f'Financial Analysis\n'
    f'-----------------------------\n'
    f'Total Months:{len(date)}\n' 
    f'Total Revenue: $ {sum(revenue)}\n'
    f'Average Revenue Change: $ {round(avgChange)}\n'
    f'Greatest Increase in Revenue:, maxChangeDate,($,{maxChange})\n'
    f'Greatest Decrease in Revenue:, minChangeDate,($, {minChange})')

    print(output)

    with open(budgetoutput,"w+") as textf:
        textf.write(output)
        

