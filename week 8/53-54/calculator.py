import calculateModule
import datetime


x = calculateModule.add(2, 4)
print(x)
X = calculateModule.sub(2, 4)
print(X)
y = x = calculateModule.multi(2, 4)
print(y)
Y = calculateModule.devide(2, 4)


a = datetime.datetime.now()
print(a)
year = a.strftime("%Y")
print(year)
month = a.strftime("%B")
print(month)
day = a.strftime("%A")
print(day)
