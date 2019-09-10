import os
import csv

# Path to collect data from the Resources folder
path = r"C:\Users\AG\Documents\SMU COURSE\SMU-DAL-DATA-PT-08-2019-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

#Creating empty lists to be filled later
voter_id = []
county = []
candidate = []

# Read in the CSV file
with open(path, 'r') as election_data:

    # Split the data on commas
    csvreader = csv.reader(election_data, delimiter=',')
    
    #Skipping the header row
    next(csvreader)

    #Looping through csv file with our handle
    for row in csvreader:
        
        #Reading and adding every row in first column (Voter ID column) to voter_id list
        voter_id.append(int(row[0]))

        #Reading and adding every row in second column (County column) to county list
        county.append(str(row[1]))

        #Reading and adding every row in third column (Candidate column) to candidate list
        candidate.append(str(row[2]))
        
    #Calculating total votes with the length of Voter ID column
    total_votes = len(voter_id)

    #Creating a dictionary for Contestants
    votes_dict = {}

    #Creating a loop for 
    for contestant in candidate:
        if contestant in votes_dict:
            votes_dict[contestant] += 1
        else:
            votes_dict[contestant] = 1

    #Sorting contestants 
    candidates_sorted = sorted(
        votes_dict.items(),
        key=lambda contestant: contestant[1], 
        reverse = True
    )

    #Creating an empty list for percentage values
    percentages = []

    #Calculating percentages and adding values to the percentages list with a loop
    for value in votes_dict.values():
        percent = (value/total_votes)*100
        percentages.append(percent)


    #Printing results
    print("Election Results")
    print("-"*20)
    print(f"Total Votes: {total_votes}")
    print("-"*20)
    print(f"{candidates_sorted[0][0]}: {round(percentages[0], 5)}% ({candidates_sorted[0][1]})")
    print(f"{candidates_sorted[1][0]}: {round(percentages[1], 5)}% ({candidates_sorted[1][1]})")
    print(f"{candidates_sorted[2][0]}: {round(percentages[2], 5)}% ({candidates_sorted[2][1]})")
    print(f"{candidates_sorted[3][0]}: {round(percentages[3], 5)}% ({candidates_sorted[3][1]})")
    print("-"*20)
    print(f"Winner: {candidates_sorted[0][0]}")
    print("-"*20)



    # Open function to create and write on the file "Results.txt"  
    file_object = open(r"C:\Users\AG\Documents\python-challenge\PyPoll\Results.txt","w+")

    #Assigning each lines in results table as variable 
    str1 = "Election Results"
    str2 = str("-"*20)
    str3 = str(f"Total Votes: {total_votes}")
    str4 = str(f"{candidates_sorted[0][0]}: {round(percentages[0], 5)}% ({candidates_sorted[0][1]})")
    str5 = str(f"{candidates_sorted[1][0]}: {round(percentages[1], 5)}% ({candidates_sorted[1][1]})")
    str6 = str(f"{candidates_sorted[2][0]}: {round(percentages[2], 5)}% ({candidates_sorted[2][1]})")
    str7 = str(f"{candidates_sorted[3][0]}: {round(percentages[3], 5)}% ({candidates_sorted[3][1]})")
    str8 = str(f"Winner: {candidates_sorted[0][0]}")

    #Uniting results table and writing line by line to text file
    results = [str1 + "\n", str2 + "\n", str3 + "\n", str2 + "\n", str4 + "\n", str5 + "\n", str6 + "\n", str7 + "\n", str2 + "\n", str8 + "\n", str2 + "\n"]
    file_object.writelines(results)
    #Closing text file
    file_object.close()
