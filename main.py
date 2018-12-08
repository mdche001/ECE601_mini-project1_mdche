import sys
import os
import twitterimage
import generatevedio
import describe_images1
import mysql_search
import mysql.connector
import mongodb_search
from statistics import mode
import pymongo

def main():
    # Connection to mysql db
    while (True):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456",auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS  mini_project3_db")
        mycursor.execute("use mini_project3_db")
        mycursor.execute("CREATE TABLE  IF NOT EXISTS user_options (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255), img_num VARCHAR(255),description VARCHAR(255),description_num VARCHAR(255),file_name VARCHAR(255),Modified_time VARCHAR(255))")
        mycursor.execute("use mini_project3_db")
        print( "Database Options:\n ")
        print("1.Create new user name\n")
        print("2.Search exsist user name\n")
        print("3.Delete user\n")
        print("4.Search words\n")
        print("Or press any other 5 to Exit")

        databasenum = input("Select your database style:\n 1.Mysql\n 2. Mongodb\n")
        databasenum = int(databasenum)
        options = input("Select option by number: ")
        options = int(options)
        print(options)
        if (options == 1):
            if (databasenum == 1):
                mysql_search.add_user(mycursor,databasenum)
            elif (databasenum == 2):
                mysql_search.add_user(mycursor,databasenum)
        elif (options == 2):
            if (databasenum == 1):
                mysql_search.search_user(mycursor)
            elif (databasenum == 2):
                mongodb_search.search_user()
        elif (options == 3):
            if (databasenum == 1):
                mysql_search.delete_db(mycursor)
            elif (databasenum == 2):
                mongodb_search.delete_db()
        elif (options == 4):
            if (databasenum == 1):
                mysql_search.search_word(mycursor)
            elif (databasenum == 2):
                mongodb_search.search_word()
        elif (options == 5):
            return

main()



