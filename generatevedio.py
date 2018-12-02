import os
import subprocess
import pymongo
import mysql.connector
import datetime

def create(screen_name,username,img_num):

    # Convert images with labels into vedio
    try:
        #os.chdir('C:/Users/synox/mini_project1/') change to dirctionary including images
        subprocess.Popen("ffmpeg -r 1 -i " + "./" + screen_name + "/image%d.jpg -vcodec mpeg4 -y " + "./" +screen_name + "/" + screen_name + ".avi"" -vf scale=trunc(iw/2)*2:trunc(ih/2)*2")
        # subprocess.call(['ffmpeg', '-framerate', '1', '-i', screen_name +  '/image%d.jpg', '-vcodec', 'mpeg4', screen_name + '.avi'])

    except:
        print('error')

    # connect database
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456", auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("use mini_project3_db")
    sql = "INSERT INTO user_options (username,img_num,description,description_num,file_name,Modified_time) VALUES (%s,%s,%s,%s,%s,%s)"

    # connect mongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini_project3_mongo"]
    mycol = mydb["users"]

    if os.path.exists('./' + screen_name + '/' + screen_name + '.avi') == True:
        file_name = 'C:/Users/synox/mini_project1/' + screen_name + '/' + screen_name + '.avi'

        #insert Mysql
        mtime = datetime.datetime.now()
        val = (username, img_num, "N/A", "N/A", file_name, mtime)
        mycursor.execute(sql, val)
        mydb.commit()

        # insert mongodb
        mydict = {"username": username, "img_num": img_num, "description": "N/A", "description_num": "N/A","file_name": file_name, "Modified_time": mtime}
        x = mycol.insert_one(mydict)