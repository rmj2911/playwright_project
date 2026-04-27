# framework/utils/helpers.py
import json  
import os  
  
def load_planet_name(key):  
    path = "../data/test_data_planet_name.json"  
    # Build full path to the JSON file  
    json_path = os.path.join(os.path.dirname(__file__), path)  
  
    # Open the JSON file  
    with open(json_path, 'r') as file:  
        data = json.load(file)  
  
    # Access JSON value and immediately return it  
    return data[key]