import os
import csv


oprocess = os.path.join('Resources','election_data.csv')
nprocess = os.path.join ('Results', 'new_process.txt')

with open(oprocess, newline = '') as voteCount:
    
    reader = csv.reader(voteCount)
    header = next (reader)

    #print (header)

    voteTally = list(reader) 
    
# i need the count for each khan, correy, li, and o'tooley
    khanCounter =0
    correyCounter=0
    liCounter=0
    tooleyCount=0
    
    for row in voteTally:
        #print(row[2])
        if row[2] == "Khan":
            khanCounter = khanCounter+1
        if row[2] == "Correy":
            correyCounter = correyCounter+1
        if row[2] =="Li":
            liCounter = liCounter+1
        if row[2] == "O'Tooley":
            tooleyCount = tooleyCount+1

    
    
    khanRate = khanCounter/len(voteTally)
    correyRate = correyCounter/len(voteTally)
    liRate = liCounter/len(voteTally)
    tooleyRate = tooleyCount/len(voteTally)

       

    output = (f'Election Results\n'
    f'------------------------------\n'
    f'Total Votes: {len(voteTally)}\n'
    f'---------------------\n'
    f'Khan Votes: {khanCounter}\n'
    f'Percent: {round(khanRate*100,3)}%\n'
    f'---------------\n'
    f'Correy Votes: {correyCounter}\n'
    f'Percent: {round(correyRate*100,3)}%\n'
    f'---------------\n'
    f'Li Votes: {liCounter}\n'
    f'Percent: {round(liRate*100,3)}%\n'
    f'---------------\n'
    f"O'Tooley Votes: {tooleyCount}\n"
    f'Percent: {round(tooleyRate*100,3)}%\n'
    f'-------------------------------\n'
    f'Winner: Khan\n')


    print(output)

    with open(nprocess, "w+")  as textf:
        textf.write(output)
    




    
    
    
    
    
    

    
   






