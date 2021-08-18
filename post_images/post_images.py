import glob
import os
import cv2
import requests

result = {}
url = 'http://202.191.57.61:8081/'
path = "./images/original/"
resized_path = "./images/resized/"
scale_percents = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for img_path in glob.glob(os.path.join(path,"*.jpg")):
    # img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # print("Original shape: ", img.shape)
    for scale_percent in scale_percents:
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized_image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        new_path = os.path.join(resized_path, "{}_{}_{}.jpg".format(os.path.basename(img_path).split(".")[0], str(height), str(width)))
        cv2.imwrite(new_path, resized_image)
        img = cv2.imread(new_path, cv2.IMREAD_UNCHANGED)
        my_img = {'file': open(new_path, 'rb')}
        r = requests.post(url, files=my_img)
        # convert server response into JSON format.
        print(r.json())
