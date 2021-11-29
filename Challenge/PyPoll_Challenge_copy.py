# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# import dependencies
import csv
import os

# load the election_results.csv
file_to_load = '..\Resources\election_results.csv'

# load the election_analysis.txt
file_to_save = '..\Analysis\election_analysis_challenge.txt'

# determine the total votes of all counties
total_votes = 0

# determine the counties available.
county_options = []

# determine the voter turnout for each county
county_votes = {}
#
county_name_Highest_Turnout = ''
Highest_Turnout_votes = 0
county_highestTurnout_percentage = 0

# Open the file in the read mode
with open(file_to_load, "r") as election_results:
    # read the file
    reader = csv.reader(election_results)
    # Skip the header
    header = next(reader)
    # print the header 
    #print(header)   
    # Loop through the csv file and capture the total votes count
    for row in reader:
        #    
        total_votes += 1
        #
        county = row[1]
        #
        if county not in county_options:
            #   
            county_options.append(county)
            #
            county_votes[county] = 0
            #
        county_votes[county] += 1

with open(file_to_save, 'w') as text_file:

    election_output = (
        f'Election Results\n'
        f'----------------------\n'
        f'total votes: {total_votes:,}\n'
        f'----------------------\n'
    )
    #
    print(election_output, end='')
    #
    text_file.write(election_output)
    #
    for county in county_votes:
        #
        vote = county_votes[county]
        #
        percentage_votes = float(vote) / float(total_votes) * 100
        #
        
        #
        county_results = (f'{county} county received {percentage_votes:.2f} % ({vote:,}) votes\n')
        #
        print(county_results)
        #
        text_file.write(county_results)
        #
        if (vote > Highest_Turnout_votes) and (percentage_votes > county_highestTurnout_percentage):
            #
            Highest_Turnout_votes = vote
            #
            county_name_Highest_Turnout = county
            # 
            county_highestTurnout_percentage = percentage_votes
    # Print the county with the highest turnout results to the terminal.
    county_withTheHighest_summary = (
        f"-------------------------\n"
        f"County with the highest turnout: {county_name_Highest_Turnout}\n"
        f"Highest turnout vote count: {Highest_Turnout_votes:,}\n"
        f"Percentage of the county with the highest turnout: {county_highestTurnout_percentage:.2f}%\n"
        f"-------------------------\n")
    print(county_withTheHighest_summary)
    # Save the winning candidate's results to the text file.
    text_file.write(county_withTheHighest_summary)