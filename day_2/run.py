import csv
import json
import os
import math
import sys

all_passwords = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    for row in input_reader:
        nums, letter, password = row[0].split()
        letter = letter[:-1]

        min_, max_ = nums.split('-')
        pass_object = {
            'min_num': int(min_),
            'max_num': int(max_),
            'letter': letter,
            'password': password
        }

        all_passwords.append(pass_object)

print(len(all_passwords)) #make sure you read them all in silly


def is_valid(password, letter, min_, max_):
    if password.find(letter) == -1:
        return False
    elif password.count(letter) < min_ or password.count(letter) > max_:
        return False
    else:
        return True  

def is_valid_part2(password, letter, min_, max_):
    min_ = min_ - 1 # account for indexing
    max_ = max_ - 1 # account for indexing

    if password[min_:min_+1] == letter and password[max_:max_+1] != letter:
        return True
    elif password[min_:min_+1] != letter and password[max_:max_+1] == letter:
        return True
    else:
        return False

valid_passwords = 0
valid_part_2 = 0
for o in all_passwords:
    if is_valid(o['password'], o['letter'], o['min_num'], o['max_num']):
        valid_passwords += 1

    if is_valid_part2(o['password'], o['letter'], o['min_num'], o['max_num']):
        valid_part_2 += 1

print(valid_passwords)
print(valid_part_2)