import os
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import ImageDraw, Image, ImageFont
FONT_PATH = os.environ.get("FONT_PATH", 'C:/Windows/Fonts/Tahoma/tahoma.ttf')

client = vision.ImageAnnotatorClient()


def get_describe( screen_name):
    '''
    list = os.listdir('C:/User/synox/mini_project1/'+screen_name+'/')
    for i in (0, len(list))                                            P:  cannot find images in screen_name/
    '''
    i=0
    while(True):
        if os.path.exists('./'+screen_name+'./'+'image'+ str(i) + '.jpg') == True:
            file_name = os.path.join(os.path.dirname('C:/Users/synox/mini_project1/'+screen_name+'/image%s.jpg'), 'image%s.jpg'%(i))
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            j=0
            for label in labels:
                raw_image = Image.open(file_name)
                draw = ImageDraw.Draw(raw_image)  #
                font = ImageFont.truetype('C:/Windows/Fonts/Tahoma/tahoma.ttf', 15) #P:OSError: cannot open resource  wrong path to .ttf
                draw.text((10, 10+15*j), label.description, fill=(255,255,0), font=font)#P:  labels overlap on the same position
                j=j+1
                raw_image.save(file_name)
            i = i+1

        else:
            print('no more jpg existed')
            break