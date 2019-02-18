class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)


class Manager():
  def __init__(self, name, age, skills):
    self.name = name
    self.age = age
    self.skills = skills

  def get_managed_names(self):
    names = ''
    for dev in self.skills :
      names+=f"{dev.name} "
    return names

  def __str__(self):
    return "{} is {} years old and manages {}".format(self.name,self.age, self.get_managed_names)


angel = Manager("Angel",75,('Mac','Windows'))
pesho = Manager("Pesho",25,['Java','html'])

print(angel)
print(pesho)



print("--------")


class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  """docstring for Employee"""
  def __init__(self, name, age, salary):
    super().__init__(name,age)
    self.salary = salary

  def __str__(self):
    # return super().__str__() + ". Has salary: {}".format(self.salary)
    return Person.__str__(self) + ". Has salary: {}".format(self.salary)


pesho = Employee("Pesho",25, 3500)
print(pesho)


print("--------")

class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  def __init__(self,name,age,skills):
    Person.__init__(self,name,age)
    self.skills = skills

  def skills_len(self): # returns number of object skills
    return len(self.skills)

  def __str__(self):
    return "{} is  employee".format(self.name)
  
maria = Person("Maria", 20)
pesho = Employee("Pesho",25,['Java','C++'])

print(maria)
print(pesho)
print(pesho.skills_len())

class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  def __init__(self,name,age,skills):
    Person.__init__(self,name,age)
    self.skills = skills

  def skills_len(self): # returns number of object skills
    return len(self.skills)

  def __str__(self):
    return super ().__str__() + " and is an employee"
  
maria = Person("Maria", 20)
pesho = Employee("Pesho",25,['Java','C++'])

print(maria)
print(pesho)
print(pesho.skills_len())

class Person():
  """docstring for Person"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{} is {} years old".format(self.name, self.age)

class Employee(Person):
  """docstring for Employee"""
  def __init__(self, name, age, salary):
    super().__init__(name,age)
    self.salary = salary

  def __str__(self):
    # return super().__str__() + ". Has salary: {}".format(self.salary)
    return Person.__str__(self) + ". Has salary: {}".format(self.salary)

  def __add__(self,other):
    return self.salary + other.salary


pesho = Employee("Pesho",25, 3500)
maria = Employee("maria",20, 2500)
print(pesho)
print(maria)

print("pesho + maria = ",pesho + maria)
# pesho + maria =  6000


class Duck:
   def quack(self):
      print('Quack, Quack')

class Goose:
   def quack(self):
      print('Quack!')

def quack(obj):
   obj.quack()


donald = Duck()
lea = Goose()

quack(donald)
quack(lea)












