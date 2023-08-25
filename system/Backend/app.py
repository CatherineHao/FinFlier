'''
Description: 
Author: Qing Shi
Date: 2022-11-20 19:14:42
LastEditTime: 2023-07-14 12:48:04
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

FILE_ABS_PATH = os.path.dirname(__file__)

app = Flask(__name__)
CORS(app)

def read_json(add):
    with open(add, 'rt', encoding="utf-8") as f:
        cr = json.load(f)
    f.close()
    return cr

@app.route('/api/test/hello/', methods=['POST'])
def hello_resp():
    params = request.json
    # msg = int(params['msg'])
    # print(msg)
    return "hello VUE"

@app.route('/api/test/fetchBasicChart/', methods=['POST'])
def fetch_basic_chart():
    params = request.json
    # print(params)
    file_path = '{}/data/chart.json'.format(FILE_ABS_PATH)
    data = read_json(file_path)
    print(data);
    return jsonify(data)

@app.route('/api/test/postQuery/', methods=['POST'])
def post_query():
    params = request.json
    file_path = '{}/data/description.json'.format(FILE_ABS_PATH)
    data = read_json(file_path)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)