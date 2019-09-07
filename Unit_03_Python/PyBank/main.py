import os
import csv

# Path to collect data from the resource
path = r"C:\Users\AG\Documents\SMU COURSE\SMU-DAL-DATA-PT-08-2019-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

# Read in the CSV file
with open(path, 'r') as budget_data:

    # Split the data on commas
    csvreader = csv.reader(budget_data, delimiter=',')

    #Skipping the header row
    next(csvreader)

    #Creating empty lists to be filled later
    profit = []
    months = []
    
    #Looping through csv file with our handle
    for row in csvreader:
        
        #Reading and adding every row in second column (profit/loss column) to profit list
        profit.append(int(row[1]))

        #Reading and adding every row in first column (months column) to months list
        months.append(row[0])

    #Since every month represents one row, total number of rows (length of months list) give us total number of months
    total_months = len(months)

    #Every row includes profit for one month. Summing them up gives us total profit (summing each element in profit list)
    total_profit = sum(profit)
    
    #Creating empty list for profit changes 
    profit_change = []

    #Looping through profit list, getting differences of each profit and adding them to profit_change list 
    for i in range(1,len(profit)):
        profit_change.append(profit[i] - profit[i-1])   

    #Calculating average change
    average_change = sum(profit_change)/len(profit_change)

    #Calculating maximum and minimum profit change
    max_profit_change = max(profit_change)
    min_profit_change = min(profit_change)

    #Retrieving maximum and minimum profit change month 
    max_profit_change_month = str(months[profit_change.index(max(profit_change))])
    min_profit_change_month = str(months[profit_change.index(min(profit_change))])

    #Printing the final values
    print("FINANCIAL ANALYSIS")
    print("-"*20)
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {max_profit_change_month} (${max_profit_change})")
    print(f"Greatest Decrease in Profits: {min_profit_change_month} (${min_profit_change})")

    # Open function to create and write on the file "Results.txt"  
    file_object = open(r"C:\Users\AG\Documents\python-challenge\PyBank\Results.txt","w+")

    #Assigning each lines in results table as variable
    str1 = "FINANCIAL ANALYSIS"
    str2 = str("-"*20)
    str3 = str(f"Total Months: {total_months}")
    str4 = str(f"Total: ${total_profit}")
    str5 = str(f"Average Change: ${round(average_change, 2)}")
    str6 = str(f"Greatest Increase in Profits: {max_profit_change_month} (${max_profit_change})")
    str7 = str(f"Greatest Decrease in Profits: {min_profit_change_month} (${min_profit_change})")

    #Uniting results table and writing line by line to text file
    results = [str1 + "\n", str2 + "\n", str3 + "\n", str4 + "\n", str5 + "\n", str6 + "\n", str7 + "\n"] 
    file_object.writelines(results)
    #Closing text file
    file_object.close()