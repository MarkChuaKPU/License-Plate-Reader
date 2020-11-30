#  Written by Mark Chua

import requests
import base64
import json
import cv2


IMAGE_PATH = 'plate.jpg'
SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data=img_base64)

try:
    print({
        'Plate': r.json()['results'][0]['plate']
    })
except:
    print('Plate cannot be identified. Please make sure plate is at the center and clear.')

img = cv2.imread('plate.jpg')
cv2.imshow('OutputImage', img)

cv2.waitKey(0)
