# OCR_Implementation
This repo will give you basic implementation of google cloud vision api, microsoft Azure api and tesseract-ocr for text recognition from documents like adhaar card, Pan card.
# This code have functions which can blur the image, sharpen the image by giving the kernal matrix, change it into grey scale and then implement ocr technique for text detection. 

![image](https://github.com/captainjack0003/OCR_Implementation/assets/75877962/46358e0f-1d13-4829-a2a4-8bdcb02b5187)


# Steps to use Google Cloud Vision API

To use the Google Cloud Vision API, you need to follow these steps:

1. Set up a Google Cloud Platform (GCP) project: 
   - Go to the Google Cloud Console (console.cloud.google.com).
   - Create a new project or select an existing one.

2. Enable the Cloud Vision API:
   - In the Cloud Console, navigate to the API Library.
   - Search for "Cloud Vision API" and click on it.
   - Click on the "Enable" button.

3. Create service account credentials:
   - In the Cloud Console, navigate to the IAM & Admin section.
   - Click on "Service Accounts" and then "Create Service Account".
   - Provide a name and description for the service account.
   - Under "Service account permissions," select the appropriate roles.
   - Click on "Create key" to generate a JSON key file.
   - Save the key file securely, as you will need it to authenticate your API requests.

4. Install the required client library:
   - The client library allows you to interact with the Cloud Vision API in your preferred programming language.
   - Visit the official Google Cloud client libraries documentation to find the library relevant to your programming language.
   - Install the library using the package manager or other installation method provided.

5. Write code to interact with the API:
   - Import the necessary libraries and dependencies.
   - Authenticate your API requests using the service account key file you obtained earlier.
   - Write code to send requests to the Cloud Vision API, specifying the desired features and the image you want to analyze.
   - Handle the API response to extract the desired information or perform further actions based on the analysis.

6. Run your code and analyze the results:
   - Execute your code, ensuring that it properly sends requests to the Cloud Vision API.
   - Review the response from the API, which will contain the results of the requested image analysis, such as labels, faces, text, or landmarks.
   - Process and utilize the obtained data according to your application's needs.


# Steps to use Microsoft Azure Vision API

To use Azure APIs, you can follow these general steps:

1. Create an Azure Account:
   - Go to the Azure portal (portal.azure.com).
   - Sign in or create a new Azure account.

2. Set up a subscription and resource group:
   - Create a subscription if you don't have one.
   - Create a resource group to organize your Azure resources.

3. Choose the Azure service/API you want to use:
   - Azure provides a wide range of APIs for various purposes, such as computer vision, natural language processing, machine learning, etc.
   - Identify the specific Azure service that provides the API you need. For example, Azure Cognitive Services for AI-related APIs.

4. Create an instance of the API service:
   - In the Azure portal, search for the specific service you identified in the previous step.
   - Follow the service-specific instructions to create an instance of the API service.
   - Configure the instance with the desired settings, such as location and pricing tier.

5. Obtain the API key or authentication credentials:
   - Most Azure APIs require authentication using an API key or other credentials.
   - In the Azure portal, navigate to the instance of the API service you created.
   - Look for the "Keys" or "Credentials" section to find the necessary API key or authentication information.

6. Write code to interact with the API:
   - Select your preferred programming language and environment.
   - Install any required client libraries or SDKs provided by Azure for the specific API service.
   - Use the provided libraries to authenticate your API requests using the API key or credentials.
   - Write code to send requests to the API, specifying the desired parameters and data.

7. Process the API response:
   - Handle the response from the API, which will contain the results of your request.
   - Extract the desired information or perform further actions based on the API response.

# how to use Tesseract API
https://github.com/tesseract-ocr/tessdoc



