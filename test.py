#Load dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources','election_results.csv')

#Assign a variable to save the file to a path.
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

#Set total_votes to 0
total_votes = 0

#Create a list of candidates.
candidate_options = []

#Create an empty dictionary.
candidate_votes = {}

#Create the variables for the winning candidate.
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open the election results and read that file.
with open(file_to_load) as election_data:
    
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    print(type(file_reader))
    print(file_reader)
    #Read the header row.
    # headers = next(file_reader)
    # for header in headers:
    #     #next_headers = next(header)
    #     print(header)
    #     print(type(header))

#     #Print each row in the CSV file.
#     for row in file_reader:
        
#         #Add to the total vote count
#         total_votes += 1

#         #Get the candidate name from each row.
#         candidate_name = row[2]

#         #Check to see if the candidate_name is in the candidate_options list.
#         if candidate_name not in candidate_options:
        
#             #Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#             #Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#         #Add a vote to that candidate's count.
#         candidate_votes[candidate_name] += 1

# # #Save the results to our text file.
# # with open(file_to_save,'w') as txt_file:

# #     #Create the string for the election results.
# #     election_results = (
# #         f'\nElection Results\n'
# #         f'------------------------\n'
# #         f'Total votes: {total_votes:,}\n'
# #         f'------------------------\n')
    
# #     #Print out the election results to the terminal.
# #     print(election_results, end = '')

# #     #Save the results to the txt file. 
# #     txt_file.write(election_results)

# #     #Loop through the candidate_votes dictionary for the candidate's name.
# #     for candidate_name in candidate_votes:
                
# #         #Set the votes equal to the candidate's vote value of the candidate name key.
# #         votes = candidate_votes[candidate_name]

# #         #Calculate the vote percentage and transform integers to float.
# #         vote_percentage = float(votes)/float(total_votes) * 100
        
# #         #Create each candidate's name, vote count and percentage of votes.
# #         candidate_results = (f'{candidate_name}: {vote_percentage:1f}% ({votes:,})\n')
        
# #         #Print these results to the terminal.
# #         print(candidate_results)

# #         #Write these results to the txt file.
# #         txt_file.write(candidate_results)

# #         #Determine if the votes are greater than the winning count and the percentage is greater than the winning percentage.
# #         if (votes > winning_count) and (vote_percentage > winning_percentage):
                
# #             #If both of these are true, set the votes, vote percentage and candidate to the values indicated. 
# #             winning_count = votes
# #             winning_percentage = vote_percentage
# #             winning_candidate = candidate_name
    
# #     #Create the string that holds the winners information.
# #     winning_candidate_summary = (
# #         f'---------------------------\n'
# #         f'Winner: {winning_candidate}\n'
# #         f'Winning Vote Count: {winning_count:,}\n'
# #         f'Winning Percentage: {winning_percentage:.1f}%\n'
# #         f'---------------------------\n')
    
# #     #Print the results to the terminal.
# #     print(winning_candidate_summary)

# #     #Write the winning results to the txt file.
# #     txt_file.write(winning_candidate_summary)