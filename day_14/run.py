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
memory = {}

print(instructions)
current_mask = instructions[0]

for ins in instructions:
    print('------------')
    if ins['type'] == 'mask':
        current_mask = ins['value']
        continue

    mem_key = str(ins['location'])
    
    if not memory.get(mem_key):
        memory[mem_key] = {}
    print('memory value before:', memory.get(mem_key))
    memory[mem_key] = mask_value(ins, current_mask)
    print('instruction:', ins)
    print('memory value after:', memory.get(mem_key))

#print(memory[8])

sum_of_memory = 0
for m, v in memory.items():
    sum_of_memory += v['value']

print(sum_of_memory)