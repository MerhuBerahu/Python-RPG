#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals with generating NPC's and Enemies
with random names dependent on race and sex and gear/equipment
dependent on race job etc
"""

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


### - Function that combines the below - ###
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
    surname = None
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
    elif race == elf:
        if sex == 'M':
            name = random.choice(("Carran", "Vakian", "Erro", "Thelamin", "Sarbalar", "Ianzumin", "Ralofaren", "Dornorin", "Ilitoris", "Thefir", "Daeqen", "Kelzeiros", "Thezeiros", "Urimenor", "Adris", "Wrancan", "Glynmaer", "Omafir", "Beiyarus", "Perjeon", "Daero", "Yinquinal", "Farnelis", "Ililamin", "Farwarin", "Tranorin", "Qipeiros", "Adjor", "Carwarin", "Zumlamin", "Genlar", "Fargolor", "Craxalim", "Dorneiros", "Wranxalim", "Fenhice", "Sarwraek", "Zumtoris", "Elbalar", "Syllar", "Mormenor", "Qipeiros", "Aequinal", "Adneiros", "Umelar", "Ralojor", "Morvalur", "Petsalor", "Carmyar", "Ianwarin", "Waesberos", "Virhice", "Virro", "Wransalor", "Herceran", "Adnorin", "Iannelis", "Elaquinal", "Rokas", "Wranris", "Beihorn", "Beikian", "Rofaren", "Fenmaris", "Sylren", "Urifir", "Elaro", "Leolar", "Vahice", "Padan", "Fenhorn", "Qikian", "Petlen", "Norwraek", "Elyarus", "Thetoris", "Ralobalar", "Qinzeiros", "Norwarin", "Vaneiros", "Cramaer", "Tragolor", "Rokas", "Beidan", "Fenlar", "Hermenor", "Perven", "Kelris", "Daeric", "Fenmenor", "Dorkas", "Ilixidor", "Ralolar", "Yinsalor", "Fenlar", "Morven", "Hermaer", "Olowraek", "Zumpeiros", "Kelven"))
        else: 
            name = random.choice(("Oriphyra", "Eilynore", "Ravaxisys", "Inana", "Ensys", "Loragwyn", "Holanala", "Zinfina", "Biwynn", "Sylgella", "Xilroris", "Grestina", "Wysaxisys", "Daqirelle", "Faehana", "Phifiel", "Wysarie", "Lialee", "Nerihana", "Ulathana", "Gilhana", "Sylsatra", "Chaekrana", "Reyrona", "Daera", "Grerie", "Valrona", "Chaerora", "Zylroris", "Reyjyre", "Yessatra", "Reyroris", "Triskalyn", "Trisrieth", "Valrel", "Zylfina", "Urifina", "Eilkrana", "Keylana", "Keyrora", "Daezana", "Yllasatra", "Venfiel", "Yesjyre", "Quiwynn", "Orizana", "Grewynn", "Gilmoira", "Qihana", "Zinroris", "hazana", "Dawenys", "Gilstina", "Shafiel", "Gilxisys", "Qidove", "Trisrel", "Iarharice", "Wynsatra", "Loragella", "Gilrona", "Iarrel", "Inasatra", "Shafiel", "Wysasatra", "Quixina", "Xilcyne", "Xilra", "Sylbanise", "Xyrgwyn", "Zinxina", "Nerimys", "Chaebella", "Faefina", "Jorieth", "Magcyne", "Enkrana", "Miayra", "Quirona", "Araxisys", "Trislee", "Syllee", "Gregwyn", "Greharice", "Presnala", "Holamys", "Birel", "Miara", "Helera", "Keythyra", "Jowynn", "Zylrie", "Dalee", "Daelynn", "Preslana", "Liabella", "Eiljyre", "Daleth", "Caixisys", "Shaphine"))
        surname = random.choice(("Aelasar", "Aelorothi", "Aendryr", "Aerasumé", "Aeravansel", "Agayous", "Agrivar", "Ahmaquissar", "Alaenree", "Alantar", "Alavara", "Alastrarra", "Alenuath", "Alerothi", "Alluth", "Aloevan", "Aluianti", "Aluviirsaan", "Amalith", "Amarallis", "Amaratharr", "Amarthen", "Ammath", "Amrallatha", "Anuaer", "Argentaamn", "Arren", "Ash", "Ashgrove", "Audark", "Auglamyr", "Auglathla", "Aunglor", "Autumnfire", "Bellas", "Berethryl", "Berilan", "Bharaclaiev", "Bhephel", "Blackhelm", "Braegen", "Briarbosk", "Brightcloak", "Brightsong", "Brightwing", "Caersaelk", "Calaudra", "Calauth", "Camusiil", "Cathdeiryn", "Ceretlan", "Chaadren", "Chamaranthe", "Clatharla", "Cormyth", "Coudoarluth", "Craulnober", "Crystalembers", "Dahast", "Dawnhorn", "Dhorinshyl", "Dlardrageth", "Doedance", "Donnathlascen", "Dracoseir", "Dree", "Duirsar", "Durothil", "Duskmere", "Duthjuth", "Ealoeth", "Echorn", "Elaéyadar", "Elassidil", "Elian", "Ellarian", "Elond", "Eluarshee", "Ereuvyn", "Erkowe", "Erladden", "Eroth", "Erlshade", "Estelda", "Evanara", "Eveningfall", "Everlove", "Evioro", "Eyriendor", "Faerondaerl", "Faerondarl", "Falanae", "Felinaun", "Fellmirr", "Fenmarel", "Fflannidan", "Floshin", "Fynnasla", "Gildenguard", "Goadulphyn", "Goldenleaf", "Gourael", "Greencloak", "Gwaelon", "Haell", "Haerlgent", "Haladar", "Hawksong", "Haevaul", "Halavanthlarr", "Hlarr", "Hyshaanth", "Iazymnal", "Ibryiil", "Ilbaereth", "Ilbenalu", "Ildacer", "Ildroun", "Iliathor", "Iliathor", "Iliathorr", "Ilnatar", "Immeril", "Ipyllasc", "Irian", "Irithyl", "Irithyl", "Ithruen", "Iydril", "Jaglene", "Kadelaryn", "Kelerandri", "Kelpor’ral", "Keove", "Kevanarial", "Korianthil", "Kraok", "Laelithar", "Laralytha", "Larenthanil", "Larethian", "Laughingwater", "Leafbower", "Leafsigil", "Le’Quella", "Lharithlyn", "Lhoril", "Llundlar", "Loceath", "Lightshiver", "Maendellyn", "Maerdrym", "Melruth", "Meirityn", "M'Haaren", "Miritar", "Mistrivvin", "Mistwinter", "Mithalvarin", "Moonbow", "Moondown", "Moonflower", "Moonglade", "Moonglamaer", "Moonsnow", "Moonweather", "Morningdove", "Mornmist", "Mrhulaedir", "Nacnar", "Naelgrath", "Narlbeth", "Narlbeth", "Neirdre", "Nelnueve", "Never", "Nhachashaal", "Nhaéslal", "Nharimlur", "Nightstar", "Nightwing", "Nihmedu", "Ni’Tessine", "Nierde", "Nightmeadow", "Nimesin", "Nlossae", "Nlossae", "Nolbrae", "Nyamtharsar", "Nyntynel", "Oakstaff", "Oakwood", "Olortynnal", "Olyrnn", "Omberdawn", "Ongluth", "Orama", "Orbryn", "Orbryn", "Ortauré", "Oumryn", "Phenthae", "Pholont", "Presrae", "Q'Naepp,", "Rachiilstar", "Raedrimn", "Raryndur", "Reithel", "Revven", "Rhaevaern", "Rhothomir", "Rhuidhen", "Rhyllgallohyr", "Rivleam", "Rivvikyn", "Runemaster", "Sarsantyr", "Selakiir", "Selmer", "Selorn", "Shadowmantle", "Shadowwater", "Shaeremae", "Shaethe", "Shalandalan", "Sharrith", "Shaurlanglar", "Shraiee", "Shyr", "Sicafei", "Siltral", "Silverbow", "Silverhand", "Silveroak", "Silverspear", "Sinaran", "Slenderbow", "Spellstalker", "Soryn", "Srinshee", "Starnar", "Starbrow", "Starglance", "Starglow", "Starym", "Stillhawk", "Stilmyst", "Straeth", "Strongbow", "Suldusk", "Sultaasar", "Summerstars", "Sunweaver", "Swordstar", "Symbaern", "Talandren", "Talesspur", "Tamlyranth", "Tanagathor", "Tarnruth", "Tarsap", "Tarsis", "Tassarion", "Taurntyrith", "Tellynnan", "Teshurr", "Thea", "Tlanbourn", "Tohrthaal", "Toralynnsyr", "Tornglara", "Tornglara", "Torthtan", "Toryvhallen", "Trueshot", "Tsornyl", "Tyrneladhelu", "Uirthur", "Ulondarr", "Ulongyr", "Vandiir", "Veverell", "Vispasial", "Vyshaan", "Waelvor", "Whitethistle", "Windstar", "Windwalker", "Xantrani", "Yeschant", "Yhendorn", "Yraueme", "Yridnae", "Yundraer"))
    return name

### - Get armour set from sqlite3 valid for enemy race, job and level - ###
def NPC_armour(race, job, level): 
    print("race is", race)
    cur.execute('SELECT * FROM armour WHERE armour_race =?''AND  armour_level = 3', (race,),) 
    inventory = None
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
        weapon_selection = row
    weapon = random.choice(weapon_selection)
    print("Weapon is: ",weapon)
    return weapon

### - Get items from sqlite3 valid for enemy race, job and level - ###
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
print(NPC_weapons(goblin['race_name'],warrior['name'],3)) # works needs to not manually input
y = Enemy(goblin,'M',goblin['race_name'],NPC_random_name(goblin, 'M'),6,warrior,monk,52,inventory = create_enemy(goblin['race_name'],'M',5,warrior["name"]))
print("y is: ", y)
print("y name is: ",y.name,y.sex,y.gold,y.mainjob["name"],y.supportjob["name"])
print("y inventory is: ",y.inventory)
z = Enemy(goblin,'F',goblin['race_name'],NPC_random_name(goblin,'F'),15,warrior,thief,23,create_enemy(goblin['race_name'],'F',15,warrior['name']))
print(z.name)
