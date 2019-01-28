user_name = "ivan"

for i in range(len(user_name)):
  print("{} - {}".format(i, user_name[i]))


# l = [1,2,3]

# for i,el in enumerate(l)
#   print (f"{i} - {l[i]}")

for i,l in enumerate(user_name):
  print("{} - {}".format(i, l))

#list creates the list in memory identified by the formula tupple or range
### list from tupple:
point3d = (4, 0, 3)
point3d_list = list(point3d)
print(point3d_list)
# [4, 0, 3]

### list from range:
digits = range(0, 10)
digits_list = list(digits)
print(digits_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

### list from string:
user_name = "ada byron"

fruits = ["apple", "orange", "strawberry"]
### Delete a list item by index
del fruits[1]
fruits.append("plum")
fruits.insert(2, "NEW")
print(fruits)
str=list(user_name)
str.insert(2,'!')

# user_name.insert(2, "N") ->'str' object has no attribute 'insert'
print(str)
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#A list item can be any data type, including list, tuples and so on





