# **BlindColourBot**

Telegram bot that converts images for blind colour people. Tested on Raspberry Pi 2 Model B.:+1:

## Installation process

Choose your favorite GNU/Linuc distribution and install these programs:

### Install Python utils:

```
sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
```

### Install Pillow:

```
pip install Pillow
```

### Install MatPlot Library:

```
sudo apt-get install python-matplotlib
```

### Install Scipy:

```
sudo apt-get install python-scipy
```

### Install Numpy >= 1.9.0:

```
pip install numpy
```

### Install MySQL and Python utillities for MySQL:

```
sudo apt-get install mysql-server python-mysqldb
```

### Import MySQL Database:

* Create MySQL database in your MySQL database engine:

```
CREATE DATABASE IF NOT EXISTS DALTONIC_BOT;
```

* Import the MySQL dump file:

```
mysql -u <username> -p DALTONIC_BOT < DALTONIC_BOT_2016-10-22.sql
```

### Temporal folder creation

Inside telegram_daltonic_bot.py file there is a variable called SAVE_PATH, you can set your own path to save the images created. Inside this path create two folders **incoming_images** and **outcoming_images**.

```
mkdir SAVE_PATH/incoming_images
mkdir SAVE_PATH/outcoming_images
```

## Usage

List of command for [@BlindColourBot](https://telegram.me/BlindColourBot):

```
/start : Starts BlindColourBot
/help : Help for BlindColourBot
/stop : Stop BlindColourBot
/setmydaltonism : Set your daltonism configuratio
/resetmydaltonism : Reset your configuration
```

This bot also uses Daltonize project. Big thank you for this wonderful tool:heartbeat::

[https://github.com/joergdietrich/daltonize](https://github.com/joergdietrich/daltonize)

Add this bot to your conversation at [@BlindColourBot](https://telegram.me/BlindColourBot).
