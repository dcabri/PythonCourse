def greet(name):
  print("Hello, {}".format(name))

class A:
  pass
#a function can be assigned to variable:
a=A()
foo = greet
greet("Maria")
foo("Pesho")
print(greet.__dir__())
print(a.__dir__())
#OUTPUT
# Hello, Maria
# Hello, Pesho
# a function can be passed as argument to another function
def wrapper(f, n):
  f(n)
wrapper(greet, "Alex")

#OUTPUT
# Hello, Alex
def greet_wrapper(name):
  def wrapper():
    print("Hello, {}".format(name))

  return wrapper

greet = greet_wrapper("Viktor")
greet()

def stars_decorator(f):
  def wrapper():
    print("*" * 50)
    f()
    print("*" * 50)

  return wrapper

def greet():
  print("Howdy World!")

# let's decorate greet:
greet = stars_decorator(greet)

# and use it:
greet()
def stars_decorator(f):
  def wrapper(n):
    print("*" * 50)
    f(n)
    print("*" * 50)
  return wrapper
# let's decorate greet:
@stars_decorator
def greet(name):
  print(f"Howdy World! {name}")
# and use it:
greet('Maria')

#lambda  parameter_list: expression
# = 
#def some_func(arguments):
#  return expression

def foo(x,y):
  # print (x**2+y**2)
  return x**2+y**2
# = 
bar = lambda x,y: x**2+y**2
print (foo(2,3))
print(bar(2,3))

bar = lambda x,y:x+2
print(bar(3,2))

def foo(f,a,b):
  f(a,b)

foo(lambda x,y : x+y, 2,3)

l = [1,2,3]
even_l = []
for i in l:
  if i%2 == 0:
    even_l.append(i)
print( even_l )
#    =
def is_even(i):
  if i%2 == 0:
    return True
  else:
    return False
even_l = filter( is_even, l )
print(list(even_l))
#    =
even_l = filter(lambda i: i%2==0,l)    
print(list(even_l))

names = ["Ivan", "", "Alex", "", "Maria", "Angel", ""]
not_empty_names = filter(lambda s: s, names)
print( list(not_empty_names) )
filtered_names = filter(lambda s: s and s[0]=="A", names)
print( list(filtered_names) )
#
filtered_names = filter(lambda s: len(s)==4, names)
print( list(filtered_names) )
#

#if cond1:
#  body1
#else:
#  body2
#       =    
# x = body1 if cond1 else body2
# Print non-zero numbers
numbers = [1,-1,0,2,3,0]
not_empty_nr = filter(lambda s: s, numbers)
print(list(not_empty_nr))

# Print squared numbers
numbers = [1,2,3,4,5]
numbers2 = [5,4,3,2,1]
sqr_numbers = map(lambda x:x**2, numbers)
print( list(sqr_numbers) )
#[1, 4, 9, 16, 25]
mynumbers = map(lambda x,y:x+y,numbers,numbers2)
print(list(mynumbers))
#
letters = map(chr, range(1040, 1072))
print( list(letters) )
#['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

from functools import reduce
l=[1,2,3,4]
l2=reduce( lambda x,y: x+y, l )
# prints (((1+2)+3)+4)
print(l2)
l=[8,2,0,2]
l2=reduce(lambda x,y: x/y, filter(lambda x:x,l))
print(l2)

res = reduce(lambda a,b: a+b, range(11))
print(res)

l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,2,3]
l = map(lambda *t: reduce(lambda a,b: a+b, t) , l1, l2,l3)
print( list(l) )




