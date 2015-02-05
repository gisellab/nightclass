import random

class Monster():
	def __init__ (self, nickname, attack, element, species, health):
		self.nickname = nickname
		self.attack = attack
		self.element = element
		self.species = species
		self.health = health
	
	def __str__(self):
		return " %s is a %s. As a %s monster whose defence mode is %s" % (self.nickname, self.species, self.element, self.attack)

george = Monster("George", {"swipes":10, "pushes":20, "throws":30, "bites":50, "incinerates":100}, "Fire", "Dragon", 100)
tina = Monster("Tina", {"swipes":10, "pushes":20, "throws":30, "claws":50, "bites":100}, "Earth", "Tiger", 100)
claudette = Monster("Claudette",{"swipes":10, "snaps":20, "claws":30, "bites":50, "drowns":100}, "Water", "Crocodile", 100)
edgar = Monster("Edgar", {"swipes":10, "snaps":20, "claws":30, "pecks":50, "drops from a height":100}, "Air", "Eagle", 100)


class Pixie():
	def __init__(self, name, skill, element, healing, health):
		self.name = name
		self.skill = skill
		self.element = element
		self.healing = healing
		self.health = health

	def __str__(self):
		return " %s is a %s Pixie whose skill is %s" % (self.name,self.element, self.skill)
	
Aurelio = Pixie("Aurelio", {"swipes":30, "pushes":30, "throws":40, "freezes water":50}, "water", 20, 100)
Gisella = Pixie ("Gisella", {"swipes":10, "pushes":10, "throws":20, "blows wind":40}, "air",60, 100)
Sam = Pixie ("Sam", {"swipes":10, "pushes":20, "throws":50, "creates fireball":40}, "fire", 30, 100)
Camille = Pixie ("Camille", {"swipes":5, "pushes":10, "throws":20, "creates tremors":70},"earth",60, 100)

class Lands():
	def __init__(self, monsters):
		self.monsters = monsters

underground_caves = Lands(george)
dark_forest = Lands(tina)
marshlands = Lands(claudette)
mountains = Lands(edgar)




#actual game

print ''' ----------------------------------------------------------------
Welcome to Pixie Land!!!
--------------------------------------------------------------------------

Once upon a time there were four pixies trying to get home to PixieLand. To get there they have to cross,
treacharous lands. In the underground caves lives the ferocious George the Dragon.,
In the dark forest they must defeat Tina the cunning tiger.,
In the marshlands they must cross the river of Claudette the crocodile,
and in the mountains they must retrive the key to pixie land from around the neck of Edgar the Eagle
--------------------------------------------------------------------------'''

print Camille.skill

print Aurelio
print Gisella
print Sam
print Camille


def user_choice():
	user_name = raw_input("choose which pixie you want to lead: ").lower()
	if user_name == "aurelio":
		print "Great! Welcome to the game "
	elif user_name == "gisella":
		print "Great! Welcome to the game "
	elif user_name == "sam":
		print "Great! Welcome to the game "
	elif user_name == "camille":
		print "Great! Welcome to the game "
	else:
		print "Sorry we do not recognize your choice"
		user_choice()


user_choice()

print ''' Right lets go home then! 
---------------------------------------------------------------------
But first.... we have to defeat George the dragon in the underground caves
---------------------------------------------------------------------
Underground caves'''

print ''' We walk through the dark caves for half a mile until we encounter a fork? 
---------------------------------------------------------------------
'''

def fork_choice():
	fork_input = raw_input("should we go left or should we go right? (l/r) ").lower()
	if fork_input == "left" or fork_input == "l":
		print "oh no you walked for 200 metres but its a dead end . Lets go back"
	elif fork_input == "right" or fork_input == "r":
		print "Oh no! There is George the Dragon - quick get out of the way! "
	else :
		"Thats not an option!"
		fork.choice()

fork_choice()

def 






















