#Week 4b 20.9
C:\Users\Ye Min Myat>pip freeze
appdirs==1.4.3
atomicwrites==1.3.0
attrs==19.1.0
black==19.3b0
certifi==2019.9.11
chardet==3.0.4
Click==7.0
colorama==0.4.1
cycler==0.10.0
entrypoints==0.3
flake8==3.7.8
idna==2.8
importlib-metadata==0.23
joblib==0.13.2
kiwisolver==1.1.0
matplotlib==3.1.1
mccabe==0.6.1
more-itertools==7.2.0
mpmath==1.1.0
mypy==0.720
mypy-extensions==0.4.1
numpy==1.17.2
opencv-python==4.1.1.26
packaging==19.2
pandas==0.25.1
Pillow==6.1.0
pluggy==0.13.0
py==1.8.0
pycodestyle==2.5.0
pyflakes==2.1.1
pyparsing==2.4.2
pytest==5.1.2
python-dateutil==2.8.0
pytz==2019.2
requests==2.22.0
scikit-learn==0.21.3
scipy==1.3.1
six==1.12.0
sklearn==0.0
sympy==1.4
toml==0.10.0
typed-ast==1.4.0
typing-extensions==3.7.4
urllib3==1.25.3
wcwidth==0.1.7
zipp==0.6.0

C:\Users\Ye Min Myat>pip list
Package            Version
------------------ ---------
appdirs            1.4.3
atomicwrites       1.3.0
attrs              19.1.0
black              19.3b0
certifi            2019.9.11
chardet            3.0.4
Click              7.0
colorama           0.4.1
cycler             0.10.0
entrypoints        0.3
flake8             3.7.8
idna               2.8
importlib-metadata 0.23
joblib             0.13.2
kiwisolver         1.1.0
matplotlib         3.1.1
mccabe             0.6.1
more-itertools     7.2.0
mpmath             1.1.0
mypy               0.720
mypy-extensions    0.4.1
numpy              1.17.2
opencv-python      4.1.1.26
packaging          19.2
pandas             0.25.1
Pillow             6.1.0
pip                19.2.3
pluggy             0.13.0
py                 1.8.0
pycodestyle        2.5.0
pyflakes           2.1.1
pyparsing          2.4.2
pytest             5.1.2
python-dateutil    2.8.0
pytz               2019.2
requests           2.22.0
scikit-learn       0.21.3
scipy              1.3.1
setuptools         40.8.0
six                1.12.0
sklearn            0.0
sympy              1.4
toml               0.10.0
typed-ast          1.4.0
typing-extensions  3.7.4
urllib3            1.25.3
wcwidth            0.1.7
zipp               0.6.0

 fruits = ['orange', 'apple', 'pear', 'banana', 'coconut']
>>> fruits.reverse()
>>> fruits
['coconut', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['coconut', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.remove('apple')
>>> fruits
['coconut', 'banana', 'pear', 'orange', 'grape']
>>> fruits.insert(1, 'cucumber')
>>> fruits
['coconut', 'cucumber', 'banana', 'pear', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['banana', 'coconut', 'cucumber', 'grape', 'orange', 'pear']
>>> fruits.pop()
'pear'

>> fruits = ['orange', 'apple', 'pear', 'banana', 'coconut']
>>> fruits
['orange', 'apple', 'pear', 'banana', 'coconut']
>>> fruits.index(apple)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'apple' is not defined
>>> fruits.index('apple')
1
>>> fruits.index('apple', 1)
1
>>> fruits = ['coconut', 'banana', 'pear', 'apple', 'orange', 'grape', 'lemon', 'apple']
>>> fruits.count('apple')
2
>>> fruits.copy()
['coconut', 'banana', 'pear', 'apple', 'orange', 'grape', 'lemon', 'apple']
>>> fruits.extend()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: extend() takes exactly one argument (0 given)
>>>
>>>
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a = [6 : 2]
  File "<stdin>", line 1
    a = [6 : 2]

    >>> from collections import deque
>>> queue = deque (["Eric", "John", "Micheal"])
>>> queue.append("Terry")
>>> queue.popleft()
'Eric'
>>> x = deque (["Eric", "John", "Micheal"])
>>> x.append("Terry")
>>> x
deque(['Eric', 'John', 'Micheal', 'Terry'])
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
>>> [str(round(pi, 6))]
['3.141593']

>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

>>> import datetime
>>> x = datetime.datetime.now()
>>> x
datetime.datetime(2019, 9, 20, 18, 8, 13, 903090)
