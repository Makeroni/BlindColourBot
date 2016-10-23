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
#        print "MySQL object created"
        pass

    def new_connection(self):
        try:
            global db
            global cursor
            db = MySQLdb.connect(db_host, db_user, db_password, db_name)
            cursor = db.cursor()
        except:
            print "Error: closing databe connection..."
            close_connection()

    def insert_daltonic_data(self, daltonic_type, user_id, name, surname):
        status = False
        self.new_connection()
        try:
            query = "INSERT INTO users_bot (date, time, daltonic_type, user_id, name, surname) " 
            query += "values(CURRENT_DATE(), NOW(), '" + daltonic_type + "', '" + user_id + "', '" + name  + "', '" + surname + "') "
            query += "ON DUPLICATE KEY UPDATE date = CURRENT_DATE(), time = NOW(), daltonic_type = '" + daltonic_type + "'" 
            cursor.execute(query)
            db.commit()
#            print "Data committed" 
            status =  True
        except:
            print "Error: the database is being rolled back - update_status_bot"
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
                  result[str(user_id)] = str(daltonic)
                  break              
        except:
            print "Error: the database connection closing on fetch..."
        self.close_connection()
        return result

    def check_active_bot(self, chat_id):
        self.new_connection()
        enabled = 0
        try:
            query = "SELECT enabled FROM active_bot WHERE chat_id = '" + chat_id + "' limit 1"
            cursor.execute(query)
            data = cursor.fetchall()
            rows = len(data)
            if (rows > 0):
               for row in data:
                  enabled = row[0]
                  break
        except:
            print "Error: the database connection closing on fetch..."
        self.close_connection()
        if (enabled == 1):
           return True
        return False

    def check_chat_exists_status_bot(self, chat_id):
        self.new_connection()
        exist = False
        try:
            query = "SELECT chat_id FROM active_bot WHERE chat_id = '" + chat_id + "' limit 1"
            cursor.execute(query)
            data = cursor.fetchall()
            rows = len(data)
            if (rows > 0):
                exist = True
        except:
            print "Error: the database connection closing on fetch..."
        self.close_connection()
        return exist

    def update_status_bot(self, chat_id, status):
        self.new_connection()
        operation = False
        try:
            enabled = 0
            if status == True:
               enabled = 1
            query = "INSERT INTO active_bot (date, time, chat_id, enabled) "
            query += "values(CURRENT_DATE(), NOW(), '" + chat_id + "', " + str(enabled) + ") "
            query += "ON DUPLICATE KEY UPDATE date = CURRENT_DATE(), time = NOW(), enabled = " + str(enabled)
            cursor.execute(query)
            db.commit()
            operation = True
        except:
            print "Error: the database is being rolled back - update"
            db.rollback()
        self.close_connection()
        return operation

    def delete_user(self, user_id):
        self.new_connection()
        status = False
        try:
            statement = "DELETE FROM users_bot WHERE user_id = '" + user_id + "'" 
            cursor.execute(statement)
            db.commit()
            status = True
        except:
            print "Error: the database connection closing on fetch..."
            status = False
        self.close_connection()
        self.update_status_bot(user_id, False)
        return status

    def close_connection(self):
        db.close()
