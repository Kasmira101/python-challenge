import os
import csv
import pprint 

path = os.path.join( "Resources","election_data.csv" )

with open(path, "r") as file:
    
    reader = csv.reader(file)
    header = next(reader)
    lines = list(reader)
    total_votes = len(lines)
    
    print(f"TOTAL VOTES = {total_votes}")
    print(f"TOTAL VOTES = {total_votes}", file=open("output.txt", "a"))
    

with open(path, "r") as file:
    dict_reader = csv.DictReader(file)
    
    c=[]
    k= []
    correy = []
    o= []
    li = []
    
    for row in dict_reader:
        row = dict(row)
        
        voter_id = str(row["Voter ID"])
        county = str(row["County"])
        candidate = str(row["Candidate"])
        
        c.append(candidate)
        
    for e in c:
         if e == "Khan":
                k.append(e)
         if e == "Correy":
                correy.append(e)
         if e == "O'Tooley":
                o.append(e)
         if e == "Li":
                li.append(e)
                
    khan_total = len(k)
    correy_total = len(correy)
    o_total = len(o)
    li_total = len(li)
        
    khan_p = ((khan_total)/(total_votes)) * 100
    correy_p = ((correy_total)/(total_votes)) * 100
    o_p = ((o_total)/(total_votes)) * 100
    li_p = ((li_total)/(total_votes)) * 100
    

    
    cv =[]
    
    cv.append(khan_total)
    cv.append(correy_total)
    cv.append(o_total)
    cv.append(li_total)
    
    winner = max(cv)
    
    print (f"Khan: {khan_p} % ({khan_total})")
    print (f"Correy: {correy_p} % ({correy_total})")
    print (f"O'Tooley: {o_p} % ({o_total})")
    print (f"Li: {li_p} % ({li_total})")
    
    print("Winner: Khan")
    
    
    with open("output.txt", "a") as f:
        print(f"Khan: {khan_p} % ({khan_total})", file=f)
        print(f"Correy: {correy_p} % ({correy_total})", file=f)
        print (f"O'Tooley: {o_p} % ({o_total})", file=f)
        print (f"Li: {li_p} % ({li_total})", file=f)
        
