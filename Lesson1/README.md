# Lesson 1

## Setup

#### Python

The first thing you'll need is [Python](https://www.python.org/downloads/). Please don't use Python 2. I'll keep everything in this repo runnable in anything above 3.5, but in my opinion it would be a waste of time to limit you to the practices and limits of a soon-to-be [deprecated](https://en.wikipedia.org/wiki/Deprecation) version of Python.

This isn't a course in how to install software on your chosen OS. If you can't figure that out (did you [try this](http://www.dummies.com/software/for-seniors-how-to-install-a-new-computer-program/)?) bookmark this and come back when you've got a greater handle on what you're doing here.

#### Text Editor

The text editor you use says a lot about you in programmer circles. Since you're just starting out, keep that in mind, but don't worry about it too much. Just know that if you tell someone you know how to program, and they ask you what text editor you are using, they're sizing you up.

You can use any text editor you want, but I'd suggest [Atom](https://atom.io/). It's very configurable, the official text editor of Github, and it runs on all popular operating systems. Also, there's a built-in markdown viewer, so which is what this file is written in, so it may make it easier to read.

If you're an  [intractable](http://www.thefreedictionary.com/intractable) type, first-of-all you're going to fit right in here. Second, I've provided a few links to decent graphical text editors for you to choose from. Just find one you like, no judgement here.

* [Atom](https://atom.io/)
* [Notepad++](http://www.thefreedictionary.com/intractable)
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Sublime](http://www.sublimetext.com/)

## Download this repository

If you have git installed, you can use ``` git clone https://github.com/Cabub/ProgrammingLessons.git ``` to download the repository, otherwise, just download the .zip file and extract. If you're here to learn programming, I'm not going to help you with git. That should be its own course.

### Hello world!

Yes, it's cliché, but we're doing it anyway. Write this in a file named hello_world.py.
```python
print('Hello world!')
```
Now let's check to make sure it works.

First you'll need the 'path' to the directory you saved that file in. Typically, you can find this in the address bar of your file manager. In Windows, it'll look like this: ``` C:\Users\User\Documents\ ```, on Mac or Linux it will look more like ``` /home/User/Documnts/ ```.

Now open up a terminal. You can do this on Windows by running the program ``` cmd.exe ``` or on Mac with ``` Terminal ``` otherwise if you're running Linux and don't know how to open a terminal, what are you doing?

Change your current directory to the path of the directory you saved hello_world.py in. To do this type ``` cd <path> ``` and press enter.

Now you should be able to use the command ``` python hello_world.py ``` to run your program.

If you saw ``` Hello world! ```, you did it! You officially wrote a computer program.

I'll let you off with no tests for this lesson, since you had to install all that software. But next time, I'm going to make sure you accomplished what you set out to do!
