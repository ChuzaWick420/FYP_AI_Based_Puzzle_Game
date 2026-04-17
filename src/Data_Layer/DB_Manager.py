import json

class DB_Manager:
    def __init__(self):
        self.file_data = {}

    def load(self):
        with open('assets/DB.json', 'r') as file:
            self.file_data = json.load(file)

    def flush(self):
        with open('assets/DB.json', 'w') as file:
            json.dump(self.file_data, file)

    def log(self):
        print("Database Data: ", self.file_data)

    def debug(self):
        # print("Length of grid: ", len(self.file_data["current_map"]))
        pass
