import random
import os

# TODO: - good to add in different areas

class Monster():
	def __init__ (self, nickname, attack, element, species, health):
		self.nickname = nickname
		self.attack = attack
		self.element = element
		self.species = species
		self.health = health
	
	def __str__(self):
		return " %s is a %s. As a %s monster whose defence mode is %s" % (self.nickname, self.species, self.element, self.attack)

george = Monster("George the Dragon", {"swipes":10, "pushes":20, "throws":30, "bites":50}, "Fire", "Dragon", 50)
tina = Monster("Tina the Tiger", {"swipes":10, "pushes":20, "throws":30, "claws":50, "bites":100}, "Earth", "Tiger", 100)
claudette = Monster("Claudette the Crocodile",{"swipes":10, "snaps":20, "claws":30, "bites":50, "drowns":100}, "Water", "Crocodile", 50)
# edgar = Monster("Edgar the Eagle", {"swipes":10, "snaps":20, "claws":30, "pecks":50, "drops from a height":100, }, "Air", "Eagle", 200, )

class MountainMonster(Monster):
	def __init__( self, nickname, attack, element, species, health, key):
		self.nickname = nickname
		self.attack = attack
		self.element = element
		self.species = species
		self.health = health
		self.key = key

edgar = MountainMonster("Edgar the Eagle", {"swipes":10, "snaps":20, "claws":30, "pecks":50, "drops from a height":100, "flys towards" : 20 }, "Air", "Eagle", 200, "guards key")


class Pixie():
	def __init__(self, name, skill, element, healing, health):
		self.name = name
		self.skill = skill
		self.element = element
		self.healing = healing
		self.health = health

	def __str__(self):
		return " %s is a %s Pixie whose skill is %s" % (self.name,self.element, self.skill)
	
Aurelio = Pixie("Aurelio", {"swipes":30, "pushes":30, "throws":40, "freezes water":50}, "water", 20, 200)
Gisella = Pixie ("Gisella", {"swipes":10, "pushes":10, "throws":20, "blows wind":40}, "air",60, 200)
Sam = Pixie ("Sam", {"swipes":10, "pushes":20, "throws":50, "creates fireball":40}, "fire", 30, 200)
Camille = Pixie ("Camille", {"swipes":5, "pushes":10, "throws":20, "creates tremors":70},"earth",60, 200)

class Lands():
	def __init__(self, monsters, gamelevel):
		self.monsters = monsters
		self.gamelevel = gamelevel
		

undergroundcaves = Lands(george, 1)
darkforest = Lands(tina, 2)
marshlands = Lands(claudette, 3)
mountains = Lands(edgar, 4)


userpixie = None
userland = None


#functions --------------------------------------------------

def user_choice():
	global userpixie 
	userpixie = raw_input("choose which pixie you want to lead: ").lower()
	if userpixie == "aurelio":
		userpixie = Aurelio
		print "Great! Welcome to the game "
	elif userpixie == "gisella":
		userpixie = Gisella
		print "Great! Welcome to the game "
	elif userpixie == "sam":
		userpixie = Sam
		print "Great! Welcome to the game "
	elif userpixie == "camille":
		userpixie = Camille
		print "Great! Welcome to the game "
	else:
		print "Sorry we do not recognize your choice"
		user_choice()


def fork_choice(monster):
	fork_input = raw_input("should we go left or should we go right? (l/r) ").lower()
	if fork_input == "left" or fork_input == "l":
		print "oh no you walked for 400 feet but its a dead end . Lets go back"
		fork_choice(monster)
	elif fork_input == "right" or fork_input == "r":
		print "Oh no! There is the %s - quick get out of the way! " % (monster.nickname)
	else :
		"Thats not an option!"
		fork_choice(monster)

