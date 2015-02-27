Classes

class Store(object):
	def __init__(self, products, shopping_cart = 0, payment = 0, customer = 0):
		self.products = products
		self.shopping_cart = shopping_cart
		self.payment = payment
		self.customer = customer


class Product(object):
	def __init__(self, name, price, inventory):
		self.product = product
		self.name = name
		self.price = price
		self.inventory = inventory
		
inventory = [
	Product("milk", "$1.99", 8), 
	Product("eggs", "$3.24", 8),
	Product("wholewheat bread", "$4.99", 8),
	Product("chocolate chip cookie", "$0.99" 8),
	Product("green beans", "$4.99",8 ),
	Product("bananas", "$0.19",8 ),
	Product("sparkling water", "$2.09",8),
	Product("apple juice", "$3.45", 8)]
g_store = Store(inventory)

class Customers(object):
	def __init__(self, average_spend = 0, payment = 0):
		self.average_spend = average_spend
		self.payment = payment

customer_list = [
Customers("Sally"),
Customers("David"),
]


itemname = None


class Shopping_cart(Product):
	def __init__(basket):
		self.basket = basket
	
	
