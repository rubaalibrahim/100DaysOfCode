Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Day 27
>>> a = 10
>>> b = 20
>>> if b > a:
	print('b is greater than a')

	
b is greater than a
>>> c = 10

>>> if a > c:
	print('a is greater than c')
elif a == c:
	print('a is equal to c')

	
a is equal to c
>>> if a > b:
	print('a is greater than b')
elif a == b:
	print('a is equal tom be')
else:
	print('b is greater than a')

	
b is greater than a
>>> if b > a: print('b is greater than a')

b is greater than a
>>> print('b') if b > a else print('a')
b
>>> 
>>> print('A') if b > a else print('B')
A
>>> 
>>> print('B') if b > a else print('A')
B
>>> a = 300
>>> b = 100
>>> c = 200
>>> if a > b and c > b:
	print('true')

	
true
>>> if b > a or c > b:
	print('at least one condition is true')

	
at least one condition is true
>>> # Day 28
>>> f = 13
>>> while f < 2:
	print(f)
	f+=1

	
>>> 
>>> x = 4
>>> while x < 5:
	print(x)
	x+=1

	
4
>>> x = 1
>>> while x < 5:
	print(x)
	x+= 1

	
1
2
3
4
>>> y = 1
>>> while y < 9:
	print(y)
	y+=2

	
1
3
5
7
>>> z = 1
>>> while z < 8:
	print(z)
	if z == 6:
		break
	i+=1

	
1
Traceback (most recent call last):
  File "<pyshell#58>", line 5, in <module>
    i+=1
NameError: name 'i' is not defined
>>> while z < 8:
	print(z)
	if z == 6:
		break
	z+=1

	
1
2
3
4
5
6
>>> w = 3
>>> while w < 10:
	w+=1
	if w == 8:
		continue
	print(w)

	
4
5
6
7
9
10
>>> r = 1
>>> while r < 4:
	r+=1
	print(r)
else:
	print('r is no longer less than 4')

	
2
3
4
r is no longer less than 4
>>> r = 10
>>> while r < 4:
	r+=1
	print(r)
else:
	print('r is no longer less than 4')

	
r is no longer less than 4
