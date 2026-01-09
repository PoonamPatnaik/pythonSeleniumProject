import json
import os

def get_test_data():
    file_path = os.path.join(os.path.dirname(__file__), "../data/test_data.json")
    with open(file_path) as file:
        return json.load(file)
