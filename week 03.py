>>> # Day 13


>>> f = []
>>> print(f)
[]
>>> numbers = [10,20,30]
>>> print(numbers)
[10, 20, 30]
>>> order = ['burger', 'fries', 'coke', 1, 2]
>>> print(order)
['burger', 'fries', 'coke', 1, 2]
>>> print(order[1])
fries
>>> for x in order:
	print(x)

	
burger
fries
coke
1
2
>>> list = [88,33,0.4,3.6]
>>> print(list)
[88, 33, 0.4, 3.6]
>>> a = [2.7,0.2,7.4]
>>> print(a)
[2.7, 0.2, 7.4]
>>> order[2] = 'orange juice'
>>> print(order)
['burger', 'fries', 'orange juice', 1, 2]
>>> del order[3]
>>> print(order)
['burger', 'fries', 'orange juice', 2]


>>> # Day 14


>>> z = ['r','u','b','a']
>>> print(z[0:2])
['r', 'u']
>>> if 'fries' in order:
	print("yes 'fries' is in the list")

	
yes 'fries' is in the list
>>> x = ["í love python"]*4
>>> print(x)
['í love python', 'í love python', 'í love python', 'í love python']
>>> y = order + x
>>> print(y)
['burger', 'fries', 'orange juice', 2, 'í love python', 'í love python', 'í love python', 'í love python']
>>> a = [1,2,3,4]
>>> b = [0.3,7.1,4.2]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 0.3, 7.1, 4.2]


>>> # Day 15


>>> print(len(c))
7
>>> c.append(0.6)
>>> print(c)
[1, 2, 3, 4, 0.3, 7.1, 4.2, 0.6]
>>> order.insert(0,'sandwich')
>>> print(order)
['sandwich', 'burger', 'fries', 'orange juice', 2]
>>> order.remove('orange juice')
>>> print(order)
['sandwich', 'burger', 'fries', 2]
>>> order.pop()
2
>>> order.pop(0)
'sandwich'
>>> c.clear()
>>> print(c)
[]
>>> n = order.copy()
>>> print(n)
['burger', 'fries']


>>> # Day 16


>>> tuple = ('apple','orange','banana')
>>> print(tuple)
('apple', 'orange', 'banana')
>>> EmptyTuple = ()
>>> print(EmptyTuple)
()
>>> ThisTuple=(7,)
>>> print(ThisTuple)
(7,)
>>> print(tuple[2])
banana
>>> for x in tuple:
	print(x)

	
apple
orange
banana
>>> del EmptyTuple
>>> print(EmptyTuple)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(EmptyTuple)
NameError: name 'EmptyTuple' is not defined
>>> print(tuple[0:1])
('apple',)


# Day 17


>>> if "banana" in tuple:
	print('yes "banana" is in tuple')

	
yes "banana" is in tuple
>>> thistuple = ("ruba",)*4
>>> print(thistuple)
('ruba', 'ruba', 'ruba', 'ruba')
>>> x = (3,4,5,6)
>>> x = x + (1,2,3)
>>> print(x)
(3, 4, 5, 6, 1, 2, 3)
>>> print(len(tuple))
3


>>> # Day 18,19


>>> list = [1,2,3,4,5]
>>> list.append(7)
>>> print(list)
[1, 2, 3, 4, 5, 7]
>>> list.pop(5)
7
>>> list.insert(0, 0)
>>> print(list)
[0, 1, 2, 3, 4, 5]
>>> list.remove(3)
>>> print(list)
[0, 1, 2, 4, 5]
>>> tuple = ("java","python","swift")
>>> if "python" in tuple:
	print('yes "python" is in tuple')

	
yes "python" is in tuple
>>> 
