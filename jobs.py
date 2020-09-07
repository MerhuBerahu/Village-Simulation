#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals with jobs that an NPC can have
"""

class Base_job():
    def __init__(self, job_name, job_safety, job_hours, job_type):
        self.job_name = job_name
        self.job_safety = job_safety
        self.job_hours = job_hours
        self.job_type = job_type

class Baker(Base_job): # I would need to instantiate jeff with a 'baker_recipes' 
    def __init__(self):
        self.job_name = "Baker"
        self.job_safety = "Low Risk"
        self.job_hours = "04:00 - 12:00"
        self.job_type = "crafter"
        self.baker_recipes = ["Bread","Baguette"]

class Shopkeep(Base_job): 
    def __init__(self ):
        self.job_name = "Shopkeep"
        self.job_safety = "Low Risk"
        self.job_hours = "09:00 - 17:00"
        self.job_type = "merchant"
        self.shop_type = "Armour Store"
        
"""
# testing jeff
jeff = Baker()
print(jeff.job_hours)
print(jeff.baker_recipes)

#testing bob
bob = Shopkeep()
print(bob.job_hours)
print(bob.shop_type)
"""

