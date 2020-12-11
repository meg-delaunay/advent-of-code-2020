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

all_seats = {}
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

            key = str(number_row) + '|' + str(number_column)
            all_seats[key] = current_seat
            number_column+=1
        total_columns = number_column
        number_row+=1
    total_rows = number_row

print(all_seats)

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
            seat_key = str(v[0]) + '|' + str(v[1])
            s = seats[seat_key]

            if s['floor'] == True:
                # if it is a floor, it does not matter for here
                adjacents[k] = None

    return adjacents                

    

def determine_occupied(coords, seats):
    seat_key = str(coords[0]) + '|' + str(coords[1])
    seat = seats[seat_key]
    return seat['occupied']

def play_round(seats):
    changes_in_round = 0
    updating_seats = copy.deepcopy(seats)
    # seat_index = 0
    for seat_key, seat in seats.items(): 
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
            updating_seats[seat_key]['occupied'] = True
            changes_in_round += 1
        
        elif seat['occupied'] == True and count_occupied_adjacents >= 4:
            print('flipped seat to empty')
            updating_seats[seat_key]['occupied'] = False
            changes_in_round += 1

        else:
            print('no change?')
            # print(seat)
        
        # print('my seat: ', seat_coordinates)
        # print('number_adjacent', count_occupied_adjacents)

    return changes_in_round, updating_seats

print('------- PART 1 ------------')
# for seat_key, seat_data in all_seats.items():
#     print(seat_key)
#     seat_coordinates = (seat_data['row'], seat_data['column'])
#     seat_data['adjacents'] = set_adjacents(seat_coordinates, all_seats)

# print(all_seats)

# number_rounds = 0
# had_changes = True
# while had_changes == True:
#     print('-----------start round--------------------')
#     seats_for_round = copy.deepcopy(all_seats)
#     number_changes, updated_seats = play_round(all_seats)
#     print('in round: ', number_rounds, ' we changed: ', number_changes)
#     all_seats = copy.deepcopy(updated_seats)
#     if number_changes == 0:
#         had_changes = False 
#     else: 
#         number_rounds += 1
    

# print('number rounds', number_rounds)

# # now we count occupied seats!
# count_final_occupied = 0
# for seat_key, seat in all_seats.items():
#     if seat['occupied'] == True:
#         count_final_occupied += 1

# print('final number of occupied seats: ', count_final_occupied)

def find_visibles(seat_key, seat, seats):
    #print('-- finding visibles of: ', seat_key)
    visible_count = 0
    seat_row = seat['row']
    seat_col = seat['column']
    # top - decrease row and not column
    start_search_row = seat_row - 1
    while start_search_row >= 0:
        search_key = str(start_search_row) + '|' + str(seat_col)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        #print('checking top', search_key)
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_row -= 1 
    # top-right - decrease row and increase column
    start_search_row = seat_row - 1
    start_search_col = seat_col + 1
    while start_search_row >= 0 and start_search_col < total_columns:
        
        search_key = str(start_search_row) + '|' + str(start_search_col)
        #print('checking tr', search_key)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_row -= 1 
        start_search_col += 1
    # right - increase col and not row
    start_search_col = seat_col + 1
    while start_search_col < total_columns:
        
        search_key = str(seat_row) + '|' + str(start_search_col)
        #print('checking r', search_key)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_col += 1 
    # bottom right - increase row and increase col
    start_search_row = seat_row + 1
    start_search_col = seat_col + 1
    while start_search_row < total_rows and start_search_col < total_columns:
        
        search_key = str(start_search_row) + '|' + str(start_search_col)
        #print('checking br', search_key)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_row += 1 
        start_search_col += 1
    # bottom - increase row and not column
    start_search_row = seat_row + 1
    while start_search_row < total_rows:
        
        search_key = str(start_search_row) + '|' + str(seat_col)
        #print('checking b', search_key)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_row += 1 
    # bottom left - increase row and decrease col
    start_search_row = seat_row + 1
    start_search_col = seat_col - 1
    while start_search_row < total_rows and start_search_col >= 0:
        
        search_key = str(start_search_row) + '|' + str(start_search_col)
        #print('checking bl', search_key)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_row += 1 
        start_search_col -= 1
    # left - decrease col and not row
    start_search_col = seat_col - 1
    while start_search_col >= 0:
        
        search_key = str(seat_row) + '|' + str(start_search_col)
        #print('checking l', search_key)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_col -= 1 
    # top left - decrease row and decrease col
    start_search_row = seat_row - 1
    start_search_col = seat_col - 1
    while start_search_row >= 0 and start_search_col >= 0:
        
        search_key = str(start_search_row) + '|' + str(start_search_col)
        #print('checking tl', search_key)
        if seats[search_key]['occupied'] == False and seats[search_key]['floor'] == False:
            break 
        if seats[search_key]['occupied'] == True:
            visible_count += 1
            #print('found occupied:', search_key)
            break
        start_search_row -= 1 
        start_search_col -= 1

    #print('visible count for: ', seat_key, ' -- ', visible_count)
    return visible_count

def play_round_part_2(seats):
    changes_in_round = 0
    updating_seats = copy.deepcopy(seats)
    # seat_index = 0
    for seat_key, seat in seats.items(): 
        seat_coordinates = (seat['row'], seat['column'])

        
        if seat['floor'] == True:
            continue

        count_occupied_visibles = find_visibles(seat_key, seat, seats)
        
        if seat['occupied'] == False and count_occupied_visibles == 0:
            #print('flipped seat to occupied')
            updating_seats[seat_key]['occupied'] = True
            changes_in_round += 1
        
        elif seat['occupied'] == True and count_occupied_visibles >= 5:
            #print('flipped seat to empty')
            updating_seats[seat_key]['occupied'] = False
            changes_in_round += 1

        else:
            pass
            #print('no change?')
            # print(seat)
        
        # print('my seat: ', seat_coordinates)
        # print('number_adjacent', count_occupied_adjacents)

    return changes_in_round, updating_seats

def print_seat_grid(seats):
    grid = []
    for i in range(total_rows):
        row = ''
        for j in range(total_columns): 
            icon = 'X'
            key = str(i) + '|' + str(j)
            seat = seats[key]
            if seat['floor'] == True:
                icon = '.'
            elif seat['occupied'] == True:
                icon = '#'
            elif seat['occupied'] == False:
                icon = 'L'

            row += (icon)
        grid.append(row)
    for r in grid:
        print(r)



print('------- PART 2 ------------')
print_seat_grid(all_seats)
number_rounds = 1
had_changes = True
while had_changes == True:
    print('-----------start round--------------------')
    seats_for_round = copy.deepcopy(all_seats)
    number_changes, updated_seats = play_round_part_2(seats_for_round)
    print('in round: ', number_rounds, ' we changed: ', number_changes)
    # print_seat_grid(updated_seats)
    all_seats = copy.deepcopy(updated_seats)
    if number_changes == 0:
        had_changes = False 
    else: 
        number_rounds += 1
    
#print('final_state', all_seats)
#print('number rounds', number_rounds)

# now we count occupied seats!
count_final_occupied = 0
for seat_key, seat in all_seats.items():
    if seat['occupied'] == True:
        count_final_occupied += 1

print('final number of occupied seats: ', count_final_occupied)