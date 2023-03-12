import csv
import os

file = "C:\Users\Chris\Documents\SCS\python-challenge\PyBank\Resources\\budget_data.csv"

with open(file) as csv_file:
    budget_data = csv.reader(csv_file, delimiter=",")

    header = next(budget_data)
    
    month_count = 0
    for row in budget_data:
        month_count+= 1
    
    print("Total Months: " + str(month_count))
