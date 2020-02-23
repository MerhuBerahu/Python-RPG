
from races import *
from jobs import *
from beings import Player
from inventory import *


def choose_name():
    print("what is your name Mighty Hero?")
    name = input()
    return name

def choose_race():
    print("choose your race\n\n")

    def print_race(whatrace):
        for i in whatrace.values(): #print out the stats for races
            print(i)
        print("\n")
            
    print_race(human)
    print_race(dwarf)
    print_race(elf)

def race_selection():
    print("So what was your choice?")
    print("1. - Human")
    print("2. - Dwarf")
    print("3. - Elf")
    race_choice = input()
    if race_choice == "1":
        race = human
        print("you have chosen to be a ", race["race_name"])
    elif race_choice == "2":
        race = dwarf
        print("you have chosen to be a ", race["race_name"])
    elif race_choice == "3":
        race = elf
        print("you have chosen to be a ", race["race_name"])
    else:
        print("invalid selection")
        race_selection()
    return race

def sex_selection():
    print("What sex are you?")
    print("1. - Male")
    print("2. - Femail")
    sex_input = input()
    if sex_input == "1":
        sex = 'M'
        print("you have chosen to be a Male")
    elif sex_input == "2":
        sex= 'F'
        print("you have chosen to be a Female")
    return sex
    
def job_selection():
    print("So what was your choice?")
    #print list of job names that have level >= 1 with number assignment
    num = 0
    for x in unlockedJobs:
        if x[1] >= '1':
            num = num + 1
            print(num," - ",x[0]['name'])
    
    #print("1. - White Mage")
    #print("2. - Black Mage")
    #print("3. - Warrior")
    job_choice = input()
    if job_choice == num:
        job = None #stuck here
        #old code below
    elif job_choice == "1":
        job = white_mage
        print("you have chosen to be a ", job["name"])
    elif job_choice == "2":
        job = black_mage
        print("you have chosen to be a ", job["name"])
    elif job_choice == "3":
        job = warrior
        print("you have chosen to be a ", job["name"])     
    else:
        print("invalid selection")
        job_selection()
    return job

def supportjob_selection():
    print("So what was your supportjob choice?")
    print("1. - White Mage")
    print("2. - Black Mage")
    print("3. - Warrior")
    supportjob_choice = input()
    if supportjob_choice == "1":
        supportjob = white_mage
        print("you have chosen to be a ", job["name"] ,"/" , supportjob["name"])
    elif supportjob_choice == "2":
        supportjob = black_mage
        print("you have chosen to be a ", job["name"] ,"/" , supportjob["name"])
    elif supportjob_choice == "3":
        supportjob = warrior
        print("you have chosen to be a ", job["name"] ,"/" , supportjob["name"])     
    else:
        print("invalid selection")
        supportjob_selection()
    return supportjob
    
    
def choose_job():
    print("choose your job\n\n")

        
    def print_jobs(what_job):
        for i in what_job.values(): #print out the stats for jobs
            print(i)
        print("\n")

    for x in unlockedJobs:
        if x[1] >= '1':
            print_jobs(x[0])

    #print_jobs(white_mage)
    #print_jobs(black_mage)
    #print_jobs(warrior)
    #print_jobs(red_mage)


    
    
name = choose_name()  
choose_race()
race = race_selection()
sex = sex_selection()
choose_job()
job = job_selection()
supportjob = supportjob_selection()
inventory = item_by_owned(1)


#race,name,level,mainjob,supportjob,gold,inventory,current exp, exp tnl
player = Player(race,sex, name, 1, job, supportjob,20,inventory,0,100) 


""" print(player.name,race['name'],job['name'])
print(player.mainjob['name'])
print_inventory_names(player.inventory) """






