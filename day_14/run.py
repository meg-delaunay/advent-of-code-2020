import csv
import json
import os
import math
import sys

# is it cheating to use this and not write it myself? 
get_bin = lambda x, n: format(x, 'b').zfill(n)

# is a list of {'type':'mem', 'location':int(location), 'value':int(value), 'binary':get_bin(int(value), 36)} objects
instructions = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        row = row[0]
        task, value = row.split(' = ')
        if task == 'mask':
            obj = {'type':'mask', 'location':None, 'value':value, 'binary':None}
            instructions.append(obj)
        else: 
            location = task[task.index('[')+1:task.index(']')]
            instructions.append({'type':'mem', 'location':int(location), 'value':int(value), 'binary':get_bin(int(value), 36)})

def mask_value(ins, mask):
    new_binary_string = ''
    for i in range(len(mask)):
        char = mask[i]
        if char == 'X':
            new_binary_string += ins['binary'][i]
        elif char == '1' and ins['binary'][i] == '0':
            new_binary_string += '1'
        elif char == '0' and ins['binary'][i] == '1':
            new_binary_string += '0'
        else:
            new_binary_string += char
    
    new_value = int(new_binary_string, 2)
    return {'binary': new_binary_string, 'value':new_value}

# is an object of {'binary': new_binary_string, 'value':new_value}
# where the key is the address in memory
def part_1(instructions):
    memory = {}
    current_mask = instructions[0]

    for ins in instructions:
        #print('------------')
        if ins['type'] == 'mask':
            current_mask = ins['value']
            continue

        mem_key = str(ins['location'])
        
        if not memory.get(mem_key):
            memory[mem_key] = {}
        #print('memory value before:', memory.get(mem_key))
        memory[mem_key] = mask_value(ins, current_mask)
        #print('instruction:', ins)
        #print('memory value after:', memory.get(mem_key))

    #print(memory[8])

    sum_of_memory = 0
    for m, v in memory.items():
        sum_of_memory += v['value']

    return sum_of_memory

part1 = part_1(instructions)
print('part 1: ', part1)

def mask_key(mask, binary_key):
    new_binary_key = ''
    for i in range(len(mask)):
        char = mask[i]
        if char == 'X':
            new_binary_key += 'X'
        elif char == '1':
            new_binary_key += '1'
        else:
            new_binary_key += binary_key[i]
    return new_binary_key

def get_addresses(mask, binary_key):
    addresses = []

    masked_key = mask_key(mask, binary_key)
    number_of_floats = masked_key.count('X')
    number_of_address = int(math.pow(2, number_of_floats))

    replacements = []
    # this generates every binary string between 0 and the number of options
    for i in range(number_of_address):
        replacements.append(get_bin(i, number_of_floats))
    #print(replacements)

    ##   00 01 10 11
    # basically this loops through all of the option replacements strings and substitutes them in
    for replacement_string in replacements:
        local_key = masked_key
        for index in range(number_of_floats):
            # this replaces the first 'X' with the character at that index from the replacement string
            # and then on each loop the "first" X is now the second and so on
            local_key = local_key.replace('X', replacement_string[index], 1)
        addresses.append(int(local_key, 2))
        # send back the int values which are being used as the primary keys

    return addresses

def part_2(instructions):
    memory = {}
    current_mask = instructions[0]

    for ins in instructions:
        #print('------------')
        if ins['type'] == 'mask':
            current_mask = ins['value']
            continue

        mem_key = str(ins['location'])
        binary_key = get_bin(int(mem_key), 36)

        addresses = get_addresses(current_mask, binary_key)
        for a in addresses:
            if not memory.get(a):
                memory[a] = {}
            #print('memory value before:', memory.get(mem_key))
            memory[a] = {'binary': ins['binary'], 'value':ins['value']}

    sum_of_memory = 0
    for m, v in memory.items():
        sum_of_memory += v['value']

    return sum_of_memory




part2 = part_2(instructions)
print(part2)