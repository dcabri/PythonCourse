names = []

cycles=int(input('How many names are you going to enter?'))
for i in range(0,cycles):
    names.append(input("Enter a name, please:"))
names.sort()
print ("The names you've entered are: ",names)