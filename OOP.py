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
