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

number_of_turns = 2020
turns = []

# is each number encountered as key and value is a tuple of turns
encountered_numbers = {}

for turn in range(1, number_of_turns+1):
    #print(turns)
    index = turn - 1 

    if index < len(starting_numbers):
        value_said = starting_numbers[index]
        turns.append(value_said)
        encountered_numbers[value_said] = (None, turn)
        # print(encountered_numbers)
        continue

    previous_turn = turns[index-1]

    times_said = turns.count(previous_turn)

    if times_said == 1:
        value_said = 0
        if encountered_numbers.get(value_said) != None:
            previous_last_index = encountered_numbers.get(value_said)[1]
            encountered_numbers[value_said] = (previous_last_index, turn)
            # print(encountered_numbers)
        else:
            encountered_numbers[value_said] = (None, turn)
        turns.append(value_said)
        continue
    else: 
        print(encountered_numbers)
        print(previous_turn)
        indices = encountered_numbers.get(previous_turn)
        value_said = indices[1] - indices[0]
        turns.append(value_said)

        if encountered_numbers.get(value_said) != None:
            previous_last_index = encountered_numbers.get(value_said)[1]
            encountered_numbers[value_said] = (previous_last_index, turn)
            print(encountered_numbers)
        else:
            encountered_numbers[value_said] = (None, turn)
        #turns.append(value_said)

        # values = np.array(turns)
        # indices = np.where(values == previous_turn)[0]
        # #print(len(indices))
        # new_val = indices[len(indices)-1] - indices[len(indices)-2]
        # #print(new_val)
        # turns.append(new_val)
        # encountered_numbers[starting_numbers[index]] = (encountered_numbers.get(new_val)[0], turn)

print(turns)
print(turns[len(turns)-1])