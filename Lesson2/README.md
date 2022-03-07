# Lesson 2

Welcome to Lesson 2! This time around we're going to get a feel for the syntax of python. The things we'll talk about are data types, syntax, expressions, and variables.

## Data Types

In Python (and in object-oriented languages in general) everything is an object. An object is an instance of a class. A class is a collection of methods and properties used to make objects. You can think of classes as object factories. A few of the basic classes (or Types) in Python are ``` int ``` (integers), ``` float ``` (floating-point numbers), ``` str ``` (strings).

#### Integers

[Integers](https://en.wikipedia.org/wiki/Integer) are "whole" numbers. As in they can be expressed as the sum of an arbitrary number of ones or negative ones. If that seemed too technical, think about it like this: There are 7 letters in the word 'integer', there's not a way that there can be 6.5 or 7.01 letters, so an integer is the right 'Type' to use to store that information. Integers are represented in Python as numbers without decimal places.
```python
1
2
3
291928390
```

#### Floats

[Floating Point Numbers](https://en.wikipedia.org/wiki/Real_number) are "real" numbers. This means all of the numbers (including integers) that can be represented as a ratio of two integers. A good example of this is if you were to measure how many kilograms an object is, and the result was 8.5kg. If you were to store this as an integer, you would throw away some information. Thus, we would be better off storing this value as a float. Floats are represented in python as numbers with decimal places.
```python
1.0
2.5
3.9
7328913.9432432
```

#### Strings

[Strings](https://en.wikipedia.org/wiki/String_(computer_science) are a sequence of characters. Technically, this entire document is a string (mind. blown.). Strings are represented in Python as a series of characters between a pair of either single or double quotes.
```python
"This is a string"
'This is also a string'
'This is a string with "quotes" in it!'
"This is another string with 'quotes' in it!"
```

#### Boolean

A [boolean](https://en.wikipedia.org/wiki/Boolean_data_type) data type is a data type with only two possible values, either ``` True ``` or ``` False ```. We use booleans to create flags indicating the state of a program, or to modify the control flow. When an integer is converted into a boolean value, zero means ``` False ```, and anything else is ``` True ```

```python
some_flag = True
other_flag = False
```

### Variables

Variables are places to store data that might change. A variable can be named just about whatever you want, as long as it begins with a letter, only contains letters or numbers, and has no spaces. You can assign data to a variable by using the ``` = ``` operator.
```python
my_string = "This is a string"
my_integer = 1
my_float = 64
my_bool = True
```
now the value of "This is a string" is stored in the variable named 'my_string' and we can reference it by using 'my_string' again like this:
```python
print(my_string)
```
This will cause the string "This is a string" to be printed out.

### The 'Type' Talk

Back in my day, we had to be very careful about the datatypes we were using and converting between them. Nowadays Python takes care most of that for you, but you still need to be careful or you could be burned by bad typing. I'm sure we'll talk more about it later in the course, but for now, you should know that you can check the type of a variable by using the ``` type ``` function.
```python
type('1')  # == str  # '1' is a string
type(1)    # == int  # 1 is an integer
type(1.0)  # == float # 1.0 is a float
type(True) # == bool # True is boolean
```
You can also 'cast' variables or constants (a constant is just some data that doesn't change) into another data type by using it's 'constructor' (we'll get more into that later, just remember the terminology).
```python
a = int(123.123)  # a == 123   # assign a to 123.123 casted to an integer
b = float(5)       # b == 5.0   # assign b to 5 casted to a float
c = str(123)      # c == '123' # assign c to 123 casted to a string
d = bool(1)       # d == True  # assign d to 1 casted to boolean
```
After running the above code, a = ``` 123 ```, b = ``` 5.0 ```, c = ``` '123' ``` and d = ``` True ```.

## Requirements

In this directory, you'll find a file called ``` datatypes.py ```. I've taken the liberty of writing a few comments (oh yeah I haven't talked about comments! I'll get to that next) with instructions for how to pass the first part of the lesson. Please pass the grader for datatypes.py before proceeding.

## Operators

Operators allow you manipulate and compare values in Python. Operators are usually unary (one operand) or binary (two operands).

### Arithmetic Operators

Arithmetic operators are binary operators used to perform math operations. The operators available to use in Python are: Addition (+) adds two values together, Subtraction (-) subtracts the right operand by the left operand, Multiplication (\*) multiplies the right operand by the left operand, Division (/) divides the left operand by the right operand, Modulus (%) divides the left operand by the right operand and returns the remainder, Exponent (\*\*) calculates the exponential value, and Floor division (//) performs integer division.

```python
1 + 1   # == 2   # addition
2 - 1   # == 1   # subtraction
2 * 6   # == 12  # multiplication
14 / 5  # == 2.8 # division
14 % 5  # == 4   # modulus (remainder)
14 // 5 # == 2   # floor division (integer division)
2 ** 4  # == 16  # exponent (power)
```

### Apply and Assign Operators

All of the basic Arithmetic operators can be combined with an equals sign to create an 'Apply and assign' operator. This is a special type of binary operator that takes a variable and a value, then applies the specified operaton to the variable, and saves the result. This overwrites the variable's value with the resulting value.

```python
a = 1    # assign 1 to a
a += 1   # a == 2   # assign a + 1 to a
a -= 1   # a == 1   # assign a - 1 to a
a *= 20  # a == 20  # assign a * 20 to a
a /= 5   # a == 5   # assign a / 5 to a
```

### Comparison Operators

Sometimes, you may need to ask your program to take two items and see if they match or if one is greater than, less than, and/or equal to another. The operators used for this are: ``` == ``` (equal to), ``` != ``` (not equal to), ``` > ``` (greater than), ``` < ``` (less than), ``` >= ``` (greater than or equal to), ``` <= ``` (less than or equal to). Comparison operators always return a boolean result.

```python
2 >= 1
2 > 1
2 < 3
3 <= 3
'3' != 'a'
1 == 1
```

### Boolean Operators

Boolean operators are operators that use boolean input and provide a boolean output. The two boolean operators you need to know in Python are ``` and ``` and ``` or ```. ``` and ``` returns ``` True ``` if and only if both the left and right operands are both true, otherwise, it returns ``` False ```. ``` or ``` returns ``` True ``` if either of the operands are true, and returns ``` False ``` only if both of the operands are false.

```python
a = True and False  # a == False
a = False or True   # a == True
a = True or True    # a == True
a = True and True   # a == True
a = False or False  # a == False
```

### Unary Operators

Unary operators are operators with only one operand. A good example is the boolean operator ``` not ```. ``` not ``` returns the negated boolean value of the target expression.

```python
a = True        # a == True   # assign True to a
b = not a       # b == False  # assign not a to b
a = not a and b # a == False  # assign (not a) and b to a
```

## Requirements

In this directory, you'll find a file called ``` operators.py ```. Please follow the instructions in the comments, and pass the grader before proceeding.

## Concepts

 Next, we're going to focus on a few of the basics of Python syntax, and how to avoid common errors.

### Syntax

[Syntax](https://www.merriam-webster.com/dictionary/syntax) is the set of rules that we must follow in order for our code to be correctly interpreted. If you try to run your code and see a syntax error, it means that some part of your code cannot be correctly interpreted by the computer, and must be changed before it will run.


### Expressions

An expression in a programing language is a section of code that gets evaluated to a single value. In the operators exercise, everything on the right side of each equals sign is an expression. 

### Code Blocks

Code is separated into sections called blocks. In Python, blocks are separated by indentation levels; in C or Java, code blocks are separated by curly braces. Code blocks can be nested, as with an if statement:

```python
print('about to enter a different code block')
if True:
    print('inside nested block')
print("and now I'm back!")
```  

As you can see from the above code, the "flow of control" went from the bottom level for first statement, inside the 'if' block, then back to the bottom level. How is this any different from what we've done already? Let me show you by changing the code a bit:

```python
print('skipping code block...')
if False:
    print("oh no don't skip me!")
    print("I really want to get executed!")
    print("aww man...")
print("now I'm here!")
```

If you ran the above code, you'd see: 
```
skipping code block...
now I'm here!
```
because we didn't execute the code in the nested block. 

###### Notes:
* In Python, indentation levels must be a multiple of four. 

# Summary

In this lesson, you've learned about operators, data types, and some basic programming concepts. You may wish to keep the solved problems on your computer so that your can refer back to them. In any case, you're well on your way to learning Python! Congratulations!
