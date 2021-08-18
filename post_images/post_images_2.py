import glob
import os
import cv2
import requests

result = {}
result["diagnosis"] = "Mào vách ngăn mũi trái- Viêm họng, Amydan mạn tính"
url = 'http://202.191.57.61:8081/'
path = "./images/original/"
resized_path = "./images/resized/"
scale_percents = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
scale_percents = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for img_path in glob.glob(os.path.join(path,"*.jpg")):
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    print("Original shape: ", img.shape)
    my_img = {'file': open(img_path, 'rb')}
    r = requests.post(url, files=my_img)
    # convert server response into JSON format.
    print(r.json())
