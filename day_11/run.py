import csv
import json
import os
import math
import sys
import copy

seat = {
    'row': 0,
    'column': 0,
    'floor': False,
    'occupied': False
}

all_seats = []
total_rows = 0
total_columns = 0

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    number_row = 0
    number_column = 0
    for row in input_reader:
        row = row[0]
        number_column = 0
        for col in row:
            current_seat = copy.deepcopy(seat)
            current_seat['row'] = number_row
            current_seat['column'] = number_column

            if col == '.':
                current_seat['floor'] = True

            all_seats.append(current_seat)
            number_column+=1
        total_columns = number_column
        number_row+=1
    total_rows = number_row

# print(all_seats)

def set_adjacents(coords, seats):
    row = coords[0]
    col = coords[1]

    adjacents = {
        'top': (row-1, col),
        'top_right': (row-1, col+1),
        'top_left': (row-1, col-1),
        'right': (row, col+1),
        'left': (row, col-1),
        'bottom': (row+1, col),
        'bottom_right': (row+1, col+1),
        'bottom_left': (row+1, col-1),
    }

    for k, v in adjacents.items():
        if v[0] >= total_rows or v[1] >= total_columns or v[1] < 0 or v[0] < 0:
            # if it is an edge, it does not exist
            adjacents[k] = None
        else:
            for s in seats:
                if s['row'] == v[0] and s['column'] == v[1]:
                    if s['floor'] == True:
                        # if it is a floor, it does not matter for here
                        adjacents[k] = None

    return adjacents                

        



for seat in all_seats:
    seat_coordinates = (seat['row'], seat['column'])
    seat['adjacents'] = set_adjacents(seat_coordinates, all_seats)

print(all_seats)

def determine_occupied(coords, seats):
    for seat in seats:
        if seat['row'] == coords[0] and seat['column'] == coords[1]:
            return seat['occupied']

def play_round(seats):
    changes_in_round = 0
    updating_seats = copy.deepcopy(seats)
    for i in range(len(seats)): 
        seat = seats[i]
        seat_coordinates = (seat['row'], seat['column'])

        count_occupied_adjacents = 0
        if seat['floor'] == True:
            continue

        for k, v in seat['adjacents'].items():
            adjacent_seat_coords = v
            if adjacent_seat_coords == None:
                continue
            occupied = determine_occupied(adjacent_seat_coords, seats)
            if occupied == True:
                count_occupied_adjacents += 1
        
        if seat['occupied'] == False and count_occupied_adjacents == 0:
            print('flipped seat to occupied')
            updating_seats[i]['occupied'] = True
            changes_in_round += 1
        
        elif seat['occupied'] == True and count_occupied_adjacents >= 4:
            print('flipped seat to empty')
            updating_seats[i]['occupied'] = False
            changes_in_round += 1

        else:
            print('no change?')
            print(seat)
        
        # print('my seat: ', seat_coordinates)
        # print('number_adjacent', count_occupied_adjacents)

    return changes_in_round, updating_seats

number_rounds = 0
had_changes = True
while had_changes == True:
    print('-----------start round--------------------')
    seats_for_round = copy.deepcopy(all_seats)
    number_changes, updated_seats = play_round(all_seats)
    print('in round: ', number_rounds, ' we changed: ', number_changes)
    all_seats = copy.deepcopy(updated_seats)
    if number_changes == 0:
        had_changes = False 
    else: 
        number_rounds += 1
    

print('number rounds', number_rounds)

# now we count occupied seats!
count_final_occupied = 0
for seat in all_seats:
    if seat['occupied'] == True:
        count_final_occupied += 1

print('final number of occupied seats: ', count_final_occupied)