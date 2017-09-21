# if statements

One of the fundamental purposes of programming is to compare, test, and
verify. You could spend all day looking at two excel sheets, comparing lists
and trying to find matches to write or type on a third file. This is where your
new found tool(python) comes in to play.

if statements are an important part of programming and by the end of this Lesson
you will see why.

Lets say you have two variables, one contains the time now, "10:00am" and the
other variable contains the time you are waiting for, "11:00am".

You dont have time to check it yourself and want python to quickly check the
data for you and alert you when the times match. Well with if statements python
can check data and run a bit of code when the trigger happens.

FORMAT :
if(ARGUMENT):
  <DO THIS>

To create an if statement first you must use the object "if". Within Parenthesis
you will create your argument. after that a colon to let python know your argument is over.
Now you will indent the following lines. Anything indented after your
"if(ARGUEMNT)" will be considered part of that code.

Indentation can be accomplished by either a space(or more) or a tab(which is 3
spaces.)

So lets try out our problem by plugging the data into our if statement line by
line.

if(varTimeNow == varTimeINeed):

Remembering lesson two you should recognize the Comparison operator being used.
we are literally asking python "if the variable 'TimeNow' is equal to 'TimeINeed'
then proceed to run the following indented code."

We then decide what we want to happen if these variables match.
   - we could create a new variable //  TimeIsNow = True
   - Increase or decrease the amount of a variable holding a number // Tick += 1
   - send a message to the user  // print("time is now!").

if(varTimeNow == varTimeINeed):
  print("time is now")

So as you can see with our code complete we alert the user when the times match.
Basically we are beginning to create an alarm clock, Issue is we would have
to run the code every minute ourselves. By the end of the course you will know
how to make python run this if statement every minute if you wanted to.

What if we also wanted to alert the user when the Time WAS NOT a match. We would
ad the else object allowing our code to have an action whether or not the
matches.

if(varTimeNow == varTimeINeed):
  print("time is now")
else:
  print("not yet time")

As you can see else is not indented because its not to be ran inside of the
conditions that the variables match. It follows the same format as the IF statement except because its
a broad statement it does not need an argument. It has its colon at the end and
the following line is indented.

Now lets say we did want something to happen if the if statement wasn't a match but
it did require a specific argument. Lets say you wanted to be notified an hour
before the time came. YOu would use an elif(ELSE IF) object and it would look indentical
to the if part.

if(varTimeNow == varTimeINeed):
  print("time is now")
elif(varTimeNow == (varTimeINeed - 1)):
  print("one hour before time needed")
else:
  print("not yet time")

So we have created the perfect net to catch our time, When the time happens we
are alerted, when the time is about to happen we are alerted, and to CATCH-ALL
we have our broad else statement to handle any situation that we did not
specifically need but wanted to do something with.

So lets break down the if statement and see what else we could do with it:
We know there are several operators with which we could compare arguments with.

  - == equal to
  - =! not equal to
  - >= Greater than or equal to
  - > greater than
  - <= Less than or equal to
  - < less than

So we could use any of the statements to compare, for instance :

if(1 > 2): // if 1 is greater than 2

or

if(5 >= 5): // is 5 is greater than or equal to 5

Lets say we wanted need two arguments to be true in order for a peice of code to
run :

if(5 = 5 and 1 > 2):
  print("hi")

Basically this is saying if 5 is 5 and 1 is greater than 2 then print "hi". The
same would apply if we wanted one or the other but not necessarily both:

if(5 = 5 or 1 > 2):
  print("hi")

By adding "and" or "or" we have a really powerful and dynamic tool to compare
data and sculpt code that will work precisely how we need it to.

# Quick Reference - if Statement

FORMAT:
if(<ARGUMENT>):
  <DO THIS>
elif(<ARGUMENT>):
  <DO THIS>
else:
  <DO THIS>

FORMAT:
if(<ARGUMENT> and <ARGUEMENT>)
  - if argument 1 and 2 are true do this

FORMAT
if(<ARGUMENT> or <ARGUEMENT>)
  - if argument 1 or 2 are true do this
