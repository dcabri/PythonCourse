# OOP explained
#object_name = ClassName()

# create Person class (still dummy):
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return "name = {}\nage = {}\n".format(self.name, self.age)
  def __repr__(self):
    return """# This is representation of an object:
    obj = Person()
    obj.name = {}
    obj.age = {}""".format(self.name, self.age)
  def greet(self):
    print("Hi there! I'm", self.name)
  name = "Anonymous"
  age = 100

# create objects of class Person:
#pesho = Person()
#maria = Person()
maria = Person("Maria Popova", 25)
# let's check:
#print( type(pesho) )
print( type(maria) )
print(maria)
# <class '__main__.Person'>
# <class '__main__.Person'>
maria.name = 'Maria Popova'
print(maria.name, maria.age)

# read from attribute:
mn = maria.name
print(mn)
print(maria.__dict__)
maria.greet()


class Person:
  count=1
  def __init__(self, name, age):
    self.count+=1
    self.name = name
    self.age = age
    #print(f'Object {Person.count} is created')

  def greet(self):
    print("Hi there! I'm {}, {} years old!".format(self.name, self.age))

  def __str__(self):
    return "name = {} & age = {}\n".format(self.name, self.age)

  def __repr__(self):
    return """# This is representation of an object:
    obj = Person()
    obj.name = {}
    obj.age = {}""".format(self.name, self.age)

maria = Person("Maria Popova", 25)
pesho = Person("Pesho", 27)

#maria.greet()
#pesho.greet()

#print(maria.__dict__)
#print(maria.__str__())
#print(maria.__repr__())

#print(pesho.count)
print(maria)


def foo(x):
  def bar(y):
    print(y-x)
  return bar
tmp=foo(2) #foo(2) is function definition
tmp(3)
foo(2)(6)

class A():
  count = 0
  other=0
  def __init__(self):
    A.count+=1
    self.other+=1
  @classmethod 
  def foo():
    pass

a1=A()
a2=A()
a3=A()
print(A.count)
print(A.other) # provides the number of instances created of A

class Person():
  count = 0

  @classmethod
  def increment_counter(cls):
    cls.count += 1
    print("count:",cls.count )

  def __init__(self, name, age):
    self.name = name
    self.age = age

    self.increment_counter()
    # attach count to an object
    self.count = Person.count

p1=Person
p2=Person
p3=Person
print()

class A():
  @staticmethod
  def staticMethod():
    print("STATIC method fired!")
    print("Nothing is bound to me (but I'm defined inside a class)")
    print("~" * 30)

  @classmethod
  def classMethod(cls):
    print("CLASS method fired!")
    print(str(cls) + " is bound to me")
    print("~" * 30)

  # normal method
  def normalMethod(self):
    print("'normalMethod' fired!")
    print(str(self) + " is bound to me")
    print("~" * 30)


a = A()
a.staticMethod()
a.classMethod()
a.normalMethod()


