# Election_Analysis
# Project Analysis
The following tasks needed to be completed when analyzing the tabulated results of the U.S. congressional precinct election in Colorado:
  1. Calculate and report the number of votes cast.
  2. Create a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
  
# Resources
  * Data Source: election_results.csv
  * Software: Python 3.9.2, Visual Studio Code, 1.71.2
 # Summary
  * There were 369,711 votes cast in this election.
  * The Candidates Were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
 * The Candidate results were:
    *  Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
    *  Diana DeGette received 73.8% of the vote with 272,892 votes.
    *  Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
* The Winner of the election was:
  *   Candidate Diana DeGette who received 73.8% of the vote and 272,892 votes.
# Overview of Election Audit
The purpose of this Election Audit is to define the voting results by county. In this audit I have defined the number of votes per county, the percentage of votes from each county, and the county with the highest turnout.
  * 369,711 votes were cast in this election
  * County Votes:
  
    * Jefferson: 10.5% (38,855)
    
    * Denver: 82.8% (306,055)
    
    * Arapahoe: 6.7% (24,801)
    
* Denver was the county with the highest number of votes.

See the full election results below:

<img width="479" alt="Screen Shot 2022-10-27 at 11 37 47 AM" src="https://user-images.githubusercontent.com/113859036/198334967-91a44fb2-3322-42da-a8a3-9292817d0739.png">


# Election-Audit Summary
This script can be used for any election with select modifications depending on what data needs to be defined. For example, the code can be altered to pull information from the csv file from different rows seen in the code below.
<img width="366" alt="Screen Shot 2022-10-27 at 11 34 56 AM" src="https://user-images.githubusercontent.com/113859036/198334302-fa6165b6-bbf9-4905-8f53-768b7da10c74.png">
Another reason to alter the code depending on the data set is if you want to find a more precise voting percentage. If the election results are very close, you will need to extend the decimal place for a more precise number. This is the code you will need to alter to extend the decimal points on percentages.
<img width="490" alt="Screen Shot 2022-10-27 at 11 45 38 AM" src="https://user-images.githubusercontent.com/113859036/198336918-79469b65-8d92-4d82-ab60-6fa79122bdca.png">
The Vote Percentage ({vote_percentage:.1f) code needs to be altered at the end before the 'f' to extend the decimal place.
