import os
import csv

csvpath = os.path.join("~","UCSDSAN201904DATA2","02-Homework","03-Python","Instructions","PyBank", "Resources", "budget_data.csv")

with open(csvpath, newline="") as count_file:
    csv_reader = csv.reader(count_file, delimiter="")
    for row in csv_reader:
        count += 1

        print(row)

    revenue += int(row[1])
    average_change = (revenue/count)
    greatest_increase = max(row[1])
    greatest_decrease = min(row[1])

    
print(f"Total Months: {count}")
print(f"Total Revenue: ${revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: ${greatest_increase}")
print(f"Greatest Decrease: ${greatest_decrease}")

#Export to CSV File

analysis_output = os.path.join("analysis.csv")
with open(analysis_output, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([f"Total Months: {count}"])
        csvwriter.writerow([f"Total Revenue: ${evenue}"])
        csvwriter.writerow([f"Average Change: ${average_change}"])
        csvwriter.writerow([f"Greatest Increase: ${greatest_increase}"])
        csvwriter.writerow([f"Greatest Decrease: ${greatest_decrease}"])

