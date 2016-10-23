# **BlindColourBot**

Telegram bot that converts images for blind colour people. Tested on Raspberry Pi 2 Model B.:+1:

## Installation process

Choose your favorite GNU/Linuc distribution and install these programs:

### Install Python utils:

```{r, engine='bash', count_lines}
sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
```

### Install Pillow:

```{r, engine='bash', count_lines}
pip install Pillow
```

### Install MatPlot Library:

```{r, engine='bash', count_lines}
sudo apt-get install python-matplotlib
```

### Install Scipy:

```{r, engine='bash', count_lines}
sudo apt-get install python-scipy
```

### Install Numpy >= 1.9.0:

```{r, engine='bash', count_lines}
pip install numpy
```

### Install MySQL and Python utillities for MySQL:

```{r, engine='sql', count_lines}
sudo apt-get install mysql-server python-mysqldb
```

### Import MySQL Database:

* Create MySQL database in your MySQL database engine:

```{r, engine='bash', count_lines}
CREATE DATABASE IF NOT EXISTS DALTONIC_BOT;
```

* Import the MySQL dump file:

```{r, engine='bash', count_lines}
mysql -u <username> -p DALTONIC_BOT < DALTONIC_BOT_2016-10-22.sql
```

### Temporal folder creation

Inside **telegram_daltonic_bot.py** file there is a variable called SAVE_PATH, you can set your own path to save the images created. Inside this path create two folders **incoming_images** and **outcoming_images**.

```{r, engine='bash', count_lines}
mkdir SAVE_PATH/incoming_images
mkdir SAVE_PATH/outcoming_images
```

## MySQL credentials

On **mysql_manager.py** file set your MySQL credentials:

```{r, engine='python', count_lines}
db_host = "localhost"
db_name = "DALTONIC_BOT"
db_user = "root"
db_password = ""
```

## Usage

Ccommands list for [@BlindColourBot](https://telegram.me/BlindColourBot):

* /start : Starts BlindColourBot
* /help : Help for BlindColourBot
* /stop : Stop BlindColourBot
* /setmydaltonism : Set your daltonism configuration
* /resetmydaltonism : Reset your configuration

This bot also uses Daltonize project. Big thank you for this wonderful tool:heartbeat::

[https://github.com/joergdietrich/daltonize](https://github.com/joergdietrich/daltonize)

Add this bot to your conversation at [@BlindColourBot](https://telegram.me/BlindColourBot).
