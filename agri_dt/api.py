import pandas as pd
import numpy as np
import random, os

def seed_everything(seed: int):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    
seed_everything(42)

def simulate():
    num_house = 5
    num_lane_per_house = 10
    num_plant_per_lane = 30
    max_plant = num_house * num_lane_per_house * num_plant_per_lane
    possible_max_plant = max_plant
    total_days = 75
    ini_date = "2022-02-12"
    ini_temp = 20
    ini_humid = 85
    if ini_temp > 26 and ini_humid < 80:
        has_bug = True
        print("Đây là điều kiện tốt để bọ phấn trắng phát triển!")
        possible_max_plant = int(max_plant * 0.95)
    ini_light = 400
    predictions = predict_whole_process(possible_max_plant, total_days, ini_date, ini_temp, ini_humid, ini_light)
    print(pd.DataFrame(predictions))
    return max_plant, possible_max_plant, predictions

def predict_whole_process(possible_max_plants, total_days, ini_date, ini_temp, ini_humid, ini_light):
    scale = possible_max_plants / 1000
    ini_ure = 0.43*scale
    ini_super_lan = 1.25*scale
    ini_k2so4 = 0.3*scale
    ini_eco = 0.5*scale
    ini_water = 1000*scale
    # details = {"temp": ini_temp, "humid": ini_humid, "light": ini_light, "ure": ini_ure, "super_lan": ini_super_lan, "K2SO4": ini_k2so4, "ECO": ini_eco, "water": ini_water, "max_plant": possible_max_plants}
    predictions = {str((pd.to_datetime(ini_date) + pd.DateOffset(days=i+1)).date()): {} for i in range(total_days)}
    dates = list(predictions.keys())
    for i, k in enumerate(predictions):
        details = {}
        if i == 0:
            details["temp"] = ini_temp * (1 - random.uniform(-0.09, 0.09))
            details["humid"] = ini_humid * (1 - random.uniform(-0.09, 0.09))
            details["light"] = ini_light * (1 - random.uniform(-0.09, 0.09))
            details["ure"] = ini_ure * (1 - random.uniform(-0.09, 0.09))
            details["super_lan"] = ini_super_lan * (1 - random.uniform(-0.09, 0.09))
            details["K2SO4"] = ini_k2so4 * (1 - random.uniform(-0.09, 0.09))
            details["ECO"] = ini_eco * (1 - random.uniform(-0.09, 0.09))
            details["water"] = ini_water * (1 - random.uniform(-0.09, 0.09))
            details["max_plant"] = possible_max_plants
            predictions[k] = details
        else:
            details["temp"] = predictions[dates[i-1]]["temp"] * (1 - random.uniform(-0.09, 0.09))
            details["humid"] = predictions[dates[i-1]]["humid"] * (1 - random.uniform(-0.09, 0.09))
            details["light"] = predictions[dates[i-1]]["light"] * (1 - random.uniform(-0.09, 0.09))
            details["ure"] = predictions[dates[i-1]]["ure"] * (1 - random.uniform(-0.09, 0.09))
            details["super_lan"] = predictions[dates[i-1]]["super_lan"] * (1 - random.uniform(-0.09, 0.09))
            details["K2SO4"] = predictions[dates[i-1]]["K2SO4"] * (1 - random.uniform(-0.09, 0.09))
            details["ECO"] = predictions[dates[i-1]]["ECO"] * (1 - random.uniform(-0.09, 0.09))
            details["water"] = predictions[dates[i-1]]["water"] * (1 - random.uniform(-0.09, 0.09))
            details["max_plant"] = predictions[dates[i-1]]["max_plant"] * (1 - random.uniform(-0.09, 0.09))
            while details["max_plant"] > possible_max_plants:
                details["max_plant"] = predictions[dates[i-1]]["max_plant"] * (1 - random.uniform(-0.09, 0.09))
            predictions[k] = details
    return predictions 

def change(predictions, date, parameter, value):
    dates = list(predictions.keys())
    for i, k in enumerate(predictions):
        if k > date:
            details = {}
            details["temp"] = predictions[dates[i-1]]["temp"] * (1 - random.uniform(-0.09, 0.09))
            details["humid"] = predictions[dates[i-1]]["humid"] * (1 - random.uniform(-0.09, 0.09))
            details["light"] = predictions[dates[i-1]]["light"] * (1 - random.uniform(-0.09, 0.09))
            details["ure"] = predictions[dates[i-1]]["ure"] * (1 - random.uniform(-0.09, 0.09))
            details["super_lan"] = predictions[dates[i-1]]["super_lan"] * (1 - random.uniform(-0.09, 0.09))
            details["K2SO4"] = predictions[dates[i-1]]["K2SO4"] * (1 - random.uniform(-0.09, 0.09))
            details["ECO"] = predictions[dates[i-1]]["ECO"] * (1 - random.uniform(-0.09, 0.09))
            details["water"] = predictions[dates[i-1]]["water"] * (1 - random.uniform(-0.09, 0.09))
            details["max_plant"] = predictions[dates[i-1]]["max_plant"] * (1 - random.uniform(-0.09, 0.09))
            details[parameter] = value
            while details["max_plant"] > predictions[dates[0]]["max_plant"]:
                details["max_plant"] = predictions[dates[i-1]]["max_plant"] * (1 - random.uniform(-0.09, 0.09))
            predictions[k] = details
    return predictions 


simulate()