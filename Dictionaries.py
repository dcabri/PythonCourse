
#Set
#Dictionary
# 
# list:
fruits = ["apple", "banana", "strawberry", "banana", "orange"]
# tupple:
point3d = (4, 0, 3)
# range:
digits = range(0,10)
# string:
user_name="ada byron"
#
#Concatenation	+
#Repetition	*
#Membership Testing	in (not in)
#Indexing	[i]
#Slicing	[i:j]
#x in sequence
#a[:] copy whole array
#print("{} - {}".format(i, user_name[i]))
#fruits.insert(2, "NEW")
#del fruits[1]
#fruits_tuple = tuple(fruits)
#apples_price = prices.pop('apples')
#fruits = prices.keys()
## dict_keys(['apples', 'oranges', 'bananas'])
#prices["new_key"]="new value"
#prices.values()
# An unordered collection of unique and immutable objects.
#Note that the set itself is a mutable object.
#A Set can not contain duplicate items! Dictionaries can. 
#set = {value1, value2, valueN}
#union2 = set1.union(set2)
#intersec2 = set1.intersection(set2)
#dif1 = set1.difference(set2)
#sym_dif = set1.symmetric_difference(set2)


prices_list=[2.50, 2.40, 3.50, 2.4]

prices_dict = {
 'apple': 2.50,
 'orange': 2.43,
 'banana':3.50,
 ('apples','germany'): 5,
 ('A',2):4,
 1:2,
 'orange': 20.43,
 'strawberry':3.4,
}

print(prices_list[1])
print(prices_dict['banana'])
print(prices_dict['orange'])
prices_dict['orange'] = 99
print(prices_dict['orange'])
prices_dict['plums'] = 4.30
print(prices_dict['plums'])
del prices_dict['banana']
print( prices_dict )
print( '{:.1f}'.format(prices_dict[1]) )


print( prices_dict )
orange_price=prices_dict.pop('orange')
print( prices_dict )
print( orange_price )
print()
for v in prices_dict:
  print(v)
print()
prices_keys = prices_dict.keys()
print("@keys:", prices_keys)

price_list = prices_dict.values()
print("@list:", prices_list )

prices_items = prices_dict.items()
print("@items:",prices_items)
print()

for v in prices_dict:
	print('v in prices_dict {} - {:.2f}'.format(v, prices_dict[v]) )
print()

for v in prices_dict.keys():
	print('v in prices_dict.keys {}'.format(v) )
print()

for key, value in prices_dict.items():
	print('key, value in prices_dict.items {} - {:.2f}'.format(key, value) )
print()
# The Python2 equivalents are viewkeys(), viewvalues() and viewitems() methods.

price_set = { 2.50, 3.40, 3.50, 3.4 }
mylist = set(prices_list)
print(type(mylist))
print(mylist)


#Sets vs Dictionaries
#Similarities:
#. Both are unordered collection of objects (values).
#. Both are mutable (add/remove/modify elements)
#. Both use curly braces for their literals.
#Differences:
#. A Set can not contain duplicate items! Dictionaries can.
#. A dictionary is a collection of key:value pairs.
#. Set is just a values collection
int_numbers = {1, 2, 3, 4, 5}
int_dup_numbers = {1, 2, 3, 1, 2, 4, 3, 5, 1, 2, 3}
print(int_numbers == int_dup_numbers) #only unique numbers will be printed
print()

set1 = {6, 2, 3, 4}
set2 = {5, 4}

union1 = set1 | set2 # or union1 = set1.union(set2)
print(union1)        # all unique elements in set1 and set2
intersec1 = set1 & set2 # intersec1 = set1.intersection(set2)
print(intersec1)    # unique elements in set1 and set2
dif1 = set1 - set2 #dif1 = set1.difference(set2)
print(dif1)          # unique elements in set1 not in set2
sym_dif = set1.symmetric_difference(set2)
print(sym_dif)      # unique elements in set1 and set2







