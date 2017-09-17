import re
import os
import importlib
regex = re.compile("'(.+)'")

def check_type(mod, var, typ, val):
    if ((type(mod.__dict__[var]) is typ) and
        (val is None or val == mod.__dict__[var])):
        type_r = regex.search(str(typ)).group(1)
        print("type({}) is {}\n{} == {}".format(var, type_r, var,
             mod.__dict__[var] if type_r != 'str' else "'{}'".format(
                mod.__dict__[var].replace("'",'\''))))
        return True
    elif type(mod.__dict__[var]) is not typ:
        print("{} isn't appropriately typed.".format(var))
    else:
        print(("{} is the correct type, but is set to an " +
               "inappropriate value").format(var))
    return False

try:
    dt = importlib.import_module('datatypes')
    if all([check_type(dt, a, b, c) for a, b, c in
               [('a', str, None), ('b', int, None), ('c', float, None),
                ('d', bool, None), ('e', int, None), ('f', float, None),
                ('g', int, int(dt.f)), ('h', bool, bool(dt.g))]]):
        print('good job, you passed datatypes.py!')
except SyntaxError as e:
    print(("Your syntax isn't right on line {}, please remember " +
          "to finish {} and save before running the grader")
          .format(e.lineno, os.path.split(e.filename)[1]))
