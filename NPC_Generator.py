import sqlite3
import random
from items import items
from races import *
from beings import *

'''TODO
*SORT SQLITE3 QUERIES
'''

conn = sqlite3.connect('RPG.db')

cur = conn.cursor()

#x = Enemy(goblin,goblin['race_name'],race_name_random(goblin),5,white_mage,black_mage,52,inventory = mob_inventory(goblin['race_name']))



def create_enemy(race,sex,level,job):
    inventory = None
    #read in race, level and job
    #create inventory and equipped gear
    name = NPC_random_name(race,sex)
    inventory = NPC_armour(race,job,level)
    #weapons = NPC_weapons
    #items = NPC_items
    return inventory


### - Random NPC Names dependant on race and sex - ###
def NPC_random_name(race, sex): 
    name = None
    if race == goblin:
        if sex == 'M':
            name = random.choice(("Akbug", "Argav", "Brigadve", "Corbakl", "Cruncha", "Frum", "Gelmax", "Glibl", "Glogroth Von Bloov", "Glovd", "Gorf", "Grelth", "Grickstah", "Griga", "Groovilla Dar Trog", "Khroongah", "Kosrik", "Makdur", "Porgl", "Throngul", "Thuk", "Tryxtah", "Vorlag", "Yorvua"))
        else:
            name = random.choice(("femalName1","femaleName2"))
    elif race == orc:
        if sex == 'M':
            name = random.choice(("Abzag","Abzrolg","Abzug","Agganor","Aghurz","Agnar","Agrakh","Agrobal","Agstarg","Aguz","Ahzug","Arghragdush","Arghur","Ashzu","Aturgh","Avreg","Azarg","Azgarub","Azimbul","Azogu","Azrath","Azulg","Balarkh","Balknakh","Balmeg","Balorgh","Baloth","Balrook","Balzag","Bargo","Bargrug","Bash","Bashagorn","Batgrul","Bazrag","Begnar","Begok","Begozug","Bekhwug","Bhagrun","Biknuk","Bisquelas","Blodrat","Boagog","Boggeryk","Bogham","Bognash","Bogodug","Bogzul","Boldarkh","Bolg","Bolgrul","Borab","Boragrul","Borbuz","Borgath","Borgh","Bormolg","Borolg","Borth","Borz","Borzighu","Borzugh","Bothamul","Braadoth","Braghul","Brog","Brogdul","Brokk","Brugagikh","Brugdush","Brughamug","Brulak","Bugnerg","Bugunh","Bulg","Bullig","Bulugbek","Bulzog","Bulozog","Bumnog","Buragrub","Burush","Burzgrag","Burzunguk","Burzura","Buzog","Carzog","Charlvain","Cognor","Dagnub","Dorzogg","Dragom","Dromash","Drudun","Dugakh","Dugan","Dugroth","Dugtosh","Dugug","Dugugikh","Dular","Dulph","Dulphago","Dulrat","Dumolg","Durak","Durang","Dushgor","Dushkul","Dushugg","Fangoz","Farbalg","Fheg","Gag","Gagogru","Gahar","Gahgdar","Gahznar","Gard","Gargak","Garikh","Garmeg","Garnikh","Gashdug","Gasheg","Gezdak","Gezorz","Ghagrub","Ghak","Ghaknag","Ghakorz","Ghamokh","Ghamosh","Ghamron","Ghamulg","Ghash","Ghashugg","Ghashur","Ghatrugh","Ghaturn","Ghaz","Ghobargh","Ghogurz","Ghorn","Ghornag","Ghornugag","Ghrategg","Ghromrash","Ghrubugbash","Ghrum","Gladba","Glag","Glagbor","Glamalg","Glarg","Glaz","Glazgor","Glazulg","Glegokh","Gloorag","Gloorot","Gloorz","Glorgzorgo","Gloth","Glothozug","Glothun","Glud","Glundeg","Glunrum","Glunurgakh","Glurdag","Glurnt","Glushonkh","Gluthob","Gluthush","Gobur","Goburbak","Godrun","Gogaz","Gogbag","Gogrikh","Goh","Gohazgu","Gohorg","Golbag","Golg","Goorgul","Goragol","Gorak","Goramalg","Gorbakh","Gorblad","Gorbu","Gordag","Gorgath","Gorgrolg","Gorlar","Gorotho","Gorrath","Goruz","Gorzesh","Gothag","Gothurg","Gozarth","Graalug","Graguz","Gralturg","Grashbag","Grashegg","Grashub","Gravik","Grazhwu","Grezgor","Grishduf","Grodagur","Grodoguz","Grog","Gromazgu","Gronov","Grookh","Grubdosh","Grudogub","Grugnur","Grulbash","Gruldum","Gruloq","Gruluk","Grulzul","Grumth","Grundu","Grunyun","Grushbub","Grushnag","Gruudus","Gruzdash","Gruznak","Gulargh","Gulburz","Gulug","Gulzog","Gunagud","Gunda","Gunran","Gurag","Gurg","Gurgozod","Gurlak","Guruzug","Gushagub","Gushorg","Guzg","Gwilherm","Hagard","Hazbur","Horak","Hothmuk","Hruz","Ilthag","Inazzur","Kadrun","Kargnuth","Kazok","Kelrog","Kentosh","Khal","Khamagash","Kharsh","Kharsthun","Khartag","Khoruzoth","Khralek","Kurog","Kirgut","Klang","Klovag","Kogaz","Kradauk","Krodak","Krog","Krogrash","Kulth","Kurd","Kurlash","Lagarg","Lagrog","Lahkgarg","Lakhalg","Lakhdosh","Larhoth","Larob","Lashbag","Latumph","Laurig","Lazgel","Lob","Logbur","Logogru","Lorbash","Lothdush","Lothgud","Lozotusk","Lozruth","Lozwug","Lug","Lugbagg","Lugbur","Lugdakh","Lugdugul","Lugnikh","Lugolg","Lugrots","Lugrun","Lugulg","Lugzod","Lum","Lumgol","Lungruk","Lurash","Lurbozog","Lurg","Lurgonash","Luzmash","Maaga","Mag","Magrol","Magunh","Makhoguz","Makhug","Margog","Marzul","Maugash","Mauhoth","Mazabakh","Mazgro","Mazogug","Megorz","Mekag","Mog","Mogazgur","Mogrub","Mokhrul","Mokhul","Monru","Morbrogug","Mordrog","Mordugul","Mordularg","Morgaz","Morgbrath","Morlak","Morothmash","Morotub","Mort","Mothozog","Muduk","Mudush","Muglugd","Mugrub","Muhaimin","Mulatub","Mulgargh","Mulgu","Mulur","Mulzalt","Murdodosh","Murgonak","Murgoz","Murgrud","Murkh","Murlog","Murukh","Murzog","Muzb","Muzbar","Muzdrulz","Muzgalg","Muzgash","Muzgu","Muzogu","Nabshuq","Nagoth","Nagrul","Nahzgra","Nahzush","Nakhul","Namoroth","Narazz","Nargbagorn","Narhag","Narkhagikh","Narkhozikh","Narkhukulg","Narkularz","Nash","Nashruth","Nenesh","Norgol","Nugok","Nugwugg","Nunkuk","Obdeg","Obgol","Obgurob","Obrash","Ofglog","Ogmash","Ogodosh","Ogog","Ogorosh","Ogozod","Ogruk","Ogularz","Ogumalg","Ogzar","Ogzor","Okrat","Olfim","Olfin","Olfrig","Olgol","Olugush","Ontogu","Oodeg","Oodegu","Oogron","Oorg","Oorgurn","Oorlug","Oosh","Ordooth","Orgak","Orgdragog","Orgdugrash","Orgotash","Orgush","Orntosh","Orzbara","Orzuk","Osgrikh","Osgulug","Othbug","Othigu","Othogor","Othohoth","Otholug","Othukul","Othulg","Othzog","Ozor","Pergol","Putor","Rablarz","Ragbul","Ragbur","Ragnast","Ramash","Ramazbur","Ramorgol","Ramosh","Razgor","Razgugul","Razgurug","Rhosh","Rogbum","Rognar","Rogrug","Rogurog","Roguzog","Rokaug","Rokut","Roog","Rooghub","Rooglag","Rorburz","Rozag","Rugdugbash","Rugdrulz","Rugmeg","Ruzgrol","Sgagul","Sgolag","Shab","Shagol","Shagrod","Shakh","Shakharg","Shakhighu","Shamagug","Shamar","Shamlakh","Shargarkh","Shargunh","Sharkagub","Sharkuzog","Sharnag","Shogarz","Shogorn","Shugral","Shukul","Shulthog","Shurkol","Shurrog","Skagurn","Skagwar","Skalgunh","Skalguth","Skarath","Skordo","Skorgat","Skulzak","Slagwug","Slayag","Slegbash","Smagbogoth","Smauk","Snabazkur","Snagbash","Snagdurl","Snagg","Snagh","Snakh","Snakzut","Snalikh","Snarbugag","Snargorg","Snazumph","Sneg","Snegbug","Snegburgak","Snegh","Sneghar","Snikhbat","Snoog","Snoorg","Snugar","Snugok","Snukh","Snushbat","Sogh","Spagel","Storgh","Stugbrulz","Stugbulukh","Szugburg","Szugogroth","Targak","Targoth","Tazgol","Tazgul","Thagam","Thagbruth","Thagbush","Thakaz","Thakh","Thakush","Tharag","Tharkul","Thaz","Thazeg","Thaznog","Thegur","Thereg","Tholog","Thoogh","Thorkh","Thorzh","Thorzhul","Thrag","Thragdosh","Thragosh","Threg","Thrug","Thrugb","Thrunikh","Thukbug","Thungdosh","Todrak","Togbrig","Tograz","Torg","Torug","Tugam","Tugawuz","Tumuthag","Tungthu","Ufthag","Ugdush","Uggnath","Ugorz","Ugruntuk","Uguntig","Ugurz","Ulagash","Ulagug","Ulang","Ulgdagorn","Ulghesh","Ulmamug","Ulozikh","Undrigug","Undugar","Ungruk","Unrahg","Unthrikh","Uragor","Urak","Urdbug","Urgdosh","Urok","Ushang","Usn","Usnagikh","Uugus","Uulgarg","Uuth","Uznom","Vargos","Vulmon","Vundrum","Vunp","Waghuth","Wardush","Wort","Wuzgu","Yagarg","Yagorkh","Yagramak","Yakegg","Yamukuz","Yargob","Yargonk","Yarnabakh","Yarnag","Yarulg","Yat","Yatog","Yggnast","Yggoz","Yggruk","Yggurz","Yozth","Yzzgol","Zagh","Zaghurbak","Zagrakh","Zagrugh","Zbulg","Zegol","Zgog","Zhagush","Zhasim","Zhosh","Zilbash","Zogbag","Zosh","Zugnor","Zulbash","Zulbek","Zulgozu","Zulgroth","Zulgukh","Zulohoth","Zumog","Zungarg","Zunlog"))
        else:
            name = random.choice(("femalName1","femaleName2"))
    return name

