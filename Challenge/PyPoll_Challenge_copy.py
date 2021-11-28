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
percentage_votes = 0

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
    print(election_output, end='')
    text_file.write(election_output)

        