import csv
import json
import os
import math
import sys
import copy

filename = sys.argv[1]
def read_program(filename):
    program = []
    with open(filename) as input_file:
        input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

        for row in input_reader:
            instruction, value = row[0].split()
            program.append({
                'instruction': instruction,
                'value': value,
                'hit_count': 0
            })
    return program


def run_program(p):
    program_end = False 
    infinite = True
    i = 0
    accumulator = 0
    while not program_end:
        if i >= len(p):
            print('hit last instruction')
            program_end = True
            infinite = False
            continue
        current_instruction = p[i]
        # print(current_instruction)

        if current_instruction['hit_count'] > 0:
            program_end = True
            infinite = True
            continue

        # LIKE SOMEHOW THIS IS PROPAGATING HOW!?!?!?!?!? WHAT AM I DOING STUPID!?!?
        current_instruction['hit_count'] += 1
        if current_instruction['instruction'] == 'nop':
            i += 1
        elif current_instruction['instruction'] == 'acc':
            accumulator += int(current_instruction['value'])
            i += 1
        elif current_instruction['instruction'] == 'jmp':
            direction = current_instruction['value'][0:1]
            number = int(current_instruction['value'][1:])

            if direction == '+':
                i += number
            elif direction == '-':
                i -= number

    return accumulator, infinite

def update_instruction(i):
    if i['instruction'] == 'acc':
        return i
    elif i['instruction'] == 'jmp':
        print('changed jmp to nop')
        i['instruction'] = 'nop'
    elif i['instruction'] == 'nop':
        print('changed nop to jmp')
        i['instruction'] = 'jmp'
    else:
        pass

    return i


# acc_part_1, infinite = run_program(program)
# print(acc_part_1)

accumulator=0
infinite =True
program = read_program(filename)
for i in range(len(program)):
    local_program = copy.deepcopy(program)
    print('--------------------------')
    print('changing instruction number: ', i)
    local_program[i] = update_instruction(local_program[i])
    accumulator, infinite = run_program(local_program)
    
    if infinite == False:
        print('Final Accumulator Value: ', accumulator)
        break

