#PyBank Homework Assignment - two columns - Date & Profit/Loss

#Read budget_data.csv file
import os
import csv

# Path to collect data from the Resoures folder
 
budget_csv = os.path.join(".","Resources","budget_data.csv")
 
with open(budget_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    # set list to collect month over month profit & loss & month   
    Profit_month = []
    profit_Monthly = []

    # skip first header & set foundation
    row = next(csvreader, None)
    total_revenue = 0
    total_month = 0
    previous_revenue = 0
    monthly_profit_loss = 0

    # loop to calculate count of months, net total of profit loss 
    # and collect data for lists
    for row in csvreader:
  
        if(previous_revenue == 0):
            previous_revenue = int(row[1])
            
        else:
             Profit_month = int(row[1]) - previous_revenue
             profit_Monthly = str(row[0])
             monthly_profit_loss += Profit_month
             
            # test to see if lists are populated
            # print(f'{profit_Monthly}')
            # print(f'{Profit_month}')
    # test 
    # print(f'{monthly_profit_loss}')
    
        total_month = total_month + 1
        total_revenue += int(row[1])
          

#average of the changes in "Profit/loss
    length =  total_month - 1
    print(length)
    average_change = monthly_profit_loss/length
    print(average_change)

#greatest increase in profits (date and amount)
#greatest decrease in losses (date and amount
# min_monthly = min(profit_Monthly)
# print(min_monthly)
# max_monthly = max(profit_Monthly)
# print(max_monthly)


# Code tests
    print(f'{total_month}')
    print(f'{total_revenue}')



# Financial Analysis Display
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


#both print the analysis to the terminal and export a text file