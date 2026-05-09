import json
import sqlite3

class DB_Manager:
    def __init__(self):
        self.file_data = {}
        self.db_data = []

    def load(self):
        with open('assets/other_data.json', 'r') as file:
            self.file_data = json.load(file)

        db = sqlite3.connect("assets/data.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM COMPLETION_TIMES")
        results = cursor.fetchall()

        self.db_data = results

        cursor.close()
        db.close()

    def flush(self):
        with open('assets/other_data.json', 'w') as file:
            json.dump(self.file_data, file)

        db = sqlite3.connect("assets/data.db")
        cursor = db.cursor()

        for entry in self.db_data:
            query = "UPDATE COMPLETION_TIMES SET time_data = ? WHERE position = ?;"
            cursor.execute(query, (entry[1], entry[0]))

        db.commit()

        cursor.close()
        db.close()

    def log(self):
        print("Database Data: ", self.file_data)

    def getDBData(self):
        return self.db_data

    def setDBData(self, data):
        self.db_data = data

    def debug(self):
        # data = [
        #     (1, '00:00:00'),
        #     (2, '00:10:00'),
        #     (3, '00:00:00'),
        #     (4, '00:00:00'),
        #     (5, '00:00:00'),
        # ]
        #
        # self.db_data = data

        # NOTE: debug
        # print(self.db_data)

        # NOTE: Testing
        data = [
            '08:00:00',
            '09:30:00',
            '18:20:00',
            '11:15:00',
            '14:45:00'
        ]

        data.sort()

        print(data)

        pass
