import csv
import json
import os
import math
import sys
import re

def to_int(str):
    if not str: return None
    try:
        x = int(str)
    except ValueError:
        return None
    return x

class Passport: 
    def __init__(self, string_list):
        self.is_valid = None
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None 
        self.pid = None
        self.cid = None

        for i in string_list: 
            k, v = i.split(':')
            if k == 'byr':
                self.byr = to_int(v)
            elif k == 'iyr':
                self.iyr = to_int(v)
            elif k == 'eyr':
                self.eyr = to_int(v)
            elif k == 'hgt':
                units = v[-2:]
                value = to_int(v[0:-2])

                if units != 'cm' and units != 'in':
                    units = None

                self.hgt = {'units': units, 'value': value}
            elif k == 'hcl':
                self.hcl = v
            elif k == 'ecl':
                if not (v == 'amb' or v == 'blu' or v == 'brn' or v == 'gry' or v == 'grn' or v =='hzl' or v =='oth'):
                    self.ecl = None
                else: 
                    self.ecl = v
            elif k == 'pid':
                self.pid = v 
            elif k == 'cid':
                self.cid = v

    def get_validity(self):
        return self.is_valid
    
    def validate_passport(self):
        self.is_valid = True
        if not self.byr or not (self.byr >= 1920 and self.byr <= 2002):
            self.is_valid = False

        if not self.iyr or not (self.iyr >= 2010 and self.iyr <= 2020):
            self.is_valid = False

        if not self.eyr or not (self.eyr >= 2020 and self.eyr <= 2030):
            self.is_valid = False

        if not self.hgt or not self.hgt['units']:
            self.is_valid = False
            
        if self.hgt:
            if self.hgt['units'] == 'in' and not (self.hgt['value'] >= 59 and self.hgt['value'] <=76):
                self.is_valid = False 

            if self.hgt['units'] == 'cm' and not (self.hgt['value'] >= 150 and self.hgt['value'] <=193):
                self.is_valid = False 

        if not self.hcl:
            self.is_valid = False
        
        if self.hcl:
            first_char = self.hcl[0:1]
            if first_char is not '#':
                self.is_valid = False
            
            color = self.hcl[1:]
            _rex = re.compile("[0-9a-fA-F]+")
            if not _rex.fullmatch(color):
                self.is_valid = False

        if not self.ecl:
            self.is_valid = False

        if not self.pid or not (len(self.pid) == 9 and self.pid.isdigit()):
            self.is_valid = False
        
        



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

num_total_valid = 0

for p in passports:
    passport = Passport(p)
    passport.validate_passport()
    is_valid = passport.get_validity()
    if is_valid == True:
        num_total_valid += 1

print('total num valid', num_total_valid)