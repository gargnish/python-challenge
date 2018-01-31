# Below can be done easily by using packages. But task is to use only basic skills
# This will allow us to create file paths across operating systems
import os
import csv

###################################################
# getting all the files data for single aggregation
# change filename here for new files, change myfiles to directory reference from this script
Result_file = 'PyBank_result.txt'
file_directory = 'myfiles'
file1 = 'budget_data_1.csv'
file2 = 'budget_data_2.csv'
file_list = [os.path.join(file_directory, file1), os.path.join(file_directory, file2)]
###################################################


# set 0 for no header
v_header_line_index = 1
# defining 2d aggregation list
v_agg_2dlist = [[]]
v_agg_2dlist.pop(0)
# Adding dict to get month conversion
My_month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

for file in file_list:
    with open(file, newline="") as f1:
        v_csv_cursor_2dlist = csv.reader(f1, delimiter=",")
        # not interested in header record
        for skip_count in range(v_header_line_index):
            next(v_csv_cursor_2dlist)
        for v_csv_cursor_1dlist in v_csv_cursor_2dlist:
            present = False
            # date fix ---converting to numeric date for sorting
            # using dict to get month to integer conversion
            # Intentionally did not use datetime package and  dateutil.parser as we have to perform this without using them
            v_date = v_csv_cursor_1dlist[0]
            v_date_list = v_date.split("-")
            if int(v_date_list[1]) < 100:  # if less that 100 year then adding 2000
                v_date_int = int(My_month_dict[v_date_list[0]]) + 100 * (int(v_date_list[1]) + 2000)
            else:
                v_date_int = int(My_month_dict[v_date_list[0]]) + 100 * int(v_date_list[1])
            # date fix end
            v_rev = int(v_csv_cursor_1dlist[1])
            for v_agg_1dlist in v_agg_2dlist:  # creating aggregation and unique dates list
                n1 = v_agg_2dlist.index(v_agg_1dlist)
                if v_date_int == v_agg_1dlist[0]:
                    v_rev = int(v_agg_1dlist[1]) + int(v_rev)
                    v_agg_2dlist.pop(n1)
                    v_agg_2dlist.append([v_date_int, v_rev])
                    present = True
                    break

            if present == False:
                v_agg_2dlist.append([v_date_int, v_rev])

# length of list is total months as it is aggregation
# import the package for sorting the list by month
v_total_month = len(v_agg_2dlist)
from operator import itemgetter

v_agg_sorted_2dlist = sorted(v_agg_2dlist, key=itemgetter(0))

# Initiating various variables
v_total_rev = 0
v_prev_rev = 0
v_rev = 0

v_min_change_in_rev = 0
v_max_change_in_rev = 0
v_sum_change_in_rev = 0
v_change_in_rev = 0

# Looping through the list to get pre rev and max, min
for v_agg_sorted_1dlist in v_agg_sorted_2dlist:
    n2 = v_agg_sorted_2dlist.index(v_agg_sorted_1dlist)
    v_prev_rev = v_rev
    v_prev_change_in_rev = v_change_in_rev
    # ------
    v_rev = v_agg_sorted_1dlist[1]
    v_month = v_agg_sorted_1dlist[0]
    v_change_in_rev = v_rev - v_prev_rev
    v_total_rev += v_rev
    # filtering out first record for previous change in revenues
    if n2 != 0:
        v_sum_change_in_rev += v_change_in_rev
        if v_min_change_in_rev > v_change_in_rev:
            v_min_change_in_rev = v_change_in_rev
            v_min_change_in_rev_month = v_month
        if v_max_change_in_rev < v_change_in_rev:
            v_max_change_in_rev = v_change_in_rev
            v_max_change_in_rev_month = v_month

# parsing yearmonth of min, max months to string values
v_str_min_change_in_rev_month = str(v_min_change_in_rev_month / 100)
v_str_max_change_in_rev_month = str(v_max_change_in_rev_month / 100)

v_min_list = v_str_min_change_in_rev_month.split(".")
v_max_list = v_str_max_change_in_rev_month.split(".")

# using reverse dict to get string months
My_month_reverse_dict = dict(map(reversed, My_month_dict.items()))

# concat date and rev for max and min
v_min = My_month_reverse_dict[v_min_list[1]] + '-' + str(int(v_min_list[0]) - 2000) + '($' + str(
    v_min_change_in_rev) + ')'
v_max = My_month_reverse_dict[v_max_list[1]] + '-' + str(int(v_max_list[0]) - 2000) + '($' + str(
    v_max_change_in_rev) + ')'

v_Result_blog = '  Financial Analysis'
v_Result_blog += chr(10) + '  ----------------------------'
v_Result_blog += chr(10) + '  Total Months: ' + str(v_total_month)
v_Result_blog += chr(10) + '  Total Revenue: $' + str(v_total_rev)
v_Result_blog += chr(10) + '  Average Revenue Change: $' + str(
    round(v_sum_change_in_rev / v_total_month))
v_Result_blog += chr(10) + '  Greatest Increase in Revenue: ' + v_max
v_Result_blog += chr(10) + '  Greatest Decrease in Revenue: ' + v_min

#Printing results
print(v_Result_blog)

# creating result file
with open(Result_file, 'w', newline='') as f2:
    f2.write(v_Result_blog)
