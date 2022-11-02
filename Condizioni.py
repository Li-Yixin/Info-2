# lochiche matemactiche 
#Uguale a == b
#Diverso a != b
#Minore  a < b
#Minore o uguale a: a <= b
#Maggiore di: a > b
#Maggiore o uguale a: a >= b

#If
a = 33
b = 200
if b > a:
  print("b is greater than a")
#Python relies on indentation (whitespace at the beginning of a line)  error
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#Es 2
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short form
if a > b: print("a is greater than b")
a = 2
b = 330
print("A") if a > b else print("B")

#Ternary Operators
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
a = 33
b = 200
if b > a:
  pass