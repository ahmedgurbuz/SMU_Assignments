import os
import csv

# Path to collect data from the Resources folder

path = r"C:\Users\AG\Documents\SMU COURSE\SMU-DAL-DATA-PT-08-2019-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"


# Read in the CSV file
with open(path, 'r') as election_data:

    # Split the data on commas
    csvreader = csv.reader(election_data, delimiter=',')
    
    #Skipping the header row
    next(csvreader)

    #Looping through csv file with our handle
    for row in csvreader:

        #Assigning values to variables with descriptive names
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        #Calculating total votes (total rows of data)
        total_votes = (csvreader.line_num)-1
    

   # Open function to create and write on the file "Results.txt"  
    file_object = open(r"C:\Users\AG\Documents\python-challenge\PyPoll\Results.txt","w+")

    #Assigning each lines in results table as variable
    str1 = "Election Results"
    str2 = str("-"*20)
    str3 = str(f"Total Votes: {total_votes}")
    str4 = str(f"Khan: {total_votes}")
    str5 = str(f"Correy: {total_votes}")
    str6 = str(f"O'Tooley: {total_votes}")
    str7 = str(f"Winner: {total_votes}")

    #Printing the final values
    print(str1)
    print(str2)
    print(str3)
    print(str2)
    print(str4)
    print(str5)
    print(str6)
    print(str2)
    print(str7)
    print(str2)

    #Uniting results table and writing line by line to text file
    results = [ str1 + "\n", str2 + "\n", str3 + "\n", str2 + "\n", str4 + "\n", str5 + "\n", str6 + "\n", str2 + "\n", str7 + "\n", str2] 
    file_object.writelines(results)
    #Closing text file
    file_object.close()