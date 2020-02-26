#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals Combat. Reading in the character, checking 
their stats and that of the enemy, then doing the combat math
"""

from characterCreation import *
from beings import Enemy
import random
from game_time import getTime
from testing import mob_inventory

'''TODO
*PLAYER AND ENEMY MP CHECKS FOR SPELLS
*ADD ABILITIES
*MIN/MAX STATS
*ENEMY AI COMBAT
*HAVE ACTION AMOUNTS MODIFIED BY STATS
'''


def battle(enemy):
    '''
        • Read enemy
        • Decide who turn initially
            ○ While playerHP >0 and enemyHP >0:
                § Turn = turn + 1
                § Display actions
                § Choose action
                § Calculate actions numbers
                § Update relevant numbers
    '''
    
 
    #PlayerStats
    playerStats = {
        'playerHP': player.race['stats']['hp'] + player.mainjob['hp'] + int ((player.level/100)*100),
        'playerMP': player.race['stats']['mp'] + player.mainjob['mp'] + int ((player.level/100)*100),
        'playerStrength' : player.race['stats']['strength'] + int ((player.level/100)*100), 
        'playerDexterity' : player.race['stats']['dexterity'] + int ((player.level/100)*100), 
        'playerVitality' : player.race['stats']['vitality'] + int ((player.level/100)*100), 
        'playerAgility' : player.race['stats']['agility'] + int ((player.level/100)*100), 
        'playerInteligence' : player.race['stats']['intelligence'] + int ((player.level/100)*100), 
        'playerMind' : player.race['stats']['mind'] + int ((player.level/100)*100), 
        'playerCharisma' : player.race['stats']['charisma'] + int ((player.level/100)*100) }



    #Enemy stats
    enemyStats = {
        'enemyHP': enemy.race['stats']['hp'] + enemy.mainjob['hp'] + int ((enemy.level/100)*100) ,
        'enemyMP': enemy.race['stats']['mp'] + enemy.mainjob['mp'] + int ((enemy.level/100)*100),
        'enemyStrength': enemy.race['stats']['strength'] + int ((enemy.level/100)*100) ,
        'enemyDexterity': enemy.race['stats']['dexterity'] + int ((enemy.level/100)*100) ,
        'enemyVitality': enemy.race['stats']['vitality'] + int ((enemy.level/100)*100) ,
        'enemyAgility': enemy.race['stats']['agility'] + int ((enemy.level/100)*100) ,
        'enemyInteligence': enemy.race['stats']['intelligence'] + int ((enemy.level/100)*100) ,
        'enemyMind': enemy.race['stats']['mind'] + int ((enemy.level/100)*100), 
        'enemyCharisma': enemy.race['stats']['charisma'] + int ((enemy.level/100)*100) }


    def print_battle_stats():
        print("-------------------------------------------------------------------------------------------------")
        print("| ",player.name,'\t\t|\t\t\t|', enemy.name)
        print("| PlayerHP \t\t| ",playerStats['playerHP'], '|\t\t\t|',' EnemyHP \t\t| ', enemyStats['enemyHP'], '|\t\t\t|')
        print("| PlayerMP \t\t| ",playerStats['playerMP'], '|\t\t\t|',' EnemyMP \t\t| ', enemyStats['enemyHP'], '|\t\t\t|')
        print("| playerStrength \t| ",playerStats['playerStrength'], '|\t\t\t|',' EnemyStrength \t| ', enemyStats['enemyStrength'], '|\t\t\t|')
        print("| playerDexterity \t| ",playerStats['playerDexterity'], '|\t\t\t|',' EnemyDexterity \t| ', enemyStats['enemyDexterity'], '|\t\t\t|')
        print("| playerVitality \t| ",playerStats['playerVitality'], '|\t\t\t|',' EnemyVitality \t| ', enemyStats['enemyVitality'], '|\t\t\t|')
        print("| playerAgility \t| ",playerStats['playerAgility'], '|\t\t\t|',' EnemyAgility \t| ', enemyStats['enemyAgility'], '|\t\t\t|')
        print("| playerInteligence \t| ",playerStats['playerInteligence'], '|\t\t\t|',' EnemyInteligence \t| ', enemyStats['enemyInteligence'], '|\t\t\t|')
        print("| playerMind \t\t| ",playerStats['playerMind'], '|\t\t\t|',' EnemyMind \t\t| ', enemyStats['enemyMind'], '|\t\t\t|')
        print("| playerCharisma \t| ",playerStats['playerCharisma'], '|\t\t\t|',' EnemyCharisma \t| ', enemyStats['enemyCharisma'], '|\t\t\t|')
        print("------------------------------------------------------------------------------------------------")
                              

    def battle(enemy):
        '''
        • Read enemy
        • Decide who turn initially
            ○ While playerHP >0 and enemyHP >0:
                § Turn = turn + 1
                § Display actions
                § Choose action
                § Calculate actions numbers
                § Update relevant numbers
    '''
    
 
    #PlayerStats
    playerStats = {
        'playerHP': player.race['stats']['hp'] + player.mainjob['hp'] + int ((player.level/100)*100),
        'playerMP': player.race['stats']['mp'] + player.mainjob['mp'] + int ((player.level/100)*100),
        'playerStrength' : player.race['stats']['strength'] + int ((player.level/100)*100), 
        'playerDexterity' : player.race['stats']['dexterity'] + int ((player.level/100)*100), 
        'playerVitality' : player.race['stats']['vitality'] + int ((player.level/100)*100), 
        'playerAgility' : player.race['stats']['agility'] + int ((player.level/100)*100), 
        'playerInteligence' : player.race['stats']['intelligence'] + int ((player.level/100)*100), 
        'playerMind' : player.race['stats']['mind'] + int ((player.level/100)*100), 
        'playerCharisma' : player.race['stats']['charisma'] + int ((player.level/100)*100)}
        #playerDefense
        #playerRangedAttack



    #Enemy stats
    enemyStats = {
        'enemyHP': enemy.race['stats']['hp'] + enemy.mainjob['hp'] + int ((enemy.level/100)*100) ,
        'enemyMP': enemy.race['stats']['mp'] + enemy.mainjob['mp'] + int ((enemy.level/100)*100),
        'enemyStrength': enemy.race['stats']['strength'] + int ((enemy.level/100)*100) ,
        'enemyDexterity': enemy.race['stats']['dexterity'] + int ((enemy.level/100)*100) ,
        'enemyVitality': enemy.race['stats']['vitality'] + int ((enemy.level/100)*100) ,
        'enemyAgility': enemy.race['stats']['agility'] + int ((enemy.level/100)*100) ,
        'enemyInteligence': enemy.race['stats']['intelligence'] + int ((enemy.level/100)*100) ,
        'enemyMind': enemy.race['stats']['mind'] + int ((enemy.level/100)*100), 
        'enemyCharisma': enemy.race['stats']['charisma'] + int ((enemy.level/100)*100) }


    def print_battle_stats():
        print("-------------------------------------------------------------------------------------------------")
        print("| ",player.name,'\t\t|\t\t\t|', enemy.name)
        print("| PlayerHP \t\t| ",playerStats['playerHP'], '|\t\t\t|',' EnemyHP \t\t| ', enemyStats['enemyHP'], '|\t\t\t|')
        print("| PlayerMP \t\t| ",playerStats['playerMP'], '|\t\t\t|',' EnemyMP \t\t| ', enemyStats['enemyMP'], '|\t\t\t|')
        print("| playerStrength \t| ",playerStats['playerStrength'], '|\t\t\t|',' EnemyStrength \t| ', enemyStats['enemyStrength'], '|\t\t\t|')
        print("| playerDexterity \t| ",playerStats['playerDexterity'], '|\t\t\t|',' EnemyDexterity \t| ', enemyStats['enemyDexterity'], '|\t\t\t|')
        print("| playerVitality \t| ",playerStats['playerVitality'], '|\t\t\t|',' EnemyVitality \t| ', enemyStats['enemyVitality'], '|\t\t\t|')
        print("| playerAgility \t| ",playerStats['playerAgility'], '|\t\t\t|',' EnemyAgility \t| ', enemyStats['enemyAgility'], '|\t\t\t|')
        print("| playerInteligence \t| ",playerStats['playerInteligence'], '|\t\t\t|',' EnemyInteligence \t| ', enemyStats['enemyInteligence'], '|\t\t\t|')
        print("| playerMind \t\t| ",playerStats['playerMind'], '|\t\t\t|',' EnemyMind \t\t| ', enemyStats['enemyMind'], '|\t\t\t|')
        print("| playerCharisma \t| ",playerStats['playerCharisma'], '|\t\t\t|',' EnemyCharisma \t| ', enemyStats['enemyCharisma'], '|\t\t\t|')
        print("------------------------------------------------------------------------------------------------")
                              

    ### -- BATTLE -- ###
    battleTime = getTime()
    playerAttack = playerStats['playerStrength'] - enemyStats['enemyVitality']
    print('NOW IN BATTLE')
    print(enemy.name)
    print(playerAttack)
    number = random.randint(1,2)
    if number == 1:
        player_turn = True
    else:
        player_turn = False
    while playerStats['playerHP'] >= 0 and enemyStats['enemyHP'] >= 0: 
        if player_turn == True:
                print("Which action will you take?\n1.Attack\n2.Magic\n3.Item\n4.Run")
                choice = input()
                if choice == '1':
                    playerAttack = playerStats['playerStrength'] - enemyStats['enemyVitality']
                    enemyStats['enemyHP'] = enemyStats['enemyHP'] - playerAttack
                    print_battle_stats()
                elif choice == '2':
                    num = 0
                    for name, spell_dict in player.mainjob['spelllist'].items():
                        num = num + 1
                        if player.level >= spell_dict['level']:
                            print(num,player.mainjob["name"],".- {} costs {} MP".format(name, spell_dict['mp_cost']))
                    for name, spell_dict in player.supportjob['spelllist'].items():
                        num = num + 1
                        if player.level >= spell_dict['level']:
                            print(num,player.supportjob["name"],".- {} costs {} MP".format(name, spell_dict['mp_cost']))
                    action = input().lower()
                    if action in (player.mainjob['spelllist']):
                        action = player.mainjob['spelllist'][action]
                        if playerStats['playerMP'] < action['mp_cost']:
                            print("You dont have enough MP")
                        else:
                            #CHECK IF DAMAGE ACTION
                            if action['effect'] == 'damage':
                                if action['element'] == battleTime['day']:### - Bonus based on which day it is matching spell element
                                    enemyStats['enemyHP'] = enemyStats['enemyHP'] - action['amount']
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(battleTime['day'],'  Bonus!')
                                    print_battle_stats()
                                else:
                                    enemyStats['enemyHP'] = enemyStats['enemyHP'] - action['amount']
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(action['mp_cost'])
                                    print_battle_stats()
                            #CHECK IF HEALING ACTION        
                            elif action['effect'] == 'healing':
                                if action['element'] == battleTime['day']:### - Bonus based on which day it is matching spell element
                                    playerStats['playerHP'] = playerStats['playerHP'] + action['amount'] 
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(battleTime['day'],' Bonus!')
                                    print_battle_stats()
                                else:
                                    playerStats['playerHP'] = playerStats['playerHP'] + action['amount']
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(action['mp_cost'])
                                    print_battle_stats()
                            #CHECK IF ENHANCING ACTION  
                            elif action['effect'] == 'enhancing':
                                if action['element'] == battleTime['day']:### - Bonus based on which day it is matching spell element
                                    stat_to_amend = action['modifier']
                                    playerStats[stat_to_amend] = playerStats[stat_to_amend] + action['modifier_amount'] 
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(battleTime['day'],' Bonus!')
                                    print_battle_stats()
                                else:
                                    stat_to_amend = action['modifier']
                                    playerStats[stat_to_amend] = playerStats[stat_to_amend] + action['modifier_amount'] 
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(action['mp_cost'])
                                    print_battle_stats()  
                            #CHECK IF ENFEEBLING ACTION
                            elif action['effect'] == 'enfeebling':
                                if action['element'] == battleTime['day']:### - Bonus based on which day it is matching spell element
                                    stat_to_amend = action['modifier']
                                    enemyStats[stat_to_amend] = enemyStats[stat_to_amend] + action['modifier_amount'] 
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(battleTime['day'],' Bonus!')
                                    print_battle_stats()
                                else:
                                    stat_to_amend = action['modifier']
                                    enemyStats[stat_to_amend] = enemyStats[stat_to_amend] - action['modifier_amount'] 
                                    playerStats['playerMP'] = playerStats['playerMP'] - action['mp_cost']
                                    print(action['mp_cost'])
                                    print_battle_stats()
                #CHOOSE AN ITEM
                elif choice == '3':
                    i = None
                    print("Which item do you want to use?")
                    print_consumable_items(inventory)
                    #choice = input()
                    #if choice == '1':
                     #   use_consumable(i)
                elif choice == '4':
                    print("YOU WANT TO RUN AWAY!")
                else:
                    print("Choose a Valid Option!")
                    player_turn = False
        elif player_turn == False:
            print("Enemy attacks")
            player_turn = True




#Enemy - race, name, level, mainjob, support job, gold, inventory
#battle(Enemy(goblin,"Crikz", 10,white_mage, black_mage,52,inventory = mob_inventory(race,Enemy.level,Enemy.mainjob)))
#x = Enemy(goblin,goblin['race_name'],race_name_random(goblin),5,white_mage,black_mage,52,inventory = mob_inventory(goblin['race_name']))
#print(x.name)
#print(x.inventory)

battle(Enemy(dwarf,'M',"Orc", 'Crikz', 25,warrior, black_mage,52,inventory = [('Matted Fur',70),('High Quality Fur',10)]))





