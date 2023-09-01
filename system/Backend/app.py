'''
Description: 
Author: Qing Shi
Date: 2022-11-20 19:14:42
LastEditTime: 2023-08-27 21:26:46
'''
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import re
from front_format import result_to_frontend, transform_result

FILE_ABS_PATH = os.path.dirname(__file__)

app = Flask(__name__)
CORS(app)
app.config['ENV'] = "development"
openai.api_key = "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"

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

# prompt: 一共14个example 9个normal/uptrend/downtrend + 5个超级长的head and shoulder/cup with handle/double top/triple top/rounding bottom
default_prompt = """Please think as an financial data analyst. Now I wish to complete the matching of tha data to text, identifying the objects, trend in the text and their position in the data. For each pair, give me the matching result and the reason.
The matching result should be in the format of {"ObjectName":[object in the text], "DataName":"column name in the data", "Position":[{"Begin":[the object/trend corresponds to the row of start index in data,the object/trend corresponds to the column of start index in data],"End":[the object/trend corresponds to the row of end index in data,the object/trend corresponds to the column of end index in data]}],"Trend":"the corresponding trend","Num":[the corresponding data],"Text":"the corresponding textual description"}.
Please refer to the example below for the desired format.

data: [{'Position':'United Kingdom','Billions of dollars':'59.9'},
	    {'Position':'Netherlands','Billions of dollars':'43.1'},
        {'Position':'France','Billions of dollars':'35.3'},
	    {'Position':'Canada','Billions of dollars': '30'},
        {'Position':'Japan','Billions of dollars':'29.6'}]
text: ["Investment by British investors accounted for 18 percent of new foreign direct investment expenditures. The Netherlands ($43.1 billion) was the second-largest investing country, followed by France ($35.3 billion)."]
result: [{"ObjectName":["Netherlands"],"DataName":"Billions of dollars","Position":[{"Begin":[1,1],"End":[1,1]}],"Trend":"None","Num":[43.1],"Text":"The Netherlands ($43.1 billion)"},
        {"ObjectName":["France"],"DataName":"Billions of dollars","Position":[{"Begin":[2,1],"End":[2,1]}],"Trend":"None","Num":[35.3],"Text":"France ($35.3 billion)"}]
reason: "The text 'Netherlands' corresponds to the row 'Netherlands' in data, and its corresponding value is '43.1'. The text 'France' corresponds to the row 'France' in data, and its corresponding value is '35.3' in 'Billions of dollars' column."


data: [{'Category':'Real GDP','Outdoor recreation':'18.9','U.S. economy':'5.9'},
        {'Category':'Real Gross Output','Outdoor recreation':'21.8','U.S. economy':'6.3'},
        {'Category':'Compensation','Outdoor recreation':'16.2','U.S. economy':'7.8'},
        {'Category':'Compensation','Outdoor recreation':'13.1','U.S. economy':'2.7'}]
text: ["Inflation-adjusted ("real") GDP for the outdoor recreation economy increased 18.9 percent in 2021, compared with a 5.9 percent increase for the overall U.S. economy, reflecting a rebound in outdoor recreation after the decrease of 21.6 percent in 2020."]
result: [{"ObjectName":["Inflation-adjusted ("real") GDP"],"DataName":"Outdoor recreation", "Position":[{"Begin":[0,1],"End":[0,1],"Trend":"increase","Num":[18.9],"Text":"Inflation-adjusted ("real") GDP for the outdoor recreation economy increased 18.9 percent in 2021"},
        {"ObjectName":["overall U.S. economy"],"DataName":"U.S. economy", "Position":["Begin":[0,2],"End":[0,2],"Trend":"rebound","Num":[5.9],"Text":"compared with a 5.9 percent increase for the overall U.S. economy, reflecting a rebound in outdoor recreation"}]
reason: "The text 'Inflation-adjusted ("real") GDP for the outdoor recreation economy' corresponds to the column 'Outdoor recreation' and the row 'Real GDP' in data. Its value is '18.9'. The text 'U.S. economy' corresponds to the column 'U.S. economy' and row 'Real GDP' in data and its value is '5.9', reflecting a rebound trend."


data: [{'time': 2021, 'Installed wind + PV capacity (GW)': 615, 'energy consumption percentage': '13.80%'}, 
        {'time': 2022, 'Installed wind + PV capacity (GW)': 695, 'energy consumption percentage': '15.10%'}, 
        {'time': 2023, 'Installed wind + PV capacity (GW)': 775, 'energy consumption percentage': '16.60%'}, 
        {'time': 2024, 'Installed wind + PV capacity (GW)': 855, 'energy consumption percentage': '18.30%'}, 
        {'time': 2025, 'Installed wind + PV capacity (GW)': 935, 'energy consumption percentage': '20.00%'}, 
        {'time': 2030, 'Installed wind + PV capacity (GW)': 1200, 'energy consumption percentage': '25.00%'}]
text: ["The China Lithium Industry Development Index white paper predicts a rising trend for installed wind and PV capacity (GW). It is expected to reach 1,200 GW and reach a 25% energy percentage in 2030."]
result: [{"ObjectName":["installed wind and PV capacity (GW)"],"DataName":"Installed wind + PV capacity (GW)","Position":[{"Begin":[0,1],"End":[5,1]}],"Trend":"rising","Num":"None","Text":"a rising trend for installed wind and PV capacity (GW)"},
        {"ObjectName":["It"],"DataName":"Installed wind + PV capacity (GW)","Position":[{"Begin":[5,1],"End":[5,1]}],"Trend":"None","Num":[1200],"Text":"It is expected to reach 1,200 GW"},
        {"ObjectName":"None","DataName":"energy consumption percentage","Position":[{"Begin":[5,2],"End":[5,2]}],"Trend":"None","Num":[25.00%],"Text":"reach a 25% energy percentage in 2030"}]
reason: "'It' in text refers to the column 'installed wind + PV capacity (GW)' in data. It has a "rising" trend from 2021 to 2030. The text 'installed wind and PV capacity (GW)' corresponds to the column 'installed wind + PV capacity (GW)' in data. Its value reachs '1200' in 2030. The text 'energy percentage' corresponds to the column 'energy consumption percentage' and the value is '25%' in 2030."


data: [{'time': 2010, 'coal': 290, 'natural gas ': 306, 'renewables ': 112, 'nuclear': 287, 'liquids': 103}, 
        {'time': 2015, 'coal': 323, 'natural gas ': 408, 'renewables ': 154, 'nuclear': 3, 'liquids': 112}, 
        {'time': 2020, 'coal': 315, 'natural gas ': 417, 'renewables ': 151, 'nuclear': 94, 'liquids': 85}, 
        {'time': 2025, 'coal': 311, 'natural gas ': 427, 'renewables ': 198, 'nuclear': 116, 'liquids': 7}, 
        {'time': 2030, 'coal': 305, 'natural gas ': 436, 'renewables ': 201, 'nuclear': 107, 'liquids': 4}, 
        {'time': 2035, 'coal': 304, 'natural gas ': 439, 'renewables ': 203, 'nuclear': 111, 'liquids': 3}, 
        {'time': 2040, 'coal': 300, 'natural gas ': 438, 'renewables ': 211, 'nuclear': 110, 'liquids': 4}]
text: ["The Japan Electric Institute has made a forecast for future electricity generation sources, predicting that the renewables will continuously increase and reach 211 billion kilowatt hours in 2040."]
result: [{"ObjectName":["the renewables"],"DataName":"renewables","Position":[{"Begin":[6,3],"End":[6,3]}],"Trend":"increase","Num":[211],"Text":"the renewables will continuously increase and reach 211 billion kilowatt hours in 2040"}]
reason: "'The renewables' in text corresponds to 'renewables' column in data. In '2040', the corresponding value is '211'"


data: [{'month': 'Jan', '2018': '29.70%', '2019': '37.60%', '2020': '37.60%'}, 
        {'month': 'Feb', '2018': '25.30%', '2019': '18.65%', '2020': '28.50%'}, 
        {'month': 'Mar', '2018': '35.10%', '2019': '35.10%', '2020': '50.10%'}, 
        {'month': 'Apr', '2018': '37.90%', '2019': '38.40%', '2020': '54.20%'}, 
        {'month': 'May', '2018': '37.10%', '2019': '37.60%', '2020': '49.40%'}, 
        {'month': 'Jun', '2018': '37.30%', '2019': '40.20%', '2020': '54.50%'}, 
        {'month': 'Jul', '2018': '31.90%', '2019': '43.40%', '2020': '56.50%'}, 
        {'month': 'Aug', '2018': '20.60%', '2019': '32.40%', '2020': '62.80%'}, 
        {'month': 'Sep', '2018': '22.20%', '2019': '34.60%', '2020': '59.80%'}, 
        {'month': 'Oct', '2018': '19.30%', '2019': '36.40%', '2020': '61.00%'}, 
        {'month': 'Nov', '2018': '22.70%', '2019': '30.20%', '2020': '56.70%'}, 
        {'month': 'Dec', '2018': '21.30%', '2019': '23.80%', '2020': '53.50%'}]
text: ["According to the data from Amazon's US station released by marketplacepulse, the proportion of Chinese sellers among new sellers in 2020 has greatly increased compared with the previous two years, and the proportion of Chinese sellers has stabilized at more than 50% since June 2020. In August 2020, it reached its highest point, 62.8%, getting an increase of 93.83% year-on-year."]
result: [{"ObjectName":["The proportion of Chinese sellers"],"DataName":"2020","Position":[{"Begin":[0,3],"End":[11,3]}],"Trend":"increased","Num":"None","Text":"the proportion of Chinese sellers among new sellers in 2020 has greatly increased compared with the previous two years"},
        {"ObjectName":["The proportion of Chinese sellers"],"DataName":"2020","Position":[{"Begin":[5,3],"End":[11,3]}],"Trend":"stabilized","Num":"None","Text":"the proportion of Chinese sellers has stabilized at more than 50% since June 2020"},
        {"ObjectName":["It"],"DataName":"2020","Position":[{"Begin":[7,3],"End":[7,3]}],"Trend":"highest","Num":[62.8%],"Text":"In August 2020, it reached its highest point, 62.8%"}]
reason: "The columns in the data are uncertain, combined with text, we can identify that 'the proportion of Chinese sellers' is the object, and 'it' refers to 'the proportion of Chinese sellers'. All values from 'Jun' in '2020' column are higher than 50%. Compared with August 2019, the '62.8%' in August 2020 gets an increase of 93.83%."


data: [{'Time': '2022 Q1', 'Current account (billion)': 34.43}, 
        {'Time': '2022 Q2', 'Current account (billion)': 33.72}, 
        {'Time': '2022 Q3', 'Current account (billion)': 32.72}, 
        {'Time': '2022 Q4', 'Current account (billion)': 23.52}, 
        {'Time': '2023 Q1', 'Current account (billion)': 30.55}, 
        {'Time': '2023 Q2', 'Current account (billion)': 31.02}]
text: ["Singapore's current account surplus declined to SGD 31.02 billion in the second quarter of 2023 from SGD 33.72 billion in the same period of 2022."]
result: [{"ObjectName":["Singapore's current account surplus"],"DataName":"Current account (billion)","Position":[{"Begin":[1,1],"End":[5,1]}],"Trend":"declined","Num":[31.02,33.72],"Text":"Singapore's current account surplus declined to SGD 31.02 billion in the second quarter of 2023 from SGD 33.72 billion in the same period of 2022"}]
reason: "The text 'Singapore's current account surplus' corresponds to the column 'Current account (billion)' in data. Its value is SGD 31.02 billion in the second quarter of 2023 and is SGD 33.72 in the second quarter of 2022, which shows a declined pattern."


data: [{'Time': 'Aug 2022', 'Inflation rate': 8.3},
        {'Time': 'Sep 2022', 'Inflation rate': 8.2}, 
        {'Time': 'Oct 2022', 'Inflation rate': 7.7}, 
        {'Time': 'Nov 2022', 'Inflation rate': 7.1}, 
        {'Time': 'Dec 2022', 'Inflation rate': 6.5}, 
        {'Time': 'Jan 2023', 'Inflation rate': 6.4}, 
        {'Time': 'Feb 2023', 'Inflation rate': 6.0}, 
        {'Time': 'Mar 2023', 'Inflation rate': 5.0}, 
        {'Time': 'Apr 2023', 'Inflation rate': 4.9}, 
        {'Time': 'May 2023', 'Inflation rate': 4.1}, 
        {'Time': 'Jun 2023', 'Inflation rate': 3.0}, 
        {'Time': 'Jul 2023', 'Inflation rate': 3.2}]
text: ["Annual inflation rate in the US accelerated to 3.2% in July 2023 from 3% in June, but below forecasts of 3.3%. It marks a halt in the 12 consecutive months of declines, due to base effects."]
result: [{"ObjectName":["Annual inflation rate"],"DataName":"Inflation rate","Position":[{"Begin":[10,1],"End":[11,1]}],"Trend":"accelerate","Num":[3,3.2],"Text":"Annual inflation rate in the US accelerated to 3.2% in July 2023 from 3% in June"},
        {"ObjectName":["It"],"DataName":"Inflation rate","Position":[{"Begin":[0,1],"End":[11,1]}],"Trend":"decline","Num":"None,"Text":"It marks a halt in the 12 consecutive months of declines"}]
reason: "The column 'Inflation rate' corresponds to the 'Annual inflation rate' and 'it' in the text. The annual inflation rate acceletated from 3% in June to 3.2% in July, which corresponds the 'Jun 2023' row and the 'Jul 2023' row. The 12 consecutive months of declines correspond to the interval from 'Aug 2022' to 'Jun 2023'."


data: [{'Time': '2021 Q3', 'GDP Growth Rate': 1.7}, 
        {'Time': '2021 Q4', 'GDP Growth Rate': 1.5}, 
        {'Time': '2022 Q1', 'GDP Growth Rate': 0.5}, 
        {'Time': '2022 Q2', 'GDP Growth Rate': 0.1}, 
        {'Time': '2022 Q3', 'GDP Growth Rate': -0.1}, 
        {'Time': '2022 Q4', 'GDP Growth Rate': 0.1}, 
        {'Time': '2023 Q1', 'GDP Growth Rate': 0.1}, 
        {'Time': '2023 Q2', 'GDP Growth Rate': 0.2}]
text: ["The British economy expanded 0.2% on quarter in Q2 2023, following a 0.1% growth in Q1 and beating forecasts of a flat reading, preliminary estimates showed."]
result: [{"ObjectName":["The British economy"],"DataName":"GDP Growth Rate","Position":[{"Begin":[7,1],"End":[6,1]}],"Trend":"expanded","Num":[0.2,0.1],"Text":"The British economy expanded 0.2% on quarter in Q2 2023, following a 0.1% growth in Q1"}]
reason: "The column 'GDP Growth Rate' corresponds to 'The British economy' in the text. The '0.2% on quarter in Q2 2023' corresponds to row '2023 Q2' and the '0.1% growth in Q1' corresponds to row '2023 Q1'."


data: [{'Time': 2012, 'Launches': 46, 'Liquidations': 14, 'Active': 271}, 
        {'Time': 2013, 'Launches': 50, 'Liquidations': 18, 'Active': 303}, 
        {'Time': 2014, 'Launches': 76, 'Liquidations': 18, 'Active': 361}, 
        {'Time': 2015, 'Launches': 68, 'Liquidations': 18, 'Active': 411}, 
        {'Time': 2016, 'Launches': 51, 'Liquidations': 14, 'Active': 448}, 
        {'Time': 2017, 'Launches': 63, 'Liquidations': 20, 'Active': 491}, 
        {'Time': 2018, 'Launches': 61, 'Liquidations': 24, 'Active': 528}, 
        {'Time': 2019, 'Launches': 64, 'Liquidations': 19, 'Active': 573}, 
        {'Time': 2020, 'Launches': 65, 'Liquidations': 32, 'Active': 606}, 
        {'Time': 2021, 'Launches': 75, 'Liquidations': 17, 'Active': 664}, 
        {'Time': 2022, 'Launches': 26, 'Liquidations': 21, 'Active': 669}, 
        {'Time': 2023, 'Launches': 5, 'Liquidations': 18, 'Active': 656}]
text: ["The number of active China-focused hedge funds has slipped for the first time since at least 2012, with only five new funds launched this year as of June. Another 18 funds were liquidated, the data show."]
result: [{"ObjectName":["active China-focused hedge funds"],"DataName":"Active","Position":[{"Begin":[11,3],"End":[11,3]}],"Trend":"slipped","Num":"None","Text":"The number of active China-focused hedge funds has slipped for the first time since at least 2012"},
        {"ObjectName":["funds launched"],"DataName":"Launches","Position":[{"Begin":[11,1],"End":[11,1]}],"Trend":"None","Num":[5],"Text":"only five new funds launched this year as of June"},
        {"ObjectName":["funds were liquidated"],"DataName":"Liquidations","Position":[{"Begin":[11,2],"End":[11,2]}],"Trend":"None","Num":[18],"Text":"Another 18 funds were liquidated"}]
reason: "There are three objects in data and text: active funds, liquidated funds and launched funds. The has a down trend in  active funds as its number keep increasing before 2023. The 'funds launched' corresponds to the column 'Launches', and the 'funds were liquidated' corresponds to the column 'Liquidation'."
"""

