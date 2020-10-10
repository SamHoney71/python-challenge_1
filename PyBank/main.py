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
    profit_loss = 0

    # loop to calculate count of months, net total of profit loss 
    # and collect data for lists
    for row in csvreader:
  
        if(previous_revenue == 0):
            previous_revenue = int(row[1])
        else:
             Profit_month = int(row[1]) - previous_revenue
             profit_Monthly = str(row[0])
    
    total_month = total_month + 1
    total_revenue += int(row[1])
   
    # Code tests
    # print(f'{total_month}')
    # print(f'{total_revenue}')
    # print(f'{Profit_month}')
    # print(f'{profit_Monthly}')

#average of the changes in "Profit/loss
#greatest increase in profits (date and amount)
#greatest decrease in losses (date and amount

    def budget_description(budget_data):
        Profit_month = []
        profit_Monthly = []





# Financial Analysis Display
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


#both print the analysis to the terminal and export a text file