#Week5A 26.9.2019

>>> table = {
...     'Sjoerd' : 4127,
...     'jack'   : 4098,
...     'Dcab'   : 7678
... }
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
jack       ==>       4098
Dcab       ==>       7678

animals = { 'Tiger'  : 3000,
			'Lion'   : 3822,
			'Leopard': 400
			}


for animal,amount in animals.items():
	print(f'{animal:1} ==> {amount:1d}')

#

bird = 'sparrow'

print(f'My plane hits {bird} over the cloud.')
print(f'{bird}{bird}My plane hits {bird!r} over the cloud.')


#The String Format

print('We are the {} who say" {}!"'.format('Knights','Nee'))

print('This {food} is {adjective}{object}'.format(food='cake',adjective='very',object='good'))

Reading & Writing Files

f = open('workfile', 'w')

with open('workfile') as f:
	read_data = f.read()
f.close()