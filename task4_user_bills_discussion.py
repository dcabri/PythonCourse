# Dictionary
user_data = {
'id' : [1,2,3],
'name' : ["Maria", "Ivan", "Asen" ],
'number' : ["+39587111111", "+39587222222", "+39587333333"],
}
# Dictionary
user_bill = {
'id' : [1,2,3],
'bill' : [25.50, 30.48, 5.98 ],
}
# Dictionary
user_bills = {
  '1' : 25.50,
  '2' : 30.48,
  '3' : 5.98, 
}
# List of tupples
user_set = [
(1, "Maria", "+39587111111" ),
(2, "Ivan", "+39587222222"),
(3, "Asen", "+39587333333"),
]
# List of tupples
bill_set = [
(1, 25.50 ),
(2, 30.48),
(3, 5.98),
]

# Todo print phone number 
for k,v in user_bills.items() :
	if v == max(bills.values()) :
		print(user_set[k])






test='''one two three four
    one two three four
    one two three two
    '''
listtest=test.split()
print(listtest)

sub='two'
print(listtest.count(sub))
sub='four'
print(listtest.count(sub))

for w in set(listtest) :
	print (w, listtest.count(w))