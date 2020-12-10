import csv
import json
import os
import math
import sys
import copy 
import tqdm

adapters = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        adapters.append(int(row[0]))

adapters.sort()
max_adapter = adapters[len(adapters)-1]+3
adapters.append(max_adapter)

print(adapters)

total_joltage = 0
current_adapter_joltage = 0
jolt_differences = {
    'diff_1': 0,
    'diff_2': 0,
    'diff_3': 0
}

for a in adapters:
    if a > current_adapter_joltage+3:
        print('impossible')
        break
    elif a == current_adapter_joltage+3:
        jolt_differences['diff_3'] += 1
    elif a == current_adapter_joltage+2:
        jolt_differences['diff_2'] += 1
    elif a == current_adapter_joltage+1:
        jolt_differences['diff_1'] += 1

    current_adapter_joltage = a

print(jolt_differences)

calculated_answer = jolt_differences['diff_1']*jolt_differences['diff_3']
print('final answer (part 1):', calculated_answer)



adapters.insert(0, 0)
print(adapters)


print('max: ', max_adapter)


sequences = []

i=0
while i <= len(adapters)-1:
    if i == len(adapters)-1:
        sequence = [adapters[i]]
        sequences.append(sequence)
        break
    a = adapters[i]
    sequence = [a]
    current_num = a
    new_index = 0
    for j in range(i+1, len(adapters)):
        next_a = adapters[j]
        new_index = j
        if not next_a == current_num+1:
            break
        sequence.append(next_a)
        current_num = next_a 
        
    sequences.append(sequence)
    i = j

print(sequences)
branches = []

total_branches = 1
for seq in sequences: 
    seq_len = len(seq)
    if seq_len < 2:
        continue
    elif seq_len == 2:
        continue
    else:
        start = seq_len - 2
        branches = 1
        for i in range(1, start+1):
            branches += i
        total_branches *= branches

print('total branches: ', int(total_branches))