import os
import json
import random

class TestDataManager:
    def __init__(self):
        self.__folder_path = "TEST_DATA"

    def load_json_file(self, file_name):
        file_path = f"{self.__folder_path}/{file_name}"
        with open(file_path) as f:
            data = json.load(f)
        return data

    def get_location_data(self, file_name, count=1):
        data = self.load_json_file(file_name)
        locations = data["locations"]
        return random.sample(locations, count)
    
    def get_test_cases_parametrization(self,file_name):
        pass



    def get_user_data(self, file_name):
        data = self.load_json_file(file_name)
        user = random.choice(data["users"])
        return {"username": user["username"], "password": user["password"]}
