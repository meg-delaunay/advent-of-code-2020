import csv
import json
import os
import math
import sys
import numpy as np

starting_numbers = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter=',', quotechar='|')

    for row in input_reader:
        for i in row:
            starting_numbers.append(int(i))

print(starting_numbers)

number_of_turns = 30000000
turns = []

# is each number encountered as key and value is a tuple of its two most recent turns
encountered_numbers = {}

for turn in range(1, number_of_turns+1):
    index = turn - 1 

    if index < len(starting_numbers):
        value_said = starting_numbers[index]
        turns.append(value_said)
        encountered_numbers[value_said] = (None, turn)
        # print(encountered_numbers)
        continue

    previous_turn = turns[index-1]
    indices = encountered_numbers.get(previous_turn)

    if indices[0] == None:
        value = 0
        turns.append(value)
        cache = encountered_numbers.get(value)
        previous_last_index = encountered_numbers.get(value)[1]
        encountered_numbers[value] = (previous_last_index, turn)
    else: 
        value = indices[1] - indices[0]
        turns.append(value)
        if encountered_numbers.get(value) != None:
            previous_last_index = encountered_numbers.get(value)[1]
            encountered_numbers[value] = (previous_last_index, turn)
            # print(encountered_numbers)
        else:
            encountered_numbers[value] = (None, turn)

print(turns[len(turns)-1])