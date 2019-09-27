with open('test.txt', 'r') as f:

	# scope_to_read = 1
	# f_text = f.read(scope_to_read)

	# while len(f_text) > 0:
	# 	print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

	# for n in f:
	# 	print(n,end='')

	# f_text = f.read(1000)
	# print(f_text,end='')

	# f = open('test.txt', 'r')
	# print(f.name)

	# f.close()	

	f = open('test2.txt', 'r')
	print(f.name)

	for n in f:
		print(n,end='')

	f.close()