from llm import createTT
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def process():
    data = request.json
    prompt = data.get('prompt')
    if prompt:
        result = createTT(prompt)
        return jsonify({'result': result})
    return jsonify({'error': 'No prompt provided'}), 400

if __name__ == '__main__':
    app.run()