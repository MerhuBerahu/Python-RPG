import random
'''TODO
*ADD ALL RACES IN

'''

human = {'race_name': 'Human','description': 'The most prevalent of the races, also the shortest lived.','stats': {
'hp': 20,
'mp': 20,
'strength': 5,
'dexterity':5 , 
'vitality': 5, 
'agility': 5, 
'intelligence': 5, 
'mind': 5, 
'charisma': 5,}}

dwarf = {'name': 'Dwarf','description': 'A race of hardy miners','stats': {
'hp': 25,
'mp': 15,
'strength': 10,
'dexterity':5 , 
'vitality': 9, 
'agility': 2, 
'intelligence': 5, 
'mind': 1, 
'charisma': 2,}}

elf = {'race_name': 'Elf','description': 'The long lived elves, despised by many','stats': {
'hp': 15,
'mp': 25,
'strength': 4,
'dexterity':10 , 
'vitality': 1, 
'agility': 10, 
'intelligence': 7, 
'mind': 0, 
'charisma': 3,}}

goblin = {'race_name': 'Goblin','description': 'One of the race og Gonlonkind','stats': {
'hp': 15,
'mp': 25,
'strength': 4,
'dexterity':10 , 
'vitality': 1, 
'agility': 10, 
'intelligence': 7, 
'mind': 0, 
'charisma': 3,}}

orc = {'race_name': 'Goblin','description': 'One of the race og Gonlonkind','stats': {
'hp': 15,
'mp': 25,
'strength': 4,
'dexterity':10 , 
'vitality': 1, 
'agility': 10, 
'intelligence': 7, 
'mind': 0, 
'charisma': 3,}}

