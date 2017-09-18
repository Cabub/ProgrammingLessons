import re
import os
import importlib
regex = re.compile("'(.+)'")

def check_type(mod, var, typ, val):
    if ((type(mod.__dict__[var]) is typ) and
        (val is None or val(mod.__dict__[var]))):
        type_r = regex.search(str(typ)).group(1)
        # print("type({}) is {}\n{} == {}".format(var, type_r, var,
        #      mod.__dict__[var] if type_r != 'str' else "'{}'".format(
        #         mod.__dict__[var].replace("'",'\''))))
        return True
    elif type(mod.__dict__[var]) is not typ:
        print("\t{} isn't appropriately typed.".format(var))
    else:
        print(("\t{} is the correct type, but is set to an " +
               "inappropriate value").format(var))
    return False

try:
    """
    filename = 'datatypes.py'
    dt = importlib.import_module('datatypes')
    print('{}: '.format(filename))
    if all([check_type(dt, a, b, c) for a, b, c in
               [('a', str, None), ('b', int, None), ('c', float, None),
                ('d', bool, None), ('e', int, None), ('f', float, None),
                ('g', int, lambda x: x == int(dt.f)),
                ('h', bool, lambda x: x == bool(dt.g))]]):
        print('\tpassed!')
    """
    filename = 'operators.py'
    op = importlib.import_module('operators')
    print('{}'.format(filename))
    if all([check_type(op, a, b, c) for a, b, c in
                [('a', int, lambda x: x < 10 and x > op.b),
                 ('b', int, lambda x: x < 10 and x < op.a),
                 ('c', int, lambda x: x == op.a + op.b),
                 ('d', float, lambda x: x == op.c / op.b),
                 ('e', int, lambda x: x == op.a * op.a),
                 ('f', int, lambda x: x == sum([op.a, op.b, op.c, op.e])),
                 ('g', int, lambda x: x == (op.a + 2)*(op.b - op.c)),
                 ('h', int, lambda x: x == 20),
                 ('i', int, lambda x: x == 30),
                 ('j', bool, lambda x: x == (not (not True))),
                 ('k', bool, lambda x: x != False),
                 ('n', bool, lambda x: x),
                 ('o', bool, lambda x: x == True),
                 ('p', bool, lambda x: x)
                 ]]):
        print('\tpassed!')
except SyntaxError as e:
    print(("Your syntax isn't right on line {}, please remember " +
          "to finish {} and save before running the grader")
          .format(e.lineno, filename))
