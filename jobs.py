
#job
#spells
#abilities
#armour type
#weapon proficencies

#White Mage
white_mage = {'name': 'White Mage', 'description': 'Healer','hp':7 ,'mp':8 ,'spelllist': {
'cure': {'name': 'Cure','description': 'Restore\'s HP','level': 1, 'effect': 'healing','amount':2, 'mp_cost': 8, 'cast_time': 3,'modifier':'playerMind','modifier_amount':10,'element': 'lightsday'},
'dia': {'name': 'Dia','description' : 'Lowers an enemy\'s defense and gradually deals Light elemental damage.','level': 3, 'effect': 'enfeebling','amount':2, 'mp_cost': 7, 'cast_time': 3,'modifier':'enemyMind','modifier_amount':10,'element': 'lightsday'},
'paralyze': {'name': 'Paralyze','description': 'Paralyzes an enemy.','level': 4, 'effect': 'enfeebling','amount':2, 'mp_cost': 6, 'cast_time': 3,'modifier':'enemyMind','modifier_amount':10,'element': 'lightsday'},
'banish': {'name': 'Banish','description': 'Deals Light elemental damage to an enemy.','level': 5, 'effect': 'damage','amount':2, 'mp_cost': 15, 'cast_time': 3,'modifier':'playerMind','modifier_amount':10,'element': 'lightsday'},
'barstonra': {'name': 'Barstonra','description': 'Increases resistance against Earth.','level': 5, 'effect': 'enhancing','amount':2, 'mp_cost': 12, 'cast_time': 1,'modifier':'playerMind','modifier_amount':10,'element': 'windsday'}},
'abilities': {'rage':{'level': 1, 'effect': 'Damage x2, Defense halved', 'tp_cost': 100, 'cast_time':3,'modifier':'playerStrength'}}, 
'armourtype': 'robes'}
 
 #Black Mage
black_mage = {'name': 'Black Mage','description': 'Elemental Damage Dealer', 'hp':5 , 'mp':10 ,'spelllist': {
'thunder': {'name': 'Thunder','level': 1, 'effect': 'damage','amount':5, 'mp_cost': 6, 'cast_time': 3,'modifier':'playerInteligence','element': 'darksday'},
'fire': {'name': 'Fire','level': 1, 'effect': 'damage','amount':10, 'mp_cost': 6, 'cast_time': 3,'modifier':'playerInteligence','element': 'firesday'},
'Gust': {'name': 'Wind','level': 4, 'effect': 'damage','amount':12, 'mp_cost': 8, 'cast_time': 3,'modifier':'playerInteligence','element': 'windsday'}}, 
'armourtype': 'robes'}

#RED MAGE
red_mage = {'name': 'Red Mage','description': 'Enfeebler','hp':15 ,'mp':0 ,'spelllist': {
'rage': {'name': 'Rage','level': 1, 'effect': 'damage','amount':10, 'mp_cost': 6, 'cast_time': 3,'modifier':'playerStrength','element': 'Darksday'}},
'abilities': {'coax':{'level': 1, 'effect': 'Damage x2, Defense halved', 'tp_cost': 100, 'cast_time':3,'modifier':'playerStrength'}},
'armourtype': 'Heavy Armour'}

#Warrior
warrior = {'name': 'Warrior','description': 'Tank','hp':15 ,'mp':0 ,'spelllist': {
'rage': {'name': 'Rage','level': 1, 'effect': 'damage','amount':10, 'mp_cost': 6, 'cast_time': 3,'modifier':'playerStrength','element': 'Darksday'}},
'abilities': {'coax':{'level': 1, 'effect': 'Damage x2, Defense halved', 'tp_cost': 100, 'cast_time':3,'modifier':'playerStrength'}},
'armourtype': 'Heavy Armour'}

#THIEF
thief = {'name': 'Warrior','description': 'Tank','hp':15 ,'mp':0 ,'spelllist': {
'rage': {'name': 'Rage','level': 1, 'effect': 'damage','amount':10, 'mp_cost': 6, 'cast_time': 3,'modifier':'playerStrength','element': 'Darksday'}},
'abilities': {'coax':{'level': 1, 'effect': 'Damage x2, Defense halved', 'tp_cost': 100, 'cast_time':3,'modifier':'playerStrength'}},
'armourtype': 'Heavy Armour'}

#MONK
monk = {'name': 'Warrior','description': 'Tank','hp':15 ,'mp':0 ,'spelllist': {
'rage': {'name': 'Rage','level': 1, 'effect': 'damage','amount':10, 'mp_cost': 6, 'cast_time': 3,'modifier':'playerStrength','element': 'Darksday'}},
'abilities': {'coax':{'level': 1, 'effect': 'Damage x2, Defense halved', 'tp_cost': 100, 'cast_time':3,'modifier':'playerStrength'}},
'armourtype': 'Heavy Armour'}

#Old Dictionary
'''
unlockedJobs = {
    white_mage:{'name': white_mage,'level': 1,'experience':15 ,'tnl':85},
    black_mage:{'name': black_mage,'level': 1,'experience':15 ,'tnl':85},
    {'name': red_mage,'level': 0,'experience':0 ,'tnl':100},
    {'name': warrior,'level': 1,'experience':0 ,'tnl':100},
    {'name': thief,'level': 0,'experience':0 ,'tnl':100},
    {'name': monk,'level': 0,'experience':0 ,'tnl':100}
    }
'''

#Unlocked jobs list: JobName, Level, Exp, Tnl
unlockedJobs = [
    [white_mage,'1','15' ,'85'],
    [black_mage,'1','15' ,'85'],
    [red_mage,'0','15' ,'85'],
    [warrior,'1','15' ,'85'],
    [thief,'0','15' ,'85'],
    [monk,'0','15' ,'85']
    ]

### - Testing - ###

'''
print(white_mage['abilities'].keys())
#print(white_mage['spelllist']['cure']['mp_cost'])

print(white_mage['description'])
print(white_mage['armourtype'])
print(white_mage['spelllist'].values())
print(white_mage['spelllist'].keys())
print(white_mage['spelllist']['cure']['name'])


print(warrior['description'])
print(warrior['armourtype'])
print(warrior['abilities'].keys())
print(warrior['abilities']['rage']) 


print(warrior['name']) 

for name, spell_dict in white_mage['spelllist'].items():
    print("{} spell which {} and costs {} MP".format(spell_dict['name'], spell_dict['description'],spell_dict['mp_cost']))

'''