def race_name_random(race):
    if race == goblin:
        name = random.choice(("Akbug", "Argav", "Brigadve", "Corbakl", "Cruncha", "Frum", "Gelmax", "Glibl", "Glogroth Von Bloov", "Glovd", "Gorf", "Grelth", "Grickstah", "Griga", "Groovilla Dar Trog", "Khroongah", "Kosrik", "Makdur", "Porgl", "Throngul", "Thuk", "Tryxtah", "Vorlag", "Yorvua"))
    elif race == orc:
        name = random.choice(("Abzag","Abzrolg","Abzug","Agganor","Aghurz","Agnar","Agrakh","Agrobal","Agstarg","Aguz","Ahzug","Arghragdush","Arghur","Ashzu","Aturgh","Avreg","Azarg","Azgarub","Azimbul","Azogu","Azrath","Azulg","Balarkh","Balknakh","Balmeg","Balorgh","Baloth","Balrook","Balzag","Bargo","Bargrug","Bash","Bashagorn","Batgrul","Bazrag","Begnar","Begok","Begozug","Bekhwug","Bhagrun","Biknuk","Bisquelas","Blodrat","Boagog","Boggeryk","Bogham","Bognash","Bogodug","Bogzul","Boldarkh","Bolg","Bolgrul","Borab","Boragrul","Borbuz","Borgath","Borgh","Bormolg","Borolg","Borth","Borz","Borzighu","Borzugh","Bothamul","Braadoth","Braghul","Brog","Brogdul","Brokk","Brugagikh","Brugdush","Brughamug","Brulak","Bugnerg","Bugunh","Bulg","Bullig","Bulugbek","Bulzog","Bulozog","Bumnog","Buragrub","Burush","Burzgrag","Burzunguk","Burzura","Buzog","Carzog","Charlvain","Cognor","Dagnub","Dorzogg","Dragom","Dromash","Drudun","Dugakh","Dugan","Dugroth","Dugtosh","Dugug","Dugugikh","Dular","Dulph","Dulphago","Dulrat","Dumolg","Durak","Durang","Dushgor","Dushkul","Dushugg","Fangoz","Farbalg","Fheg","Gag","Gagogru","Gahar","Gahgdar","Gahznar","Gard","Gargak","Garikh","Garmeg","Garnikh","Gashdug","Gasheg","Gezdak","Gezorz","Ghagrub","Ghak","Ghaknag","Ghakorz","Ghamokh","Ghamosh","Ghamron","Ghamulg","Ghash","Ghashugg","Ghashur","Ghatrugh","Ghaturn","Ghaz","Ghobargh","Ghogurz","Ghorn","Ghornag","Ghornugag","Ghrategg","Ghromrash","Ghrubugbash","Ghrum","Gladba","Glag","Glagbor","Glamalg","Glarg","Glaz","Glazgor","Glazulg","Glegokh","Gloorag","Gloorot","Gloorz","Glorgzorgo","Gloth","Glothozug","Glothun","Glud","Glundeg","Glunrum","Glunurgakh","Glurdag","Glurnt","Glushonkh","Gluthob","Gluthush","Gobur","Goburbak","Godrun","Gogaz","Gogbag","Gogrikh","Goh","Gohazgu","Gohorg","Golbag","Golg","Goorgul","Goragol","Gorak","Goramalg","Gorbakh","Gorblad","Gorbu","Gordag","Gorgath","Gorgrolg","Gorlar","Gorotho","Gorrath","Goruz","Gorzesh","Gothag","Gothurg","Gozarth","Graalug","Graguz","Gralturg","Grashbag","Grashegg","Grashub","Gravik","Grazhwu","Grezgor","Grishduf","Grodagur","Grodoguz","Grog","Gromazgu","Gronov","Grookh","Grubdosh","Grudogub","Grugnur","Grulbash","Gruldum","Gruloq","Gruluk","Grulzul","Grumth","Grundu","Grunyun","Grushbub","Grushnag","Gruudus","Gruzdash","Gruznak","Gulargh","Gulburz","Gulug","Gulzog","Gunagud","Gunda","Gunran","Gurag","Gurg","Gurgozod","Gurlak","Guruzug","Gushagub","Gushorg","Guzg","Gwilherm","Hagard","Hazbur","Horak","Hothmuk","Hruz","Ilthag","Inazzur","Kadrun","Kargnuth","Kazok","Kelrog","Kentosh","Khal","Khamagash","Kharsh","Kharsthun","Khartag","Khoruzoth","Khralek","Kurog","Kirgut","Klang","Klovag","Kogaz","Kradauk","Krodak","Krog","Krogrash","Kulth","Kurd","Kurlash","Lagarg","Lagrog","Lahkgarg","Lakhalg","Lakhdosh","Larhoth","Larob","Lashbag","Latumph","Laurig","Lazgel","Lob","Logbur","Logogru","Lorbash","Lothdush","Lothgud","Lozotusk","Lozruth","Lozwug","Lug","Lugbagg","Lugbur","Lugdakh","Lugdugul","Lugnikh","Lugolg","Lugrots","Lugrun","Lugulg","Lugzod","Lum","Lumgol","Lungruk","Lurash","Lurbozog","Lurg","Lurgonash","Luzmash","Maaga","Mag","Magrol","Magunh","Makhoguz","Makhug","Margog","Marzul","Maugash","Mauhoth","Mazabakh","Mazgro","Mazogug","Megorz","Mekag","Mog","Mogazgur","Mogrub","Mokhrul","Mokhul","Monru","Morbrogug","Mordrog","Mordugul","Mordularg","Morgaz","Morgbrath","Morlak","Morothmash","Morotub","Mort","Mothozog","Muduk","Mudush","Muglugd","Mugrub","Muhaimin","Mulatub","Mulgargh","Mulgu","Mulur","Mulzalt","Murdodosh","Murgonak","Murgoz","Murgrud","Murkh","Murlog","Murukh","Murzog","Muzb","Muzbar","Muzdrulz","Muzgalg","Muzgash","Muzgu","Muzogu","Nabshuq","Nagoth","Nagrul","Nahzgra","Nahzush","Nakhul","Namoroth","Narazz","Nargbagorn","Narhag","Narkhagikh","Narkhozikh","Narkhukulg","Narkularz","Nash","Nashruth","Nenesh","Norgol","Nugok","Nugwugg","Nunkuk","Obdeg","Obgol","Obgurob","Obrash","Ofglog","Ogmash","Ogodosh","Ogog","Ogorosh","Ogozod","Ogruk","Ogularz","Ogumalg","Ogzar","Ogzor","Okrat","Olfim","Olfin","Olfrig","Olgol","Olugush","Ontogu","Oodeg","Oodegu","Oogron","Oorg","Oorgurn","Oorlug","Oosh","Ordooth","Orgak","Orgdragog","Orgdugrash","Orgotash","Orgush","Orntosh","Orzbara","Orzuk","Osgrikh","Osgulug","Othbug","Othigu","Othogor","Othohoth","Otholug","Othukul","Othulg","Othzog","Ozor","Pergol","Putor","Rablarz","Ragbul","Ragbur","Ragnast","Ramash","Ramazbur","Ramorgol","Ramosh","Razgor","Razgugul","Razgurug","Rhosh","Rogbum","Rognar","Rogrug","Rogurog","Roguzog","Rokaug","Rokut","Roog","Rooghub","Rooglag","Rorburz","Rozag","Rugdugbash","Rugdrulz","Rugmeg","Ruzgrol","Sgagul","Sgolag","Shab","Shagol","Shagrod","Shakh","Shakharg","Shakhighu","Shamagug","Shamar","Shamlakh","Shargarkh","Shargunh","Sharkagub","Sharkuzog","Sharnag","Shogarz","Shogorn","Shugral","Shukul","Shulthog","Shurkol","Shurrog","Skagurn","Skagwar","Skalgunh","Skalguth","Skarath","Skordo","Skorgat","Skulzak","Slagwug","Slayag","Slegbash","Smagbogoth","Smauk","Snabazkur","Snagbash","Snagdurl","Snagg","Snagh","Snakh","Snakzut","Snalikh","Snarbugag","Snargorg","Snazumph","Sneg","Snegbug","Snegburgak","Snegh","Sneghar","Snikhbat","Snoog","Snoorg","Snugar","Snugok","Snukh","Snushbat","Sogh","Spagel","Storgh","Stugbrulz","Stugbulukh","Szugburg","Szugogroth","Targak","Targoth","Tazgol","Tazgul","Thagam","Thagbruth","Thagbush","Thakaz","Thakh","Thakush","Tharag","Tharkul","Thaz","Thazeg","Thaznog","Thegur","Thereg","Tholog","Thoogh","Thorkh","Thorzh","Thorzhul","Thrag","Thragdosh","Thragosh","Threg","Thrug","Thrugb","Thrunikh","Thukbug","Thungdosh","Todrak","Togbrig","Tograz","Torg","Torug","Tugam","Tugawuz","Tumuthag","Tungthu","Ufthag","Ugdush","Uggnath","Ugorz","Ugruntuk","Uguntig","Ugurz","Ulagash","Ulagug","Ulang","Ulgdagorn","Ulghesh","Ulmamug","Ulozikh","Undrigug","Undugar","Ungruk","Unrahg","Unthrikh","Uragor","Urak","Urdbug","Urgdosh","Urok","Ushang","Usn","Usnagikh","Uugus","Uulgarg","Uuth","Uznom","Vargos","Vulmon","Vundrum","Vunp","Waghuth","Wardush","Wort","Wuzgu","Yagarg","Yagorkh","Yagramak","Yakegg","Yamukuz","Yargob","Yargonk","Yarnabakh","Yarnag","Yarulg","Yat","Yatog","Yggnast","Yggoz","Yggruk","Yggurz","Yozth","Yzzgol","Zagh","Zaghurbak","Zagrakh","Zagrugh","Zbulg","Zegol","Zgog","Zhagush","Zhasim","Zhosh","Zilbash","Zogbag","Zosh","Zugnor","Zulbash","Zulbek","Zulgozu","Zulgroth","Zulgukh","Zulohoth","Zumog","Zungarg","Zunlog"))
    return name

###Test Cases
"""
print(dwarf['name'])
print(human['description'])
print(human['stats'].keys())
print(human['stats'].values())
print(human['stats']['charisma'])


strength = 1
dexterity = 1
playerjob = white_mage
playerrace = human

if playerjob == white_mage and playerrace == human:
    strength = strength + human['stats']['strength']
    spelllist = white_mage["spelllist"].keys()
    print(strength)
    print(spelllist)

if  playerrace == human:
    strength = strength + human['stats']['strength']
    print(strength)
     """
