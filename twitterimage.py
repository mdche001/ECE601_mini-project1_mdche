import tweepy  # Ref:https://tweepy.readthedocs.io/en/v3.5.0/index.html
import os, sys
import wget

#Authentication for using twitter API
consumer_key = 'lklWiDCCsr4XrKfj8lHEv5vo3'
consumer_secret = '7a50uiKUoJqjwjKdWOT6kbf9otrYTnsrCxJo56tB4bf1htZJyQ'
access_token = '1038239626966822917-DOF0WSniAo3COib0JFFDqhHC3sNFhU'
access_token_secret = 'GVsO61PvAanANCZFhTk4tgRdJaXGZv2UYglA0hbG5BdQG'


def get_images(screen_name):
    #set authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # Receive the 1st set of user status
    try:
        tweets = api.user_timeline(screen_name, count=200)
    except:
        print ('error')
        exit()
    # Check if there are no more tweets
    if (len(tweets) == 0):
        print('No more tweets existed')
    # Get url of jpg
    else:
        media_files = set()
        for status in tweets:
            media = status.entities.get('media', [])
            if (len(media) > 0):
                url = media[0]['media_url']
                # find .jpg images
                file_type = url.split(".")[-1]
                if (file_type == "jpg"):
                    media_files.add(media[0]['media_url'])
        if (len(media_files) == 0):
            print ("no more jpg images")
            exit()
    # creat a new folder for twitter images
    directory = os.getcwd() + "/" + screen_name
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print ("already exsist")
    except:
        print('Error')
    # Download images into the folder
    i=0
    for url in media_files:
        image_name = directory + '/image'+str(i) +".jpg"
        image=wget.download(url, out= image_name)
        i += 1


