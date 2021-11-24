##################################################################################################################################################################################################################################################
# Section 3.4.2: Open and Read Files using Python
# Open and close a file using the open() and close()
# assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

# open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.


# Close the file.
election_data.close()

# Alternatively, open and close a file using with() statement
# Open the election results and read the file
file_to_load = '.\Resources\election_results.csv'

with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
     
# Indirect way of accessing a file
import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')

# open the election results and read the file.
with open(file_to_load, 'r') as election_data:
     # Print the file
     print(election_data)

##########################################################################################################################################################################################################################################
# Section 3.4.3: Write to Files with Python

import csv
import os
# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('Analysis', 'election_analysis.txt')
# using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, 'w')

# write some data to the file
outfile.write('Hello world.\n')

# Close the file
outfile.close()

# Alternatively, using "with" statement 
import csv
import os

#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# using the with statement open the file as a text file.
with open(file_to_save, 'w') as outfile:
     # write some data to the file
     outfile.write('Counties in the Election\n')
     outfile.write('----------------------------\n')
     outfile.write('Arapahoes\nDenver\nJefferson\n')

########################################################################################################################################################

# Section 3.4.4: Read the Election Results
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Add the total vote counter before the with open() statement and initialize it with zero.
total_votes = 0

# Candidate options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    # print the header row.
    headers = next(file_reader)
    #print(headers)

    # print each row in the csv file.
    for row in file_reader:
         # print(row)
         # 2. Add to the total vote count.
         total_votes += 1
         # Print the candidate name from each row.
         candidate_name = row[2]
         # If the candidate does not match any existing candidate...
         if candidate_name not in candidate_options:
              # Add it to the list of candidates.
              candidate_options.append(candidate_name)

# 3. print the total votes
print(total_votes)
# Print the candidate options
print(candidate_options)


##############################################################################################################################################################################################################################################
# Section 3.5.2: Get the candidats in the Election
