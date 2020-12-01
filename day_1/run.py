import csv
import json
import os
import math
import sys

all_nums = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        all_nums.append(row[0])

winning_numbers = None

# easy option
for i in all_nums:
    for j in all_nums:
        for k in all_nums:
            i = int(i)
            j = int(j)
            k = int(k)
            total = i+j+k
            if total == 2020:
                winning_numbers = (i, j, k)
                break

print(winning_numbers)
final_answer = winning_numbers[0]*winning_numbers[1]*winning_numbers[2]
print(final_answer)