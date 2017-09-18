''' Okay so lets practice some data types.
To complete this exercise, replace all ellipses
(...) with the appropriate values.
I'll assign a to a string,
you assign b to an int,
assign c to a float, and d to a boolean.
'''
# Set b to an int and c to a float
a = "This is how you assign a string to a variable"
b = ...
c = ...
d = ...

""" Cool.
now lets have some fun with these numbers.
when you 'cast' a string to an integer, Python
will automatically try to parse the number from
the text. This means I can set e to an integer
just by writing e = int('123'). You try it:
"""
# Set e to a numeric string casted to an integer
e = ...

""" You can also convert back and forth between
integers and floats this way, but if you convert a
float to an int, it will truncate (chop-off) the
fractional portion instead of rounding.
This means that int(123.9999) equals 123.
Now try setting f to a float (ex. 123.999),
and the next line will convert it to the string
("123.999"), then cast it to a float again (123.999),
before finally casting it to an int (123). then
it will assign this value to g. h will then be assigned
the value of g casted to boolean
"""
# Set f to a float
f = ...
g = int(float(str(f)))
h = bool(g)

""" Now that you're finished with datatypes.py,
please run the grader to find out how you did.
To do this, open up a terminal window, (as described
in lesson 1), navigate to this directory using the cd
command, and run the grader by running: python grader.py
"""
