from flask import Flask, jsonify
from utils import process_data

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Untilhow backend running", "token": "$UNTIL"})

@app.route('/process/<string:data>', methods=['GET'])
def process(data):
    result = process_data(data)
    return jsonify({"input": data, "processed": result})

if __name__ == '__main__':
    app.run(debug=True)
