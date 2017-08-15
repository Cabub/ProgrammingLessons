import re
regex = re.compile("'(.+)'")
try:
    import datatypes as dt
    def check_type(var, typ):
        if type(dt.__dict__[var]) is typ:
            type_r = regex.search(str(typ)).group(1)
            print("{} is a {}".format(var, type_r))
            return True
        print("it seems {} isn't appropriately typed.".format(var))
        return False
    if all([check_type(a, b) for a, b in
               [('a',str), ('b',int), ('c',float)]]):
        print('good job, you passed datatypes.py!')
except SyntaxError as e:
    print(("Your syntax isn't right on line {}, please remember " +
          "to finish datatypes.py before running the grader")
          .format(e.lineno))
