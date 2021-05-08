## Project Overview - Election Audit

Based on a directive from a local Board of Elections, an audit was completed uitilizing election data. The following tasks were completed:

1. Calculation of the total number of votes cast.
2. Calculation of the number of votes cast by each county.
3. Calculation of the percentage of votes represented by each county.
4. Determination of the county with the largest turnout and vote count.
5. Getting a complete list of candidates who received at least 1 vote.
6. Calculation of the total number of votes each candidate received.
7. Calculation of the percentage of votes that each candidate won.
8. Determination of the winner of the election based on popular vote.

## Resources Utilized
* Data Source (Resources Folder): election_results.csv
* Audit Results (Analysis Folder): election_analysis.txt
* Software Utilized: Python 3.7.6, Visual Studio Code 1.56.0

## Election Audit Results

* How many votes were cast in this congressional election?
    * Utilizing the following code:
    ```
   with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    for row in reader:
    total_votes = total_votes + 1
    ```
    We utilized a for loop to go through the entire CSV datasheet to gather the total number of votes. From this code, we determined the total number of votes casted in this election to be: **369,711 votes**

* Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    * Utilizing the same for loop (and an if statement with conditional), the counties represented were determined and the individual count of the votes represented for each county (in a dictionary) were calculated:
    ```
     if county_name not in county_list:

            # Add the existing county to the list of counties.
            county_list.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1
    ```
    After this, the results are presented both within the terminal (print) and within the election_analysis txt file (txt_file.write(election_results))
    
    __County Votes:__
    
    Jefferson: 10.5% (38,855 votes)
    
    Denver: 82.8% (306,055 votes)
    
    Arapahoe: 6.7% (24,801 votes)

* Which county had the largest number of votes?
    * Based on the information gathered, the following county has the largest amount of votes:
    
    __Denver: 306,055 votes__

* Breakdown of the number of votes and the percentage of the total votes each candidate received.

    * Utilizing a for loop and if statement (with conditional), we went through the CSV file to determine the complete list of candidates and their vote count:
    ```
    for row in reader:
        # Get the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
    
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    ```
    This yielded the following:
    
    List of candidates:
    
    Charles Casper Stockham received 85,213 number of votes.
    
    Diana DeGette received 272,892 number of votes.
    
    Raymon Anthony Doane received 11,606 number of votes.
    
    From here, we were able to determine the percentage of votes each candidate received utilizing a for loop:
    
    ```
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
    ```
    
    And these results were then output here:
    
    Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    
    Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    
    Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
    
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    * Based on the information provided in the last question, we can determine the winnder of the election to be:
    
        * __Diana DeGette who received 73.8% of the vote and 272,892 number of votes.__


## Election Audit Summary

As demonstrated within this audit, Python is a powerful tool that can be utilized to conduct an audit of a local election and do it quicker and more efficiently than utilizing Microsoft Excel. Now that the script is written, the audit can be completed and the results printed out efficiently as a txt file that can be quickly and easily referenced. Taking into consideration the amount of time that would be required within Excel, utilizing the Python script here could automate this process thus saving time and money in the future. For future projcts, there would be two modifications that could be considered:

* Modification for file paths:

In the original script, the Election results are gathered from a CSV file contained within a "Resources" folder where the script is held and an Analysis folder where the results are printed: 

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```

Future projects would need to either ensure that future election results are saved as CSV files with the name "election_results.csv" within a folder titled "Resources" or the script could be modified to point to another file path or file name. 

Similarly, for the ouput of results, an Analysis Folder will need to be present or another file path where the results should be printed will need to be modified within the script. 

* Modification for outputting results:

Another consideration for future results would be to focus on those individuals who may not have as much experience with the terminal or for consideration to have one set of data present. In the original script, the results from the analyis are output into the terminal:

``` 
# Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
```

For this, a modification could be made to remove the line print(election_results, end = "") and simply have the results output to the txt file of the analysis. Doing so could eliminate two sets of data that have the final audit results (and thus eliminate chances of misinterpretation or manipulation in the future). Should it be determined that the printing to the terminal would be absolutely necessary, adding in the print() statement would be easy to do. 

* Modification for multiple columns or changing columns:

The current CSV file only has 3 columns making indexing of specific items fairly easy:

```
candidate_name = row[2]
```

Therefore, in anticipation of datasets with many columns, it could be useful to consider utilizing the headers created in the script:

```
headers = next(file_reader)
```

As a point of reference to index the data itself going forward for future iterations of the Python script. As mentioned however, it would depend on the exact number of columns that are present within other datasets that are present to make it worthwhile to edit the script itself. However, it could be a modification that could be considered if subsequent datasets do not match the format of the one currently utilized. 
