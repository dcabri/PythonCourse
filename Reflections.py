class Person:
  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height
  def greet(self):
  	print("Hello")



maria = Person("Maria Popova", 25, 103.23)

# print(dir(maria))

print(type(maria))
# <class '__main__.Person'>
print(type(3))

Employee = type('Employee', (object,), dict())
pesho = Employee()
print(type(pesho))
# <class '__main__.Employee'>
Employee = type('Employee', (Person,), dict())
pesho = Employee("Pesho", 30,123.2)
print(type(pesho))
# <class '__main__.Employee'>
print(id(1))
x = 1
print(id(x))
y=x
print(id(y))
#11065920
#11065920
#11065920
del maria.name
print(hasattr(maria,"name"))
print(hasattr(maria,"surname"))
#True#False
print(getattr(maria, "age"))
setattr(maria, "surname", "Popova")
maria.bla = '12'
print(getattr(maria, "surname"))
print(maria.bla)




print(type(3.23))
print(dir(3.23))
print(isinstance(3.23, float))
print(issubclass(float, float))
print(issubclass(float, Person))

class Employee(Person):
  def __init__(self, name, age, height,cv):
    super().__init__(name, age, height)
  	#Person.__init__()
    self.cv=cv

pesho = Employee("Pesho",32,323.2,"CV")

print(issubclass(Employee, Person))

import inspect

def foo():
  func_name = inspect.stack()[0][3]
  caller_name = inspect.stack()[1][3]
  print("I'm {}.\n{} called me!".format(func_name,caller_name))
  print(inspect.stack()[0][3])

def bar(f):
  f()
  print(inspect.stack())

bar(foo)
# I'm foo.
# bar called m

print(dir(inspect))

