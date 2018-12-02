import pymongo
import describe_images1
import generatevedio
import twitterimage


def query_user():
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
    word = input("Input a word to search: ")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mini_project3_mongo"]
    mycol = mydb["users"]
    for user in mycol.find():
        desc = user.get('description')
        desc = desc.split(',')
        if word in desc:
            print(user.get('username'))