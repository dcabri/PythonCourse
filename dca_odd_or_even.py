#!/usr/local/bin/python3
#
# Write a program, which will print out for any integer number if it is odd or even.
#
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
