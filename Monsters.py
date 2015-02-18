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
		return " %s is a %s, a %s monster whose defence moves include:" % (self.nickname, self.species, self.element)

george = Monster("George", {"swipes":10, "pushes":20, "throws":30, "bites":50}, "Fire", "Dragon", 100)
tina = Monster("Tina", {"swipes":10, "pushes":20, "throws":30, "claws":50, "bites":100}, "Earth", "Tiger", 100)
claudette = Monster("Claudette",{"swipes":10, "snaps":20, "claws":30, "bites":50, "drowns":100}, "Water", "Crocodile", 100)
# edgar = Monster("Edgar the Eagle", {"swipes":10, "snaps":20, "claws":30, "pecks":50, "drops from a height":100, }, "Air", "Eagle", 200, )

class MountainMonster(Monster):
	def __init__( self, nickname, attack, element, species, health):
		self.nickname = nickname
		self.attack = attack
		self.element = element
		self.species = species
		self.health = health
	

	def __str__(self):
		return " %s is a %s, a %s monster whose defence moves include :" % (self.nickname, self.species, self.element)


edgar = MountainMonster("Edgar", {"swipes":10, "snaps":20, "claws":30, "pecks":50, "drops from a height":100, "flys towards" : 20 }, "Air", "Eagle", 200)


class Pixie():
	def __init__(self, name, skill, element, healing, health):
		self.name = name
		self.skill = skill
		self.element = element
		self.healing = healing
		self.health = health

	def __str__(self):
		return "%s is a %s Pixie whose skills include : " % (self.name,self.element)
	
Aurelio = Pixie("Aurelio", {"swipes":30, "pushes":30, "throws":40, "freezes water":50}, "Water", 20, 200)
Gisella = Pixie ("Gisella", {"swipes":10, "pushes":10, "throws":20, "blows wind":40}, "Air",60, 200)
Sam = Pixie ("Sam", {"swipes":10, "pushes":20, "throws":50, "creates fireball":40}, "Fire", 30, 200)
Camille = Pixie ("Camille", {"swipes":5, "pushes":10, "throws":20, "creates tremors":70},"Earth",60, 200)

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

#narrative

welcomelevel = '''WELCOME TO PIXIE LAND!!!
--------------------------------------------------------------------------

Once upon a time there were four pixies trying to get home to PixieLand. 

To get back home they have to cross treacherous lands. 

In the UNDERGROUND CAVES lives the ferocious George the Dragon,

In the DARK FOREST they must defeat Tina the cunning tiger, 

In the MARSHLANDS they must cross the river of Claudette the crocodile,

and in the MOUNTAINS they must retrieve the key to PIXIE LAND from the nest of Edgar the Eagle

--------------------------------------------------------------------------'''



Welcomelevel1 = '''Right lets go home then! 
---------------------------------------------------------------------
But first.... we have to defeat George the Dragon in the Underground Caves
'''

opening_narrative_level1 = '''ENTERING THE UNDERGROUND CAVES

We walk through the dark caves for half a mile until we encounter a fork? 
---------------------------------------------------------------------
'''
closing_narrative_level1 = ''' 

----------------------------------------------------------------------
YES you defeated George the Dragon. 

Lets get out of the UNDERGROUND CAVES and into the DARK FOREST. 

Lets hope we don't meet Tina the Tiger!! 

-----------------------------------------------------------------------

''' 

opening_narrative_level2 =  '''ENTERING THE DARK FOREST

The pixies walk for half a mile until they encounter two dark paths...

----------------------------------------------------------------'''
closing_narrative_level2 = ''' 
------------------------------------------------------------------

YES you defeated Tina the Tiger. 

Lets get out of the DARK FOREST and into the MARSHLANDS.

Lets hope we don't meet Collette the Crocodile. 

-------------------------------------------------------------------
'''

opening_narrative_level3 = '''ENTERING THE MARSHLANDS 

The pixies walk for long time until they encounter two bridges over a murky river...

----------------------------------------------------------------'''
closing_narrative_level3 = ''' 

-------------------------------------------------------------------

YES you defeated Claudette the Crocodile. 

Lets get out of the MARSHLANDS and into the final land - the MOUNTAINS. 

Lets hope we don't meet Edgar the Eagle 

while we retrieve the key to PIXIE LAND!! 

-------------------------------------------------------------------
''' 

opening_narrative_level4 =''' ENTERING THE MOUNTAINS 

You are in the final land of the quest to get home to PIXIE LAND. 

Now for the final test. 

You must retrieve the key to open the door to PIXIE LAND. 

The key is in the eagle's nest. 

But since there are chicks why not make him 

fly away while you retrieve the key?

----------------------------------------------------------------'''
closing_narrative_level4 = '''

----------------------------------------------------------------

He flew away, quick GRAB THE KEY in the nest

Quick open the door to PIXIE LAND before Edgar comes back 

PHEW - We made it! 

---------------------------------------------------------------------
                    WELCOME HOME TO PIXIE LAND!!!
---------------------------------------------------------------------'''

#functions --------------------------------------------------

def user_choice():
	global userpixie 
	userpixie = raw_input("Choose which pixie you want to lead: ").lower()
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

def printattack(monster):
	for x in monster.attack:
		print " - %s" % x.title()
def printskill(pixie):
	for y in pixie.skill:
		print " - %s" % y.title()

def fork_choice(monster):
	fork_input = raw_input("should we go left or should we go right? (l/r) ").lower()
	if fork_input == "left" or fork_input == "l":
		print "oh no you walked for 400 feet but its a dead end . Lets go back"
		fork_choice(monster)
	elif fork_input == "right" or fork_input == "r":
		print "Oh no! There is %s - quick get out of the way! " % (monster.nickname)
	else :
		print "Thats not an option!"
		fork_choice(monster)

