#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
MODULE FOR TESTING PURPOSES
"""


import sqlite3
from items import items


conn = sqlite3.connect('RPG.db')

cur = conn.cursor()
print('Data')

#cur.execute('SELECT * FROM items WHERE item_race =?''', ('elf',)) 
#cur.execute('SELECT * FROM items WHERE item_race =?''AND  item_weight < 14', ('elf',),) 
#for row in cur:
#    print(row)

def mob_inventory(race):
    print(race)
    cur.execute('SELECT * FROM items WHERE item_race =?''AND  item_weight < 14', (race,),) 
    for row in cur:
        print(row)
    return cur.fetchall()



