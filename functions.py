
## print(help(max))

def f(x):
	''' This is a help part of the function
	    You can write something here that explains the function
	'''
	print(x)


#print(help(f))

y=f(3)
print(f(3))


# read user input
def read_user_input() :
	pass
    

# Calc BMI
def calculate_BMI() :
	pass

print('qqq')
def greet():
    """Just prints hello"""
    print("Hello")

greet()
#print(greet())
# print result

def add(x=0,y=0):
  """ subtracts y from x and prints the result """
  print(x + y)

add(20, 22)
add(123, 321)
add(16, 10)

def sub(x=0,y=0):
  """ subtracts y from x and prints the result """
  print(x - y)

def greet(name="Nobody", surname="", age=0, upass=""):
  """ greets a user """
  print("Hello {} {}".format( name, surname))

greet(name="Maria", surname="Valeris")
greet()

# The below is UNpacking
def foo(*args):
  print(args)

foo(1)
foo(1,2)
foo(1,2,3)

names = [ '1', '2', '3' ]
for i in names :
	print("{}".format(i))

print( names)
print (*names)
a,b,c = names
print(b)

# The below is packing
def add(p1, *args):
  print(p1, end=", ")
  print(args)

add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

print ("*"*20)

def add(*args) :
  #print(args)
  #o=0
  #for i in args :
  #  o += i
  #print(o)
  print(sum(args))

add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

print ("*"*20)

#dict = {
#	'a':3,
#	'b':2,
#	'c':1,
#}

def foo(**kwargs):
  print(sum(kwargs.values()))

foo(a=1, b=2)


def my_func(p1,p2,p3):
  print(p1, p2, p3)

args = [1,2,3]
my_func(*args)
my_func(*[3,4,5])

def menu_print(fruit, price):
  print("{:.<20s}{:.2f}".format(fruit,price))

menu_print(**{
  "price": 2.5,
  "fruit": "apple"
})
menu_print('apple', 2.5)

print ("*"*20)

def add(x,y):
  return x+y
print(add(2,4)**2)

def pow(a) :
    return a*a
    print('hi there this is not being printed')
print (pow(3)+pow(5))


x=1
def outer():
  x=2

  def inner():
    # nonlocal x
    # global x
    x = 3
    print(f'x = {x} in inner')

  inner()
  print(f'x = {x} in outer')

outer()
print(f'x = {x} in global')
















