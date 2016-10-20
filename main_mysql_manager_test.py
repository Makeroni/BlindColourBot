#!/usr/bin/env python

from mysql_manager import SQLManager

def main():
    mmanager = SQLManager()
    mmanager.insert_daltonic_data('protanopia', '222')
    result = mmanager.load_daltonic_data('222')
    print result

if __name__ == "__main__":
     main()


