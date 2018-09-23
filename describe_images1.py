import os
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import ImageDraw, Image, ImageFont


def get_describe( screen_name):
    client = vision.ImageAnnotatorClient()
    # list = os.listdir('C:/User/synox/mini_project1/'+screen_name+'/')
    # for i in (0, len(list))  P:  I cannot find images in screen_name/ by this method
    i=0
    while(True):
        # Find all images from twitter and add labels
        if os.path.exists('./'+screen_name+'./'+'image'+ str(i) + '.jpg') == True:
            file_name = os.path.join(os.path.dirname('C:/Users/synox/mini_project1/'+screen_name+'/image%s.jpg'), 'image%s.jpg'%(i))
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Detection labels of the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            # Attach labels to the images
            j=0
            for label in labels:
                raw_image = Image.open(file_name)
                draw = ImageDraw.Draw(raw_image)
                font = ImageFont.truetype('C:/Windows/Fonts/Tahoma/tahoma.ttf', 15) #solved problem: OSError: cannot open resource   ∵ set wrong path to .ttf
                fillcolor = 'yellow'
                draw.text((10, 10+15*j), label.description, fill=fillcolor, font=font)#solved problem: labels overlap on the same position   soluton: using for loop to give offset
                j=j+1
                raw_image.save(file_name)
            i = i+1

        else:
            print('no more jpg existed')
            break