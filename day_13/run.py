import csv
import json
import os
import math
import sys

goal = 0
all_routes = []
available_routes = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    rows = []
    for row in input_reader:
        rows.append(row)

    goal = int(rows[0][0])
    temp_array = rows[1][0].split(',')

    for route in temp_array:
        if route != 'x':
            available_routes.append(int(route))
            all_routes.append(int(route))
        elif route == 'x':
            all_routes.append(None)

available_time = 0
chosen_route = 0

for route in available_routes:
    print('route:', route)
    divisor, remainder = divmod(goal, route)
    route_available_time = (divisor+1)*route

    if route_available_time == goal:
        available_time = route_available_time
        break
    # for the first one, always set it, from then on, compare to self 
    elif available_time == 0:
        available_time = route_available_time
        chosen_route = route 
    elif route_available_time < available_time:
        available_time = route_available_time
        chosen_route = route


print("route: ", chosen_route, " is available at: ", available_time)
wait_time = available_time - goal
final_answer = wait_time * chosen_route
print('final answer: ', final_answer)

# --------------------------------- PART 2 --------------------------------------------------

# need to find a number such that: 
#     minutes % route = [t+index in array]

# first we need to find the highest route in the array and increment by that
longest_route = max(available_routes)
longest_route_index = all_routes.index(longest_route)
# starting_time = longest_route

divisor, mod = divmod(100000000000000, longest_route)
starting_time = longest_route * divisor
found_already = []

print(len(all_routes))

found_answer = False 
while found_answer != True: 
    print('starting:', starting_time)
    bailed = False
    found_this_turn = found_already
    for route in available_routes:
        print('route: ', route)

        index_of_route = all_routes.index(route)
        if index_of_route < longest_route_index:
            time_for_route = starting_time - (longest_route_index - index_of_route)
        elif index_of_route > longest_route_index:
            time_for_route = starting_time + (index_of_route - longest_route_index)
        elif index_of_route == longest_route_index:
            time_for_route = starting_time

        mod = time_for_route % route
        if mod != 0:
            bailed = True 
            break
        if mod == 0 and route not in found_already and len(found_already) < 5:
            found_this_turn.append(route)
            ## basically now that we have found a number that 
            longest_route *= route

    
    if bailed == False: 
        found_answer = True
        break

    found_already = found_this_turn
    print(found_this_turn)
    print(found_already)
    print('should not get here')
    starting_time += longest_route

start_time_of_first_train = starting_time - longest_route_index
print(start_time_of_first_train)