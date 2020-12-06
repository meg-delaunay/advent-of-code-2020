import csv
import json
import os
import math
import sys

group_answers_1 = []
group_answers_2 = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    group_answer_part_1 = ''
    group_answer_part_2 = ''
    num_in_group = 0

    for row in input_reader:
        if row == []:
            group_answers_1.append(group_answer_part_1)
            group_answer_part_1 = ''

            group_answers_2.append({'string':group_answer_part_2, 'size':num_in_group})
            group_answer_part_2 = ''
            num_in_group = 0
            continue
        
        # part 1 is count uniques 
        for letter in row[0]:
            if letter not in group_answer_part_1:
                group_answer_part_1 += letter

        # part 2 is count where all answer
        group_answer_part_2 += row[0]
        num_in_group += 1
    
    group_answers_1.append(group_answer_part_1)
    group_answers_2.append({'string':group_answer_part_2, 'size':num_in_group})

total = 0
for a in group_answers_1:
    total += len(a)
print(total)


total_part_2 = 0
for group in group_answers_2:
    size = group['size']
    answers = group['string']
    sort = ''.join(sorted(answers))

    sub_start = 0
    num_all = 0

    for letter in sort:
        cnt = sort.count(letter, sub_start)
        sub_start += cnt
        if cnt == size:
            num_all += 1
    total_part_2 += num_all



print(total_part_2)