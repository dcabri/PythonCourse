#!/usr/local/bin/python3
# 
# Write a simple Python program, implementing the "Guess the number" game, following the rules:
#The program will "think" of a number using the random module, as shown in code shown in next slide.
#You have to implement now only the first user move:
#Prompt the user for his/her guess
#If the user guess is equal to the machine number => print out a congratulation message!
#If the user guess is less than the machine number => print out "your guess is less than my number. Try again!"
#If the user guess is greater than the machine number => print out "your guess is greater than my number. Try again!"
#
#
from random import randint
machine_number = randint(1,10)

print("machine_number={}".format(machine_number))

### your code goes bellow:

num = int(input("Enter a number between 1 and 10 : "))
if  num == machine_number :
  print( "Congratulations, you guessed it!" )
elif  num < machine_number :
  print( "your guess is less than my number. Try again!" )
elif  num > machine_number :
  print( "your guess is greater than my number. Try again!" )
