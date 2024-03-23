import os
import json
import random
from datetime import datetime,timedelta


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

    def get_payment_detail(self,file_name,count=1):
        data=self.load_json_file(file_name)
        payments=data["payment_detail"]
        return random.sample(payments,count)
    
    def get_test_cases_from_file(self,file_name):
        test_cases_file=self.load_json_file(file_name)
        test_cases=test_cases_file["test_cases"]
        return test_cases

    def save_json_file(self, data, file_name):
        file_path = os.path.join(self.__folder_path, file_name)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_user_data(self, file_name):
        data = self.load_json_file(file_name)
        user = random.choice(data["users"])
        return {"username": user["username"], "password": user["password"]}

    def prepare_all_test_data(self):
        user_data = self.get_user_data("customer_data.json")
        location_data = self.get_location_data("location.json", 2)
        test_cases = self.get_test_cases_from_file("test_cases.json")

      
        all_data = {
            "username": user_data["username"],
            "password":user_data["password"],
            "pick_up_location": location_data[0],
            "drop_off_location": location_data[1],
            "test_cases": test_cases
        }

        return all_data





