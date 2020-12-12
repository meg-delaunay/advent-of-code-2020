import csv
import json
import os
import math
import sys

directions = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        
        directions.append(
            {
                'action': row[0][:1],
                'value': int(row[0][1:])
            }
        )

def basic_move(direction, location):
    action = direction['action']
    distance = direction['value']
    if action == 'N':
        return (location[0], location[1]+distance)
    if action == 'S':
        return (location[0], location[1]-distance)
    if action == 'E':
        return (location[0]+distance, location[1])
    if action == 'W':
        return (location[0]-distance, location[1])

def rotate(direction, face):
    turn = direction['action']
    current_degrees = 0
    if face == 'N':
        current_degrees = 90
    elif face == 'S':
        current_degrees = 270
    elif face == 'E':
        current_degrees = 0
    elif face == 'W':
        current_degrees = 180
    
    new_degrees = 0
    if turn == 'R':
        new_degrees = current_degrees - direction['value']
    elif turn == 'L':
        new_degrees = current_degrees + direction['value']

    if new_degrees >= 360:
        new_degrees = new_degrees % 360
    elif new_degrees < 0:
        new_degrees += 360
        new_degrees = new_degrees % 360
    
    if new_degrees == 0:
        return 'E'
    elif new_degrees == 90:
        return 'N'
    elif new_degrees == 180:
        return 'W'
    elif new_degrees == 270:
        return 'S'
    else:
        print('rotation is fucked')
        return 'F'


def move_part_1(direction, location, face):
    if direction['action'] == 'N' or direction['action'] == 'S' or direction['action'] == 'E' or direction['action'] == 'W':
        # this is a basic increment of one coordinate
        # they way you are facing does not matter 
        new_location = basic_move(direction, location) 
        return new_location, face
    elif direction['action'] == 'F':
        new_direction = {
            'action': face,
            'value': direction['value']
        }
        new_location = basic_move(new_direction, location)
        return new_location, face
    elif direction['action'] == 'R' or direction['action'] == 'L':
        new_face = rotate(direction, face)
        return location, new_face
    

current_location = (0, 0)
current_face = 'E'

for direction in directions:
    current_location, current_face = move_part_1(direction, current_location, current_face)

manhattan_distance = abs(current_location[0]) + abs(current_location[1])

print('manhattan distance is: ', manhattan_distance)


# ---------------------------------------------------------------------------
def rotate_waypoint(direction, waypoint):
    rotation = direction['action']
    degrees = direction['value']
    new_waypoint = waypoint
    if rotation == 'R':
        if degrees == 90:
            new_waypoint = (waypoint[1], -waypoint[0])
        elif degrees == 180:
            new_waypoint = (-waypoint[0], -waypoint[1])
        elif degrees == 270:
            new_waypoint = (-waypoint[1], waypoint[0])
    elif rotation == 'L':
        if degrees == 90:
            new_waypoint = (-waypoint[1], waypoint[0])
        elif degrees == 180:
            new_waypoint = (-waypoint[0], -waypoint[1])
        elif degrees == 270:
            new_waypoint = (waypoint[1], -waypoint[0])
    return new_waypoint



def move_part_2(waypoint, direction, location):
    if direction['action'] == 'N' or direction['action'] == 'S' or direction['action'] == 'E' or direction['action'] == 'W':
        # this is a basic increment of one coordinate
        # they way you are facing does not matter 
        new_waypoint = basic_move(direction, waypoint) 
        return new_waypoint, location
    elif direction['action'] == 'F':
        new_x = location[0] + (direction['value'] * waypoint[0])
        new_y = location[1] + (direction['value'] * waypoint[1])
        new_location = (new_x, new_y)
        # new_waypoint = (new_x+waypoint[0], new_y+waypoint[1])
        return waypoint, new_location
    elif direction['action'] == 'R' or direction['action'] == 'L':
        new_waypoint = rotate_waypoint(direction, waypoint)
        return new_waypoint, location


current_location = (0, 0)
waypoint_distance = (10, 1)
current_waypoint = (10, 1)

for direction in directions:
    current_waypoint, current_location = move_part_2(current_waypoint, direction, current_location)
    print('after: ', direction, ': waypoint: ', current_waypoint, ': current_location:', current_location)

manhattan_distance = abs(current_location[0]) + abs(current_location[1])

print('manhattan distance is: ', manhattan_distance)