### - Get armour set from sqlite3 valid for enemy race, job and level - ###
def NPC_armour(race, job, level): 
    print("race is", race)
    cur.execute('SELECT * FROM armour WHERE armour_race =?''AND  armour_level = 3', (race,),) 
    for row in cur:
        print("Armour from DB is: ",row)
        inventory = row
        print("inventory is: ",inventory)
    return inventory

### - Get weapon from sqlite3 valid for enemy race, job and level - ###
def NPC_weapons(race, job, level):
    print("race is", race)
    weapon = None
    cur.execute('SELECT * FROM weapons WHERE weapon_race =? AND  weapon_job =?', (race,(job)),) 
    for row in cur:
        print("Weapon from DB is: ",row)
        weapon = row
        weapon = random.choice(weapon)
        print("Weapon is: ",weapon)

    return weapon

### - Get armour set from sqlite3 valid for enemy race, job and level - ###
def NPC_items(race, job, level):
    print(race)
    cur.execute('SELECT * FROM items WHERE item_race =?''AND  item_weight < 14', (race,),) 
    for row in cur:
        print(row)
        items = random.choice(row)
    return cur.fetchall()


    """ print(race)
    cur.execute('SELECT * FROM items WHERE item_race =?''AND  item_weight < 14', (race,),) 
    for row in cur:
        print(row)
    return cur.fetchall() """

#print(NPC_random_name(goblin, 'M'))
print(NPC_weapons(goblin['race_name'],'warrior',3)) # works needs to not manually input
y = Enemy(goblin,'M',goblin['race_name'],NPC_random_name(goblin, 'M'),6,warrior,monk,52,inventory = create_enemy(goblin['race_name'],'M',5,warrior["name"]))
print("y is: ", y)
print("y name is: ",y.name,y.sex,y.gold,y.mainjob["name"],y.supportjob["name"])
print("y inventory is: ",y.inventory)