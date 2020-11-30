#  Written by Mark Chua

import requests
import base64
import json
from picamera import PiCamera
from time import sleep
import cv2
from PIL import Image, ImageFilter


camera = PiCamera()

#  Takes a picture and saves it.
camera.start_preview()
sleep(5)
camera.capture('picTaken.jpg')
camera.stop_preview()

IMAGE_PATH = 'picTaken.jpg'
SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO'

#  Convert image to greyscale
IMG_G = Image.open('picTaken.jpg').convert('L')
IMG_G.save('greyscale.jpg')
GRAY_IMG_PATH = 'greyscale.jpg'

#  Denoise greyscaled image
IMG_D = IMG_G.filter(ImageFilter.MinFilter(3))
IMG_D.save('denoise.jpg')
DENOISE_IMG_PATH = 'denoise.jpg'

with open(DENOISE_IMG_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data=img_base64)

try:
    print({
        'Plate': r.json()['results'][0]['plate']
    })
except:
    print('Plate cannot be identified. Please make sure plate is at the center and clear.')

IMG = cv2.imread('picTaken.jpg')
IMG_GRAY = cv2.imread('greyscale.jpg')
IMG_DENOISE = cv2.imread('denoise.jpg')

#  Output 3 images
cv2.imshow('OutputImage-picTaken', IMG)
cv2.imshow('OutputImage-greyscale.jpg', IMG_GRAY)
cv2.imshow('OutputImage-denoise.jpg', IMG_DENOISE)

cv2.waitKey(0)