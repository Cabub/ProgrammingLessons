''' Okay so lets practice some data types.
I'll assign a to a string,
you assign b to an int,
assign c to a float, and d to a boolean.
'''
# Set b to an int and c to a float
a = "This is how you assign a string to a variable"
b = 1
c = 2.0
d = True

""" Cool.
now lets have some fun with these numbers.
when you 'cast' a string to an integer, Python
will automatically try to parse the number from
the text. This means I can set e to an integer
just by writing e = int('123'). You try it:
"""
# Set e to a numeric string casted to an integer
e = int('12')

""" You can also convert back and forth between
integers and floats this way, but if you convert a
float to an int, it will truncate (chop-off) the
fractional portion instead of rounding.
This means that int(123.9999) equals 123.
Now try setting f to a float (ex. 123.999),
and the next line will convert it to the string
("123.999"), then cast it to a float again (123.999),
before finally casting it to an int (123). then
it will assign this value to g.
"""
# Set e to a float
f = 0.1
g = int(float(str(f)))
h = bool(g)
