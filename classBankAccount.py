class BankAccount():
  def __init__(self, owner, balance):
    self.owner = owner
    self.__balance = balance

  def change_balance(self,amount):
    print(f"{self.owner} balance is {self.__balance}")
    self.__balance=amount

  def deposit(self,amount):
    self.__balance+=amount
    #print(self.balance)

  def withdrawal(self,amount):
    self.__balance-=amount
    #print(self.balance)

  def __str__(self):
  	return f"{self.owner} balance is {self.__balance}"


maria_account = BankAccount("Maria", 1_300)
pesho_account = BankAccount("Pesho", 100)


print(maria_account)
maria_account.deposit(100)
print(maria_account)
#print("Hi there! Maria's account balance is now {}.".format(maria_account.balance))
maria_account.withdrawal(100)
#print("Hi there! Maria's account balance is now {}.".format(maria_account.balance))

print(maria_account)
maria_account.__balance = 0
print()
print(maria_account.__dir__())
print()
print(maria_account.__dict__)
#name	Public	Attributes, that can be freely used inside or outside of a class definition.
#_name	Protected	Protected attributes should not be used outside of the class definition, unless inside of a subclass definition.
#__name	Private	This kind of attribute should be inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.
print(maria_account.__sizeof__())
print(id(maria_account))

num=2
def foo():
  print('foo')

foo.id=1
print(id(foo))
print(foo.__dict__)
print(foo.__dir__())
print('\n\n')
print(dir(2))
print('\n\n')
class A:
	pass

A.id=1
print(A.__dict__)

