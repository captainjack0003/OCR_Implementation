# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:56:01 2023

@author: Rohan Jain
"""


import tesserocr
import os

import cv2
import numpy as np


print(os.getcwd())
print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages
# from tesserocr import get_languages


from tesserocr import PyTessBaseAPI
PyTessBaseAPI(path='C:/Users/jainr/.spyder-py3')


def image_storer_printer(image_loc):
    
    with PyTessBaseAPI() as api:
        api.SetImageFile(image_loc)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
    # api is automatically finalized when used in a with-statement (context manager).
    # otherwise api.End() should be explicitly called when it's no longer needed.

    


def image_sharpner(image_loc):
    imager = cv2.imread(image_loc)
    imager = cv2.resize(imager , (400 , 400))
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(imager, -1, sharpen_kernel)
    
    # cv2.imshow('sharpen', sharpen)
    # cv2.waitKey()

    cv2.imwrite('sharpened_image.jpg', sharpen)
    print("Sharpened image saved successfully!")

    image_path ='sharpened_image.jpg'
    image_storer_printer(image_path)
    


def image_grayscale(image_loc):

    # Load the image
    imager = cv2.imread(image_loc)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(imager, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite('gray_image.jpg', gray_image)
    print("gray_scale image saved successfully!")

    image_path ='gray_image.jpg'
    image_storer_printer(image_path)
    


def image_blur(image_loc):
    # Load the image
    image = cv2.imread(image_loc)
    
    # Apply the blur effect (5, 5) argument specifies the size of the blurring kernel,
    # which can be adjusted based on the desired blur strength.
    blurred_image = cv2.blur(image, (5, 5))
    cv2.imwrite('blurr_image.jpg',  blurred_image)
    print("blurr_image saved successfully!")

    image_path ='blurr_image.jpg'
    image_storer_printer(image_path)


  
    

# sharpening the image and then printing data
image_sharpner('example5.jpg')
# image_storer_printer('example5.jpg')




# from PIL import Image

# def auto_crop_image(image_path):
#     # Open the image
#     image = Image.open(image_path)
#     # Convert the image to grayscale
#     grayscale_image = image.convert('L')
#     # Find the bounding box of the actual content
#     bbox = grayscale_image.getbbox()
#     # Crop the image using the bounding box
#     cropped_image = image.crop(bbox)
#     # Save the cropped image
#     cropped_image.save('sam.jpg')

# # Specify the path to the image
# image_path = 'sample2.jpg'

# # Call the function to auto crop the image
# auto_crop_image(image_path)