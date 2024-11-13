import re
import boto3
from botocore.exceptions import ClientError
import json

# Import the hints module from the utils package
from utils import hints

bedrock_client = boto3.client(service_name='bedrock-runtime', region_name=region)
def get_completion(prompt, system_prompt=None):
    # Define the inference configuration
    inference_config = {
        "temperature": 0.0,  # Set the temperature for generating diverse responses
        "maxTokens": 200,  # Set the maximum number of tokens to generate
        "topP": 1,  # Set the top_p value for nucleus sampling
    }
    # Create the converse method parameters
    converse_api_params = {
        "modelId": modelId,  # Specify the model ID to use
        "messages": [{"role": "user", "content": [{"text": prompt}]}],  # Provide the user's prompt
        "inferenceConfig": inference_config,  # Pass the inference configuration
    }
    # Check if system_text is provided
    if system_prompt:
        # If system_text is provided, add the system parameter to the converse_params dictionary
        converse_api_params["system"] = [{"text": system_prompt}]

    # Send a request to the Bedrock client to generate a response
    try:
        response = bedrock_client.converse(**converse_api_params)

        # Extract the generated text content from the response
        text_content = response['output']['message']['content'][0]['text']

        # Return the generated text content
        return text_content

    except ClientError as err:
        message = err.response['Error']['Message']
        print(f"A client error occured: {message}")