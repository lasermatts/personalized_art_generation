# imports for using OpenAI
import openai  # OpenAI Python library to make API calls
import requests  # used to download images
import os  # used to access filepaths
from PIL import Image  # used to print and edit images
# imports for the homebrew
import pandas as pd # happiness is a warm CSV

# we've got to mess at the OS level to play with API keys
openai.api_key = os.environ.get("OPENAI_API_KEY")


# now let's get a directory going so we can get things rolling
image_dir_name = "images"
image_dir = os.path.join(os.curdir, image_dir_name) 
# we'll just squirt our images here for now

# creating a directory if it doesn't exist already
if not os.path.isdir(image_dir)
    os.mkdir(image_dir)

# and for good measure let's print out where things are going
print(f"{image_dir=}")

# TODO add option to move an image from this directory to our selected favorites to show for the world

# OK NOW things are getting interesting. Probably don't want to call in the other function but let's see.


