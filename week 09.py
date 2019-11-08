# Day 55


>>> import json

>>> x = '{"name":"john", "age":30, "city":"new york"}'
>>> y = json.loads(x)
>>> print(y['name'])
john
>>> p = {"name":"john","age":30, "city":"new york"}
>>> j = json.dumps(p)
>>> print(j)
{"name": "john", "age": 30, "city": "new york"}
>>> print(json.dumps({'name':'ruba', 'age':21}))
{"name": "ruba", "age": 21}
>>> print(json.dumps(['hat','shirt','shoes']))
["hat", "shirt", "shoes"]
>>> print(json.dumps(None))
null
>>> P = {
	'name':'jessica',
	'age': 28,
	'married': True,
	'divorced': False,
	'children': ('sandra','martin'),
	'pets': None,
	'cars': [
		{'model':'bmw 230', 'mpg': 27.5},
		{'model': 'ford edge', 'mpg': 24.1}
		]
	}
>>> J = json.dumps(P)
>>> print(J)
{"name": "jessica", "age": 28, "married": true, "divorced": false, "children": ["sandra", "martin"], "pets": null, "cars": [{"model": "bmw 230", "mpg": 27.5}, {"model": "ford edge", "mpg": 24.1}]}


>>> # Day 56


>>> print(json.dumps(x, indent=4))
"{\"name\":\"john\", \"age\":30, \"city\":\"new york\"}"
>>> print(json.dumps(J, indent=4))
"{\"name\": \"jessica\", \"age\": 28, \"married\": true, \"divorced\": false, \"children\": [\"sandra\", \"martin\"], \"pets\": null, \"cars\": [{\"model\": \"bmw 230\", \"mpg\": 27.5}, {\"model\": \"ford edge\", \"mpg\": 24.1}]}"
>>> print(json.dumps(J, indent=4, separators=(".","=")))
"{\"name\": \"jessica\", \"age\": 28, \"married\": true, \"divorced\": false, \"children\": [\"sandra\", \"martin\"], \"pets\": null, \"cars\": [{\"model\": \"bmw 230\", \"mpg\": 27.5}, {\"model\": \"ford edge\", \"mpg\": 24.1}]}"
>>> print(json.dumps(J, indent=4, sort_keys=True))
"{\"name\": \"jessica\", \"age\": 28, \"married\": true, \"divorced\": false, \"children\": [\"sandra\", \"martin\"], \"pets\": null, \"cars\": [{\"model\": \"bmw 230\", \"mpg\": 27.5}, {\"model\": \"ford edge\", \"mpg\": 24.1}]}"


>>> # Day 57


>>> import re
>>> txt = 'the city in spain'
>>> X = re.search('ˆthe,*spain$', txt)
>>> if(x):
	print('YES we have a match')
else:
	print('no match')

	
YES we have a match


>>> # Day 58


>>> f = re.findall('in', txt)
>>> print(f)
['in', 'in']
>>> a = re.findall('portugal', txt)
>>> print(a)
[]
>>> if(a):
	print('YES we have a match')
else:
	print('no match')

	
no match
>>> k = re.split('\s', txt)
>>> print(k)
['the', 'city', 'in', 'spain']


>>> # Day 59


>>> x = re.sub('\s', '9', txt)
>>> print(x)
the9city9in9spain
>>> q = re.search('ai', txt)
>>> xx= re.search(r"\bs\w+", txt)
>>> print(xx)
<re.Match object; span=(12, 17), match='spain'>
>>> print(xx.string)
the city in spain
>>> print(xx.group())
spain


>>> # Day 60,61


>>> print(json.dumps(('saturday','sunday','monday','tuesday','wednesday','thursdayy','friday')))
["saturday", "sunday", "monday", "tuesday", "wednesday", "thursdayy", "friday"]
>>> str = 'data is the new oil'
>>> h = re.findall("data", str)
>>> print(h)
['data']
>>> 
