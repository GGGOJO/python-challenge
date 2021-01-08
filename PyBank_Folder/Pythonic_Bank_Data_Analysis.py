#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PyBank

# Import modules
import csv
import os

# Upload the starting file or the raw data into jupyter notebook
start_file = os.path.join('.', "Week 3", "Homework", "Resources", "budget_data.csv")
# Save the clean dataset for future analysis
final_file = os.path.join('.', "Week 3", "Homework", "Analysis", "budget_analysis.txt")


# In[2]:


# Create desired financial variables to count and store each line read
total_months = 0
total_amount = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]


# Python csv.reader function reads data one line of data at a time
# Create csv data into a list dictionaries
with open(start_file) as financial_data:
    reader = csv.reader(financial_data)

    # csv has a header. Read and skip the header row in the csv
    header = next(reader)
    #print(header)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    #print(first_row)
    total_months = total_months + 1

    total_amount = total_amount + int(first_row[1])
    prev_net = int(first_row[1])
    #print("Loop starts here")
    
    # loop through your data
    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_amount = total_amount + int(row[1])
        # print(total_amount)
        # DATA CHECK: The print should be $38382578, and it is. 

        # Track the new change between the current row and previous row of data. 
        # Then add it to the running list called net_change_list as well as
        # Store the associated month of that net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])
        #print (net_change_list)
        #print(month_of_change)
        # DATA CHECK: This should print out the values of the accummulated list that is being stored in these variables.


        # figure out which net_change had the greatest increase and decrease Column 1 of the data.
        # identify the month/year associated with that amount. Column 0 of the data.
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    # Calculate the Average Change
    # Could also try out another mathematical calc (last value - first value) / (num_of_rows-1) ?
    average_change = sum(net_change_list) / len(net_change_list)

    output = (
        f"\nFinancial Analysis\n"
        f"=========================\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_amount}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits {greatest_increase[0]}, (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n"

    )

    print(output)


# In[3]:


with open(final_file, "w") as financial_data:
    financial_data.write(output)


# In[ ]:





# In[ ]:




