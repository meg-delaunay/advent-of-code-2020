import csv
import json
import os
import math
import sys

def determine_row(current_row, letter):
    new_row = (-1, -1)
    length = current_row[1] - current_row[0]
    if letter == 'F':
        new_row = (current_row[0], current_row[0] + math.floor(length/2))
    elif letter == 'B':
        new_row = (current_row[0] + math.ceil(length/2), current_row[1])
    
    return new_row

def determine_seat(current_seat, letter):
    new_seat = (-1, -1)
    length = current_seat[1] - current_seat[0]
    if letter == 'R':
        new_seat = (current_seat[0] + math.ceil(length/2), current_seat[1])
    elif letter == 'L':
        new_seat = (current_seat[0], current_seat[0] + math.floor(length/2))
    return new_seat

seat_ids = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        current_row = (0, 127)
        current_seat = (0, 7)
        for i in range(len(row[0])):
            letter = row[0][i]
            if i < 7:
                current_row = determine_row(current_row, letter)
                # print(current_row)
            
            if i >= 7:
                current_seat = determine_seat(current_seat, letter)
                # print(current_seat)

        final_row = current_row[0]
        final_seat = current_seat[0]

        seat_id = (final_row*8) + final_seat
        seat_ids.append(seat_id)

seat_ids.sort(reverse=True)

max_id = seat_ids[0]
min_id = seat_ids[len(seat_ids)-1]

for i in range(min_id, max_id):
    if i not in seat_ids:
        print(i)
