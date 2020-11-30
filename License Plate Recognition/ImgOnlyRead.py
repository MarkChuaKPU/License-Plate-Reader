#  Written by Mark Chua

import requests
import base64
import json
import cv2
from PIL import Image, ImageFilter

IMAGE_PATH = 'plate.jpg'
SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO'

#  Convert image to greyscale
IMG_G = Image.open('plate.jpg').convert('L')
IMG_G.save('greyscaleEX.jpg')
GRAY_IMG_PATH = 'greyscaleEX.jpg'

#  Denoise greyscaled image
IMG_D = IMG_G.filter(ImageFilter.MinFilter(3))
IMG_D.save('denoiseEX.jpg')
DENOISE_IMG_PATH = 'denoiseEX.jpg'

#  Reads the license plate
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

IMG = cv2.imread('plate.jpg')
IMG_GRAY = cv2.imread('greyscaleEX.jpg')
IMG_DENOISE = cv2.imread('denoiseEX.jpg')

#  Output 3 images
cv2.imshow('OutputImage-plate.jpg', IMG)
cv2.imshow('OutputImage-greyscaleEX.jpg', IMG_GRAY)
cv2.imshow('OutputImage-denoiseEX.jpg', IMG_DENOISE)

cv2.waitKey(0)
