#17.10.2019 Functions

# def say_hello():
# 	print("Hello World")


# say_hello()



# #Function_param.py):

# def print_max(a,b):
# 	if a > b:
# 		print(a, 'is maxium')
# 	elif a == b:
# 		print(a,'is equal to' ,b)
# 	else:
# 		print(b,'is maxium')

# print_max(3, 4)

# x = 8
# y = 11

# print_max(x,y)


# #Local Variables


# x = 50

# def func(x):
# 	print('x is',x)
# 	x = 2
# 	print('Changed local x to',x)

# func(x)
# print('x is still', x)




# #Global Statement

# def func():
# 	global x

# 	print('x is',x)
# 	x = 2
# 	print('Changed global x to'.x)

# x = 50
# func()
# print('Value of x is',x)


# Default Argument Values

# def say(message, times=1):
# 	print(message * times )

# say('Hello')
# say('World',5 )
# say('Good Bye')

#Keyword Argument 

def func(a, b=5, c=10):
	print('a is',a,'and b is',b, 'and c is', c)

func(3, 8)
func(24, c=26)
func(c=29,a=39)

