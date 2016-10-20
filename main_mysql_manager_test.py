#!/usr/bin/env python

from mysql_manager import SQLManager

def main():
    mmanager = SQLManager()
    mmanager.insert_language('protanopia', '222')
    result = mmanager.load_language('222')
    print result

if __name__ == "__main__":
     main()


