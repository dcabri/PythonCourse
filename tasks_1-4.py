x
#-----------------------------------
#2 lists
first_names = ['ivan','maria','petar']
sur_names = ['ivanov', 'popova', 'petrov']

###### Start of task 1 #############
#contactenate 2 lists
# names = first_names + sur_names

##Task1

#print (names)  <-- Task1

###### EOT #############

###### Start of task 2 #############

#need to see if one list longer than the other...
if len(sur_names) != len(first_names):
    print('That is not how this works, you know!')
    exit(0)

#Using index
for i in range(len(sur_names)):
    print (first_names[i],sur_names[i],end=' ')
print ('\n')

###### Start of task 3 #############
sum_even_numbers = 0

for number in range(1000,1201,2):
    sum_even_numbers += number
print (sum_even_numbers)
    

#### Task 3 done #####

###### Task 4 Start #####################
results = []
words = ["dog", "talent", "loop", "aria", "tent", "choice"]
for index in range(len(words)):
    element = words[index]
    if element[0] == element[-1]:
        results.append(words[index])
print (results)

######### Task 4 End ######################

