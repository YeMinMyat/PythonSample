#for statement

fruits = ['Apple', 'Banana', 'coconut']
for f in fruits:
	print(f, len(f))

for i in range(8,20):
	print(i)

#answer:8,9,10,.........19
for i in range(10):
	print(i)

#answer:0,1,2,3->9

a = ['Mary', 'Had', 'A', 'Little', 'Boy']
for i in range(len(a)):
	print(i,a(i))
#answer:
		0 Mary
		1 Had
		2 A
		3 Little
		4 Boy

for num in range(2, 10):
	if num % 2 == 0:
			print("Found an even number", num)
			continue
			print("Foung a number", num)

Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9 

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equal', x, '*', n//x)
			break
		else:
			print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equal 2 * 2
5 is a prime number
6 equal 2 * 3
7 is a prime number
8 equal 2 * 4
9 equal 3 * 3