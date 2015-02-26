class Store(object):
	def __init__(self, products, shopping_cart = 0, payment = 0, customer = 0):
		self.products = products
		self.shopping_cart = shopping_cart
		self.payment = payment
		self.customer = customer


class Product(Store):
	def __init__(self, product, name, weight, price, brand, area):
		self.product = product
		self.name = name
		self.weight = weight
		self.price = price
		self.brand = brand
		self.area = area

inventory = [
	Product("milk", "- Mollys full fat milk", "1 pint","$1.99", "Mollys", "dairy"), 
	Product("eggs", "- Farm fresh eggs", "1 dozen", "$3.24", "The Red Farm", "dairy"),
	Product("wholewheat bread", "- Dave's Killer Bread wholewheat bread", "400 grammes", "$4.99", "Dave's Killer Bread", "Bakery"),
	Product("chocolate chip cookie", "- Dan's best chocolate chip cookie", "100 grammes", "$0.99", "Dan's", "Bakery"),
	Product("green beans", "- Farm fresh green beans", "250gr", "$4.99", "farmfresh", "produce"),
	Product("bananas", "- Individual banana", "200gr", "$0.19", "African", "produce"),
	Product("sparkling water", "- San Pelligrino Sparkling water", "1 litre", "$2.09", "San Pelligrino", "Beverages"),
	Product("Apple Juice", "- Treetop Apple Juice", "1 litre", "$3.45", "Treetop", "Beverages")]
g_store = Store(inventory)


class Shopping_cart(Product):
	def __init__(basket):
		self.basket = basket
	
	def new_item_in_basket():
		new_item_in_basket = raw_input("Would you like to add %s to your basket" % (Product.name)).lower
		if answer == "yes" or answer == "y":
			print "You have added %s to your basket''' %" % (Product.name)
		elif answer == "no" or answer == "n":
			print "You have not added %s to your basket" % (Product.name)
		else :
			print "Sorry I didn't understand"
	
	
class Customers(object):
	def __init__(self, average_spend = 0, payment = 0):
		self.average_spend = average_spend
		self.payment = payment

	def get_customer(self):
		customer_name = raw_input("What is your name?\n")
		print "Welcome %s" % (customer_name)

#Script

Welcome = '''
----------------------------
Welcome to The Grocery store 
----------------------------
'''

List_of_products = '''
---------------------------
Here are the list of products we stock :
---------------------------
'''


#functions

def Welcome_greeting(cust):
	print Welcome
	cust.get_customer()

def Search(item):
	for i in g_store.products:
		if item == i.product or item == i.brand or item == i.name:
			return i 

	return None

# def search(Product):
#     for name in Product:
#         if name == x:
#             return True
#     return False
# def checkout

#Actual Shopping experience
customer = Customers()

Welcome_greeting(customer)

print List_of_products
for product in g_store.products:
	print product.name
print '''
------------------------------
'''

item = raw_input(" What would you like to add to your basket?  ").lower()
found = Search(item)
if found:
	print found.product
	print found.price
	
else:
	print "We don't have that item in stock "
	# print item = raw_input(" What would you like to add to your basket?  ").lower()

print '''
------------------------------
'''
basket = raw_input( "Would you like to add this to your basket?  ")














