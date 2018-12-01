import twitterimage
import generatevedio
import describe_images1

def add_user(mycursor):
    screen_name = input("Enter a user name: ")
    mycursor.execute("SELECT * FROM user_options WHERE username='" + screen_name + "'")
    myresult = mycursor.fetchall()
    if (len(myresult) != 0):
        print("User name already exsist")
        return
    print(screen_name)
    print("-------------------------------------")
    print("downloading image from tweeter feed " + screen_name)
    print("-------------------------------------")
    img_num = twitterimage.get_images(screen_name)
    print("-------------------------------------")
    print("analyzing video")
    print("-------------------------------------")
    describe_images1.get_describe(screen_name, screen_name, img_num)
    print("-------------------------------------")
    print("creating video from ", str(img_num), " images")
    print("-------------------------------------")
    generatevedio.create(screen_name,screen_name,img_num)

    return

def query_user(mycursor):
    screen_name = input("Enter a user name to query: ")
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
    word = input("Enter a word to search: ")
    mycursor.execute(("SELECT * FROM user_options"))
    myresult = mycursor.fetchall()
    print("The next user has the word", word, "in their description:")
    for user in myresult:
        desc = user[3]
        desc = desc.split(',')
        if word in desc:
            print(user[1])

