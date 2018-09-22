import sys
import os

import twitterimage
import generatevedio as generatevedio
import describe_images1

def main():
    screen_name = sys.argv[1]
    print (screen_name)
    print ("*")
    print ("downloading image from "+screen_name)
    print ("*")
    twitterimage.get_images(screen_name)
    print ("*")
    print ("analyzing video")
    print ("*")
    describe_images1.get_describe( screen_name)
    print ("*")
    print ("creating video from images"+screen_name)
    print ("*")
    generatevedio.create(screen_name)
main()
