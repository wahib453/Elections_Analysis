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
with open(file_to_load) as election_data:
     # Print the file
     print(election_data)

##########################################################################################################################################################################################################################################
# Section 3.4.3: Write to Files with Python

import csv
import os
# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('Analysis', 'election_analysis.txt')
# using the open() function with the "w" mode we will write data to the file.
open(file_to_save, 'w')