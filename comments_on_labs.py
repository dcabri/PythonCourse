# sorted function in Python
student_scores =  {
	'I1van'  : 5.0,
	'A2lex'  : 3.5,
	'M3aria' : 4.0,
	'G4eorgy': 2.5,
	'J5ohn'  : 4.0,
}

def my_sort_value(item) :
	print(f'item: {item}')
	return item[1]

def my_sort_value_lastletter(item) :
	print(f'item: {item}')
	return item[0][-1]

my_sort_value_lastletter = lambda item:item[0][-1]

srt=sorted(student_scores.items(), key=my_sort_value_lastletter)
#Lamda functionas are always anonymous, you can't give the functio a name
srt=sorted(student_scores.items(), key=lambda item:item[0][-1])

print (srt)

# 