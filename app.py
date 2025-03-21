from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Name is required!"}), 400
    return jsonify({"message": f"Hello, {data['name']}!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
