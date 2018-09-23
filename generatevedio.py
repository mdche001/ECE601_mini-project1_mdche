#import os
import subprocess


def create(screen_name):
    # Convert images with labels into vedio
    try:
        #os.chdir('C:/Users/synox/mini_project1/') change to dirctionary including images
        subprocess.Popen("ffmpeg -r 1 -i "+screen_name+"/image%d.jpg -vcodec mpeg4 -y "+screen_name+"/"+screen_name+".mp4"" -vf scale=trunc(iw/2)*2:trunc(ih/2)*2")
    except:
        print('error')