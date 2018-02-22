discord_bot.py
==========
#### INSTALL PRE-REQUISITES FOR PYTHON 3.6.X AND DISCORD.PY
1. Install libssl-dev (to ensure we can use pip when we install the newest version of Python):
```
sudo apt-get install libssl-dev
```
2. Install libffi-dev (to ensure audio works with the Discord bot):
```
sudo apt-get install libffi-dev
```
3. Install libsqlite3-dev (this will be handy, as it installs libraries needed to install sqlite3 support):
```
sudo apt-get install libsqlite3-dev
```

#### INSTALL PYTHON 3.6.X
1. Grab the latest version of Python 3.x from https://www.python.org/downloads/:
```
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
```
2. Extract the files, and enter the directory
```
tar xzvf Python-3.6.0.tgz
cd Python-3.6.0/
```
3. Run configure to check for dependencies, and get ready to build the Python installation (This will take 2-5 minutes)
```
./configure
```
4. Run make to start compiling the software
```
make
```
5.  Install Python 3.6.x
```
sudo make install
```

#### INSTALL DISCORY.PY, AND GET A BOT WORKING
1. Install latest version of the Discord library for Python (Discord.Py)
```
sudo python3 -m pip install -U discord.py[voice]
```

Jangle 0.0.1 General Info
------------------

