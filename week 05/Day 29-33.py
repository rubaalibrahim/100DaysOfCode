
>>> # Day 29

>>> numbers = ['1','2','3']
>>> for x in numbers:
	print(x)

	
1
2
3
>>> for x in'python':
	print(x)

	
p
y
t
h
o
n
>>> fruits = ['apple','strawberry','orange']
>>> for x in fruits:
	print(x)
	if x == 'strawberry':
		break

	
apple
strawberry
>>> for x in fruits:
	if x == 'strawberry':
		break
	print(x)

	
apple
>>> for x in fruits:
	if x =='strawberry':
		continue
	print(x)

	
apple
orange


>>> # Day 30


>>> for x in range(7):
	print(x)

	
0
1
2
3
4
5
6
>>> for x in range(3,9):
	print(x)

	
3
4
5
6
7
8
>>> for x in range(3,13,2):
	print(x)

	
3
5
7
9
11
>>> for x in range(4):
	print(x)
else:
	print('done')

	
0
1
2
3
done
>>> clothes = ['t-shirt','pants','shoes']
>>> color = ['white','red','black']
>>> for x in color:
	for y in clothes:
		print(x,y)

		
white t-shirt
white pants
white shoes
red t-shirt
red pants
red shoes
black t-shirt
black pants
black shoes


>>> # Day 31


>>> def new_func():
	print('hello')

	
>>> new_func()
hello
>>> def my_func(Fname):
	print(Fname + " refsnes")

	
>>> my_func('emil')
emil refsnes
>>> my_func('tobias')
tobias refsnes
>>> my_func('linus')
linus refsnes
>>> def Func(country = 'norway'):
	print("i'm from " + country)

	
>>> Func('sweden')
i'm from sweden
>>> Func('india')
i'm from india
>>> Func()
i'm from norway


>>> # Day 32,33


>>> for x in range(3,18,2):
	for y in range(2,17,2):
		print(x,y)

		
3 2
3 4
3 6
3 8
3 10
3 12
3 14
3 16
5 2
5 4
5 6
5 8
5 10
5 12
5 14
5 16
7 2
7 4
7 6
7 8
7 10
7 12
7 14
7 16
9 2
9 4
9 6
9 8
9 10
9 12
9 14
9 16
11 2
11 4
11 6
11 8
11 10
11 12
11 14
11 16
13 2
13 4
13 6
13 8
13 10
13 12
13 14
13 16
15 2
15 4
15 6
15 8
15 10
15 12
15 14
15 16
17 2
17 4
17 6
17 8
17 10
17 12
17 14
17 16
>>> 
