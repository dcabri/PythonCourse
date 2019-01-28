# list:
fruits = ["apple", "banana", "strawberry", "banana", "orange"]
l1=[[1,2], 2, 3, 'a']
l2=[1,1,1]
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]
print(matrix[2][1])

# retrieve last item in the list:
itemN = fruits[-2]
print (itemN)

# range:
digits = range(0,10)
# string:
user_name="ada byron"

fruits[0]='jaws'
print(fruits[0])


for i in [0,1,2]:
  for j in [0,1,2]:
    print (matrix[i][j])

for i in matrix:
  for j in i:
    print (j)

# print sum of left diagonal
# TASK !!
j=0
sum=0
for i in matrix:
  sum+=i[j]
  j+=1
print(sum)

# tupple:
point3d = (4, 0, 3)
# point3d[1]=1 cannot be done, 'tuple' object does not support item assignment

print (type (matrix) )
t=(1,) #notice the comma!
print (type (t) )

#range(stop)
#range(start, stop[, step])
r1=range(1,6,1)
print (list(r1))

for i in range(2,11,-2):
    print(i, end=" ")

str="123"
for i in range(len(str)) :
    print(i)