def fork_choice_mountain(mountainmonster) :
	fork_input = raw_input("should we go left, right or straight ahead (l/r/s) ").lower()
	if fork_input == "left" or fork_input == "l" :
		print "It looks like there is a sheer cliff ahead... Let's go back"
		fork_choice_mountain(mountainmonster)
	elif fork_input == "right" or fork_input == "r" :
		print "Oh no this is a dead end... Lets go back"
		fork_choice_mountain(mountainmonster)
	elif fork_input == "straight" or fork_input == "s" :
		print "Oh no! There is %s. Quick get out of the way! " % (mountainmonster.nickname)
		playlevel4(mountainmonster, userpixie)
	else:
		print "thats not an option "
		fork_choice_mountain(mountainmonster)

# def pixiehealthnumber(pixie) :


def playchoice(monster, pixie):
	play_choice = raw_input("Would you like %s to attack or to heal themself? (a,h) " % pixie.name).lower()
	if play_choice == "attack" or play_choice == "a":
		pixie_skill = random.choice(pixie.skill.keys())
		monster.health -= pixie.skill[pixie_skill]
		print "%s %s and hits %s for %d points. %s's health is now %d points" % (pixie.name, pixie_skill, monster.nickname, pixie.skill[pixie_skill], monster.nickname, monster.health)
	elif play_choice == "healing" or play_choice == "h" :
		pixie_healing = pixie.healing
		pixie.health += pixie_healing
		print " %s heals themself and adds %d to health. %s's health is now %d" % (pixie.name, pixie_healing, pixie.name, pixie.health)
	else :
		print "sorry I do not understand your statement"
		playchoice (monster, pixie)

def play(monster, pixie):
	while pixie.health > 0 and monster.health > 0 :
		monster_attack = random.choice(monster.attack.keys())
		pixie.health -= monster.attack[monster_attack]
		print "%s %s %s for %d points. %s's health is now %d points" % (monster.nickname, monster_attack, pixie.name, monster.attack[monster_attack], pixie.name, pixie.health)
		if monster.health <= 0 :
			print "you killed the monster"
		elif pixie.health <= 0 :
			print " Oh no you died. Start again "
			pixie.health = 200
			user_level()
		else:
			playchoice(monster, pixie)
	else :
		if monster.health <= 0 :
			print "you killed the monster"
		elif pixie.health <= 0 :
			print " Oh no you died. Start again "
			pixie.health = 200
			user_level()


def playlevel4(mountainmonster, pixie):
	# print("playlevel4 was called")
	global closing_narrative_level4
	while pixie.health > 0 and mountainmonster.health > 10 :
		mountainmonster_attack = random.choice(mountainmonster.attack.keys())
		pixie.health -= mountainmonster.attack[mountainmonster_attack]
		if mountainmonster.health <= 10 :
			print closing_narrative_level4
			exit()
		elif pixie.health <= 0 :
			print " Oh no you died. Start again "
			pixie.health = 200
			user_level()
		else :
			print "%s %s %s for %d points. %s's health is now %d points" % (mountainmonster.nickname, mountainmonster_attack, pixie.name, mountainmonster.attack[mountainmonster_attack], pixie.name, pixie.health)
			playchoice(mountainmonster, pixie)
	else :
		if mountainmonster.health <= 10 :
			print closing_narrative_level4
			exit()
		elif pixie.health <= 0 :
			print " Oh no you died. Start again "
			pixie.health = 200
			user_level()

#functions :player levels -----------------------------------------

def level4(pixie):
	global userland 
	global opening_narrative_level4
	mountain_level = raw_input( "Are you ready to climb the mountain? (y/n) ").lower()
	if mountain_level == "y" or mountain_level == "yes" :
		userland = mountains
		print opening_narrative_level4
		fork_choice_mountain(edgar)	
		print edgar
		printattack(edgar)
		playlevel4(edgar, userpixie)
		print closing_narrative_level4
	elif mountain_level == "n" or mountain_level == "no":
		userland = None
		print "Thankyou for playing the game"
		exit()
	else :
		print "sorry I do not recognise your choice"
		level4(userpixie)


def level3(pixie):
	global userland 
	global opening_narrative_level3
	global closing_narrative_level3
	marshlands_level = raw_input("Are you ready to enter the marshlands? (y/n) ").lower()
	if marshlands_level == "y" or marshlands_level == "yes" :
		userland = marshlands
		print opening_narrative_level3 
		fork_choice(claudette)	
		print claudette
		printattack(claudette)
		play(claudette, userpixie)
		print closing_narrative_level3
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
	global opening_narrative_level2
	global closing_narrative_level2
	darkforest_level = raw_input( "Are you ready enter the dark forest? (y/n) ").lower()
	if darkforest_level == "y" or darkforest_level == "yes" :
		userland = darkforest
		print opening_narrative_level2
		fork_choice(tina)	
		print tina
		printattack(tina)
		play(tina, userpixie)
		print closing_narrative_level2
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
	global opening_narrative_level1
	undergroundcaves_level = raw_input( "Are you ready enter the underground caves? (y/n) ").lower()
	if undergroundcaves_level == "y" or undergroundcaves_level == "yes" :
		userland = undergroundcaves
		print opening_narrative_level1
		fork_choice(george)	
		print george
		printattack(george)
		play(george, userpixie)
		print closing_narrative_level1
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
	print Welcomelevel1
	level1(userpixie)

def welcome():
	print welcomelevel
	print Aurelio
	printskill(Aurelio)
	print Gisella
	printskill(Gisella)
	print Sam
	printskill(Sam)
	print Camille
	printskill(Camille)

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

































