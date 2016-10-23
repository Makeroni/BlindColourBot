#!/usr/bin/env python

from mysql_manager import SQLManager

def main():
    mmanager = SQLManager()
#    mmanager.insert_daltonic_data('protanopia', '222', "John", "Doe")
    result = mmanager.load_daltonic_data('222')
    print result
#    result = mmanager.delete_user('222')
#    if result == True:
#       print "Deleted"
#    else:
#       print "Not deleted"
    enabled = mmanager.check_active_bot('222')
    if enabled == True:
       print "Bot enabled"
    else:
       print "Bot disabled"
    update_status = mmanager.update_status_bot('222', False)
    if update_status == True:
       print "Bot updated status"
    else:
       print "Bot not updated status"

if __name__ == "__main__":
     main()


