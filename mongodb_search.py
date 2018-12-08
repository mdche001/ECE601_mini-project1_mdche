import pymongo
import describe_images1
import generatevedio
import twitterimage
import numpy as np
from collections import Counter

def search_user():
    screen_name = input("Input your username: ")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini_project3_mongo"]
    mycol = mydb["users"]
    if (mycol.count() == 0):
        print("No such user name")
    else:
        for user in mycol.find():
            if (user.get('username') == screen_name):
                print(user)


def delete_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini_project3_mongo"]
    mycol = mydb["users"]
    x = mycol.delete_many({})

    return


def search_word():
    twitterIDs = []
    word = input("Input a word to search: ")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini_project3_mongo"]
    mycol = mydb["users"]
    for user in mycol.find():
        desc = user.get('description')
        desc = desc.split(',')
        if word in desc:
            twitterIDs.append(user.get('username'))
    if twitterIDs == []:
        print("There is no TitterID has the label (",word,") in their images.")
    else:
        print("These TitterID has the label (",word,") in their images:")
        # ignore the same users
        l = []
        for i in twitterIDs:
            if not i in l:
                l.append(i)
        print(l)


def popular():
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini_project3_mongo"]
    mycol = mydb["users"]
    label = []

    for twitterID in mycol.find():
        labels = twitterID.get('Labels')
        x = labels.split(',')
        label = np.append(x, label)



    #print(label)
    label_counts = Counter(label)
    top_three = label_counts.most_common(4)
    print("The top three popular labels are:\n",top_three[1:])