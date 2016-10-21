#!/usr/bin/env python

from mysql_manager import SQLManager

def main():
    mmanager = SQLManager()
    mmanager.insert_daltonic_data('protanopia', '222', "John", "Doe")
    result = mmanager.load_daltonic_data('222')
    print result
    result = mmanager.delete_user('222')
    if result == True:
       print "Deleted"
    else:
       print "Not deleted"

if __name__ == "__main__":
     main()


