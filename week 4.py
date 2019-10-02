>>> # Day 20


>>> set = {}
>>> print(set)
{}
>>> Set = {'apple','banana','cherry'}
>>> print(Set)

{'banana', 'cherry', 'apple'}
>>> SET = {'ruba','ruba','1','1'}
>>> print(SET)
{'1', 'ruba'}
>>> for x in SET:
	print(x)

	
1
ruba
>>> print('çherry' in Set)
False
>>> print('cherry' in Set)
True
>>> Set.add('grapes')
>>> print(Set)
{'grapes', 'banana', 'cherry', 'apple'}
>>> Set.update(['orange','pineapple'])
>>> print(Set)
{'apple', 'orange', 'banana', 'grapes', 'pineapple', 'cherry'}


>>> # Day 21


>>> print(len(Set))
6
>>> Set.remove('orange')
>>> print(Set)
{'apple', 'banana', 'grapes', 'pineapple', 'cherry'}
>>> Set.discard('grapes')
>>> print(Set)
{'apple', 'banana', 'pineapple', 'cherry'}
>>> x = Set.pop()
>>> print(x)
apple
>>> print(Set)
{'banana', 'pineapple', 'cherry'}
>>> Set.clear()
>>> print(Set)
set()


>>> # Day 22


>>> dict = { 'name':'ruba' ,'age':21 ,'major':'CS'}
>>> print(dict)
{'name': 'ruba', 'age': 21, 'major': 'CS'}
>>> x = dict['name']
>>> print(x)
ruba
>>> dict['age'] = 22
>>> print(dict)
{'name': 'ruba', 'age': 22, 'major': 'CS'}
>>> for x in dict:
	print(x)
	
name
age
major
>>> for x in dict:
	print(dict[x])
	
ruba
22
CS
>>> for x in dict.values():
	print(x)

ruba
22
CS
>>> for x ,y in dict.items():
	print(x,y)

name ruba
age 22
major CS


>>> # Day 23


>>> if 'major' in dict:
	print('true')

	
true
>>> print(len(dict))
3
>>> dict['hight'] = 'five feet'
>>> print(dict)
{'name': 'ruba', 'age': 22, 'major': 'CS', 'hight': 'five feet'}
>>> dict.pop('age')
22
>>> dict.popitem()
('hight', 'five feet')


>>> # Day 24


>>> Dict = dict.copy()
>>> print(Dict)
{'name': 'ruba', 'major': 'CS'}
>>> family = { 'child1' : { 'name': 'emil', 'year':2001}, 'child2' : { 'name':'tobias', 'year': 2000}, 'child3' : { 'name':'linus', 'year':1999}}
>>> print(family)
{'child1': {'name': 'emil', 'year': 2001}, 'child2': {'name': 'tobias', 'year': 2000}, 'child3': {'name': 'linus', 'year': 1999}}
         
         
>>> # Day 25,26
         
         
>>> SET = {1,3,5,7,8}
>>> SET.update([4,8,12])
>>> print(SET)
{1, 3, 4, 5, 7, 8, 12}
>>> SET.remove(8)
>>> print(SET)
{1, 3, 4, 5, 7, 12}
>>> SET.clear()
>>> print(SET)
set()
>>> DICT = { 'name':'pigeon', 'type':'bird', 'skin cover':'feather' }
>>> x = DICT['type']
>>> print(x)
bird
>>> DICT['skin cover'] = 'feathers'
>>> print(DICT)
{'name': 'pigeon', 'type': 'bird', 'skin cover': 'feathers'}
>>> 
