'''
Author: CatherineHao 1512769550@qq.com
Date: 2023-07-12 21:37:31
LastEditors: CatherineHao 1512769550@qq.com
LastEditTime: 2023-07-26 20:49:44
Authorization: Bearer "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"
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
    
# print(chart_info(data3))
            
# def chat_with_gpt(request):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         #messages = generate_prompt(used_data,used_text),
#         prompt = request,
#         max_tokens=2000, # 设置生成的最大token数，可以根据需要调整
#         temperature=0.2, # 设置温度,值越小越确认
#         #stop = ["\n"],
#         stop=None,
#     )
#     message = response.choices[0].text
#     # print(message)  # 带reason的文本
#     start_index = message.find('reason:')
#     result = message[0:start_index]
#     # print(result)  # 仅带result文本
#     return result


"""
messages=[{"role": "system", "content": "You are a helpful assistant."}, # 告诉AI他的身份定位是啥 如果不填默认是"You are a helpful assistant."
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."}, # 模型have no memory of past requests 之前的上下文放在这
        {"role": "user", "content": "Where was it played?"}] # 用户的问题

写法一、把default_prompt+user_input拼一起放进content,也就是现在代码中的写法

写法二、另一种Few-shot prompting写法, source:https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb
messages=[{"role": "system", "content": "You are a xxxxxxxxx assistant......"}, # tell AI his role
        {"role": "system", "name": "example_user", "content": prompt_1},        # example_1 prompt
        {"role": "system", "name": "example_assistant", "content": result_1}],  # example_1 result
        {"role": "system", "name": "example_user", "content": prompt_2},        # example_2 prompt
        {"role": "system", "name": "example_assistant", "content": result_2}],  # example_2 result
        {"role": "system", "name": "example_user", "content": prompt_3},        # example_3 prompt
        {"role": "system", "name": "example_assistant", "content": result_3}],  # example_3 result
        {"role": "user", "content": user_input}]   # the prompt of user's input

可以都跑一下试试哪种写法效果好一点

"""
def chat_with_gpt(request):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", # prompt+completion 最大16384 tokens
        # messages=[{"role": "user", "content": 'Translate the following English text to French: "Have a nice day!"'}], # 测试一下把英语翻译成法语
        messages=[{"role": "user", "content": f"{request}"}],
        max_tokens=4000, # 设置生成的最大token数，可以根据需要调整
        temperature=0.2, # 设置温度,值越小越确认
        #stop = ["\n"],
        stop=None,
    )
    print(response)
    reply = response['choices'][0]['message']['content']
    start_index = reply.find('reason:')
    result = reply[0:start_index]
    return result

# prompt:
default_prompt = """Please think as an economic data analyst. Now I wish to complete the matching of tha data to text, identifying the subjects, trend in the text and their position in the data. For each pair, give me the matching result and the reason.
The matching result should be in the format of {"ObjectName":[object in the text and data], "BeginIndex":[the object/trend corresponds to the start index in data],"EndIndex":[the object/trend corresponds to the end index in data]}.
Please refer to the example below for the desired format.

data: [{'Position':'United Kingdom','Billions of dollars':'59.9'},
	                {'Position':'Netherlands','Billions of dollars':'43.1'},
                    {'Position':'France','Billions of dollars':'35.3'},
	                {'Position':'Canada','Billions of dollars': '30'},
                    {'Position':'Japan','Billions of dollars':'29.6'}]
text: ["Investment by British investors accounted for 18 percent of new foreign direct investment expenditures. The Netherlands ($43.1 billion) was the second-largest investing country, followed by France ($35.3 billion)."]
result: [{"ObjectName":"Netherlands","BeginIndex":"1","EndIndex":"1"},{"ObjectName":"France","BeginIndex":"2","EndIndex":"2"}]
reason: "According to the correspondence between data and text, there exist two subjects: "Netherlands" and "France", and their respective position index in the data are "1" and "2"."

data: [{'Time':'2017/1/1','Mini- and subcompact size':'0.61','Compact size':'0.35', 'Midsize to large':'0.04'},
	{'Time':'2018/1/1','Mini- and subcompact size':'0.49','Compact size':'0.41', 'Midsize to large':'0.10'},
	{'Time':'2019/1/1','Mini- and subcompact size':'0.33','Compact size':'0.54', 'Midsize to large':'0.13'},
	{'Time':'2020/1/1','Mini- and subcompact size':'0.35','Compact size':'0.33', 'Midsize to large':'0.32'},
	{'Time':'2021/1/1','Mini- and subcompact size':'0.37','Compact size':'0.28', 'Midsize to large':'0.35'},
	{'Time':'2022/1/1','Mini- and subcompact size':'0.37','Compact size':'0.31', 'Midsize to large':'0.32'},
	{'Time':'2023/1/1','Mini- and subcompact size':'0.30','Compact size':'0.30', 'Midsize to large':'0.40'}]
text: ["In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size."]
result: [{"ObjectName":"Mini- and subcompact size","BeginIndex":"6","EndIndex":"6","Trend":"Declined","Number":"0.30"},
{"ObjectName":"Mini- and subcompact size","BeginIndex":"0","EndIndex":"0","Trend":"None","Number":"0.61"},
{"ObjectName":"Compact Size + Midsize to large","BeginIndex":"7","EndIndex":"7","Trend":"upgrade trend","Number":"0.30 + 0.40"},
{"ObjectName":"Compact Size + Midsize to large","BeginIndex":"0","EndIndex":"0","Trend":"None","Number":"0.35 + 0.04"}]
reason: "The phrase 'the mix of compact and midsize-to-large NEVs' suggests there are two subjects 'compact size' and 'Midsize to large' in the sentence. "

"""


# 测试是否连通
if __name__ == '__main__':
    # user_input = input("you:")
    # if user_input.lower() in ["exit","quit","bye"]:
    #     print("system: Goodbye!")
    #     break
    # user_input = input("Enter the data and the text:")
    user_input = """[{"data":[{'Category':'Real GDP','Outdoor recreation':'18.9','U.S. economy':'5.9'},
                        {'Category':'Real Gross Output','Outdoor recreation':'21.8','U.S. economy':'6.3'},
                        {'Category':'Compensation','Outdoor recreation':'16.2','U.S. economy':'7.8'},
                        {'Category':'Compensation','Outdoor recreation':'13.1','U.S. economy':'2.7'}] }], 
                    "text":Inflation-adjusted ("real") GDP for the outdoor recreation economy increased 18.9 percent in 2021, compared with a 5.9 percent increase for the overall U.S. economy, reflecting a rebound in outdoor recreation after the decrease of 21.6 percent in 2020."""
    user_info = default_prompt + user_input
    # print(user_info)
    result = chat_with_gpt(user_info)
    print(result)
    
        

# if __name__ == '__main__':
#     app.run(debug=True)

# test data:
# data = """[{"data":[{'Category':'Real GDP','Outdoor recreation':'18.9','U.S. economy':'5.9'},
#                     {'Category':'Real Gross Output','Outdoor recreation':'21.8','U.S. economy':'6.3'},
#                     {'Category':'Compensation','Outdoor recreation':'16.2','U.S. economy':'7.8'},
#                     {'Category':'Compensation','Outdoor recreation':'13.1','U.S. economy':'2.7'}] }]"""
#     text = """'text':Inflation-adjusted ("real") GDP for the outdoor recreation economy increased 18.9 percent in 2021, compared with a 5.9 percent increase for the overall U.S. economy, reflecting a rebound in outdoor recreation after the decrease of 21.6 percent in 2020."""
