discord_bot.py
==========
##### INSTALL PRE-REQUISITES FOR PYTHON 3.6.X AND DISCORD.PY
Install libssl-dev (to ensure we can use pip when we install the newest version of Python):
>sudo apt-get install libssl-dev

Install libffi-dev (to ensure audio works with the Discord bot):
>sudo apt-get install libffi-dev

Install libsqlite3-dev (this will be handy, as it installs libraries needed to install sqlite3 support):
>sudo apt-get install libsqlite3-dev


##### INSTALL PYTHON 3.6.X
Grab the latest version of Python 3.x from https://www.python.org/downloads/:
>wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz

Extract the files, and enter the directory
>tar xzvf Python-3.6.0.tgz
>cd Python-3.6.0/

Run configure to check for dependencies, and get ready to build the Python installation (This will take 2-5 minutes)
>./configure

Run make to start compiling the software
>make

Install Python 3.6.x
>sudo make install

##### INSTALL DISCORY.PY, AND GET A BOT WORKING
Install latest version of the Discord library for Python (Discord.Py)
>sudo python3 -m pip install -U discord.py[voice]

Jangle 0.0.1 General Info
------------------

