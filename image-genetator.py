import openai
import os

openai.api_key = os.environ['API_KEY']


# Image Creation
def create_image(prompt_input):
    response = openai.Image.create(prompt=prompt_input], n=1,size="512x512") 
    # Sizes should be in ['256x256', '512x512', '1024x1024']  
    image_url = response['data'][0]['url']
    return image_url

# Image Variation
def create_image_with_variation(image_name):
    response = openai.Image.create_variation(
    image=open("image_name", "rb"),
    n=1,
    size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url