def fork_choice_mountain(mountainmonster) :
	fork_input = raw_input("should we go left, right or straight ahead (l/r/s) ").lower()
	if fork_input == "left" or fork_input == "l" :
		print "it looks like this there is a sheer cliff. Let's go back"
		fork_choice_mountain(mountainmonster)
	elif fork_input == "right" or fork_input == "r" :
		print "oh no this is a dead end. Lets go back"
		fork_choice_mountain(mountainmonster)
	elif fork_input == "straight" or fork_input == "s" :
		print "Oh no! There is the %s - quick get out of the way! " % (mountainmonster.nickname)
		playlevel4(mountainmonster, userpixie)
	else:
		print "thats not an option "
		fork_choice_mountain(mountainmonster)

# def pixiehealthnumber(pixie) :


def playchoice(monster, pixie):
	play_choice = raw_input("Would you like to attack or heal yourself? (a,h) ").lower()
	if play_choice == "attack" or play_choice == "a" :
		pixie_skill = random.choice(pixie.skill.keys())
		monster.health -= pixie.skill[pixie_skill]
		print "%s uses %s and hits for %d" % (pixie.name, pixie_skill, pixie.skill[pixie_skill])
	elif play_choice == "healing" or play_choice == "h" :
		pixie_healing = pixie.healing
		pixie.health += pixie_healing
		print " %s uses healing and adds %d to health" % (pixie.name, pixie.health)
	else :
		print "sorry I do not understand your statement"
		playchoice (monster, pixie)


def play(monster, pixie):
	while pixie.health > 0 and monster.health > 0 :
		monster_attack = random.choice(monster.attack.keys())
		pixie.health -= monster.attack[monster_attack]
		print "%s uses %s and hits for %d" % (monster.nickname, monster_attack, monster.attack[monster_attack])
		playchoice(monster, pixie)
	else : 
		if monster.health <= 0 :
			print "you killed the monster"
		elif pixie.health <= 0 :
			print " Oh no you died. Start again "
			pixie.health = 200
			user_level()

		else :
			print " Sorry we encountered a problem. Please start again"
			user_choice()

def playlevel4(mountainmonster, pixie):
	# print("playlevel4 was called")
	while pixie.health > 0 and mountainmonster.health > 10 :
		mountainmonster_attack = random.choice(mountainmonster.attack.keys())
		pixie.health -= mountainmonster.attack[mountainmonster_attack]
		print "%s uses %s and hits for %d" % (mountainmonster.nickname, mountainmonster_attack, mountainmonster.attack[mountainmonster_attack])
		playchoice(mountainmonster, pixie)
	else : 
		if mountainmonster.health <= 10 :
			print "He flew away, quick grab the key in the nest"
			print "We made it! Quick open the door to Pixie Land before Edgar comes back" 
			print "Welcome home to Pixie Land"
			exit()
		elif pixie.health <= 0 :
			print " Oh no you died. Start again "
			pixie.health = 200
			user_level()
		else :
			print " Sorry we encountered a problem. Please start again"
			user_choice()

#functions :player levels -----------------------------------------
def level5(pixie):
	global userland
	pixie_level = raw_input = ("Use the key to open the door and lets go home! (y/n) ").lower()
	if pixie_level == "y" or pixie_level == "yes" :
		print " Welcome Home! "
	elif pixie_level == "n" or pixie_level == "no":
		userland = None
		print "Thankyou for playing the game"
		exit()
	else :
		"sorry I do not recognise your choice"
		level4(userpixie)

def level4(pixie):
	global userland 
	mountain_level = raw_input( "Are you ready to climb the mountain? (y/n) ").lower()
	if mountain_level == "y" or mountain_level == "yes" :
		userland = mountains
		para_stringtwo = ''''ENTERING THE MOUNTAINS 

You are in the final land of the quest to get home to Pixieland. Now for the final test. 
You must retrieve the key to open the door to Pixieland. The key is in the eagle's nest. 
But since there are chicks why not make him fly away while you retrieve the key.


----------------------------------------------------------------'''
		print para_stringtwo
		fork_choice_mountain(edgar)	
		playlevel4(edgar, userpixie)
	elif mountain_level == "n" or mountain_level == "no":
		userland = None
		print "Thankyou for playing the game"
		exit()
	else :
		"sorry I do not recognise your choice"
		level4(userpixie)


