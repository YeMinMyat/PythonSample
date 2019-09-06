def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()
fib(90)
	0 1 1 2 3 5 8 13 21 34 55 89 

	def fib2(n):
		result = []
		a, b = 0, 1
		while a < n:
			result.append(a)
			a, b = b, a + b
		return result

	f100 = fib2(100)
	f100
	[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

i = 5

def f(arg=i):
	print(arg)

i = 6
f()

