import os 
import csv
csvpath= os.path.join("Resources", "budget_data.csv")
analysis_outcome= os.path.join("Analysis", "budget_analysis.txt")


month_counter= 0
month_list= []
net_change=[]
greatest_inc=["", 0]
greatest_dec=["",9999999999999]
total= 0


with open(csvpath) as data:
    reader= csv.reader(data)
    header= next(reader)
    first_row= next(reader)
    month_counter += 1
    total += int (first_row[1])
    pre_net= int (first_row[1])


    for row in reader:
        month_counter+= 1
        total += int (row[1])
        net_change_value= int (row[1])-int (pre_net)
        net_change.append(net_change_value)
        month_list.append(row[0])
        pre_net= row[1]
        

        if net_change_value> greatest_inc[1]:
            greatest_inc[1]= net_change_value
            greatest_inc[0]= row[0]
        if net_change_value< greatest_dec[1]:
            greatest_dec[1]= net_change_value
            greatest_dec[0]= row[0]

average_change= sum(net_change)/ len(net_change)


results = f"""
Financial Analysis
----------------------------
Total Months: {month_counter}
Total: ${total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})
Greatest Decrease in Profits:  {greatest_dec[0]} (${greatest_dec[1]})
"""
print(results)
with open (analysis_outcome, "w") as file:
    file.write(results)

