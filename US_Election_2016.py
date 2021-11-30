# import dependencies
import csv
import os

# load the 2018 U.S. Election file  
US_Election2016 = "primary_results.csv"

US_Election2016_Result = os.path.join("AnalysisResults","USelection2016.txt")

# Initialize total votes
total_votes = 0
# Open the file in read mode and store as US_Primary
with open(US_Election2016, "r") as US_Primary:
    # read the file as store it as primary
    reader = csv.reader(US_Primary)
    # skip the header
    header = next(reader)
    # print the header
    #print(header)

    # obtain the total votes
    for row in reader:
        total_votes += 1
    

with open(US_Election2016_Result, "w") as text_file:
    Election_result = (
        f'2016 U.S. Election Result Summary\n'
        f'--------------------------\n'
        f'total votes: {total_votes:,}\n'
        f'---------------------------\n'
    )
    print(Election_result, end="")
    text_file.write(Election_result)
