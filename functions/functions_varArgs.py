# VarArgs parameters

# def total(a=5, *numbers, **phonebook):
# 	print('a',a)

# 	for single_item in numbers:
# 		print('single_item',single_item)

# 	for firsts_part,second_part in phonebook.items():
# 		print(firsts_part,second_part)

# total(10, 1, 2, 3,Jack=1123,John=2231,Inge=1459)

# def studentbook(a=5, *students, **contact):
# 	print('a',a)

# 	for single_item in students:
# 		print('single_item',single_item)

# 	for firsts_part,second_part in contact.items():
# 			print(firsts_part,second_part)

# studentbook(1,3,4,63,Mg=1102,Aye=2203,Aung=449)

#Return statement

# def maximum(x, y):
# 	if x > y:
# 		return x
# 	elif x == y:
# 		return 'The numbers are equal'
# 	else:
# 		return y

# print(maximum(3,8))


def print_max(x, y):
	'''Print the maximum of two numbers

		The Two values must be integers.
	'''

	x = int(x)
	y = int(y)

	if x > y :
		print(x, 'is maximum')

	else:
		print(y,'is maximum')

print_max(5,9)

print(print_max.__doc__)

def paper():
	''''''