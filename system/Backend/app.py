'''
Description: 
Author: Qing Shi
Date: 2022-11-20 19:14:42
LastEditTime: 2023-08-27 21:26:46
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import re

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

@app.route('/api/test/fetchBasicChart_fake/', methods=['POST'])
def fetch_basic_chart():
    params = request.json
    print(params)
    file_path = '{}/data/chart.json'.format(FILE_ABS_PATH)
    data = read_json(file_path)
    print(data);
    return jsonify(data)



# 判断x轴属于什么类型，{time, category,linear}
def determine_x_axis_type(input_data):
    x_values = next(iter(input_data[0].values()))
    # print(x_values)
    if list(input_data[0].keys())[0] == 'time' or list(input_data[0].keys())[0] == 'Time':
        return 'time'
    # 检查是否包含数字和日期
    if re.match(r'\d{4}/(?:0?[1-9]|1[0-2])/(?:0?[1-9]|[12]\d|3[01])', x_values): 
        return 'time'
    elif re.match(r'^[-+]?\d*\.?\d+$', x_values): # 正则表达式匹配整数/浮点数
        return 'linear'
    else:
        return 'category'
    

# 返回x轴名称
def get_x_axis_name(x_type, data):
    x_name = ""
    x_attribute = list(data[0].keys())[0]
    if x_type == 'time':
        x_name = 'Time'
    elif x_type == 'category':
        x_name = 'Category'
    elif x_type == 'linear':
        x_name =  list(data[0].keys())[0]
    else:
        x_name = ' '
    return [x_name, x_attribute]

"""
这个函数将根据给定的数据判断最合适的图表类型，并将图表类型返回给前端
chart type:
0: single bar   1: single line  2:multiple bar  3:multiple line
柱状图通常用来展示不同类别/离散数据 折线图更利于展示连续数据的趋势和变化
"""
def determine_chart_type(input_data, x_type):
    # 统计数据中键的数量
    num_keys = len(input_data[0])
    
    # 如果多个y值，选择multi,是time/linear选择line
    if num_keys > 2:
        chart_type = 2
    else: 
        chart_type = 0
    
    if x_type == 'time' or x_type == 'linear':
        chart_type += 1
    
    return chart_type
#TODO: backend function 1
# @app.route('/chart-info', methods=['POST'])
@app.route('/api/test/fetchBasicChart/', methods=['POST'])
def chart_info():
    params = request.json
    print(params)
    data = params["data"]
    #data = request.get_json()   # 从前端获取数据
    num_keys = len(data[0]) - 1 # 统计键数量，对应y的数量
    
    x_type = determine_x_axis_type(data)
    [x_name, x_attribute] = get_x_axis_name(x_type,data)
    y_attribute = list(data[0].keys())[1:]
    chart_type = determine_chart_type(data, x_type)
    
    # 返回结果：
    result = {
        # "chartType": chart_type,
        "chartType": chart_type,
        "chartScale":{
            "x": {
                "scaleType": x_type,
                "scaleName": x_name,
                "attributeName": x_attribute
            },
            "y": {
                "scaleType": 'linear',
                "scaleName": ' ', # 给一个列名
                "attributeName": y_attribute
            }
        }
    }
    result['chartColor'] = {}
    color_hunt = [{
            "r": 135,
            "g": 206,
            "b": 235,
            "a": 1
        }, {
            "r": 251,
            "g": 240,
            "b": 178,
            "a": 1
        },{
            "r": 255,
            "g": 199,
            "b": 234,
            "a": 1
        },{
            "r": 216,
            "g": 180,
            "b": 248,
            "a": 1
        },{
            "r": 121,
            "g": 21,
            "b": 91,
            "a": 1
        },{
            "r": 246,
            "g": 99,
            "b": 92,
            "a": 1
        },{
            "r": 168,
            "g": 223,
            "b": 142,
            "a": 1
        }]
    cnt = 0
    for y in y_attribute:
        result['chartColor'][y] = color_hunt[cnt]
        cnt += 1
    print(result)
    return result

@app.route('/api/test/postQuery/', methods=['POST'])
def post_query():
    params = request.json
    file_path = '{}/data/description.json'.format(FILE_ABS_PATH)
    data = read_json(file_path)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)