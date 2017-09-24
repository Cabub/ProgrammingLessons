# Lesson 1

The first thing you'll need to do is set up a development environment. Your development environment is the set of programs, libraries, and tools you use to develop programs. For Python I typically use graphical text editor like [Atom](https://atom.io/) to write code and a shell like [IPython](https://ipython.org/) to test my work. For the purposes of this class however, we're going to install an IDE (Integrated Development Environment) because it has all the tools we need together in one place, and should have consistent results between users of different operating systems.

For the purposes of this class, we'll be using PyCharm from JetBrains as our IDE. If you already have a preferred IDE, or would like to use a different development stack, you should be able to follow along through each of the lessons anyway.

## Setup

#### PyCharm

Depending on your operating system, setup will be different. I'll separate the instructions below:

###### Windows

For Windows, visit [PyCharm's download page](https://www.jetbrains.com/pycharm/download/#section=windows) and select the community edition (unless you want to pay for it). This will prompt a download, accept it. Then run the executable and follow through the on-screen instructions. Once you have it installed, proced to the next section.

###### macOS

For macOS, visit [PyCharm's download page](https://www.jetbrains.com/pycharm/download/#section=mac) and select the community edition (unless you want to pay for it). This will prompt a download, accept it. Then run the executable and follow through the on-screen instructions. Once you have it installed, proced to the next section.

###### Linux

Installation on Linux is best solved through your distrobution's package manager. If you're using Ubuntu, or Linux Mint, this should work.
```bash
sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
sudo apt-get update
sudo apt-get install ubuntu-make
umake ide pycharm
```

#### Install Markdown plugin

This step isn't strictly necessary but it will make the README files easier to read. Open Pycharm and click ``` Configure ```, then ``` Plugins ```. Type ``` markdown ``` into the search bar, then click ``` Search in repositories ```. This will search for plugins with the keyword ``` markdown ``` and return a list of results. Click ``` Markdown support ```, then ``` Install ```. Finally, ``` Restart PyCharm ```. Now the markdown plugin should be installed and active.

#### Download this repository

Go to [the repository homepage](https://github.com/Cabub/ProgrammingLessons) and click ``` Clone or download ``` (the green button).  Then click ``` Download ZIP ```. When it finishes downloading, extract the contents of the zip file somewhere and remember where.

#### Open Project

Open PyCharm and click ``` Open ```. Then navigate to where you extracted the repository. Now select the folder named ProgrammingLessons or ProgrammingLessons-master and click ``` Open ```.

Now click on ``` Lesson1 ```, to make the directory expand, then double-click on README.md. This should cause this set of instructions to be opened in the work area. If you click the the document-view icon in the view selection on the top right, you should be able to read these instructions there.

### Basic concepts

In programming, theres two types of data: constants and variables. Constants are hard-coded values that never change, and variables' values can change. When you write ``` 1 + 1 ``` in Python, the value of those 1's isnt going to change, so those are constants. However if you wrote ``` a = 1 + 1 ``` you're setting the value of a to 2, but the value of a could change later; thus, a is a variable.

In code you'll see some lines of text that explains what the code does, has some basic metadata about the code (like the name of the author and when it was last changed), or just makes a joke. These are called comments, and theres a few ways to write them in Python. Anything on the same line after the ``` # ``` symbol is a comment in python. If the comment is on the same line as some non-commented code, then it's an inline comment
```python
a = 1 + 1 # like this
```
but if the comment is on a line by itself, it's called a block comment.
```python
# like this
a = 1 + 1
```
Additionally, we can use a string literal as a comment, and it's called a _docstring_.
```python
''' like this
'''
```
A string is just a bunch of characters surrounded by quotes and treated as text. In ``` HelloWorld.py ``` you'll see a docstring describing the file's purpose. Its only use is as a comment in the code and won't be used when the code is running.


### Hello world!

Yes, it's cliché, but we're doing it anyway. You need to create your first program, and we're going to make it print the words ``` Hello World! ``` on screen.

In the Lesson1 Directory double-click 'HelloWorld.py'. You should now see a text editor in the center of your screen. There you'll find the following lines:
```python
''' HelloWorld.py
This is intended to be your first program.
Input: None
Output: Prints 'Hello World!' to the screen.
'''
```
This is the aforementioned docstring, and won't be used when we run the code. You can write whatever you want between the ``` ''' ``` symbols and it will have no affect on the code.

 Type the follwing below the docstring:
```python
print('Hello World!')
```

Save the document, then on the menu bar click ``` Run ```, ``` Run ```, and select HelloWorld. Now an outbut bar should appear on the bottom of your screen with the words ``` Hello World! ```. Well done! You've just written your first program. You can try printing other strings out, writing the different types of comments, or modifying the docstring. When you're ready, begin lesson 2 by opening the ``` Lesson2 ``` directory and double-clicking the contained ``` README.md ```.
