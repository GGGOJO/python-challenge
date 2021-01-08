#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Figure out the path with the data file
import os
print(os.getcwd())


# In[2]:


# PyPoll
# import other module
import csv

# Upload the starting file or the raw data into jupyter notebook
start_file = os.path.join('..', "..", "Homework", "Resources", "election_data.csv")
# Save the clean dataset for future analysis
final_file = os.path.join('..', "..", "Homework", "Analysis", "election_analysis.txt")


# In[3]:


# Create polling variables to count and store each line being read
# Total Vote Counter
# Candidate Options and Vote Counter
# Winning Candidate and Winning Count Tracker
total_votes = 0
candidate_votes = {}
winning_candidate = None
winning_count = 0

# Read the csv and convert it into a list
with open(start_file) as election_data:
    reader = csv.reader(election_data)

    # Read the header in the raw data
    header = next(reader)

    # Begin the first loop (Part 1: Election Results)
    for row in reader:

        # Add to total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate,
        # then add that candidate in the list. It's a new candidate!
        if candidate_name not in candidate_votes:
            # begin tracking that candidate voter count
            candidate_votes[candidate_name] = 0

        # counts the votes for the candidate
        candidate_votes[candidate_name] += 1

with open(final_file, "w") as txt_file:
    # print the final vote count

    election_results = (
        f"\n\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------\n"
    )
    print(election_results, end="")

    # Save the final vote count to text file
    txt_file.write(election_results)

    # Second loop through the counts (Part II: Find out the Winner)
    for candidate in candidate_votes:

        # Retieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percent = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # print each candidate's voter count and percentage to terminal
        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"

        print(voter_output, end="")

        txt_file.write(voter_output)

    # Print the winning candidates
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate name to text file
    txt_file.write(winning_candidate_summary)


# In[ ]:




