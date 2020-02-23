from characterCreation import *
from beings import Enemy
import random
from main import press_any_key
from game_time import getTime
from inventory import *
from colorama import Fore, init
import combat

# Font Colors
white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
light_red = Fore.LIGHTRED_EX
cyan = Fore.CYAN

'''TODO
*PLAYER AND ENEMY MP CHECKS FOR SPELLS
*ADD ABILITIES
*MIN/MAX STATS
*ENEMY AI COMBAT
*HAVE ACTION AMOUNTS MODIFIED BY STATS
'''

#combat.battle(Enemy(elf,"Goblin", 25,white_mage, "Warrior",52,inventory = [('Matted Fur',70),('High Quality Fur',10)]))
