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

# final_paths = []
# potential_paths = [[adapters[0]]]
# current_path_length = 0

# for index in tqdm.tqdm(range(len(adapters))):
#     # print('---------------------------')
#     # print('index', index)
#     next_paths = []
#     for path in potential_paths:
#         # print('path', path)
#         last_jolt = path[-1:][0]
#         # print('last in path', last_jolt)

#         if last_jolt == max_adapter:
#             new_path = copy.copy(path)
#             next_paths.append(new_path)
#             #final_paths.append(new_path)


#         diff_1_value = last_jolt+1
#         diff_2_value = last_jolt+2
#         diff_3_value = last_jolt+3

#         # print('possible next values', diff_1_value, diff_2_value, diff_3_value)

        
#         if diff_1_value in adapters:
#             new_path = copy.copy(path)
#             new_path.append(diff_1_value)
#             # print('new path', new_path)
#             next_paths.append(new_path)
#             # break
#         if diff_2_value in adapters:
#             new_path = copy.copy(path)
#             new_path.append(diff_2_value)
#             next_paths.append(new_path)
#         if diff_3_value in adapters:
#             new_path = copy.copy(path)
#             new_path.append(diff_3_value)
#             next_paths.append(new_path)

#     potential_paths = copy.copy(next_paths)
#     # print(potential_paths)

# # print(potential_paths)
# print('number of potential paths: ', len(potential_paths))

print('max: ', max_adapter)
# def find_adapters_paths(adapter):
#     if adapter == max_adapter:
#         return 1

#     paths = 0
#     next_branches = []
#     for next_jolt in range(adapter+1, adapter+4):
#         if next_jolt in adapters:
#             next_branches.append(next_jolt)
#             paths = paths * find_adapters_paths(next_jolt)

    
#     paths = paths + find_adapters_paths(next_jolt)
#     return paths


# total_paths = find_adapters_paths(adapters[0])
# print('total paths:', total_paths)


# tree = {}

# total_num_branches = 1
# prev_num_branches = 1
# for a in adapters:
#     print('----------------------------')
#     print('current adapter', a)
#     if a == max_adapter:
#         break

#     next_jolts = range(a+1, a+4)
#     num_branches = 0
#     for j in next_jolts:
#         if j in adapters:
#             tree[a] = tree[a].append(j)
#             num_branches += 1

#     print('current num branches:', num_branches)
#     print('previous num branches:', prev_num_branches)

#     if num_branches != 1:
#         total_num_branches += num_branches
#         # if prev_num_branches != 1:
#         #     total_num_branches *= num_branches
#         # elif prev_num_branches == 1:
#         #     total_num_branches += num_branches
    
#     print('new total:', total_num_branches)
#     prev_num_branches = num_branches

# print(total_num_branches)

# paths = 0
# def make_tree(adapter): 
#     key = adapter
#     if key == max_adapter:
#         return {str(key): None}
    
#     potential_children = range(key+1, key+4)
#     child_trees = []
#     for p in potential_children:
#         if p in adapters:
#             p_tree = {}
#             if p == max_adapter:
#                 p_tree = {str(p): None}
#             else:
#                 p_tree = {str(p): make_tree(p)}
#             child_trees.append(p_tree)
#     return child_trees

# def iterbody(d, n_q):
#     #print(d)
#     for k,v in d.items():    
#         #print ('loop found', k, v)    
#         if isinstance(v, dict):
#             n_q = iterbody(v, n_q)
#         elif isinstance(v, list):
#             #print('LIST : ', v) 
#             for i in v:
#                 # print('LIST : ', v) #this is a string
#                 if isinstance(i, dict):
#                     n_q = iterbody(i, n_q)
#         else:            
#             # print ('END NODE', k,":",v) #this is a string
#             # print ('NQ', n_q)
#             n_q = n_q + 1
#             # k = clean_field_name(k)

#             # k = k.strip()

#             # if k.find('gt') != -1 or k.find('lt') != -1:
#             #     analyze_body_date_term(k ,v)

#             # if not self.term_map.get(k):
#             #     term_map[k] = 1
#             # else:
#             #     term_map[k] += 1
#             # # return n_q
#     return n_q   

# tree = {}
# tree = {'0': make_tree(adapters[0])}
# print(tree)

# paths = 0
# paths = iterbody(tree, 0)
# print(paths)

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
    print('seq', seq)
    seq_len = len(seq)
    if seq_len < 2:
        continue
    elif seq_len == 2:
        branches = 1
        # total_branches += branches
        print('branches', branches)
        continue
    else:
        expo = seq_len - 2
        branches = 1
        print(expo)
        for i in range(1, expo+1):
            print(i)
            branches += i
        print('branches', branches)
        total_branches *= branches
        print('total', total_branches)

print(int(total_branches))