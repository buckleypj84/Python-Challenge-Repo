# --------------------------------------------------------------------------------------------
# Date:     6/19/2019
# Pgm Name: main.py   
# Input:    (PyBank/Resources/budget_# data.csv). 
# Desc:     Python script that analyzes the financail records to calculate each of the following:
#           * total number of months included in the dataset
#           * net total amount of "Profit/Losses" over the entire period
#           * average of the changes in "Profit/Losses" over the entire period
#           * greatest increase in profits (date and amount) over the entire period
#           * greatest decrease in losses (date and amount) over the entire period:
# Sample Output: (print the analysis to the terminal and export a text file with the results)
#   #   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12 -- verify this amt
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)  
#------------------------------------------------------------------------------- 
import os
import csv

#get the current working directory
currentDir = os.getcwd()
#print(currentDir)
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#os.chdir(""../Homework")
csvpath = os.path.join('..','..', 'Homework', 'budget_data.csv')
print(csvpath)
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #-----------------------------------------------------------------------------
    # Read the header row first (skip this part if there is no header)
    # Initialize variables
    #-----------------------------------------------------------------------------
    next(csvreader, None)
    total_months = 0
    total_profit_loss = 0
    pf_loss_change = 0

    min_change = 0
    max_change = 0
    x = 0

    profit_loss_change = []
    month_yr = []
    budget = []
    rowcnt = 0
 
    #-----------------------------------------------------------------------------
    # Read through each row of data budget and month_yr lists
    # cast qty in budget as float to prevent errors in calculations
    #-----------------------------------------------------------------------------
    for row in csvreader:
        budget.append(float(row[1]))
        month_yr.append(row[0])

    #-----------------------------------------------------------------------------
    # Read through each row of data 
    #   begin reading at row 2 == subtract the qty in row 1 from qty in row 2
    #   len(month_yr) == returns nbr of items in the list
    #   load list with profit loss changes
    #-----------------------------------------------------------------------------
    for rowcnt in range(1,len(budget)):                          
        total_months = len(month_yr)
        pf_loss_change = float(budget[rowcnt]) - float(budget[rowcnt-1] )
        profit_loss_change.append(pf_loss_change)

    #----------------------------------------------------------------------------
    # Summarize and format budget data as currency with 2 decimals
    #----------------------------------------------------------------------------
    p_total_profit_loss = sum(budget)
    total_profit_loss = sum(budget)
    total_profit_loss = ('$'+ format(total_profit_loss,',.2f')) 

    p_max_change = max(profit_loss_change)
    max_change = max(profit_loss_change)
    max_change = ('$'+ format(max_change,',.2f'))

    p_min_change = min(profit_loss_change)
    min_change = min(profit_loss_change)
    min_change = ('$'+ format(min_change,',.2f'))

    #----------------------------------------------------------------------------
    # Retrieve the maximum/minimum profit lost change and the corresponding month and yr
    # on the month_yr list
    #----------------------------------------------------------------------------
    max_change_date = str(month_yr[profit_loss_change.index(max(profit_loss_change))])

    min_change_date = [profit_loss_change.index(min(profit_loss_change))]

    min_change_date = str(month_yr[profit_loss_change.index(min(profit_loss_change))])

    #----------------------------------------------------------------------------
    # Calculate and format average budget change
    #----------------------------------------------------------------------------
    p_average_change = sum(profit_loss_change)/total_months 
    average_change = sum(profit_loss_change)/total_months 
    average_change = ('$'+ format(average_change,',.2f'))

    #----------------------------------------------------------------------------
    # Display data on the terminal and write data to a file
    #----------------------------------------------------------------------------
    print("Financial Analysis")
    print("----------------------------------------")
    message="Total Months: {}\nTotal Profit Loss: {}\nAverage Change: {}\n" \
             "Greatest Increase in Projects: {} {}\nGreatest Decrease in Projects: {} {}"
    print(message.format(total_months,total_profit_loss,average_change,max_change_date,max_change,min_change_date, min_change))

    budget_file = open('budget_update.csv', 'w', newline='')
    budget_file.write("Financial Analysis" + "\n")
    budget_file.write("----------------------------------------" + "\n")
    budget_file.write(f"Total Months: {total_months}" + "\n")
    budget_file.write(f"Total Profit Loss: $ {p_total_profit_loss}" + " \n")
    budget_file.write(f"Average Revenue Change: ${p_average_change}" + "\n")
    budget_file.write(f"Greatest Increase in Revenue: {max_change_date} (${p_max_change})" + "\n")
    budget_file.write(f"Greatest Decrease in Revenue: {min_change_date} (${p_min_change})" + "\n") 