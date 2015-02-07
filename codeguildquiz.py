#1
print "Hello World"

#2-5
fruit = ['Apples','Oranges', 'Bananas']
print fruit
fruit[1] = 'Grapes'
print fruit

#6

people = {"Bob" :{"name" : "Bob", "age" : 22}, "Carol" :{"name" : "carol", "age" : 47}, "Justin": {"name" : "Justin", "age" : 14}}
print people

#7

b = 10
c = 5
d = 3
e = 6
f = 15
g = b + c

print g

#8 not sure how to do this one
# def add(a, b):
#    return int(a) + int(b)
#    print (a + b)

#  def add 

#9



#10 

x = range(1, 101)
print x


#11 to 17
class customer():
	def __init__ (self, name, age, location, creditscore):
		self.name = name
		self.age = age
		self.location = location
		self.creditscore = creditscore

	def __str__(self):
		print " %s is %d from %s with a credit score of %s" % (self.name, self.age, self.location, self.creditscore)


Jessie = customer("Jessie", 22, "washington", "718")

print Jessie.name
print Jessie.location
print Jessie.creditscore

Jessie.creditscore = 780

print Jessie.creditscore

