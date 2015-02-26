people = {
"Bob" :{"name" : "Bob", "age" : 22},
"Carol" :{"name" : "carol", "age" : 47}, 
"Justin": {"name" : "Justin", "age" : 14}
}
print people

# if "Bob" in people :
# 	print "bob"
# elif "Carol" in people :
# 	print "carol"
# else :
# 	print "justin"

# While "Bob" = "name" :
# 	print "bob"

x = "name"
y = "age"

for x in people:
    print x


for person in people:
	print person[0], person[1]

my_dict = {
'key1': 'value1',
'key2': 'value2',
'key3': 'value3'
}
for item in my_dict:
	print item

key3
key2
key1


for index, person in people.items():
	print index, person["ag e"]

