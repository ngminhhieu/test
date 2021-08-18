import json
import requests
import os
import pandas as pd
import numpy as np

def analyze(drugs_list):
    count = 0
    drug_names = pd.read_csv('./new_drugs.csv').to_numpy()
    drug_names = np.squeeze(drug_names)
    name = []
    count_labeled = []
    for i, (k,v) in enumerate(drugs_list.items()):
        name.append(k)
        count_labeled.append(v)
        if k not in drug_names:
            count += 1
    print(count)
    drugs_list_labeled = pd.DataFrame(list(zip(name, count_labeled)), columns=['name', 'count_labeled'])
    drugs_list_labeled.to_csv("drugs_list_labeled.csv", index=False)


response = requests.get('http://localhost:1999/api/drug/annotation')
response_dict = json.loads(response.text)
# Sua lai label truoc o day
ids = []
count = 0
drugs_list = {}
img_paths = []
for i in range(len(response_dict['matches'])):
    img_path = response_dict['matches'][i]['img_path']
    description = response_dict['matches'][i]['description']
    if (type(description)==str):
        des = json.loads(description)
        if (len(des)!=0):
            # Khong thuoc nao bi gan thieu va khong duoc label boi a_ va phai gan co dau' gach ngang
            if(all(label['label'] != "" and label['label'][:2] != "a_" for label in des)):
                # Khong duoc gan voi label tu nghi ra. Khong tim thay - va _. V chi can 1 label co chua dau' cach de tranh truong ten don thi khong can _ va -
                if not(all(label['label'].find("-") == -1 and label['label'].find("_") == -1 and any(label['label'].find(" ") != -1 for label in des) for label in des)):
                    count += 1
                    output_json = {}
                    output_json['path'] = img_path
                    output_json['boxes'] = []
                    for box_index in range(len(des)):
                        tmp_dict = {}
                        tmp_dict['x'] = des[box_index]['x']
                        tmp_dict['y'] = des[box_index]['y']
                        tmp_dict['h'] = des[box_index]['h']
                        tmp_dict['w'] = des[box_index]['w']
                        tmp_dict['label'] = des[box_index]['label']
                        output_json['boxes'].append(tmp_dict.copy())
                        if tmp_dict['label'] in drugs_list:
                            drugs_list[tmp_dict['label']] += 1
                        else:
                            drugs_list[tmp_dict['label']] = 1
                        if os.path.exists('../emed-web/main/static/uploaded/{}'.format(img_path)):
                            os.system('cp ../emed-web/main/static/uploaded/{} ./data_uong_thuoc/pics/'.format(img_path))
                            with open('./data_uong_thuoc/json/{}.json'.format(img_path.replace('.jpg','')), 'w') as f:
                                json.dump(output_json, f)
                else:
                    img_paths.append(img_path)

print("Total images: ", count)
analyze(drugs_list)
print(img_paths)

