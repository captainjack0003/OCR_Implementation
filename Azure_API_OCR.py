# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:43:19 2023

@author: Rohan Jain
"""


import requests
import cv2
import numpy as np

# Set the API endpoint and your subscription key
endpoint = "ENTER YOUR POINT"
subscription_key = "ENTER SUBSCRIPTION KEY"


# Set the API headers
headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": subscription_key
}


def data_printer(image_path):
    # Read the image file as binary data
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    # Check the response status code    
    response = requests.post(endpoint, headers=headers, data=image_data)
    
    # Check the response status code
    
    if response.status_code == 200:
        # Parse the response JSON
        response_json = response.json()
  
        # Extract the recognized text
        extracted_text = ""
        for region in response_json["regions"]:
            for line in region["lines"]:
                for word in line["words"]:
                    extracted_text += word["text"] + " "
  
        # Split the extracted text into lines
        lines = extracted_text.split("\n")
        # Print each line separately
        print("Text is Extracted:")
          
       
    return lines



#taking image locally
def image_storer_printer(image_path):
    
    # Read the image file and set it as the image content
    with open(image_path, 'rb') as image_file:
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


data=image_sharpner('enter_file_image_name.jpg')
print(data)