import re
import importlib
regex = re.compile("'(.+)'")


def check_type(mod, var, typ, test):
    try:
        x = mod.__dict__[var]
    except Exception:
        raise AttributeError("\tCannot find variable {}".format(var))
    if ((type(x) is typ) and
       (test is None or eval(test))):
        return True
    elif type(mod.__dict__[var]) is not typ:
        print("\t{} isn't appropriately typed.".format(var))
    else:
        print(("\t{} is the correct type, but is set to an " +
               "inappropriate value").format(var))
    return False


def grade_file(module_name, rules):
    try:
        filename = '{}.py'.format(module_name)
        print('{}: '.format(filename))
        mod = importlib.import_module(module_name)
        if all([check_type(mod, a, b, c) for a, b, c in rules]):
            print('\tpassed')
    except SyntaxError as e:
        print("\tYour syntax isn't right on line {}, please remember "
              "to finish {} and save before running the grader"
              .format(e.lineno, filename))
    except (ValueError, TypeError) as e:
        if len(e.args) > 0 and 'ellipsis' in e.args[0].lower():
            print("\tIt looks like you haven't replaced all the ellipses yet. "
                  "Please finish {} and save before running the grader."
                  .format(filename))
        else:
            raise e


answer_key = {
    "datatypes": [('a', str, None), ('b', int, None), ('c', float, None),
                  ('d', bool, None), ('e', int, None), ('f', float, None),
                  ('g', int, "x == int(mod.f)"),
                  ('h', bool, "x == bool(mod.g)")],
    "operators": [('a', int, "x < 10 and x > mod.b"),
                  ('b', int, "x < 10 and x < mod.a"),
                  ('c', int, "x == mod.a + mod.b"),
                  ('d', float, "x == mod.c / mod.b"),
                  ('e', int, "x == mod.a * mod.a"),
                  ('f', int, "x == sum([mod.a, mod.b, mod.c, mod.e])"),
                  ('g', int, "x == (mod.a + 2)*(mod.b - mod.c)"),
                  ('h', int, "x == 20"),
                  ('i', int, "x == 30"),
                  ('j', bool, "x == (not (not True))"),
                  ('k', bool, "x != False"),
                  ('n', bool, "x"),
                  ('o', bool, "x == True"),
                  ('p', bool, "x")]
}

file_order = ["datatypes", "operators"]


for mod in file_order:
    grade_file(mod, answer_key[mod])