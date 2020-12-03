import csv
import json
import os
import math
import sys

tree_coords = []
empty_coords = []
num_rows = -1
num_columns = -1


filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    # num_rows = len(input_reader)
    num_row = 0
    for row in input_reader:
        num_column = 0

        grid_row = []
        for c in row[0]:
            current_coords = (num_row, num_column)

            if c == '.':
                empty_coords.append(current_coords)
            elif c == '#':
                tree_coords.append(current_coords)

            num_column += 1
            
        num_row += 1 
        num_columns = num_column
    num_rows = num_row

# print(tree_coords)


def traverse(x, y, num_rows, num_columns):
    current_pos = (0, 0)
    number_trees = 0

    while current_pos[0] <= num_rows:
        if current_pos[1] >= num_columns:
            # back to the beginning
            current_pos = (current_pos[0], (current_pos[1]%num_columns))
        # did we hit a tree?
        if current_pos in tree_coords:
            number_trees += 1

        # increment the position
        current_pos = (current_pos[0]+x, current_pos[1]+y)
    return number_trees

print('starting 1,1')
num_trees_1_1 = traverse(1, 1, num_rows, num_columns)
print('starting 1,3')
num_trees_1_3 = traverse(1, 3, num_rows, num_columns)
print('starting 1,5')
num_trees_1_5 = traverse(1, 5, num_rows, num_columns)
print('starting 1,7')
num_trees_1_7 = traverse(1, 7, num_rows, num_columns)
print('starting 2,1')
num_trees_2_1 = traverse(2, 1, num_rows, num_columns)

total = num_trees_1_1 * num_trees_1_3 * num_trees_1_5 * num_trees_1_7 * num_trees_2_1

print('num trees', total)