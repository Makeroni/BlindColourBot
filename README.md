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

### Install Numpy:

```
pip install numpy
```

### Install MySQL and Python utillities for MySQL:

```
sudo apt-get install mysql-server python-mysqldb
```

### Import MySQL Database:

1. Create MySQL database in your MySQL databse engine:

```
CREATE DATABASE IF NOT EXISTS DALTONIC_BOT;
```

2. Import the MySQL dump file:

```
mysql -u <username> -p <databasename> < DALTONIC_BOT_2016-10-22.sql
```

This bot also uses Daltonize project. Big thank you for this wonderful tool:heartbeat::

[https://github.com/joergdietrich/daltonize](https://github.com/joergdietrich/daltonize)

Add this bot to your convertion at [https://telegram.me/BlindColourBot](@BlindColourBot).
