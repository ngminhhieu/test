import glob
import os
import cv2
import requests
from PIL import Image

result = {}
url = 'http://202.191.57.61:8081/'
path = "./images/original/"
resized_path = "./images/resized/"
scale_percents = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for img_path in glob.glob(os.path.join(path,"*.jpg")):
    img = Image.open(img_path)
    print("Original shape: ", img.size)
    for scale_percent in scale_percents:
        width = int(img.size[0] * scale_percent / 100)
        height = int(img.size[1] * scale_percent / 100)
        resized_image = img.resize((width, height), Image.NEAREST)
        new_path = os.path.join(resized_path, "{}_{}_{}.jpg".format(os.path.basename(img_path).split(".")[0], str(height), str(width)))
        resized_image.save(new_path)
        my_img = {'file': open(new_path, 'rb')}
        r = requests.post(url, files=my_img)
        # convert server response into JSON format.
        print(r.json())
