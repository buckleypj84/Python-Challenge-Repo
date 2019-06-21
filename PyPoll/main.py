# --------------------------------------------------------------------------------------------
# Date:     6/19/2019
# Pgm Name: main.py   
# Input:    (PyPoll/Resources/election_data.csv). 
# Desc:     Python script analyzes votes and calculates each of the following:
#           * The total number of votes cast
#           * A complete list of candidates who received votes
#           * The percentage of votes each candidate won
#           * The total number of votes each candidate won
#           * The winner of the election based on popular vote.
# Sample Output: (print the analysis to the terminal and export a text file with the results)
#   Election Results
#   -------------------------
#   Total Votes: 3521001     
#   -------------------------
#   Khan: 63.000% (2218231)     
#   Correy: 20.000% (704200)        
#   Li: 14.000% (492940)            
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan               
#   -------------------------`
#-------------------------------------------------------------------------------
import os
import csv
import pandas as pd
#get the current working directory
# currentDir = os.getcwd()
# print(currentDir)
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    # Initialize variables
    next(csvreader, None)

    candidate_vote_khan = 0
    candidate_vote_correy = 0
    candidate_vote_li = 0
    candidate_vote_otooley = 0
    total_votes = 0

    votes = []
    #--------------------------------------------------------------------
    # Read through each row of data and load votes[]
    # place number of votes for each candidate in variable
    #--------------------------------------------------------------------
    for row in csvreader:
        votes.append(row[2])             
        if row[2] == "Khan":
            name_khan  = "Khan"
            candidate_vote_khan +=  1
        elif row[2] == "Correy":
            name_correy = "Correy"
            candidate_vote_correy += 1
        elif row[2] == "Li":
            name_li = "Li"
            candidate_vote_li +=  1
        else:
            name_otooley = "OTooley"
            candidate_vote_otooley +=  1
        
    #--------------------------------------------------------------------
    # total number of votes cast
    #--------------------------------------------------------------------
    total_votes = len(votes) 

    #--------------------------------------------------------------------
    # calculate the percentage of votes for each candidate
    #--------------------------------------------------------------------
    khan_pct = (candidate_vote_khan / total_votes) * 100
    correy_pct = (candidate_vote_correy / total_votes) * 100
    li_pct = (candidate_vote_li / total_votes) * 100
    otooley_pct = (candidate_vote_otooley / total_votes) * 100  

    #--------------------------------------------------------------------
    # format the percentages
    #--------------------------------------------------------------------
    khan_pct = "{:1.2f}".format(khan_pct) + "%"
    correy_pct = "{:1.2f}".format(correy_pct) + "%"
    li_pct = "{:1.2f}".format(li_pct) + "%"
    otooley_pct = "{:1.2f}".format(otooley_pct) + "%"

    #--------------------------------------------------------------------
    # calculate the percentage of votes for each candidate
    #--------------------------------------------------------------------
    candidate_dicts = [{"CANDIDATE":name_khan,"VOTES":candidate_vote_khan},
                       {"CANDIDATE":name_correy,"VOTES":candidate_vote_correy},
                       {"CANDIDATE":name_li,"VOTES":candidate_vote_li},
                       {"CANDIDATE":name_otooley,"VOTES":candidate_vote_otooley},]

    df_candidates = pd.DataFrame(candidate_dicts)
 
    #count_votes = df_candidates["VOTES"].max()
    #--------------------------------------------------------------------
    # sort the DataFrame in descending to retrieve the largest 
    # number of votes cast for a candidate
    #  retrieve the name of the winning candidate using iloc
    #--------------------------------------------------------------------    
    sort_df = df_candidates.sort_values(["VOTES"])
    
    sort_df = sort_df.reset_index(drop=True)

    winner = sort_df.iloc[3, 0]
 
    #--------------------------------------------------------------------
    # Print the results to the terminal and write to a file
    #--------------------------------------------------------------------

    print("Election Results")
    print("----------------------------------------")
   
    message="Total Votes: {}\n\nKhan:        {}   {}\nCorrey:      {}   {}\n" \
             "Li:          {}   {}\nO'Tooley:     {}   {}\n"    
    print(message.format(total_votes, khan_pct,candidate_vote_khan,correy_pct,candidate_vote_correy,li_pct,candidate_vote_li,otooley_pct,candidate_vote_otooley))

    print("----------------------------------------")

    print(        "W I N N E R   "  + winner)

    vote_file = open('new_election_data.txt', 'w', newline='')
    vote_file.write("Election Results " +  "\n") 
    vote_file.write(f"----------------------------------------" + "\n")
    vote_file.write(f"Total Votes:{total_votes}" + "\n")
    vote_file.write(f"Khan: {khan_pct} {candidate_vote_khan}" +  "\n")
    vote_file.write(f"Correy: {correy_pct} {candidate_vote_correy}"  + "\n")
    vote_file.write(f"Li:{li_pct}  {candidate_vote_li}" + "\n")
    vote_file.write(f"O'Tooley:  {otooley_pct} {candidate_vote_otooley}" +  "\n") 
    vote_file.write(f"----------------------------------------" + "\n")
    vote_file.write(f"W I N N E R     {winner}")