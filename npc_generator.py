#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals with generating NPC's and Enemies
with random names dependent on race and sex and gear/equipment
dependent on race job etc
"""

import random
import sys

class Base_Being():
    def __init__(self, sex, age, name, job, wealth, personal_inventory, motivation, bravery, empathy, greed, hobby, combat_score, reputation):
        self.sex = sex
        self.age = age
        self.name = name
        self.job = job
        self.wealth = wealth
        self.personal_inventory = personal_inventory
        self.motivation = motivation
        self.bravery = bravery
        self.empathy = empathy
        self.greed = greed
        self.hobby = hobby
        self.combat_score = combat_score
        self.reputation = reputation

#generate name
#sex
#random age
#job
#wealth based on job
#personality traits - motivation, bravery, empathy, greed, hobby, combat score, reputation

### - Random NPC Names dependant on race and sex - ###
def NPC_random_name(sex): 
    name = None
    surname = None
    if sex == "M":
        try:
            with open("names//male_names.txt", "r") as first:
                first = random.choice(first.readlines())
        except IOError as e:
            print("{}\nError opening {}. Terminating program.".format(e, file),file=sys.stderr)
            sys.exit(1)
    if sex == "F":
        try:
            with open("names//female_names.txt", "r") as first:
                first = random.choice(first.readlines())
        except IOError as e:
            print("{}\nError opening {}. Terminating program.".format(e, file),file=sys.stderr)
            sys.exit(1)
    try:
        with open("names//surnames.txt", "r") as surname:
            surname = random.choice(surname.readlines())
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),file=sys.stderr)
        sys.exit(1)
    

    
    print(name)    
    return first, surname

print(NPC_random_name("M"))
