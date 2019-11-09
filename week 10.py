# Day 62


import camelcase
c = camelcase.CamelCase()
text = "i am using python"
print(c.hump(text))


# Day 63


print('enter your name:')
x = input()
print('hello', x)


# Day 64


try:
    print(y)
except:
    print("an exception occured")

try:
    print(Y)
except NameError:
    print('variable x is not defined')
except:
    print('something else went wrong')
finally:
    print('finished')


# Day 65


price = 12.67
X = 'the price is {} dollars'
print(X.format(price))

quantity = 2
itemno = 3
price = 27
order = 'i want {} pieces of itemno {} for {} dollars'
print(order.format(quantity, itemno, price))


# Day 66
age = 21
name = 'ruba'
n = 'her name is {1}, {1} is {0} years old'
print(n.format(age, name))
car = 'i have a {carname} it is a {model}'
print(car.format(carname = 'ford', model = 'mustang'))


# Day 67,68


print(" Enter the first letter of your name: ")
letter = input()
LETTER = input()
print(' your name begins with the letter ', letter, ' and ends with the letter ', LETTER)

firstname = 'ahmed'
middlename = 'ali'
balance = '55.44 $'
a = 'dear {} {} your current balance is {}'
print(a.format(firstname, middlename, balance))
