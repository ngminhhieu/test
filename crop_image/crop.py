import glob
import cv2
import json
import os

# label = [{"x_min": 493.0, "y_min": 1274.0, "x_max": 894.0, "y_max": 1880.0, "conf": 0.7600865, "id": 186.0, "pillname": "others"}, {"x_min": 1010.0, "y_min": 1080.0, "x_max": 1353.0, "y_max": 1681.0, "conf": 0.57419825, "id": 132.0, "pillname": "Moxifloxacin (Bluemoxi 400mg)"}]
label =   [{'x_min': 1065.0, 'y_min': 1752.0, 'x_max': 1408.0, 'y_max': 2414.0, 'conf': 0.58956885, 'id': 10.0, 'pillname': 'Scanax'}, {'x_min': 431.0, 'y_min': 259.0, 'x_max': 627.0, 'y_max': 454.0, 'conf': 0.5879324, 'id': 2.0, 'pillname': 'Scanax'}, {'x_min': 774.0, 'y_min': 2105.0, 'x_max': 1173.0, 'y_max': 2634.0, 'conf': 0.52717644, 'id': 7.0, 'pillname': 'Scanax'}, {'x_min': 796.0, 'y_min': 2099.0, 'x_max': 1176.0, 'y_max': 2619.0, 'conf': 0.3593718, 'id': 10.0, 'pillname': 'Scanax'}]
path_img = "CAP_F825B237-665B-4C70-BA1E-3A6D98A8439A.jpg"
boxes = label
img = cv2.imread(path_img)
print(img.shape)
for box in boxes:
    x = int(box["x_min"])
    y = int(box["y_min"])
    w = int(box["x_max"] - box["x_min"])
    h = int(box["y_max"] - box["y_min"])
    name = box["pillname"]
    print(img[y:y+h, x:x+w])
    print(y)
    print(y+h)
    crop_img = img[y:y+h, x:x+w].copy()
    print(crop_img)
    if os.path.exists("{}.jpg".format(name)):
        name = name + "2"
    cv2.imwrite("{}.jpg".format(name), crop_img)