@app.route("/api/test/postQuery/", methods=['POST'])
def chat_with_gpt():
    params = request.json
    # print(params)
    user_info = params['data']
    print(user_info)
    user_data_text = user_info[:user_info.find("\"]")+2]
    # print(user_data_text)
    t_request = default_prompt + user_data_text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", # prompt+completion 最大16384 tokens
        # model="gpt-4-32k",
        # messages=[{"role": "user", "content": 'Translate the following English text to French: "Have a nice day!"'}], # 测试一下把英语翻译成法语
        messages=[{"role": "user", "content": t_request}],
        max_tokens=2000, # 设置生成的最大token数，可以根据需要调整
        temperature=0.2, # 设置温度,值越小越确认
        #stop = ["\n"],
        stop=None,
    )
    print(response)
    reply = response['choices'][0]['message']['content']
    start_index = reply.find('reason:')
    result = reply[0:start_index]
    reason = reply[start_index:]
    result_frontend = result_to_frontend(user_info, result)
    final_result = transform_result(result_frontend)
        # Save the updated data back to the JSON file
    output_file_path = 'output.json'
    data = {"result":result, "reason": reason, "final": final_result}
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print("Saved to", output_file_path)
    return {"result":result, "reason": reason, "final": final_result}



@app.route('/api/test/postQuery_fake/', methods=['POST'])
def post_query():
    params = request.json
    file_path = '{}/data/output_1.json'.format(FILE_ABS_PATH)
    data = read_json(file_path)
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



if __name__ == '__main__':
    app.run(debug=True)