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

## Download this repository

If you have git installed, you can use ``` git clone https://github.com/Cabub/ProgrammingLessons.git ``` to download the repository, otherwise, just download the .zip file and extract it in your documents folder.

### Hello world!

Yes, it's cliché, but we're doing it anyway.

Open up PyCharm, then click ``` Create New Project ```. In the ``` Location ``` instead of ``` untitled ``` write ``` HelloWorld ```. Make sure your interpreter is ``` python3.6 ```, then click ``` Create ```.
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

## Download this repository

If you have git installed, you can use ``` git clone https://github.com/Cabub/ProgrammingLessons.git ``` to download the repository, otherwise, just download the .zip file and extract it in your documents folder.

### Hello world!

Yes, it's cliché, but we're doing it anyway.

Open up PyCharm, then click ``` Create New Project ```. In the ``` Location ``` instead of ``` untitled ``` write ``` HelloWorld ```. Make sure your interpreter is ``` python3.6 ```, then click ``` Create ```. Right click on the ``` HelloWorld ``` project in the left-hand bar, and click on ``` New ```, ``` Python File ```. Name it ``` HelloWorld ```.

You should now see a text editor in the center of your screen. Type the follwing into the text area:
```python
print('Hello World!')
```

Save the document, then on the menu bar click ``` Run ```, ``` Run ```, and select HelloWorld. Now an outbut bar should appear on the bottom of your screen with the words ``` Hello World! ```. Well done! You've just written your first program.
