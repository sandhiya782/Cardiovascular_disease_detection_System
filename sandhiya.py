Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
while None:
    print('hi')

    
1+2
3
[1,2,3]+(3,5,6)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    [1,2,3]+(3,5,6)
TypeError: can only concatenate list (not "tuple") to list
[1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
1+3+4j
(4+4j)
5.4+5.4
10.8
5.4+3
8.4
'I am'+'Sandhiya'
'I amSandhiya'
{1,2,5}+{9,5,7,8}
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    {1,2,5}+{9,5,7,8}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
(3,5,7,8)+{2,9,4,12}
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    (3,5,7,8)+{2,9,4,12}
TypeError: can only concatenate tuple (not "set") to tuple
{1,2,4}+{3,7,9}
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    {1,2,4}+{3,7,9}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
true+true
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    true+true
NameError: name 'true' is not defined. Did you mean: 'True'?
True+True
2
False+True
1
False+False
0
True+True+True
3
False+False+False+True
1
True+False+False+True
2
True-False
1
False-True
-1
False+True-True+False+True-False
1
None+None
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    None+None
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
None+True
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    None+True
TypeError: unsupported operand type(s) for +: 'NoneType' and 'bool'
None+[1,4,5]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    None+[1,4,5]
TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'
None+(3,6,7)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    None+(3,6,7)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'tuple'
3*5
15
3*4.56
13.68
3*4+7j
(12+7j)
3*true
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    3*true
NameError: name 'true' is not defined. Did you mean: 'True'?
3*"Sandhiya"
'SandhiyaSandhiyaSandhiya'
4*[1,3,5,8]
[1, 3, 5, 8, 1, 3, 5, 8, 1, 3, 5, 8, 1, 3, 5, 8]
[1,3,5,8]*[1,3,5,8]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    [1,3,5,8]*[1,3,5,8]
TypeError: can't multiply sequence by non-int of type 'list'
True*3
3
False*5
0
5*false
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    5*false
NameError: name 'false' is not defined. Did you mean: 'False'?
5*True
5
(3,5,9.0)*5
(3, 5, 9.0, 3, 5, 9.0, 3, 5, 9.0, 3, 5, 9.0, 3, 5, 9.0)
 if False:
     
SyntaxError: unexpected indent
if False:
    print('ac')
else:
    print('gh')

    
gh
if 0:
    print('ac')
else:
    print('gh')

    
gh
if -1:
    print('ac')
else:
    print('it')

    
ac
if 0.0:
    print('ki')
else:
    print('fy')

    
fy
if 0+0j:
    print('ab')
else:
    print('fg')

    
fg
if 5+7.4:
    print('ab')
else:
    print('fg')

    
ab
if None:
    print('ab')

    
if None:
    print('cd')
else:
    print('gh')

    
gh
if ():
    print('ab')

    
if []:
    print('ab')
else:
    print('fe')

    
fe
if ' ':
...     print('ab')
... else:
...     print('cd')
... 
...     
ab
>>> if '':
...     print('ab')
... else:
...     print('cd')
... 
...     
cd
>>> for a in range(10,5,-1):
...     print(a)
... 
...     
10
9
8
7
6
>>> #this is also used for printing the pattern
>>> for a in range(5,3,1):
...     print(a)
... 
...     
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i,j in enumerate(range(-10,-1,1)):
...     print(i,j)
... 
...     
0 -10
1 -9
2 -8
3 -7
4 -6
5 -5
6 -4
7 -3
8 -2
