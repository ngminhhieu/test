import mysql.connector
import sshtunnel
import pandas as pd
import numpy as np
import json
import os


def query():
    try:
        connection = mysql.connector.connect(
            user='root',
            password='AIOTlab2021',
            host='127.0.0.1',
            database='emed',
            port='3306')
        count = 0
        list_drugs = []
        drugs_name_labeled = {}
        cursor = connection.cursor()
        for i in range(1,40):
            mysql_query = """SELECT description, img_path from annotation where set_id={}""".format(str(i))
            cursor.execute(mysql_query)
            results = cursor.fetchall()
            tmp_list_drugs = {}
            if len(results) > 0:
                print("Set {} has {} images".format(str(i), str(len(results))))
                for x in results:
                    count += 1
                    img_path = x[1]
                    des = x[0]
                    if des != None:
                        des = list(eval(des))
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
                            if tmp_dict['label'] in tmp_list_drugs:
                                drugs_name_labeled[tmp_dict['label']] += 1
                                tmp_list_drugs[tmp_dict['label']] += 1
                            else:
                                drugs_name_labeled[tmp_dict['label']] = 1
                                tmp_list_drugs[tmp_dict['label']] = 1
                        if os.path.exists('../emed-web/main/static/uploaded/{}'.format(img_path)):
                            os.system('cp ../emed-web/main/static/uploaded/{} ./transfer_learning_data/pics/'.format(img_path))
                            with open('./transfer_learning_data/json/{}.json'.format(img_path.replace('.jpg','')), 'w') as f:
                                json.dump(output_json, f)
                # print("Successfully query")
            list_drugs.append(tmp_list_drugs.copy())
        # print("Total images: ", count)
        # print(list_drugs)
        # max_key = max(drugs_name_labeled, key=drugs_name_labeled.get)
        # print(max_key)
        print(count)
        # analyze(list_drugs)
    except mysql.connector.Error as error:
        print("Failed to insert into table Pill {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def analyze(list_drugs):
    drug_names = pd.read_csv('./new_drugs.csv').to_numpy()
    drug_names = np.squeeze(drug_names)
    print(drug_names)
    for i in range(len(list_drugs)):
        for item_labeled in list_drugs[i]:
            if item_labeled not in drug_names:
                print("Set {} has invalid drug name: {}".format(str(i), str(item_labeled)))
        
query()