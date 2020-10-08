#PyBank Homework Assignment - two columns - Date & Profit/Loss

#Read budget_data.csv file
import os
import csv


# Path to collect data from the Resoures folder
budget_csv = os.path.join(".","Resources","budget_data.csv")

# Define the function and have it accept the "Budget Data" as its sole parameter
def print_analysis(budget_data):
    date = str(budget_data[0])
    revenue = int(budget_data[0]

# Calculate total number of months
    total_months = len(date)

print(f"Total Months equals {total_months}")


# with open(budget_csv) as csv_file:
#     csv_reader=csv.reader(csv_file, delimiter=",")
   
#     csv_header = next(csv_file)
#     print(f"Header: {csv_header}")

    # for row in csv_reader:
    #     print(row)

# # total months
#     total_months = len(date)
#     print(f"int({total_months})")


# Reading using CSV module
# with open('budget_data.csv', ) as csvfile:
#     budgetreader = csv.reader(budget_data.csv, delimiter = ",")
#     for row in budgetreader:
#         print(','.join(row))



# with open(budget_csv) as csvfile:
#     csvbudget = csv.reader(budget_csv, delimiter=',')
#     print(csvbudget)




# with open(budget_csv) as csvfile:
#     csvbudget = csv.reader(budget_data, delimiter=',')
#     budgetheader = next(cvsbudget)
#     print(f"Budget Header: {budgetheader}")

#     for row in csvbudget:
#         print(row)

# print(str(budget_csv[1]))
#     # Define the function and have it accept the budget_data as its sole parameter
# def print_budget_calculations(budget_csv):
#     # For readability, assign values
#     date = str(budget_data[0])
#     profit_loss = double(budget_data[1])
         
#     print(date)




#net total ammount of "Profit/Loss"

#average of the changes in "Profit/loss


#greatest increase in profits (date and amount)


#greatest decrease in losses (date and amount




# Financial Analysis Display
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


#both print the analysis to the terminal and export a text file