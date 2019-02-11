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
    return "{} is {} years old and manages {}".format(self.name,self.age, get_managed_names)


angel = Manager("Angel",75,('Mac','Windows'))
pesho = Manager("Pesho",25,('Java','html'))

print(angel)
print(pesho)



--------


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


