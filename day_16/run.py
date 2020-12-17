import csv
import json
import os
import math
import sys
import re 
import numpy 

my_ticket = []
tickets = []
rules = {}


regex_rules = re.compile("^[a-zA-z\s]+: .+-.+ or .+-.+$")
regex_numbers = re.compile("[0-9]+")

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    rows = []
    for row in input_reader:
        if row == []: 

            continue
        rule = re.search(regex_rules, row[0])
        if rule:
            rule_name = row[0][0:row[0].index(':')]
            rule_numbers = re.findall(regex_numbers, row[0])
            start_1 = int(rule_numbers[0])
            end_1 = int(rule_numbers[1])
            start_2 = int(rule_numbers[2])
            end_2 = int(rule_numbers[3])

            rule_numbers_all = []

            for i in range(start_1, end_1+1):
                if i not in rule_numbers_all:
                    rule_numbers_all.append(i)

            for i in range(start_2, end_2+1):
                if i not in rule_numbers_all:
                    rule_numbers_all.append(i)

            rules[rule_name] = rule_numbers_all
        else:
            nums = row[0].split(',')
            if len(nums) == 1:
                continue
            else:
                tickets.append(nums)

print(rules.keys())
print(tickets[0])

allowed_numbers = []
for name, numbers in rules.items():
    for n in numbers:
        allowed_numbers.append(n)

allowed_numbers.sort()

invalid_numbers = []
valid_tickets = []
for t in tickets:
    valid = True 
    for n in t:
        n = int(n)
        if n not in allowed_numbers:
            # if n not in invalid_numbers:
            invalid_numbers.append(n)
            valid = False
    if valid == True:
        valid_tickets.append(t)

tickets_based_on_index = {}
ticket_length = len(tickets[0])

for i in range(ticket_length):
    all_at_i = []
    for t in valid_tickets:
        all_at_i.append(int(t[i]))
    tickets_based_on_index[i] = all_at_i

#print(tickets_based_on_index) 

rules_per_ticket_index = []

for index, values in tickets_based_on_index.items():
    index_matches = []
    
    for name, rule in rules.items(): 
        #print('index: ', index, type(values[0]), type(rule[0]))
        if (all(x in rule for x in values)): 
            print('subset!')
            index_matches.append(name)
        # else: 
        #     print('index: ', index, values, rule)
        #     break

    rules_per_ticket_index.append(index_matches)

print(rules_per_ticket_index)


official_fieldnames = {}

def find_solo(all_options):
    for i in range(len(all_options)): 
        o = all_options[i]
        if len(o) == 1:
            return i , o[0]
    print('fuck')


while len(official_fieldnames.keys()) < len(rules.keys()):
    solo_index, solo = find_solo(rules_per_ticket_index)
    official_fieldnames[str(solo_index)] = solo
    for r in rules_per_ticket_index:
        if solo in r: 
            r.remove(solo)

print(official_fieldnames)


my_ticket = tickets[0]
to_multiply = []

for index, value in official_fieldnames.items():
    if value.find('departure') != -1:
        to_multiply.append(int(my_ticket[int(index)]))

print(to_multiply)

result1 = numpy.prod(to_multiply)
print(result1)

