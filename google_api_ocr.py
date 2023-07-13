# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:23:21 2023

@author: Rohan Jain
"""

# # ********************************************************************************************
# # ********************************************************************************************
# # ********************************************************************************************
# Rohan Jain                   26-05-2023               Development of Initial Version of Code
# Rohan Jain                   01-06-2023               Adding Different Test Cases
# Rohan Jain                   8-06-2023                Adding Different Test Cases
# Rohan Jain                   18-06-2023               Testing Different Cases
# Rohan Jain                   21-06-2023               Detecting Data from Data Sets
# Rohan Jain                   27-06-2023               Testing Different filters like Gray_Scale,Sharpner
# Rohan Jain                   02-07-2023               Testing Croping and Automation Process
# Rohan Jain                   07-07-2023               Testing Blurring of Image
# # ********************************************************************************************
# # ********************************************************************************************
# # ********************************************************************************************



# Authentication to Google API
import os
import cv2
import numpy as np

# re is used to extract 
# import re



# enter your key project here.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='ENTER_YOUR_KEY_NAME.json'
from google.cloud import vision
vision_client = vision.ImageAnnotatorClient()
image = vision.Image()

# Example images url
# image_uri = 'https://staticimg.amarujala.com/assets/images/2016/12/13/aadhar-card_1481617623.jpeg'
# image_uri='https://i.pinimg.com/originals/4e/5a/27/4e5a27c06d8c8c7ada75c3ff7541b381.jpg'
# image_uri='https://i.pinimg.com/564x/3c/82/51/3c8251d9382b42a43a26bdb240cd5324.jpg'
# image_uri='https://i.pinimg.com/564x/07/79/1f/07791f1c1762a50fb7f2e477c2d3a747.jpg'
# image_uri='https://5.imimg.com/data5/OG/WJ/MT/ANDROID-99211490/product-jpeg-1000x1000.jpeg'
# image_uri='C:/Users/jainr/.spyder-py3/sample3.jpeg'
# image_uri='https://drive.google.com/drive/folders/1UhkkoIAV-M9h8D_jOaSRDCiBJ-3a7A2f'
# image_uri='https://drive.google.com/drive/folders/1UhkkoIAV-M9h8D_jOaSRDCiBJ-3a7A2f.jpg'


def data_printer(image_content):
    image.content = image_content
    response = vision_client.text_detection(image=image)
    data = response.text_annotations[0].description
    
    return data



#taking image locally
def image_storer_printer(image_loc):
    
    # Read the image file and set it as the image content
    with open(image_loc, 'rb') as image_file:
        image_content = image_file.read()
        
    data=data_printer(image_content)
    
    # storing data using online url
    # image.source.image_uri = image_uri
    # response = vision_client.text_detection(image=image)
    # data=response.text_annotations[0].description
    
    return data

# data=image_storer('put_sample.jpeg')
# print(data)


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
    data=image_storer_printer(image_path)
    
    return data


def image_grayscale(image_loc):

    # Load the image
    imager = cv2.imread(image_loc)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(imager, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite('gray_image.jpg', gray_image)
    print("gray_scale image saved successfully!")

    image_path ='gray_image.jpg'
    data=image_storer_printer(image_path)
    
    return data


def image_blur(image_loc):
    # Load the image
    image = cv2.imread(image_loc)
    
    # Apply the blur effect (5, 5) argument specifies the size of the blurring kernel,
    # which can be adjusted based on the desired blur strength.
    blurred_image = cv2.blur(image, (5, 5))
    cv2.imwrite('blurr_image.jpg',  blurred_image)
    print("blurr_image saved successfully!")

    image_path ='blurr_image.jpg'
    data=image_storer_printer(image_path)

    return data


  
    

# sharpening the image and then printing data
data=image_sharpner('example10.jpg')
print(data)

    
# Split the data into lines
lines = data.split('\n')









# rough code for testing some cases.

# # Find the line index containing "GOVERNMENT OF INDIA" or "Government of India"
# govt_of_india_index = -1

# tracker=False
# # very basic Assumption that data retreival would retrieve line by line

# for i, line in enumerate(lines):
    
#     if "GOVERNMENT OF INDIA" == line:
#         govt_of_india_index = i
#         tracker=True
#         break
    
#     elif "Government of India" == line:
#         govt_of_india_index = i
#         tracker=True
#         break


# if not tracker:
#     print("image is not clear unable to detect data")
    
   
# hindi_name=None
# english_name=None

# # Extract the Hindi and English names from the lines following "GOVERNMENT OF INDIA"
# if govt_of_india_index != -1 and govt_of_india_index + 1 < len(lines):
#     hindi_name = lines[govt_of_india_index + 1].strip()
#     if govt_of_india_index + 2 < len(lines):
#         english_name = lines[govt_of_india_index + 2].strip()


# # Extract date of birth using pattern finder

# dob = re.findall(r"DOB:\s(\d{2}/\d{2}/\d{4})", data)
# dob = dob[0] if dob else None

# # Extract Aadhaar number
# aadhaar = re.findall(r"(\d{4}\s?\d{4}\s?\d{4})", data)
# aadhaar = aadhaar[0] if aadhaar else None


# #print relevent data
# if tracker:
#     print("Hindi Name:", hindi_name)
#     print("English Name:", english_name)
#     print("Date of Birth:", dob)
#     print("Aadhaar Number:", aadhaar)
