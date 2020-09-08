import os
import csv
import pprint 

path = os.path.join( "Resources","budget_data.csv" )

with open(path, "r") as file:
    
    reader = csv.reader(file)
    header = next(reader)
    lines = list(reader)
    months = len(lines)
    
    print(f"Total Months: {months}")
    print(f"Total Months: {months}", file=open("output.txt", "a"))
   
    
with open(path, "r") as file:
    dict_reader = csv.DictReader(file)

    
    l = []
    d = []
   
    
    for row in dict_reader:
        row = dict(row)
        
        date = str(row["Date"])
        total = int(row["Profit/Losses"])
        
        l.append(total)
        d.append(date)
        
        total_profit = sum(l)
        average = total_profit/months
        minn = min(l)
        maxx = max(l)
        min_index = l.index(min(l))
        max_index = l.index(max(l))
        lowest_date = d[min_index]
        highest_date = d[max_index]
        
    
        
    print (f"Total: ${total_profit}")
    print (f"Average Change: {average}")
    print (f"The greatest increase in profits are ${maxx} in {highest_date}.")
    print (f"The lowest increase in profits are ${minn} in {lowest_date}.")
    
    with open("output.txt", "a") as f:
        print(f"Total: ${total_profit}", file=f)
        print(f"Average Change: {average}", file=f)
        print (f"The greatest increase in profits are ${maxx} in {highest_date}.", file=f)
        print (f"The lowest increase in profits are ${minn} in {lowest_date}.", file=f)
    
    

  
        
    

    