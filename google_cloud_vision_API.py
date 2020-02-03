from google.cloud import vision
import io
from PIL import Image , ImageDraw
import os
import pymongo


#這裡要設定自己的GCP認證json
credential_path = "C:/Users/wilson_su/Desktop/skyline/python-docs-samples/vision/cloud-client/detect/yourjson.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

client = vision.ImageAnnotatorClient()

with io.open("./d11.jpg", 'rb') as image_file:
    content1 = image_file.read()
image1 = vision.types.Image(content=content1)

response1 = client.text_detection(image=image1)
texts1 = response1.text_annotations
print('Texts:')
for text in texts1:
    print('\n"{}"'.format(text.description))
