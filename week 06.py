>>> # Day 34


>>> def my_function(food):
	for x in food:
		print(x)

		
>>> fruits = ['apple','banana','cherry']
>>> my_function(fruits)
apple
banana
cherry
>>> def new_func(x):
	return 5 * x

>>> print(new_func(6))
30
>>> print(new_func(3))
15
>>> def my_func(child1,child2,child3):
	print('the youngest child is' + child3)

	
>>> my_func(child1 = 'emil', child2 = 'tobias', child3 = ' linus')
the youngest child is linus
>>> def my_function(*kids):
	print('the youngest child is ' + kids[2])

	
>>> my_function('emil','tobias','linus')
the youngest child is linus
>>> def tri_recursion(k):
	if (k > 0):
		result = k + tri_recursion(k-1)
		print(result)
	else:
		result = 0
		return result
	print('\n\nRecursion example result')
	tri_recursion(6)

	
>>> def tri_recursion(k):
	if (k > 0):
		result = k + tri_recursion(k-1)
		print(result)
	else:
		result = 0
		return result

	
>>> print('\n\nRecursion example result')
	tri_recursion(6)
	
SyntaxError: multiple statements found while compiling a single statement
>>> # Day 35
>>> x = lambda a : a +30
>>> print(x(10))
40
>>> x = lambda a,b: a*b
>>> print(x(3,2))
6
>>> x = lambda a,b,c : a+b+c
>>> print(x(1,1,1))
3


>>> # Day 36


>>> def myfunc(n):
	return lambda a : a* n

>>> mydoubler = myfunc(2)
>>> print(mydoubler(11))
22
>>> mytripler = myfunc(3)
>>> print(mytripler(11))
33


>>> # Day 37


>>> cars = ['ford','volvo','bmw']
>>> x = cars[1]
>>> print(x)
volvo
>>> print(cars[1])
volvo
>>> cars[0] = 'toyota'
>>> print(cars)
['toyota', 'volvo', 'bmw']
>>> x = len(cars)
>>> print(x)
3
>>> print(len(cars))
3


>>> # Day 38


>>> for x in cars:
	print(x)

	
toyota
volvo
bmw
>>> cars.append('honda')
>>> print(cars)
['toyota', 'volvo', 'bmw', 'honda']
>>> cars.pop(1)
'volvo'
>>> print(cars)
['toyota', 'bmw', 'honda']
>>> cars.remove('honda')
>>> print(cars)
['toyota', 'bmw']


>>> # Day 39,40


>>> def power(base,exp):
	if(exp==1):
		return(base)
	if(exp!=1):
		return (base*power(base,exp-1))
	print('result = ', power(5,3))

	
>>> def power(base,exp):
	if(exp==1):
		return(base)
	if(exp!=1):
		return (base*power(base,exp-1))

	
>>> print('result = ', power(5,3))
result =  125
>>> x = [-4,-6,-5,-1,2,3,7,9,88]
>>> list = [-4,-6,-5,-1,2,3,7,9,88]
>>> x = lambda a : a > 0
>>> for y in list:
	if x(y):
		print(y)

		
2
3
7
9
88
>>> 
