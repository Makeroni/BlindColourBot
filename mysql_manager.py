#!/usr/bin/env python

import MySQLdb

class SQLManager:
    
    global db_host 
    global db_name
    global db_user
    global db_password
   
    db_host = "localhost"
    db_name = "DALTONIC_BOT"
    db_user = "root"
    db_password = ""

    def __init__(self):
        print "object created"

    def new_connection(self):
        try:
            global db
            db = MySQLdb.connect(db_host, db_user, db_password, db_name)
            global cursor
            cursor = db.cursor()
        except:
            print "Error: closing databe connection..."
            close_connection()

    def insert_daltonic_data(self, daltonic_type, user_id):
        status = False
        self.new_connection()
        try:
            query = "INSERT INTO users_bot (date, time, daltonic_type, user_id) values(CURRENT_DATE(), NOW(), '" + daltonic_type + "', '" + user_id + "') "
            query += "ON DUPLICATE KEY UPDATE date = CURRENT_DATE(), time = NOW(), daltonic_type = '" + daltonic_type + "'" 
            cursor.execute(query)
            db.commit()
            print "Data committed" 
            status =  True
        except:
            print "Error: the database is being rolled back"
            db.rollback()
        self.close_connection()
        return status

    def load_daltonic_data(self, user_id):
        self.new_connection()
        result = {}
        try:
            query = "SELECT user_id, daltonic_type FROM users_bot WHERE user_id = '" + user_id + "' limit 1" 
            cursor.execute(query)
            data = cursor.fetchall()
            rows = len(data)
            if (rows > 0):
               for row in data:
                  user_id = row[0] 
                  daltonic = row[1]
                  result[str(user_id)] = daltonic
                  break              
        except:
            print "Error: the database connection closing on fetch..."
        self.close_connection()
        return result

    def close_connection(self):
        db.close()
