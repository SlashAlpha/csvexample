from flask import Flask
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
import csv

with open("import.csv") as file:
    app = Flask(__name__)

# pip install flask-mongoengine

app.config['MONGODB_SETTINGS'] = {
    'db': 'my_Database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class Column(db.Document):
    number = db.StringField()
    data = db.StringField()

    def toJson(self):
        return {"number": self.number,
                "data": self.data}


def data_receiver():
    csv_reader = csv.reader(file, delimiter=',')
    count = 0
    width = 0
    y = 1
    i = 0
    listdata = list
    while i <= y:
        data = list
        for line in csv_reader:
            if i == 0:
                y = line.count()
            if line[i]:
                data.append(line[i])
        listdata.append(data)
        i += 1
    return listdata





@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
