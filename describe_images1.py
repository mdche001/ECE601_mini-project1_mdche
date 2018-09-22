import os
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import ImageDraw, Image, ImageFont
FONT_PATH = os.environ.get("FONT_PATH", 'C:/Windows/Fonts/Tahoma/tahoma.ttf')

client = vision.ImageAnnotatorClient()


def get_describe( screen_name):
    for i in range(23):
        if os.path.exists('./'+screen_name+'/'+'image'+ str(i) + '.jpg') == True:
            file_name = os.path.join(os.path.dirname('C:/Users/synox/mini_project1/'+screen_name+'/image%s.jpg'), 'image%s.jpg'%(i))
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            for label in labels:
                raw_image = Image.open(file_name)
                draw = ImageDraw.Draw(raw_image)  # 修改图片
                font = ImageFont.truetype('C:/Windows/Fonts/Tahoma/tahoma.ttf', 36) #P:OSError: cannot open resource  wrong path to .ttf
                draw.text((100, 40), label.description, fill=(255,255,0+5), font=font)
                raw_image.save(file_name)
                break
        else:
            print('no file existed')