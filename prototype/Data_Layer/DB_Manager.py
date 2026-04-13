import json

class DB_Manager:
    def __init__(self):
        self.file_data = 0

    def load(self):
        with open('assets/DB.json', 'r') as file:
            self.file_data = json.load(file)

    def flush(self):
        pass

    def log(self):
        print("Database Data: ", self.file_data)
