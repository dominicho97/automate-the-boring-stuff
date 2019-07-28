Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ['cat','dog','cow'}
SyntaxError: invalid syntax
>>> ['cat','dog','cow']
['cat', 'dog', 'cow']
>>> cindy = ['cat','dog','cow'}
SyntaxError: invalid syntax
>>> cindy = ['cat','dog','cow']
>>> cindy[0]
'cat'
>>> cindy = [['cat','bat'],[10,20,30]]
>>> spam[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    spam[0]
NameError: name 'spam' is not defined
>>> cindy[0]
['cat', 'bat']
>>> cindy[1]
[10, 20, 30]
>>> cindy[0,1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cindy[0,1]
TypeError: list indices must be integers or slices, not tuple
>>> cindy[0][1]
'bat'
>>> cindy [1][2]
30
>>> 
link = https://www.youtube.com/watch?v=5n6o1MaXDoE&list=PLGoJzB271_7r-iLYuEHEPJ5pSIYxXjJEn&index=13
