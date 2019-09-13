Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.


>>> # Day 6


>>> x = int(4)
>>> y  = int(6.2)
>>> z = int('9')
>>> print(x)
4
>>> print(y)
6
>>> print(z)
9
>>> x = float(4)
>>> y = float(6.2)
>>> z = float('9')
>>> print(x)
4.0
>>> print(y)
6.2
>>> print(z)
9.0
>>> x = str('r3')
>>> y = str(66)
>>> z = str(7.3)
>>> print(x)
r3
>>> print(y)
66
>>> print(z)
7.3


>>> # Day 7


>>> print('hello')
hello
>>> print("how are you?")
how are you?
>>> r = 'ruba'
>>> print(r)
ruba
>>> a = ''' my name's ruba i'm 21 i'm a CS student and i love learning a new programming language '''
>>> print(a)
 my name's ruba i'm 21 i'm a CS student and i love learning a new programming language 
>>> print(a[5])
a
>>> print(a[3:12])
 name's r


>>> # Day 8


>>> i = "hello world"
>>> n = "    hello world    "
>>> print(n.strip())
hello world
>>> print(len(n))
19
>>> s = 'RUBA'
>>> print(s.lower())
ruba
>>> print(n.upper())
    HELLO WORLD    
>>> print(n.replace('h','J'))
    Jello world    
>>> print(n.split('ll'))
['    he', 'o world    ']
>>> x = 'hello, world'
>>> print(x.split(','))
['hello', ' world']


>>> # Day 9


>>> age = 21
>>> text = " i'm {} "
>>> print(text.format(age))
 i'm 21 
>>> quantity = 4
>>> price = 27.45
>>> order = "can i get {} drinks for {} "
>>> print(order.format(quantity , price))
can i get 4 drinks for 27.45 
>>> MyOrder = "i'm gonna pay {1} for {0} drinks "
>>> print(MyOrder.format(quantity , price))
i'm gonna pay 27.45 for 4 drinks


>>> # Day 10


>>> x = 3
>>> y = 2
>>> print(x*y)
6
>>> a = 4
>>> a += 6
>>> print(a)
10
>>> x = 5
>>> x /= 3
>>> print(x)
1.6666666666666667
>>> x = 7
>>> y = 9
>>> print(x > y)
False
>>> print(x < Y)
>>> print(x==y)
False
>>> print(y>x)
True


>>> # Day 11


>>> x = 7
>>> print(x > 3 or x < 2)
True
>>> s = 'car'
>>> p = 'train'
>>> v = p
>>> print(s is not p)
True
>>> print(s is p)
False
>>> print(v is p)
True
>>> o = ['cat','dog']
>>> print('cat' in o)
True
>>> print('puppy' in o)
False


>>> # Day 12


>>> a = 'please I want {} sandwiches and {} donuts'
>>> b = a.replace('I','we')
>>> print(b)
please we want {} sandwiches and {} donuts
>>> c = b.format(5,7)
>>> print(c)
please we want 5 sandwiches and 7 donuts
>>> d = c.replace('a','A')
>>> print(d)
pleAse we wAnt 5 sAndwiches And 7 donuts
>>> 
