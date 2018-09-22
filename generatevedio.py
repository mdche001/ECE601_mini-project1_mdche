import os
import subprocess


def create(screen_name):
    try:
        #os.chdir('C:/Users/synox/mini_project1/')
        subprocess.Popen("ffmpeg -r 1/1 -i "+screen_name+"/image%d.jpg -vcodec mpeg4 -y "+screen_name+"/"+screen_name+".mp4")
    except:
        print('error')