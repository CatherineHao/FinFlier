'''
Author: CatherineHao 1512769550@qq.com
Date: 2023-07-12 21:37:31
LastEditors: CatherineHao 1512769550@qq.com
LastEditTime: 2023-07-26 20:49:44
'''
import json
import os
import re

import openai
from flask import Flask, redirect, render_template, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['ENV'] = "development"
openai.api_key = "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"

# os.environ["http_proxy"] = "127.0.0.1:7890"
# os.environ["https_proxy"] = "127.0.0.1:7890"
# print("开始了")

# 测试数据，单y, 多y，time单y, linear单y
data1= [{'Position':'United Kingdom','Billions of dollars':'60'},{'Position':'Netherlands','Billions of dollars':'42'},
       {'Position':'France','Billions of dollars':'35'},{'Position':'Canada','Billions of dollars': '30'},
       {'Position':'Japan','Billions of dollars':'29'}]

data2 = [{'Category':'Real GDP','Outdoor recreation':'18.9','U.S. economy':'5.9'},
	{'Category':'Real Gross Output','Outdoor recreation':'21.8','U.S. economy':'6.3'},
	{'Category':'Compensation','Outdoor recreation':'16.2','U.S. economy':'7.8'},
	{'Category':'Compensation','Outdoor recreation':'13.1','U.S. economy':'2.7'}]

data3 = [{'Time':'2017/1/1','Mini- and subcompact size':'0.61','Compact size':'0.35', 'Midsize to large':'0.04'},
	{'Time':'2018/1/1','Mini- and subcompact size':'0.49','Compact size':'0.41', 'Midsize to large':'0.10'},
	{'Time':'2019/1/1','Mini- and subcompact size':'0.33','Compact size':'0.54', 'Midsize to large':'0.13'},
	{'Time':'2020/1/1','Mini- and subcompact size':'0.35','Compact size':'0.33', 'Midsize to large':'0.32'},
	{'Time':'2021/1/1','Mini- and subcompact size':'0.37','Compact size':'0.28', 'Midsize to large':'0.35'},
	{'Time':'2022/1/1','Mini- and subcompact size':'0.37','Compact size':'0.31', 'Midsize to large':'0.32'},
	{'Time':'2023/1/1','Mini- and subcompact size':'0.30','Compact size':'0.30', 'Midsize to large':'0.40'}]

# 判断x轴属于什么类型，{time, category,linear}
def determine_x_axis_type(input_data):
    x_values = next(iter(input_data[0].values()))
    # print(x_values)
    # 检查是否包含数字和日期
    if re.match(r'\d{4}/(?:0?[1-9]|1[0-2])/(?:0?[1-9]|[12]\d|3[01])', x_values): 
        return 'time'
    elif re.match(r'^[-+]?\d*\.?\d+$', x_values): # 正则表达式匹配整数/浮点数
        return 'linear'
    else:
        return 'category'

# 返回x轴名称
def get_x_axis_name(x_type, data):
    if x_type == 'time':
        return 'Time'
    elif x_type == 'category':
        return 'Category'
    elif x_type == 'linear':
        return list(data[0].keys())[0]
    else:
        return ''
    
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
        
@app.route('/chart-info', methods=['POST'])
def chart_info(data):
    #data = request.get_json()   # 从前端获取数据
    num_keys = len(data[0]) - 1 # 统计键数量，对应y的数量
    
    x_type = determine_x_axis_type(data)
    x_name = get_x_axis_name(x_type,data)
    chart_type = determine_chart_type(data, x_type)
    
    # 返回结果：
    result = {
        "chartType": chart_type,
        "chartScale":{
            "x": {
                "scaleType": x_type,
                "scaleName": x_name
            },
            "y": {
                "scaleType": 'linear',
                "scaleName": ' '
            }
        }
    }
    return result
    
print(chart_info(data3))

# if __name__ == '__main__':
#     app.run(debug=True)

