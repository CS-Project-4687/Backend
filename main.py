from llm import createTT
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import json
import os
from datetime import datetime
import time

if not os.path.exists('timetable.json'):
    with open('timetable.json', 'w') as file:
        json.dump([], file)

@app.route('/generate', methods=['POST'])
def process():
    data = request.json
    prompt = data.get('prompt')
    if prompt:
        result = createTT(prompt)
        return jsonify({'result': result})
    return jsonify({'error': 'No prompt provided'}), 400

@app.route('/save' , methods=['POST'])
def save():
    data = request.json
    tt = data["timetable"]
    item = { "date": f"Time Table {datetime.now().isoformat().split("T")[0]}_{str(time.time()).split(".")[0]}", "timetable": tt }
    try:
        with open('timetable.json', 'r+') as file:
            timetables = json.load(file)
            timetables.append(item)
            file.seek(0)
            json.dump(timetables, file, indent=4)
        return jsonify({'message': 'Timetable saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get', methods=['GET'])
def getTT():
    try:
        with open('timetable.json', 'r') as file:
            timetables = json.load(file)
        return jsonify(timetables), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()