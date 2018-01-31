# This will allow us to create file paths across operating systems
import os
import csv
###################################################
#getting all the files data for single aggregation
#change filename here for new files, change myfiles to directory reference from this script
Result_file = 'converted_employee_data.csv'
file_directory = 'myfiles'
file1 = 'employee_data1.csv'
file2 = 'employee_data2.csv'
file_list = [os.path.join(file_directory,file1),os.path.join(file_directory, file2)]
###################################################

# set 0 for no header
v_header_line_index = 1
# defining 2d aggregation list
v_target_2dlist = [[]]
v_target_2dlist.pop(0)

# Adding dict to get state conversion
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


#getting all the files data and converting
for file in file_list:
    with open(file, newline="") as f1:
        v_counter = 0
        v_csv_cursor_2dlist = csv.reader(f1, delimiter=",")
        for v_csv_cursor_1dlist in v_csv_cursor_2dlist:
            if v_counter > v_header_line_index - 1 and v_csv_cursor_1dlist[1] != '' : #not interested in header record and empty strings
                present = False
                v_EmpID = v_csv_cursor_1dlist[0]
                v_name = v_csv_cursor_1dlist[1]
                v_DOB = v_csv_cursor_1dlist[2]
                v_SSN = v_csv_cursor_1dlist[3]
                v_State = v_csv_cursor_1dlist[4]
                # name fix
                v_name_list = v_name.split(" ")
                v_fix_FirstName = v_name_list[0]
                v_fix_LastName = v_name_list[1]
                # DOB fix
                v_dob_list = v_DOB.split("-")
                v_fix_dob_yyyy = v_dob_list[0]
                v_fix_dob_mm = v_dob_list[1]
                v_fix_dob_dd = v_dob_list[2]
                v_fix_dob = v_fix_dob_dd +'/'+ v_fix_dob_mm +'/' +v_fix_dob_yyyy
                # SSN fix
                v_ssn_list = v_SSN.split("-")
                v_fix_ssn = '***-**-'+v_ssn_list[2]
                # state fix
                # using dict to get conversion
                while True:
                    try:
                        v_fix_state = us_state_abbrev[v_State]
                        break
                    except:
                        v_fix_state = ''
                        break
                v_target_2dlist.append([v_EmpID, v_fix_FirstName, v_fix_LastName,v_fix_dob,v_fix_ssn,v_fix_state])
            v_counter = v_counter + 1

# writing to file
# used newline to remove extra blank lines between each record
with open(Result_file, 'w', newline='') as f2:
    # creating header record
    f2.write('Emp ID,First Name,Last Name,DOB,SSN,State'+chr(10))
    wr = csv.writer(f2)
    for v_target_1dlist in v_target_2dlist:
        wr.writerow(v_target_1dlist)



