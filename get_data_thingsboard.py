import requests
import pandas as pd
from datetime import datetime

startTs = str(int(datetime.timestamp(datetime(2021, 7, 2, 0, 0, 0))*1000))
endTs = str(int(datetime.timestamp(datetime(2021, 7, 6, 23, 59, 0))*1000))

keys = ['PM1_0', 'PM2_5', 'PM10_0', 'SO2', 'NO2', 'CO', 'O3', 'perBat', 'celTemp', 'RH', 'cntErrWifi', 'cntErrLte', 'cntErrSD']

auth_token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiJjN2VjN2FhMC1jMGYwLTExZWItYjUzNi1mZjg0YzJjYWEyZDgiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiYzdiMTQ2NjAtYzBmMC0xMWViLWI1MzYtZmY4NGMyY2FhMmQ4IiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjI1NTU3MjM2LCJleHAiOjE2MjU1NjYyMzZ9.wZpM0KWu80fZ-uUpvH1oElyuXiPVkqJjD0ZVm63sZqfv7vw_AGPqOqyftHa8ekUL36Mc2ws7KdZlBN1xqxp7BQ'
headers = {'X-Authorization': 'Bearer ' + auth_token}
device_type = "DEVICE"
device_id = ['be02bca0-c110-11eb-a010-9b5d2dde0d98', 'cb7b8740-c110-11eb-a010-9b5d2dde0d98', 'd51ae840-c110-11eb-a010-9b5d2dde0d98',
             'ddfe2530-c110-11eb-a010-9b5d2dde0d98', 'ecd06550-c110-11eb-a010-9b5d2dde0d98', 'f47e5690-c110-11eb-a010-9b5d2dde0d98',
             'fab3b190-c110-11eb-a010-9b5d2dde0d98', 'ff5d1560-c110-11eb-a010-9b5d2dde0d98', '050b3f00-c111-11eb-a010-9b5d2dde0d98',
             '0dad7b50-c111-11eb-a010-9b5d2dde0d98', '12602df0-c111-11eb-a010-9b5d2dde0d98', '17d4d100-c111-11eb-a010-9b5d2dde0d98',
             '1e7067e0-c111-11eb-a010-9b5d2dde0d98', '22e7bf30-c111-11eb-a010-9b5d2dde0d98', '27ba2ed0-c111-11eb-a010-9b5d2dde0d98',
             '2c37a0a0-c111-11eb-a010-9b5d2dde0d98', '3040f3e0-c111-11eb-a010-9b5d2dde0d98', '351e11e0-c111-11eb-a010-9b5d2dde0d98',
             '39a23a70-c111-11eb-a010-9b5d2dde0d98', '44aceb40-c111-11eb-a010-9b5d2dde0d98', '49366b00-c111-11eb-a010-9b5d2dde0d98',
             '4d3759d0-c111-11eb-a010-9b5d2dde0d98', '54cc92f0-c111-11eb-a010-9b5d2dde0d98', '5cf83fb0-c111-11eb-a010-9b5d2dde0d98',
             '610d04a0-c111-11eb-a010-9b5d2dde0d98', '65228ce0-c111-11eb-a010-9b5d2dde0d98', '69d0aba0-c111-11eb-a010-9b5d2dde0d98',
             '72fc8a50-c111-11eb-a010-9b5d2dde0d98', '6ef6e090-c111-11eb-a010-9b5d2dde0d98', '78b38d90-c111-11eb-a010-9b5d2dde0d98',
             'a9851920-cb70-11eb-b507-8dc7c3e26413']
device_name = ['fimi_01', 'fimi_02', 'fimi_03', 'fimi_04', 'fimi_05', 'fimi_06', 'fimi_07', 'fimi_08', 'fimi_09', 'fimi_10',
               'fimi_11', 'fimi_12', 'fimi_13', 'fimi_14', 'fimi_15', 'fimi_16', 'fimi_17', 'fimi_18', 'fimi_19', 'fimi_20',
               'fimi_21', 'fimi_22', 'fimi_23', 'fimi_24', 'fimi_25', 'fimi_26', 'fimi_27', 'fimi_28', 'fimi_29', 'fimi_30',
               'fimi_31']
device_id = ['610d04a0-c111-11eb-a010-9b5d2dde0d98', '65228ce0-c111-11eb-a010-9b5d2dde0d98', '69d0aba0-c111-11eb-a010-9b5d2dde0d98',
             '72fc8a50-c111-11eb-a010-9b5d2dde0d98', '6ef6e090-c111-11eb-a010-9b5d2dde0d98', '78b38d90-c111-11eb-a010-9b5d2dde0d98',
             'a9851920-cb70-11eb-b507-8dc7c3e26413']
device_name = ['fimi_25', 'fimi_26', 'fimi_27', 'fimi_28', 'fimi_29', 'fimi_30', 'fimi_31']
# device_id = ['610d04a0-c111-11eb-a010-9b5d2dde0d98']
# device_name = ['fimi_25']

writer = pd.ExcelWriter(r".\result.xlsx")

for ind, device in enumerate(device_name):
    print(ind, device)

    url = 'http://202.191.57.62:8081/api/plugins/telemetry/{}/{}/values/timeseries'.format(device_type, device_id[ind])
    df = pd.DataFrame()
    notDate = True

    for key in keys:
        params = {'limit': 100000,
                  'agg': 'NONE',
                  'orderBy': 'DESC',
                  'startTs': startTs,
                  'endTs': endTs,
                  'keys': key}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        if len(data) != 0:
            data_key = []
            # create column datetime
            if notDate:
                notDate = False
                date = []
                for i in range(len(data[key])):
                    ticks = data[key][i]['ts']
                    date.append(datetime.fromtimestamp(float(ticks) / 1000))
                df['datetime'] = date
            
            for i in range(len(data[key])):
                data_key.append(data[key][i]['value'])
            try:
                df[key] = data_key
            except:
                print(device, key, len(data_key))
                print("Bi thieu mot so row")
                print('-----------------------------')
    df.sort_values(by='datetime', inplace=True)
    # df.to_excel(writer, sheet_name=device, index=False)
    df.to_csv("{}.csv".format(device), index=False)
writer.save()