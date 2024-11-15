# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
months = []
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        single_row_first_element = row[1]
        single_row_zero_element = row[0]

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(single_row_first_element)


        # Track the net change
        net_change = int(single_row_first_element) - previous_net
        previous_net = int(single_row_first_element)
        net_change_list.append(net_change)
        months.append(single_row_zero_element)

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase_profit = max(net_change_list)
        greatest_increase_month = months[net_change_list.index(greatest_increase_profit)]

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease_losses = min(net_change_list)
        greatest_decrease_month = months[net_change_list.index(greatest_decrease_losses)]


# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
print ("Financial Analysis")
print ("----------------------------------------")
print (f"Toal Months: {total_months}")
print (f"Total: ${total_net}")
print (f"Average Change: ${average_net_change:.2f}")
print(F"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})")
print(F"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_losses})")

# Print the output
print(file_to_output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write

