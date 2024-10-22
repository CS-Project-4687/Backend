from llm import createTT
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import json
import os

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
    tt = data.timetable
    try:
        with open('timetable.json', 'r+') as file:
            timetables = json.load(file)
            timetables.append(tt)
            file.seek(0)
            json.dump(timetables, file, indent=4)
        return jsonify({'message': 'Timetable saved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()