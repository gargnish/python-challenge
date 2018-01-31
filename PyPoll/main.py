# This will allow us to create file paths across operating systems
import os
import csv
###################################################
#getting all the files data for single aggregation
#change filename here for new files, change myfiles to directory reference from this script
Result_file = 'PyPoll_result.txt'
file_directory = 'myfiles'
file1 = 'election_data_1.csv'
file2 = 'election_data_2.csv'
file_list = [os.path.join(file_directory,file1),os.path.join(file_directory, file2)]
###################################################
# set 0 for no header
v_header_line_index = 1
# defining 2d aggregation list
v_agg_2dlist = [[]]
v_agg_2dlist.pop(0)
v_total_votes = 0

for file in file_list:
    with open(file, newline="") as f1:
        v_counter = 0
        v_csv_cursor_2dlist = csv.reader(f1, delimiter=",")
        for v_csv_cursor_1dlist in v_csv_cursor_2dlist:
            if v_counter > v_header_line_index - 1 and v_csv_cursor_1dlist[1] != '' : #not interested in header record and empty strings
                present = False
                v_voter_id = v_csv_cursor_1dlist[0]
                v_county = v_csv_cursor_1dlist[1]
                v_candidate = v_csv_cursor_1dlist[2]
                v_total_votes += 1
                for v_agg_1dlist in v_agg_2dlist: #creating aggregation and unique candidate list
                    n1 = v_agg_2dlist.index(v_agg_1dlist)
                    if v_candidate == v_agg_1dlist[0]:
                        v_vote_count = 1 + v_agg_1dlist[1]
                        v_agg_2dlist.pop(n1)
                        v_agg_2dlist.append([v_candidate,v_vote_count])
                        present = True
                        break

                if  present == False:
                     v_agg_2dlist.append([v_candidate, 1])
            v_counter += 1

# sort list by number of votes
from operator import itemgetter
v_agg_sorted_2dlist= sorted(v_agg_2dlist, key=itemgetter(1))

v_result = ''
v_Result_blog = ' Election Results'
v_Result_blog += chr(10) + ' -------------------------'
v_Result_blog += chr(10) + ' Total Votes: '+str(v_total_votes)
v_Result_blog += chr(10) + ' -------------------------'
for v_agg_sorted_1dlist in v_agg_sorted_2dlist:
    v_result = v_result +' '+v_agg_sorted_1dlist[0]+': '+str(round(100*v_agg_sorted_1dlist[1]/v_total_votes,2))+'% ('+str(v_agg_sorted_1dlist[1])+')'+chr(10)
    #Last one will be winner as list is already sorted
    v_winner = v_agg_sorted_1dlist[0]
v_Result_blog += chr(10) + v_result.rstrip(chr(10))
v_Result_blog += chr(10) + ' -------------------------'
v_Result_blog += chr(10) + ' Winner: '+v_winner
v_Result_blog += chr(10) + ' -------------------------'

#printing result
print(v_Result_blog)

#creating result file
with open(Result_file, 'w', newline='') as f2:
    f2.write(v_Result_blog)