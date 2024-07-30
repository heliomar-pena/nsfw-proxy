import os
import random

script_dir = os.path.dirname(__file__)
images_dir = "images"

abs_image_path = os.path.join(script_dir, images_dir);

images = []

for root, dirs, files in os.walk(abs_image_path, topdown=False):
   for name in files:
        image = open(os.path.join(root, name), mode='rb').read()
        images.append(image)

def getRandomImage():
    return random.choice(images)
