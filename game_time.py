#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's Calculates the game worlds date/time.
This is used during other functions, such as combat for 
element enhancements, etc
"""


import time
import random
import sys
from os import system, name

def getTime():
    #Earth Time
    seconds = int(time.time()) #seconds since epoch(1200am, Jan 01 1970)

    #Game Time
    gseconds = int(seconds * 25)
    mincount = int (gseconds / 60)
    hourcount = int(mincount / 60)
    daycount = int (hourcount / 24)
    monthcount = int (daycount / 30)  #simplified 30 day month
    yearcount = int(monthcount /12)
    weekcount = int (daycount / 8) #8 day week


    ### -- CALC HOUR -- ###
    hour = hourcount%(24)

    ### -- CALC MIN -- ###
    minute = mincount%(60)

    ### -- CALC DAY -- ###
    day = None
    dayremainder = daycount%(8)
    if dayremainder == 0:
        day = "Firesday"
    elif dayremainder == 1:
        day = "Earthsday"
    elif dayremainder == 2:
        day = "Watersday"
    elif dayremainder == 3:
        day = "Windsday"
    elif dayremainder == 4:
        day = "Iceday"
    elif dayremainder == 5:
        day = "Lightningday"
    elif dayremainder == 6:
        day = "Lightsday"
    elif dayremainder == 7:
        day = "Darksday"
    else:
        print("DefaultDay")
        print(dayremainder)

    ### -- CALC DATE -- ###
    date = daycount%(30)


    ### -- CALC MONTH -- ##
    month = None
    monthremainder = monthcount%(12)
    if monthremainder == 0:
        month = "January"
    elif monthremainder == 1:
        month = "February"
    elif monthremainder == 2:
        month = "March"
    elif monthremainder == 3:
        month = "April"
    elif monthremainder == 4:
        month = "May"
    elif monthremainder == 5:
        month = "June"
    elif monthremainder == 6:
        month = "July"
    elif monthremainder == 7:
        month = "August"
    elif monthremainder == 8:
        month = "September"
    elif monthremainder == 9:
        month = "October"
    elif monthremainder == 10:
        month = "November"
    elif monthremainder == 11:
        month = "December"
    else:
        print("DefaultMonth")
        print(monthremainder)
        
    ### -- CALC SEASON -- ###
    season = None
    if month in ("November", "December", "January"):
        season = "Winter"
    elif month in ("February", "March", "April"):
        season = "Spring"
    elif month in ("May", "June", "July"):
        season = "Summer"
    elif month in ("August", "September", "October"):
        season = "Autumn"
    else:
        print("DefaultSeason")
        print(monthremainder)


    ### -- CALC MOON
    # new moon -> crescent moon -> half moon -> gibbous moon -> full moon
    moon_day = daycount%(90)
    moon_count = 0
    if moon_day >=1 and  moon_day <= 7:
        moon = 'new_moon'
    elif moon_day >=8 and  moon_day <47:
        moon = 'crescent_moon'
    elif moon_day >=48 and  moon_day <= 64:
        moon = 'half_moon'
    elif moon_day >=65 and  moon_day <= 82:
        moon = 'gibbous_moon'
    elif moon_day >=83 and  moon_day <= 90: 
        if moon_day == 83:
            moon_count = moon_count + 1 
            
    #checking how many full moons have passed and if a prime number its a blood moon
    if moon_count > 1:
        # check for factors
        for i in range(2,moon_count):
            if (moon_count % i) == 0:
                moon = 'Full Moon'
            else:
                moon = 'Blood Moon'
    else:
        moon = 'Full Moon'
                    

           



    ### -- SPECIAL DAYS -- ###
    if date == 1 and month == 'January':
        special_day = 'New Years Day'
    elif date == 25 and month == 'March':
        special_day = 'Spring Equinox'
    elif date == 21 and month == 'June':
        special_day = 'Summer Solstice'
    elif date == 22 and month == 'September':
        special_day = 'Autumn Equinox'
    elif date == 30 and month == 'October':
        special_day = 'Halloween'
    elif date == 21 and month == 'December':
        special_day = 'Winter Solstice'
    elif date == 25 and month == 'December':
        special_day = 'Xmas'
    else:
        special_day = None


    timeNow = {'day':day,'date':date,'month':month,'yearcount':yearcount,'season':season,'hour':hour,'minute':minute}
    print(timeNow['day'])
    return timeNow


    




getTime()
