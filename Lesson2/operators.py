''' In this excersise, we'll be using operators to
assign, modify, and compare variables and constants.
Follow the instructions for each section, and run
the grader using 'python grader.py'
'''
# First, lets use the = operator to set some variables
# Set a and b to integers such that a and b are both less than 10
# and a is greater than b
a = 7
b = 3

""" Now that we have some variables set, lets
do some math.
"""
# Set c to the a plus b
c = a + b

# Set d to c divided by b
d = c / b

# Set e to the value of a squared using the power operator (**)
e = a ** 2

# Set f to the sum of a, b, c and e
f = a + b + c + e

""" Arithmetic operations generally follow the
order of operations, but for more complex expressions,
or to remove ambigutiy, it sometimes becomes necessary
to dictate the order in which operations should take place.
Say you wanted to set g to the sum of a and b multiplied
by 2. If you tried g = a + b * 2, you'd set g to b times 2
plus a. So instead, we can use g = (a + b) * 2 to get the
result we wanted. This causes a + b to be evaluated first,
and the result to be multiplied by 2.
"""
# Set g to the value of (a plus two) times (b minus c)
g = (a + 2) * (b - c)

""" Now lets use some Apply and Assign operators
"""
h = 10
i = 61

# Set h to h plus 10 using the += operator
h += 10

# Set i to i floor divided by 2 using the //= operator
i //= 2

""" Let's try out the comparison operators now.
"""

# Set j to the value of a greater than b
j = a > b

# Set k to the value of h not equal to i
k = h != i

""" Now we'll finish it off with the boolean operators
"""
l = True
m = False
# Set n to not m
n = not m

# Set o to n and l
o = n and l

# Set p to o and m or not m (this will be evaluated left to right)
p = o and m or not m

""" Now that you're finished with datatypes.py,
please run the grader to find out how you did.
To do this, open up a terminal window, (as described
in lesson 1), navigate to this directory using the cd
command, and run the grader by running: python grader.py
"""
