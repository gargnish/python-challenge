# This will allow us to create file paths across operating systems
import os
import re
###################################################
#change filename here for new files, change myfiles to directory reference from this script
file_directory = 'myfiles'
file1 = 'paragraph_1.txt' # Replce here with other file paragraph_2.txt
file = os.path.join(file_directory,file1)
###################################################
Result_file = 'Result_'+file1
# defining terminators
v_sentence_terminator = "\n|\."
v_word_terminator = "[^a-zA-Z]"
v_letter_search = "[a-zA-Z]"
###################################################

# Reading as one blog
with open(file, 'r') as f1:
    v_paaragraph_string = f1.read()
# Initializing variables
v_word_count = 0
v_sentence_count = 0
v_letter_count_per_word = 0
v_sentence_length = 0
v_total_letter_count = 0
v_sentence_count = 0

v_sentence_list = re.split(v_sentence_terminator, v_paaragraph_string)
for v_sentence_string in v_sentence_list:
    if len(v_sentence_string) != 0:
        v_sentence_count += 1
        v_word_list = re.split(v_word_terminator, v_sentence_string)
        for v_word_string in v_word_list:
            if len(v_word_string) != 0:
                v_letter_list = re.split(v_letter_search, v_word_string)
                v_word_count += 1
                v_total_letter_count += len(v_letter_list) -1


v_letter_count_per_word =round(v_total_letter_count/v_word_count,11)
v_sentence_length = round(v_word_count/v_sentence_count,11)

# Just for troubleshooting
#print('Total letter count: ' + str(v_total_letter_count))

v_Result_blog =  'Paragraph Analysis'
v_Result_blog += chr(10) + '-----------------'
v_Result_blog += chr(10) + 'Approximate Word Count: ' + str(v_word_count)
v_Result_blog += chr(10) + 'Approximate Sentence Count: ' + str(v_sentence_count)
v_Result_blog += chr(10) + 'Average Letter Count: ' + str(v_letter_count_per_word)
v_Result_blog += chr(10) + 'Average Sentence Length: ' + str(v_sentence_length)

#printing result
print(v_Result_blog)

#creating result file
with open(Result_file, 'w', newline='') as f2:
    f2.write(v_Result_blog)
