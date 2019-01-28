
print(list(range(3))+list(range(3,5,1)))

### Let's have two list:
fruits = ["apple", "banana", "strawberry"]
numbers = [1, 2, 3]

### Membership Testing (in):
print("banana" in fruits)
# True

print("banana" in numbers)
# False

### Membership Testing (not in):
print("banana" not in fruits)
# False
### Let's have two list:
fruits = ["apple", "banana", "strawberry"]
numbers = [1, 2, 3]

### Membership Testing (in):
print("banana" in fruits)
# True

print("banana" in numbers)
# False

### Membership Testing (not in):
print("banana" not in fruits)
# False
### create list of numbers:
numbers = [1,2,3,4,5]

### index from start to end:
print(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4])
# 1 2 3 4 5

### create list of numbers:
numbers = [1,2,3,4,5]

### index from end to start:
print(numbers[-1],numbers[-2],numbers[-3],numbers[-4],numbers[-5])
# 5 4 3 2 1

#sliced = sequence[start:end:step]
str = "abcdefg"
print(str[2:4])
print(str[::2])
print(str[-1::-2])

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

print(list(matrix[:][1])+list(matrix[:][2]))


