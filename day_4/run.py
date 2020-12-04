import csv
import json
import os
import math
import sys
import re

passports = []

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter=' ', quotechar='|')

    passport_string = []

    for r in input_reader:
        if r == []:
            passports.append(passport_string)
            passport_string = []

        passport_string.extend(r)

    # get the last one in the list    
    passports.append(passport_string)

def validate_fields(passport):
    for k, v in passport.items():
        if k == 'byr':
            val = int(v)
            if not (val >= 1920 and val <= 2002):
                return False
        elif k == 'iyr':
            val = int(v)
            if not (val >= 2010 and val <= 2020):
                return False
        elif k == 'eyr':
            val = int(v)
            if not (val >= 2020 and val <= 2030):
                return False
        elif k == 'hgt':
            units = v[-2:]
            if units != 'cm' and units != 'in':
                return False
            value = int(v[0:-2])
            if units == 'in' and not (value >= 59 and value <=76):
                return False
            elif units == 'cm' and not (value >= 150 and value <=193):
                return False
        elif k == 'hcl':
            first_char = v[0:1]
            if first_char is not '#':
                return False
            color = v[1:]
            _rex = re.compile("[0-9a-fA-F]+")
            if not _rex.fullmatch(color):
                return False 
        elif k == 'ecl':
            if not (v == 'amb' or v == 'blu' or v == 'brn' or v == 'gry' or v == 'grn' or v =='hzl' or v =='oth'):
                return False 
        elif k == 'pid':
            if not (len(v) == 9 and v.isdigit()):
                return False
    return True
            


def check_validity(passport):
    num_keys = len(passport)

    if num_keys == 8:
        return validate_fields(passport)
        # return True
    elif num_keys <= 6:
        return False
    else:
        # if length is 7 and CID is present, it is invalid 
        found_cid = False
        for k, v in passport.items():
            if k == 'cid':
                found_cid = True
                return False 
        return validate_fields(passport)
    
def passport_to_object(passport_array):
    passport_object = {}
    for i in passport_array:
        k, v = i.split(':')
        passport_object[k] = v
    return passport_object

num_total_valid = 0

for p in passports:
    obj = passport_to_object(p)
    is_valid = check_validity(obj)
    print(obj, is_valid)
    print('------------')

    if is_valid == True:
        num_total_valid += 1

print('total num valid', num_total_valid)