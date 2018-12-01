import sys
import os

import twitterimage
import generatevedio
import describe_images1
import mysql_search
import mysql.connector
from statistics import mode

def main():
    # Connection to mysql db
    while (True):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456",auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS  mini_project3_db")
        mycursor.execute("use mini_project3_db")
        mycursor.execute("CREATE TABLE  IF NOT EXISTS user_options (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255), img_num VARCHAR(255),description VARCHAR(255),description_num VARCHAR(255),file_name VARCHAR(255),Modified_time VARCHAR(255))")
        mycursor.execute("use mini_project3_db")
        print("\n")
        print("\n")
        print( "optionsbase Options:\n ")
        print("----------------------------------------------------")
        print("1.Create new user name\n")
        print("----------------------------------------------------")
        print("2.Query exsist user name\n")
        print("----------------------------------------------------")
        print("3.Delete user\n")
        print("----------------------------------------------------")
        print("4.Search\n")
        print("Or press any other keys to Exit")
        
        options = input("Select option by number: ")
        options = int(options)
        print(options)
        if (options == 1):
            mysql_search.add_user(mycursor)
        elif (options == 2):
            mysql_search.query_user(mycursor)
        elif (options == 3):
            mysql_search.delete_db(mycursor)
        elif (options == 4):
            mysql_search.search_word(mycursor)
        else:
            exit()

main()



