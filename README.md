# <ins>Minesweeper</ins> 

### Popular "minesweeper" game written in python.

<br>

### <u>Here you can find a synchronization between our project and Travis CI</u> 

[![Build Status](https://travis-ci.org/danielwardega/sinwo_sapper.svg?branch=master)](https://travis-ci.org/danielwardega/sinwo_sapper)

<br>

### <ins>Creating a virtualenv</ins> 


In order to run the game you will have to create a virtual environment.
 
Check if the package called **virtualenv** is installed on your computer.\
If not, install it via pip:

**pip install virtualenv**

After the package is installed, go to the repository's directory and create the virtual environment by using the following command:

**virtualenv -p python3 <your virtualenv's name>**

Now you’ll need to activate virtualenv.\
Just type the following command at the prompt:

**source <your virtualenv's name>/bin/activate**

When the virtualenv is activated you can install all necessary python packages.\
Just type the following command at the prompt:

**pip install -r requirements.txt**

When all necessary python packages are installed you can run the game.

### <ins>Running The Game</ins>

Go to the repository's directory and activate the virtual environment.\
Just type the following command at the prompt:

**source <your virtualenv's name>/bin/activate**

Now run our game:\
Type the following command at the prompt:

**python source/main.py**