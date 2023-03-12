import csv

file = "PyBank/Resources/budget_data.csv"

month_count = 0
net_amount = 0

greatest_increase = -100
increase_date = ""
greatest_decrease = 100
decrease_date = ""
changes = []

with open(file) as csv_file:
    budget_data = csv.reader(csv_file, delimiter=",")

    header = next(budget_data)
    
    prev_amount = 0

    for row in budget_data:
        amount = int(row[1])
        net_amount+= amount
        month_count+= 1

        change = amount - prev_amount
        if change > greatest_increase:
            greatest_increase = change
            increase_date = row[0]
        
        if change < greatest_decrease:
            greatest_decrease = change
            decrease_date = row[0]

        changes.append(change)

        prev_amount = amount

print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(net_amount))
print("Average Change: $" + str(round(sum(changes)/len(changes),2)))
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

write_path = "PyBank/analysis/budget_result.txt"
with open(write_path, 'w') as f: 
    f.write("Financial Analysis\n")
    f.write("--------------------\n")
    f.write("Total Months: " + str(month_count))
    f.write("\nTotal: $" + str(net_amount))
    f.write("\nAverage Change: $" + str(round(sum(changes)/len(changes),2)))
    f.write(f"\nGreatest Increase in Profits: {increase_date} (${greatest_increase})")
    f.write(f"\nGreatest Decrease in Profits: {decrease_date} (${greatest_decrease})")