#!/usr/local/bin/python3
#
# sum only even numbers in [1..100]
#
i = 1
sum = 0
while i <= 100 :
  mod = i % 2
  if mod <= 0 :
    sum += i
  i+=1
print("sum = ", sum)

