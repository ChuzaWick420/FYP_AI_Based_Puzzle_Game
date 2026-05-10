import json
import sqlite3

class DB_Manager:
    def __init__(self):
        self.__json_data = {}
        self.__db_data = []

    def load(self):
        with open('assets/other_data.json', 'r') as file:
            self.__json_data = json.load(file)

        db = sqlite3.connect("assets/data.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM COMPLETION_TIMES")
        results = cursor.fetchall()

        self.__db_data = results

        cursor.close()
        db.close()

    def flush(self):
        with open('assets/other_data.json', 'w') as file:
            json.dump(self.__json_data, file)

        db = sqlite3.connect("assets/data.db")
        cursor = db.cursor()

        for entry in self.__db_data:
            query = "UPDATE COMPLETION_TIMES SET time_data = ? WHERE position = ?;"
            cursor.execute(query, (entry[1], entry[0]))

        db.commit()

        cursor.close()
        db.close()

    def getJSONData(self):
        return self.__json_data

    def setJSONData(self, data):
        self.__json_data = data

    def getDBData(self):
        return self.__db_data

    def setDBData(self, data):
        self.__db_data = data