def level3(pixie):
	global userland 
	marshlands_level = raw_input("Are you ready to enter the marshlands? (y/n) ").lower()
	if marshlands_level == "y" or marshlands_level == "yes" :
		userland = marshlands
		para_stringthree = '''ENTERING THE MARSHLANDS 


----------------------------------------------------------------'''
		print para_stringthree
		fork_choice(claudette)	
		play(claudette, userpixie)
		print ''' yes you defeated Claudette the Crocodile. 
Lets get out of the Marshands and into the final land - the Mountains. 
Lets hope we don't meet Edgar the eagle while we rtrieve the key to Pixie Land!! ''' 
		level4(userpixie)
	elif marshlands_level == "n" or marshlands_level == "no":
		userland = None
		print "Thankyou for playing the game"
		exit()
	else :
		"sorry I do not recognise your choice"
		level3(userpixie)


def level2(pixie):
	global userland 
	darkforest_level = raw_input( "Are you ready enter the dark forest? (y/n) ").lower()
	if darkforest_level == "y" or darkforest_level == "yes" :
		userland = darkforest
		para_stringfour = '''ENTERING THE DARK FOREST


----------------------------------------------------------------'''
		print para_stringfour
		fork_choice(tina)	
		play(tina, userpixie)

		print ''' yes you defeated Tina the Tiger. 
Lets get out of the Dark Forest and into the Marshlands. 
Lets hope we don't meet Collette the Crocodile!! ''' 
		level3(userpixie)
	elif darkforest_level == "n" or darkforest_level == "no":
		userland = None
		print "Thankyou for playing the game"
		exit()
	else :
		"sorry I do not recognise your choice"
		level2(userpixie)

def level1(pixie):
	global userland 
	undergroundcaves_level = raw_input( "Are you ready enter the underground caves? (y/n) ").lower()
	if undergroundcaves_level == "y" or undergroundcaves_level == "yes" :
		userland = undergroundcaves
		para_string = '''ENTERING THE UNDERGROUND CAVES
 We walk through the dark caves for half a mile until we encounter a fork? 
---------------------------------------------------------------------
'''
		print para_string
		fork_choice(george)	
		play(george, userpixie)

		print ''' yes you defeated George the Dragon. 
Lets get out of the Underground Caves and into the Dark Forest. 
Lets hope we don't meet Tina the Tiger!! ''' 

		level2(userpixie)

	elif undergroundcaves_level == "n" or undergroundcaves_level == "no":
		userland = None
		print "Thankyou for playing the game"
		exit()
	else :
		"sorry I do not recognise your choice"
		level1(userpixie)


def intro(pixie):
	global userpixie
	print '''

%s :

Right lets go home then! 
---------------------------------------------------------------------
But first.... we have to defeat George the dragon in the underground caves
'''% pixie.name
	level1(userpixie)

def welcome():
	print '''Welcome to Pixie Land!!!
--------------------------------------------------------------------------

Once upon a time there were four pixies trying to get home to PixieLand. To get there they have to cross,
treacharous lands. In the underground caves lives the ferocious George the Dragon.,
In the dark forest they must defeat Tina the cunning tiger.,
In the marshlands they must cross the river of Claudette the crocodile,
and in the mountains they must retrive the key to pixie land from around the neck of Edgar the Eagle
--------------------------------------------------------------------------'''
	print Aurelio
	print Gisella
	print Sam
	print Camille

	user_choice()
	intro(userpixie)

def user_level():
	if userland == None :
		intro(userpixie)
	elif userland == undergroundcaves:
		level1(userpixie)
	elif userland == darkforest:
		level2(userpixie)
	elif userland == marshlands:
		level3(userpixie)
	elif userland == mountains:
		level4(userpixie)

#ACTUAL GAME

welcome()
user_level()

































