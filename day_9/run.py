import csv
import json
import os
import math
import sys

program = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        program.append(int(row[0]))


def is_valid(number, preamble):
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            two_sum = preamble[i] + preamble[j]
            if two_sum == number:
                return True
    return False

def get_preamble(program, preamble_size, current_index):
    return program[i-preamble_size:i]

preamble_size = 25
target_number = 0
for i in range(preamble_size, len(program)):
    preamble = get_preamble(program, preamble_size, i)
    validity = is_valid(program[i], preamble)
    if validity == False:
        print('INVALID NUMBER IS:', program[i])
        target_number = program[i]
        break

print('target number for part 2:', target_number)
numbers_added = []

for i in range(len(program)):
    current_sum = program[i]
    numbers_added = [program[i]]
    for j in range(i+1, len(program)):
        numbers_added.append(program[j])
        current_sum += program[j]
        if current_sum == target_number:
            break 
        elif current_sum > target_number: 
            break
        else:
            continue
    if current_sum == target_number:
        break


numbers_added.sort()
vulnerability = numbers_added[0] + numbers_added[len(numbers_added)-1]
print('program vulnerability:', vulnerability)
