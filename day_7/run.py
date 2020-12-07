import csv
import json
import os
import math
import sys

color_graph = {}

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        primary_color = row[0][0:row[0].find('bags')].split()[0] + ' ' + row[0][0:row[0].find('bags')].split()[1]
        secondary_colors = row[0][row[0].find('contain')+7:].strip()

        nodes = []

        if secondary_colors.startswith('no'):
            secondary_colors = []
        else: 
            secondary_list = secondary_colors.split(',')
            for item in secondary_list:
                item = item.strip()
                words = item.split(' ')
                number = words[0]
                color = words[1] + ' ' + words[2] 
                nodes.append({'color':color, 'number':number})

        #print(secondary_colors)
        color_graph[primary_color] = nodes

# print(color_graph)

#now that we have a graph, find the number that eventually get to gold
def find_gold(graph, color):
    found = False
    if graph[color] == []:
        return found
    
    for node in graph[color]:
        if node['color'] == 'shiny gold':
            print('found gold')
            found = True
            return found
        
        found = find_gold(graph, node['color'])
        if found == True:
            break

    return found

def count_bags(graph, color):
    if graph[color] == []:
        return 0

    bags=0
    for node in graph[color]:
        child_bags = count_bags(graph, node['color'])
        bags += int(node['number']) * child_bags
        bags += int(node['number'])

    return bags


total_gold = 0
for k, v in color_graph.items():
    print('---------------------')
    print('start:', k)
    found_gold = find_gold(color_graph, k)
    print('found?', found_gold)
    if found_gold:
        total_gold += 1



# count bags
total_bags = 0
number_bags = count_bags(color_graph, 'shiny gold')

print('number bags', number_bags)

print(total_gold)