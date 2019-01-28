#!/usr/local/bin/python3
#
# sum only even numbers in [1..10]
#
i = 0
sum = 0
while i <= 10 :
  if i%2 == 0 :
    sum += i
  i+=1

print("sum = ", sum)

sum = 0
for i in [0,1,2,3,4,5,6,7,8,9,10]:
	if i%2==0:
		sum += i
print("sum = ", sum)










