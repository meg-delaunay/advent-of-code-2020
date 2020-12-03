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

# iterate through
current_pos = (0, 0)
number_trees = 0


while current_pos[0] <= num_rows:
    # extend puzzle 
    if current_pos[1] > num_columns:
        print('extending the puzzle')
        new_tree_coords = []
        new_empty_coords = []
        #duplicate each tree coordinate
        for c in tree_coords:
            new_c = (c[0], c[1]+num_columns)
            new_tree_coords.append(new_c)
        #duplicate each empty coordiate
        for c in empty_coords:
            new_c = (c[0], c[1]+num_columns)
            new_empty_coords.append(new_c)
        
        #add to the main lists so they get looped over
        empty_coords.extend(new_empty_coords)
        tree_coords.extend(new_tree_coords)
        num_columns += num_columns
    
    # did we hit a tree?
    if current_pos in tree_coords:
        number_trees += 1

    # increment the position
    current_pos = (current_pos[0]+1, current_pos[1]+3)

print('num trees', number_trees)