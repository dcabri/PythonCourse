distances_from_sofia = [
    ("Bansko", 97),
    ("Brussels", 1701),
    ("Alexandria", 1403),
    ("Nice", 1307),
    ("Szeged", 469),
    ("Dublin", 2479),
    ("Palermo", 987),
    ("Moscow", 1779),
    ("Oslo", 2098),
    ("London", 2019),
    ("Madrid", 2259),
]

close_distances= []

for index in range(0,len(distances_from_sofia)):
    element = distances_from_sofia[index]
    if int(element[1]) < 1500:
        close_distances.append(distances_from_sofia[index])
print('Close distances are:',*sorted(close_distances, key=lambda dist: dist[1]),sep='\n ')

#
#list.sort(key=lambda r:r[0])
#sort — A method that modifies the list in-place
#sorted() — A built-in function that builds a new sorted list from an iterable

#Lambda Functions
#A lambda is an anonymous function and an anonymous function is a function that is defined without a #name, this post seems to explain it pretty nicely.
#Lambda functions are nice for calling in-line because they only have one expression which is #evaluated and returned. They syntax for a lambda is:
#lambda arguments: expression
#
#
#import traceback, matplotlib.pyplot as plt
#from datetime import datetime
#f = open(‘Data.csv’,’r’)
#results = []
#downLines = f.readlines()
#f.close()
#for line in downLines:
# try:
#   splitLine = line.split(‘,’)
#   dateTime = datetime.strptime(splitLine[0], ‘ %m/ %d/%Y %I:%M:%S %p’)
#   results.append([dateTime, splitLine[1], splitLine[2], splitLine[3]])
# except:
#   print “Error:”
#   print traceback.format_exc()
#   continue
#results.sort(key=lambda r: r[0])
#downDate = [x[0] for x in results]
#downData = [y[1] for y in results]
#plt.plot(downDate, downData, label=’Data’)
#plt.legend()
#plt.show()
