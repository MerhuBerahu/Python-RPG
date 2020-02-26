#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals with the Base being Class that players, NPC's
and enemies inherit from
"""

import random
from races import *
from jobs import *

class Character:

    def __init__(self, race, sex,name, level, mainjob, supportjob,gold,inventory):
        self.race = race
        self.sex = sex
        self.name = name
        self.level = level
        self.mainjob = mainjob
        self.supportjob = supportjob
        self.gold = gold
        self.inventory = inventory


class Player(Character):

    def __init__(self, race, sex, name,  level, mainjob, supportjob,gold,inventory,currentexp,exptnl):
        super().__init__(race, sex, name, level, mainjob, supportjob,gold,inventory)
        self.currentexp = currentexp
        self.exptnl = exptnl

"""     def __str__(self):
        return super().__str__() + ", " +  self.job """

class Enemy(Character):
    def __init__(self, race, sex, race_name, name,level, mainjob, supportjob,gold, inventory= None):
        super().__init__(race, sex, name, level, mainjob, supportjob,gold,inventory)
        self.race_name = race_name
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def loot(self):           
        choices = []
        for item, weight in self.inventory:
            choices.extend( [item]*weight )
        return random.choice(choices)    

class NPC(Character):

    def __init__(self, race, sex, name,  level, mainjob, supportjob,gold,inventory,quests,merchant = None):
        super().__init__(race, sex, name, level, mainjob, supportjob,gold,inventory)
        self.quests = quests
        self.merchant = merchant

#x = Enemy(goblin,goblin['race_name'],"Cricket",5,white_mage,black_mage,52,"stick")
#print(x.race_name)


""" #CHARACTER CREATION
print("Lets create your Character")


x = Character("Marge", 10, "Paladin", "dark Knight", 36,"potion")
y = Player("Homer", 20, "Warrior", "White Mage",400,"superpotion!",123,15)
monster1 = Enemy("Orc", 25,"Paladin", "Warrior",52,inventory = [('Matted Fur',70),('High Quality Fur',10)])

print(x.mainjob)
print(y.inventory)
print(monster1)
print(monster1.inventory)
print(monster1.loot()) """

#def starting_stats():
    #check race
    #check level
    #check mainjob
    #check support job


#def determine_stats():
    #check race
    #check level
    #check mainjob
    #check support job