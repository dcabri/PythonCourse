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


