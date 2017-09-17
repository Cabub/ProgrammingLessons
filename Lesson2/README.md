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
### Boolean

A boolean data type is a data type with only two possible values, either True or False. We use booleans to create triggers or to test something. This data type will be better explained when you learn how to use objects that use them.

### Variables

Variables are places to store data that might change. A variable can be named just about whatever you want, as long as it begins with a letter, only contains letters or numbers, and has no spaces. You can assign data to a variable by using the ``` = ``` operator.
```python
my_string = "This is a string"
my_integer = 1
my_float = 64
```
now the value of "This is a string" is stored in the variable named 'my_string' and we can reference it by using 'my_string' again like this:
```python
print(my_string)
```
This will cause the string "This is a string" to be printed out.

### Arithmetic Operators

Arithmetic operators are used to perform math operations. The operators available to use in Python are: Addition (+) adds two values together, Subtraction (-) subtracts the right operand by the left operand, Multiplication (\*) multiplies the right operand by the left operand, Division (/) divides the left operand by the right operand, Modulus (%) divides the left operand by the right operand and returns the remainder, Exponent (\*\*) calculates the exponential value, and Floor division (//) performs integer division

###Comparison operators

Sometimes, you may need to ask your program to take two items and see if they match or if one is greater than, less than, and/or equal to another. The operators used for this are: == (equal to), =!(not equal to), >(greater than), <(less than), >=(greater than or equal to), <=(less than or equal to)

#### The 'Type' Talk

Back in my day, we had to be very careful about the datatypes we were using and converting between them. Nowadays Python takes care most of that for you, but you still need to be careful or you could be burned by bad typing. I'm sure we'll talk more about it later in the course, but for now, you should know that you can check the type of a variable by using the ``` type ``` function.
```python
type('str')
type('int')
type('float')
```
You can also 'cast' variables or constants (a constant is just some data that doesn't change) into another data type by using it's 'constructor' (we'll get more into that later, just remember the terminology).
```python
a = int(123.123)
b = float(5)
c = str(123)
```
After running the above code, a = ``` 123 ```, b = ``` 5.0 ``` and c = ``` '123' ```.


## Requirements

In this directory, you'll find a file called ``` datatypes.py ```. I've taken the liberty of writing a few comments (oh yeah I haven't talked about comments! I'll get to that next) with instructions for how to pass the first part of the lesson. Please pass the grader for datatypes.py before proceeding.
