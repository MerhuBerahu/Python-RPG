#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This module's Calculates the Players inventory reading/writing 
the data in from an SQLite3 database file.
"""

import sqlite3
from items import items


conn = sqlite3.connect('items.db')

c = conn.cursor()

# c.execute("""CREATE TABLE items (
#         id integer,
#         name text,
#         attack integer,
#         elemental_damage_type text,
#         elemental_damage_amount integer,
#         parry_rate integer,
#         block_rate integer,
#         critical_attack_rate integer,
#         critical_attack_modifier integer,
#         bodypart text,
#         defense integer,
#         description text,
#         equipped integer,
#         owned integer,
#         price integer,
#         type text,
#         subtype text
#         )""")



def item_by_owned(owned):
    c.execute("SELECT * FROM items WHERE owned=:owned", {'owned': 1})
    return c.fetchall()

def print_inventory_names(inventory):
    for i in inventory: #print out the name(index[1] of each item in inventory
        print(i[1])   

inventory = item_by_owned(1)

i = 0


'''
#print(inventory)
#print(inventory[0][1]) #for loop that does this for each item in list

#for s in inventory:
#    print(*s)

#print('\n'.join(' '.join(map(str,sl)) for sl in inventory))
'''
def print_inventory_names(inventory):
    for i in inventory: #print out the name(index[1] of each item in inventory
        print(i[1])     



def print_consumable_items(inventory):
    num = 0
    
    for i in inventory: #reads through all items in inventory
        if i[17] == "yes":
            
            num = num + 1
            print(num,".{} - {}.".format(i[1],i[11])) #prints an increasing number(num) with each iteration and the fields 1 and 11 of items

    choice = int(input())
    #Make a choice to use item
    #if choice is in num, item = num
    print(consumables)
    print(i[1])
    if i[16] == 'healing':
        print("ADDED HP!")
                #NEED A DEFAULT CASE INCASE THEY DONT TYPE A NUMBER
    return i


def use_consumable(i):
    print("You chose ", i)
    #if i[17] == 'healing':
    #    print("ADDED HP!")     




'''
print('\n'.join(' '.join(map(str,sl)) for sl in inventory)) # print items in inventory


for i in inventory: #checking for matching criterea 
    if i[1] == "Hatchet":
        print("WE HAVE A MATCH!!!!!!!")
        print(i[1]) 



#conn.close()
'''

#print(inventory)
#print_inventory_names(inventory)
#print_consumable_items(inventory)

