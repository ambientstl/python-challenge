import os
import csv

#set path to csv file
pyBank_csv = os.path.join('budget_data.csv')

#read the csv file
with open(pyBank_csv, 'r') as pyBankData:
    csvreader = csv.reader(pyBankData, delimiter=",")

    #skip the header
    next(csvreader, None)

    #set variables to 0 for baseline
    totalProfit = 0
    totalMonths = 0
    greatIncrease = 0
    greatDecrease = 0

    #set previousRow to zero as baseline
    ##must pop 1st value in monthlyChanges (1st month - baseline)
    previousRow = 0

    #set empty list for monthly change values
    monthlyChanges = []

    #loop through rows
    for row in csvreader:

        #running tally of Months
        totalMonths += 1

        #add to totalProfit
        totalProfit += int(row[1])

        #check for greatest increase or decrease
        if int(row[1]) > greatIncrease:
            greatIncrease = int(row[1])
        if int(row[1]) < greatDecrease:
            greatDecrease = int(row[1])

        #set current row as thisRow  
        thisRow = int(row[1])

        #calculate difference month-to-month (row-to-row)
        monthlyChange = thisRow - previousRow

        #adds monthly difference to monthlyChanges list
        monthlyChanges.append(monthlyChange)
        
        #set current row as previousRow for next iteration
        previousRow = int(row[1])



    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total Profit: ${totalProfit}")
    print(f"Greatest Monthly Profit: ${greatIncrease}")
    print(f"Greatest Monthly Loss: -${abs(greatDecrease)}")

    #removes first value from monthlyChanges list (1st month - 0)
    monthlyChanges.pop(0)

    #calculates average monthly change 
    avgMonthChange = sum(monthlyChanges) / len(monthlyChanges)

    
    if avgMonthChange < 0:
        print(f"Average Monthly Change: -${abs(avgMonthChange)}")
    else:
        print(f"Average Monthly Change: ${avgMonthChange}")


    

        


