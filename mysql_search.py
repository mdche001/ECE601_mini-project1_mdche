import twitterimage
import generatevedio
import describe_images1
import numpy as np
from collections import Counter

def add_user(mycursor,databasenum):
    screen_name = input("Enter a user name: ")
    mycursor.execute("SELECT * FROM user_options WHERE username='" + screen_name + "'")
    myresult = mycursor.fetchall()
    if ((len(myresult) != 0) and (databasenum ==1)):
        print("User name already exsist")
        return
    print(screen_name)
    print("\n")
    print("downloading image from tweeter feed " + screen_name)
    print("\n")
    img_num = twitterimage.get_images(screen_name)
    print("\n")
    print("detect labels")
    print("\n")
    describe_images1.get_describe(screen_name, screen_name, img_num,databasenum)
    print("\n")
    print("creating video from ", str(img_num), " images")
    print("\n")
    generatevedio.create(screen_name, screen_name, img_num)
    return


def search_user(mycursor):

    screen_name = input("Enter a user name: ")
    mycursor.execute("SELECT * FROM user_options WHERE username='" + screen_name + "'")
    myresult = mycursor.fetchall()
    if (len(myresult) == 0):
        print("No such user name")

    else:
        for user in myresult:
            print(user)


def delete_db(mycursor):
    mycursor.execute("truncate user_options;")
    return


def search_word(mycursor):

    twitter_IDs = []
    word = input("Enter a word to search: ")
    mycursor.execute(("SELECT * FROM user_options"))
    myresult = mycursor.fetchall()
    for user in myresult:
        desc = user[3]
        desc = desc.split(',')
        if word in desc:
            twitter_IDs.append((user[0]))
    if twitter_IDs == []:
        print("There is no TitterID has the label (",word,") in their images.")
    else:
        print("These TitterID has the label (",word,") in their images:")
        # ignore the same users
        l = []
        for i in twitter_IDs:
            if not i in l:
                l.append(i)
        print(l)


def popular(mycursor):

    mycursor.execute(("SELECT * FROM user_options"))
    result = mycursor.fetchall()

    label = []

    for user in result:
        desc = user[3]
        desc = desc.split(',')
        label = np.append(desc, label)
    #print(label)
    label_counts = Counter(label)
    top_three = label_counts.most_common(4)
    print("The top three popular labels are:\n",top_three[1:])