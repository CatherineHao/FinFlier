'''
Description: 
Author: Qing Shi
Date: 2022-11-20 19:14:42
LastEditTime: 2023-09-02 21:38:03
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



# @app.route("get_result", methods = ("GET", "POST"))
@app.route('/api/test/postQuery_real/', methods=['POST'])
def chat_with_gpt():
    params = request.json
    # print(params)
    user_info = params['data']
    print(user_info)
    label = user_info[user_info.find("label"):]
    # print(label)
    if "start" in label:
        # user_data_text = user_info[:user_info.find("\"]")+2]
        user_data_text = user_info[:user_info.find("label")]
        # 匹配复杂pattern, 把对应的prompt加到最后面
        if "head and shoulder" in user_data_text: 
            t_request = default_prompt + head_and_shoulder + user_data_text
        elif "cup and handle" in user_data_text:
            t_request = default_prompt + cup_and_handle + user_data_text
        elif "rounding bottom" in user_data_text:
            t_request = default_prompt + rounding_bottom + user_data_text
        elif "double top" in user_data_text:
            t_request = default_prompt + double_top + user_data_text
        elif "triple top" in user_data_text:
            t_request = default_prompt + triple_top + user_data_text
        else:
            t_request = default_prompt + user_data_text

        # call gpt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", # prompt+completion 最大16384 tokens
            # model="gpt-4-32k",
            # messages=[{"role": "user", "content": 'Translate the following English text to French: "Have a nice day!"'}], # 测试一下把英语翻译成法语
            messages=[{"role": "user", "content": t_request}],
            max_tokens=2000, # 设置生成的最大token数，可以根据需要调整
            temperature=0.4, # 设置温度,值越小越确认
            #stop = ["\n"],
            stop=None,
        )
        print(response)
        reply = response['choices'][0]['message']['content']
        start_index = reply.find('reason:')
        result = reply[0:start_index]
        reason = reply[start_index:]
        result_frontend = result_to_frontend(user_info, result)
        print(result_frontend)
        final_result = transform_result(result_frontend)
        print(final_result)
        output_file_path = 'output.json'
        data = {"result":result, "reason": reason, "final": final_result}
        with open(output_file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print("Saved to", output_file_path)
        return {"result":result, "reason": reason, "final": final_result}
    
    if "following" in label:
        # user_info 包括 data+text+result+reason+follow_question+label:following
        user_data_text = user_info[:user_info.find("result")]
        result_reason = user_info[user_info.find("result"):user_info.find("question")]
        question = user_info[user_info.find("question"):user_info.find("label")]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", # prompt+completion 最大16384 tokens
            messages=[{"role": "system", "content": "You are a helpful assistant."}, # 告诉AI他的身份定位是啥 如果不填默认是"You are a helpful assistant."
                        {"role": "user", "content": user_data_text}, # 用户上传的data+text
                        {"role": "assistant", "content": result_reason}, # gpt回答的result+reason
                        {"role": "user", "content": user_data_text+question}], # follow_question
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
        result_frontend = result_to_frontend(user_data_text, result)
        final_result = transform_result(result_frontend)
        output_file_path = 'output1.json'
        data = {"result":result, "reason": reason, "final": final_result}
        with open(output_file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print("Saved to", output_file_path)
        return {"result":result, "reason": reason, "final": final_result}


   

# prompt: 一共14个example 9个normal/uptrend/downtrend + 5个超级长的head and shoulder/cup with handle/double top/triple top/rounding bottom
default_prompt = """Please think as an financial data analyst. Now I wish to complete the matching of tha data to text, identifying the objects, trend in the text and their position in the data. For each pair, give me the matching result and the reason.
The matching result should be in the format of result: [{"ObjectName":[object in the text], "DataName":"column name in the data", "Position":[{"Begin":[the object/trend corresponds to the row of start index in data,the object/trend corresponds to the column of start index in data],"End":[the object/trend corresponds to the row of end index in data,the object/trend corresponds to the column of end index in data]}],"Trend":"the corresponding trend","Num":[the corresponding data],"Text":"the corresponding textual description"}] reason: "the reason of the matching result".
Please refer to the example below for the desired format.

data: [{'Position':'United Kingdom','Billions of dollars': 59.9},
	    {'Position':'Netherlands','Billions of dollars': 43.1},
        {'Position':'France','Billions of dollars': 35.3},
	    {'Position':'Canada','Billions of dollars': 30},
        {'Position':'Japan','Billions of dollars': 29.6}]
text: ["Investment by British investors accounted for 18 percent of new foreign direct investment expenditures. The Netherlands ($43.1 billion) was the second-largest investing country, followed by France ($35.3 billion)."]
result: [{"ObjectName":["Netherlands"],"DataName":"Billions of dollars","Position":[{"Begin":[1,1],"End":[1,1]}],"Trend":"None","Num":[43.1],"Text":"The Netherlands ($43.1 billion)"},
        {"ObjectName":["France"],"DataName":"Billions of dollars","Position":[{"Begin":[2,1],"End":[2,1]}],"Trend":"None","Num":[35.3],"Text":"France ($35.3 billion)"}]
reason: "The corresponding value for object "Netherlands" is "43.1", and its shortest descriptive phrase is "The Netherlands ($43.1 billion)". The corresponding value for object "France" is "35.3" and its shortest descriptive phrase is "France ($35.3 billion)""


data: [{'Category':'Real GDP','Outdoor recreation': 18.9,'U.S. economy': 5.9},
        {'Category':'Real Gross Output','Outdoor recreation': 21.8,'U.S. economy': 6.3},
        {'Category':'Compensation','Outdoor recreation': 16.2,'U.S. economy': 7.8},
        {'Category':'Employment','Outdoor recreation': 13.1,'U.S. economy': 2.7}]
text: ["Inflation-adjusted ("real") GDP for the outdoor recreation economy increased 18.9 percent in 2021, compared with a 5.9 percent increase for the overall U.S. economy, reflecting a rebound in outdoor recreation after the decrease of 21.6 percent in 2020."]
result: [{"ObjectName":["Inflation-adjusted ("real") GDP"],"DataName":"Outdoor recreation", "Position":[{"Begin":[0,1],"End":[0,1],"Trend":"increase","Num":[18.9],"Text":"Inflation-adjusted ("real") GDP for the outdoor recreation economy increased 18.9 percent in 2021"},
        {"ObjectName":["overall U.S. economy"],"DataName":"U.S. economy", "Position":["Begin":[0,2],"End":[0,2],"Trend":"rebound","Num":[5.9],"Text":"compared with a 5.9 percent increase for the overall U.S. economy, reflecting a rebound in outdoor recreation"}]
reason: "The first object is "Inflation-adjusted ("real") GDP for the outdoor recreation economy", its value is 18.9 and its descriptive phrase is "Inflation-adjusted ("real") GDP for the outdoor recreation economy increased 18.9 percent in 2021". The second object is "U.S. economy", its value is 5.9 and its descriptive phrase is "compared with a 5.9 percent increase for the overall U.S. economy, reflecting a rebound in outdoor recreation"."


data: [{'time': 2021, 'Installed wind + PV capacity (GW)': 615, 'energy consumption percentage': 13.80%}, 
        {'time': 2022, 'Installed wind + PV capacity (GW)': 695, 'energy consumption percentage': 15.10%}, 
        {'time': 2023, 'Installed wind + PV capacity (GW)': 775, 'energy consumption percentage': 16.60%}, 
        {'time': 2024, 'Installed wind + PV capacity (GW)': 855, 'energy consumption percentage': 18.30%}, 
        {'time': 2025, 'Installed wind + PV capacity (GW)': 935, 'energy consumption percentage': 20.00%}, 
        {'time': 2030, 'Installed wind + PV capacity (GW)': 1200, 'energy consumption percentage': 25.00%}]
text: ["The China Lithium Industry Development Index white paper predicts a rising trend for installed wind and PV capacity (GW). It is expected to reach 1,200 GW and reach a 25% energy percentage in 2030."]
result: [{"ObjectName":["installed wind and PV capacity (GW)"],"DataName":"Installed wind + PV capacity (GW)","Position":[{"Begin":[0,1],"End":[5,1]}],"Trend":"rising","Num":"None","Text":"a rising trend for installed wind and PV capacity (GW)"},
        {"ObjectName":["It"],"DataName":"Installed wind + PV capacity (GW)","Position":[{"Begin":[5,1],"End":[5,1]}],"Trend":"None","Num":[1200],"Text":"It is expected to reach 1,200 GW"},
        {"ObjectName":"None","DataName":"energy consumption percentage","Position":[{"Begin":[5,2],"End":[5,2]}],"Trend":"None","Num":[25.00%],"Text":"reach a 25% energy percentage in 2030"}]
reason: "'It' in text refers to 'installed wind + PV capacity (GW)'. The object in unit 1 is "installed wind and PV capacity (GW)". It has a "rising" trend from 2021 to 2030 and its descriptive phrase is 'a rising trend for installed wind and PV capacity (GW)'. The object in unit 2 is "installed wind and PV capacity (GW)". It reachs '1200' in 2030 and its descriptive phrase is 'It is expected to reach 1,200 GW'. The object in unit 3 is "energy percentage". It reaches '25%' in 2030 and its descriptive phrase is 'reach a 25% energy percentage in 2030'."


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


data: [{'month': 'Jan', '2018': 29.70%, '2019': 37.60%, '2020': 37.60%}, 
        {'month': 'Feb', '2018': 25.30%, '2019': 18.65%, '2020': 28.50%}, 
        {'month': 'Mar', '2018': 35.10%, '2019': 35.10%, '2020': 50.10%}, 
        {'month': 'Apr', '2018': 37.90%, '2019': 38.40%, '2020': 54.20%}, 
        {'month': 'May', '2018': 37.10%, '2019': 37.60%, '2020': 49.40%}, 
        {'month': 'Jun', '2018': 37.30%, '2019': 40.20%, '2020': 54.50%}, 
        {'month': 'Jul', '2018': 31.90%, '2019': 43.40%, '2020': 56.50%}, 
        {'month': 'Aug', '2018': 20.60%, '2019': 32.40%, '2020': 62.80%}, 
        {'month': 'Sep', '2018': 22.20%, '2019': 34.60%, '2020': 59.80%}, 
        {'month': 'Oct', '2018': 19.30%, '2019': 36.40%, '2020': 61.00%}, 
        {'month': 'Nov', '2018': 22.70%, '2019': 30.20%, '2020': 56.70%}, 
        {'month': 'Dec', '2018': 21.30%, '2019': 23.80%, '2020': 53.50%}]
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

# 5个超级长的head and shoulder/cup with handle/double top/triple top/rounding bottom，全部放进prompt共2w3token。
head_and_shoulder = """
data: [{'Date': '1999/8/2', 'Close': 2.35}, {'Date': '1999/8/3', 'Close': 2.371875}, {'Date': '1999/8/4', 'Close': 2.210938}, {'Date': '1999/8/5', 'Close': 2.43125}, {'Date': '1999/8/6', 'Close': 2.239063}, {'Date': '1999/8/9', 'Close': 2.1375}, {'Date': '1999/8/10', 'Close': 2.275}, {'Date': '1999/8/11', 'Close': 2.273438}, {'Date': '1999/8/12', 'Close': 2.29375}, {'Date': '1999/8/13', 'Close': 2.435938}, {'Date': '1999/8/16', 'Close': 2.457813}, {'Date': '1999/8/17', 'Close': 2.73125}, {'Date': '1999/8/18', 'Close': 2.828125}, {'Date': '1999/8/19', 'Close': 2.653125}, {'Date': '1999/8/20', 'Close': 2.835938}, {'Date': '1999/8/23', 'Close': 2.959375}, {'Date': '1999/8/24', 'Close': 3.001563}, {'Date': '1999/8/25', 'Close': 3.321875}, {'Date': '1999/8/26', 'Close': 3.214063}, {'Date': '1999/8/27', 'Close': 3.2125}, {'Date': '1999/8/30', 'Close': 2.98125}, {'Date': '1999/8/31', 'Close': 3.109375}, {'Date': '1999/9/1', 'Close': 2.976563}, {'Date': '1999/9/2', 'Close': 3.003125}, {'Date': '1999/9/3', 'Close': 3.121875}, {'Date': '1999/9/7', 'Close': 3.146875}, {'Date': '1999/9/8', 'Close': 3.071875}, {'Date': '1999/9/9', 'Close': 3.18125}, {'Date': '1999/9/10', 'Close': 3.325}, {'Date': '1999/9/13', 'Close': 3.165625}, {'Date': '1999/9/14', 'Close': 3.3}, {'Date': '1999/9/15', 'Close': 3.278125}, {'Date': '1999/9/16', 'Close': 3.2625}, {'Date': '1999/9/17', 'Close': 3.190625}, {'Date': '1999/9/20', 'Close': 3.1375}, {'Date': '1999/9/21', 'Close': 3.1125}, {'Date': '1999/9/22', 'Close': 3.3}, {'Date': '1999/9/23', 'Close': 3.1125}, {'Date': '1999/9/24', 'Close': 3.25}, {'Date': '1999/9/27', 'Close': 3.128125}, {'Date': '1999/9/28', 'Close': 3.29375}, {'Date': '1999/9/29', 'Close': 4.0375}, {'Date': '1999/9/30', 'Close': 3.996875}, {'Date': '1999/10/1', 'Close': 3.8625}, {'Date': '1999/10/4', 'Close': 3.853125}, {'Date': '1999/10/5', 'Close': 3.921875}, {'Date': '1999/10/6', 'Close': 4.121875}, {'Date': '1999/10/7', 'Close': 4.365625}, {'Date': '1999/10/8', 'Close': 4.4625}, {'Date': '1999/10/11', 'Close': 4.41875}, {'Date': '1999/10/12', 'Close': 4.246875}, {'Date': '1999/10/13', 'Close': 3.996875}, {'Date': '1999/10/14', 'Close': 3.979688}, {'Date': '1999/10/15', 'Close': 3.753125}, {'Date': '1999/10/18', 'Close': 3.703125}, {'Date': '1999/10/19', 'Close': 3.83125}, {'Date': '1999/10/20', 'Close': 4.025}, {'Date': '1999/10/21', 'Close': 4.0375}, {'Date': '1999/10/22', 'Close': 3.93125}, {'Date': '1999/10/25', 'Close': 4.1375}, {'Date': '1999/10/26', 'Close': 4.0625}, {'Date': '1999/10/27', 'Close': 3.796875}, {'Date': '1999/10/28', 'Close': 3.55}, {'Date': '1999/10/29', 'Close': 3.53125}, {'Date': '1999/11/1', 'Close': 3.45625}, {'Date': '1999/11/2', 'Close': 3.321875}, {'Date': '1999/11/3', 'Close': 3.290625}, {'Date': '1999/11/4', 'Close': 3.153125}, {'Date': '1999/11/5', 'Close': 3.246875}, {'Date': '1999/11/8', 'Close': 3.9}, {'Date': '1999/11/9', 'Close': 3.540625}, {'Date': '1999/11/10', 'Close': 3.6}, {'Date': '1999/11/11', 'Close': 3.65}, {'Date': '1999/11/12', 'Close': 3.746875}, {'Date': '1999/11/15', 'Close': 3.675}, {'Date': '1999/11/16', 'Close': 3.946875}, {'Date': '1999/11/17', 'Close': 3.825}, {'Date': '1999/11/18', 'Close': 3.896875}, {'Date': '1999/11/19', 'Close': 3.896875}, {'Date': '1999/11/22', 'Close': 4.025}, {'Date': '1999/11/23', 'Close': 4.0875}, {'Date': '1999/11/24', 'Close': 4.3625}, {'Date': '1999/11/26', 'Close': 4.65625}, {'Date': '1999/11/29', 'Close': 4.521875}, {'Date': '1999/11/30', 'Close': 4.253125}, {'Date': '1999/12/1', 'Close': 4.25}, {'Date': '1999/12/2', 'Close': 4.453125}, {'Date': '1999/12/3', 'Close': 4.328125}, {'Date': '1999/12/6', 'Close': 4.3875}, {'Date': '1999/12/7', 'Close': 4.303125}, {'Date': '1999/12/8', 'Close': 4.428125}, {'Date': '1999/12/9', 'Close': 5.18125}, {'Date': '1999/12/10', 'Close': 5.334375}, {'Date': '1999/12/13', 'Close': 5.125}, {'Date': '1999/12/14', 'Close': 4.78125}, {'Date': '1999/12/15', 'Close': 4.825}, {'Date': '1999/12/16', 'Close': 4.74375}, {'Date': '1999/12/17', 'Close': 4.703125}, {'Date': '1999/12/20', 'Close': 4.85}, {'Date': '1999/12/21', 'Close': 4.99375}, {'Date': '1999/12/22', 'Close': 4.884375}, {'Date': '1999/12/23', 'Close': 4.5}, {'Date': '1999/12/27', 'Close': 4.05625}, {'Date': '1999/12/28', 'Close': 4.115625}, {'Date': '1999/12/29', 'Close': 4.175}, {'Date': '1999/12/30', 'Close': 3.953125}, {'Date': '1999/12/31', 'Close': 3.80625}, {'Date': '2000/1/3', 'Close': 4.46875}, {'Date': '2000/1/4', 'Close': 4.096875}, {'Date': '2000/1/5', 'Close': 3.4875}, {'Date': '2000/1/6', 'Close': 3.278125}, {'Date': '2000/1/7', 'Close': 3.478125}, {'Date': '2000/1/10', 'Close': 3.459375}, {'Date': '2000/1/11', 'Close': 3.3375}, {'Date': '2000/1/12', 'Close': 3.178125}, {'Date': '2000/1/13', 'Close': 3.296875}, {'Date': '2000/1/14', 'Close': 3.2125}, {'Date': '2000/1/18', 'Close': 3.20625}, {'Date': '2000/1/19', 'Close': 3.340625}, {'Date': '2000/1/20', 'Close': 3.2375}, {'Date': '2000/1/21', 'Close': 3.103125}, {'Date': '2000/1/24', 'Close': 3.50625}, {'Date': '2000/1/25', 'Close': 3.4625}, {'Date': '2000/1/26', 'Close': 3.240625}, {'Date': '2000/1/27', 'Close': 3.346875}, {'Date': '2000/1/28', 'Close': 3.084375}, {'Date': '2000/1/31', 'Close': 3.228125}, {'Date': '2000/2/1', 'Close': 3.371875}, {'Date': '2000/2/2', 'Close': 3.471875}, {'Date': '2000/2/3', 'Close': 4.209375}, {'Date': '2000/2/4', 'Close': 3.928125}, {'Date': '2000/2/7', 'Close': 3.75}, {'Date': '2000/2/8', 'Close': 4.15625}, {'Date': '2000/2/9', 'Close': 4.0125}, {'Date': '2000/2/10', 'Close': 3.809375}, {'Date': '2000/2/11', 'Close': 3.809375}, {'Date': '2000/2/14', 'Close': 3.721875}, {'Date': '2000/2/15', 'Close': 3.690625}, {'Date': '2000/2/16', 'Close': 3.534375}, {'Date': '2000/2/17', 'Close': 3.45}, {'Date': '2000/2/18', 'Close': 3.2375}, {'Date': '2000/2/22', 'Close': 3.178125}, {'Date': '2000/2/23', 'Close': 3.521875}, {'Date': '2000/2/24', 'Close': 3.421875}, {'Date': '2000/2/25', 'Close': 3.45625}, {'Date': '2000/2/28', 'Close': 3.2875}, {'Date': '2000/2/29', 'Close': 3.44375}, {'Date': '2000/3/1', 'Close': 3.29375}, {'Date': '2000/3/2', 'Close': 3.128125}, {'Date': '2000/3/3', 'Close': 3.125}, {'Date': '2000/3/6', 'Close': 3.196875}, {'Date': '2000/3/7', 'Close': 3.175}, {'Date': '2000/3/8', 'Close': 3.18125}, {'Date': '2000/3/9', 'Close': 3.440625}, {'Date': '2000/3/10', 'Close': 3.34375}, {'Date': '2000/3/13', 'Close': 3.265625}, {'Date': '2000/3/14', 'Close': 3.28125}, {'Date': '2000/3/15', 'Close': 3.1875}, {'Date': '2000/3/16', 'Close': 3.3125}, {'Date': '2000/3/17', 'Close': 3.240625}, {'Date': '2000/3/20', 'Close': 3.209375}, {'Date': '2000/3/21', 'Close': 3.61875}, {'Date': '2000/3/22', 'Close': 3.534375}, {'Date': '2000/3/23', 'Close': 3.384375}, {'Date': '2000/3/24', 'Close': 3.634375}, {'Date': '2000/3/27', 'Close': 3.65625}, {'Date': '2000/3/28', 'Close': 3.50625}, {'Date': '2000/3/29', 'Close': 3.3125}, {'Date': '2000/3/30', 'Close': 3.325}, {'Date': '2000/3/31', 'Close': 3.35}, {'Date': '2000/4/3', 'Close': 3.178125}, {'Date': '2000/4/4', 'Close': 3.196875}, {'Date': '2000/4/5', 'Close': 3.109375}, {'Date': '2000/4/6', 'Close': 3.2125}, {'Date': '2000/4/7', 'Close': 3.378125}, {'Date': '2000/4/10', 'Close': 3.16875}, {'Date': '2000/4/11', 'Close': 3.16875}, {'Date': '2000/4/12', 'Close': 2.81875}, {'Date': '2000/4/13', 'Close': 2.4}, {'Date': '2000/4/14', 'Close': 2.34375}, {'Date': '2000/4/17', 'Close': 2.353125}, {'Date': '2000/4/18', 'Close': 2.746875}, {'Date': '2000/4/19', 'Close': 2.671875}, {'Date': '2000/4/20', 'Close': 2.61875}, {'Date': '2000/4/24', 'Close': 2.490625}, {'Date': '2000/4/25', 'Close': 2.621875}, {'Date': '2000/4/26', 'Close': 2.675}, {'Date': '2000/4/27', 'Close': 2.64375}, {'Date': '2000/4/28', 'Close': 2.759375}, {'Date': '2000/5/1', 'Close': 2.996875}, {'Date': '2000/5/2', 'Close': 2.80625}, {'Date': '2000/5/3', 'Close': 2.70625}, {'Date': '2000/5/4', 'Close': 2.753125}, {'Date': '2000/5/5', 'Close': 2.925}, {'Date': '2000/5/8', 'Close': 2.800781}, {'Date': '2000/5/9', 'Close': 2.8125}, {'Date': '2000/5/10', 'Close': 2.665625}, {'Date': '2000/5/11', 'Close': 2.74375}, {'Date': '2000/5/12', 'Close': 2.6875}, {'Date': '2000/5/15', 'Close': 2.803125}, {'Date': '2000/5/16', 'Close': 2.953125}, {'Date': '2000/5/17', 'Close': 3.05}, {'Date': '2000/5/18', 'Close': 2.76875}, {'Date': '2000/5/19', 'Close': 2.63125}, {'Date': '2000/5/22', 'Close': 2.59375}, {'Date': '2000/5/23', 'Close': 2.334375}, {'Date': '2000/5/24', 'Close': 2.428125}, {'Date': '2000/5/25', 'Close': 2.275}, {'Date': '2000/5/26', 'Close': 2.325}, {'Date': '2000/5/30', 'Close': 2.5875}, {'Date': '2000/5/31', 'Close': 2.415625}]
text: ["There exists a 'head and shoulder' pattern on the Amazon stock moving averages from 1999/09/27 to 2000/02/22."]
result: [{"ObjectName":["Amazon stock"],"DataName":"Close","Position":[{"Begin":[39,1],"End":[141,1]}],"Trend":"head and shoulder","Num":"None","Text":"a "head and shoulder" pattern on the Amazon stock moving averages from 1999/09/27 to 2000/02/22"}]
reason: "The 'Amazon stock' in text corresponds to the 'Close' column in data. The "head and shoulder" pattern consists of three rises and falls from three localized highs. The high point in the center is higher than the other two. This pattern is around from '1999/09/27' to '2000/02/22' and the middle high point exist on '1999/12/09'."
"""

cup_and_handle = """
data: data: [{'Date': '1999/5/3', 'Adj Close': 3.7734379999999996}, {'Date': '1999/5/4', 'Adj Close': 3.575}, {'Date': '1999/5/5', 'Adj Close': 3.6625}, {'Date': '1999/5/6', 'Adj Close': 3.434375}, {'Date': '1999/5/7', 'Adj Close': 3.409375}, {'Date': '1999/5/10', 'Adj Close': 3.671875}, {'Date': '1999/5/11', 'Adj Close': 3.709375}, {'Date': '1999/5/12', 'Adj Close': 3.573438}, {'Date': '1999/5/13', 'Adj Close': 3.4}, {'Date': '1999/5/14', 'Adj Close': 3.309375}, {'Date': '1999/5/17', 'Adj Close': 3.440625}, {'Date': '1999/5/18', 'Adj Close': 3.315625}, {'Date': '1999/5/19', 'Adj Close': 3.489063}, {'Date': '1999/5/20', 'Adj Close': 3.2703130000000002}, {'Date': '1999/5/21', 'Adj Close': 3.214063}, {'Date': '1999/5/24', 'Adj Close': 2.9375}, {'Date': '1999/5/25', 'Adj Close': 2.789063}, {'Date': '1999/5/26', 'Adj Close': 3.023438}, {'Date': '1999/5/27', 'Adj Close': 2.8640630000000002}, {'Date': '1999/5/28', 'Adj Close': 2.96875}, {'Date': '1999/6/1', 'Adj Close': 2.6453130000000002}, {'Date': '1999/6/2', 'Adj Close': 2.803125}, {'Date': '1999/6/3', 'Adj Close': 2.626563}, {'Date': '1999/6/4', 'Adj Close': 2.710938}, {'Date': '1999/6/7', 'Adj Close': 2.934375}, {'Date': '1999/6/8', 'Adj Close': 2.789063}, {'Date': '1999/6/9', 'Adj Close': 2.85}, {'Date': '1999/6/10', 'Adj Close': 2.898438}, {'Date': '1999/6/11', 'Adj Close': 2.6453130000000002}, {'Date': '1999/6/14', 'Adj Close': 2.3}, {'Date': '1999/6/15', 'Adj Close': 2.4125}, {'Date': '1999/6/16', 'Adj Close': 2.792188}, {'Date': '1999/6/17', 'Adj Close': 2.823438}, {'Date': '1999/6/18', 'Adj Close': 2.782813}, {'Date': '1999/6/21', 'Adj Close': 3.0875}, {'Date': '1999/6/22', 'Adj Close': 2.9375}, {'Date': '1999/6/23', 'Adj Close': 2.94375}, {'Date': '1999/6/24', 'Adj Close': 2.840625}, {'Date': '1999/6/25', 'Adj Close': 2.7546880000000002}, {'Date': '1999/6/28', 'Adj Close': 2.767188}, {'Date': '1999/6/29', 'Adj Close': 2.901563}, {'Date': '1999/6/30', 'Adj Close': 3.128125}, {'Date': '1999/7/1', 'Adj Close': 3.059375}, {'Date': '1999/7/2', 'Adj Close': 3.101563}, {'Date': '1999/7/6', 'Adj Close': 3.171875}, {'Date': '1999/7/7', 'Adj Close': 3.046875}, {'Date': '1999/7/8', 'Adj Close': 3.134375}, {'Date': '1999/7/9', 'Adj Close': 3.1375}, {'Date': '1999/7/12', 'Adj Close': 2.934375}, {'Date': '1999/7/13', 'Adj Close': 3.153125}, {'Date': '1999/7/14', 'Adj Close': 3.375}, {'Date': '1999/7/15', 'Adj Close': 3.489063}, {'Date': '1999/7/16', 'Adj Close': 3.440625}, {'Date': '1999/7/19', 'Adj Close': 3.292188}, {'Date': '1999/7/20', 'Adj Close': 3.003125}, {'Date': '1999/7/21', 'Adj Close': 3.135938}, {'Date': '1999/7/22', 'Adj Close': 2.670313}, {'Date': '1999/7/23', 'Adj Close': 2.8640630000000002}, {'Date': '1999/7/26', 'Adj Close': 2.648438}, {'Date': '1999/7/27', 'Adj Close': 2.525}, {'Date': '1999/7/28', 'Adj Close': 2.64375}, {'Date': '1999/7/29', 'Adj Close': 2.539063}, {'Date': '1999/7/30', 'Adj Close': 2.501563}, {'Date': '1999/8/2', 'Adj Close': 2.35}, {'Date': '1999/8/3', 'Adj Close': 2.371875}, {'Date': '1999/8/4', 'Adj Close': 2.210938}, {'Date': '1999/8/5', 'Adj Close': 2.43125}, {'Date': '1999/8/6', 'Adj Close': 2.2390630000000002}, {'Date': '1999/8/9', 'Adj Close': 2.1375}, {'Date': '1999/8/10', 'Adj Close': 2.275}, {'Date': '1999/8/11', 'Adj Close': 2.273438}, {'Date': '1999/8/12', 'Adj Close': 2.29375}, {'Date': '1999/8/13', 'Adj Close': 2.435938}, {'Date': '1999/8/16', 'Adj Close': 2.4578130000000002}, {'Date': '1999/8/17', 'Adj Close': 2.73125}, {'Date': '1999/8/18', 'Adj Close': 2.828125}, {'Date': '1999/8/19', 'Adj Close': 2.653125}, {'Date': '1999/8/20', 'Adj Close': 2.835938}, {'Date': '1999/8/23', 'Adj Close': 2.959375}, {'Date': '1999/8/24', 'Adj Close': 3.001563}, {'Date': '1999/8/25', 'Adj Close': 3.321875}, {'Date': '1999/8/26', 'Adj Close': 3.214063}, {'Date': '1999/8/27', 'Adj Close': 3.2125}, {'Date': '1999/8/30', 'Adj Close': 2.98125}, {'Date': '1999/8/31', 'Adj Close': 3.109375}, {'Date': '1999/9/1', 'Adj Close': 2.976563}, {'Date': '1999/9/2', 'Adj Close': 3.003125}, {'Date': '1999/9/3', 'Adj Close': 3.121875}, {'Date': '1999/9/7', 'Adj Close': 3.146875}, {'Date': '1999/9/8', 'Adj Close': 3.071875}, {'Date': '1999/9/9', 'Adj Close': 3.18125}, {'Date': '1999/9/10', 'Adj Close': 3.325}, {'Date': '1999/9/13', 'Adj Close': 3.165625}, {'Date': '1999/9/14', 'Adj Close': 3.3}, {'Date': '1999/9/15', 'Adj Close': 3.278125}, {'Date': '1999/9/16', 'Adj Close': 3.2625}, {'Date': '1999/9/17', 'Adj Close': 3.190625}, {'Date': '1999/9/20', 'Adj Close': 3.1375}, {'Date': '1999/9/21', 'Adj Close': 3.1125}, {'Date': '1999/9/22', 'Adj Close': 3.3}, {'Date': '1999/9/23', 'Adj Close': 3.1125}, {'Date': '1999/9/24', 'Adj Close': 3.25}, {'Date': '1999/9/27', 'Adj Close': 3.128125}, {'Date': '1999/9/28', 'Adj Close': 3.29375}, {'Date': '1999/9/29', 'Adj Close': 4.0375}, {'Date': '1999/9/30', 'Adj Close': 3.996875}, {'Date': '1999/10/1', 'Adj Close': 3.8625}, {'Date': '1999/10/4', 'Adj Close': 3.853125}, {'Date': '1999/10/5', 'Adj Close': 3.921875}, {'Date': '1999/10/6', 'Adj Close': 4.121875}, {'Date': '1999/10/7', 'Adj Close': 4.365625}, {'Date': '1999/10/8', 'Adj Close': 4.4625}, {'Date': '1999/10/11', 'Adj Close': 4.41875}, {'Date': '1999/10/12', 'Adj Close': 4.246875}, {'Date': '1999/10/13', 'Adj Close': 3.996875}, {'Date': '1999/10/14', 'Adj Close': 3.979688}, {'Date': '1999/10/15', 'Adj Close': 3.753125}, {'Date': '1999/10/18', 'Adj Close': 3.703125}, {'Date': '1999/10/19', 'Adj Close': 3.83125}, {'Date': '1999/10/20', 'Adj Close': 4.025}, {'Date': '1999/10/21', 'Adj Close': 4.0375}, {'Date': '1999/10/22', 'Adj Close': 3.93125}, {'Date': '1999/10/25', 'Adj Close': 4.1375}, {'Date': '1999/10/26', 'Adj Close': 4.0625}, {'Date': '1999/10/27', 'Adj Close': 3.796875}, {'Date': '1999/10/28', 'Adj Close': 3.55}, {'Date': '1999/10/29', 'Adj Close': 3.53125}, {'Date': '1999/11/1', 'Adj Close': 3.45625}, {'Date': '1999/11/2', 'Adj Close': 3.321875}, {'Date': '1999/11/3', 'Adj Close': 3.290625}, {'Date': '1999/11/4', 'Adj Close': 3.153125}, {'Date': '1999/11/5', 'Adj Close': 3.246875}, {'Date': '1999/11/8', 'Adj Close': 3.9}, {'Date': '1999/11/9', 'Adj Close': 3.540625}, {'Date': '1999/11/10', 'Adj Close': 3.6}, {'Date': '1999/11/11', 'Adj Close': 3.65}, {'Date': '1999/11/12', 'Adj Close': 3.746875}, {'Date': '1999/11/15', 'Adj Close': 3.675}, {'Date': '1999/11/16', 'Adj Close': 3.946875}, {'Date': '1999/11/17', 'Adj Close': 3.825}, {'Date': '1999/11/18', 'Adj Close': 3.896875}, {'Date': '1999/11/19', 'Adj Close': 3.896875}, {'Date': '1999/11/22', 'Adj Close': 4.025}, {'Date': '1999/11/23', 'Adj Close': 4.0875}, {'Date': '1999/11/24', 'Adj Close': 4.3625}, {'Date': '1999/11/26', 'Adj Close': 4.65625}, {'Date': '1999/11/29', 'Adj Close': 4.521875}, {'Date': '1999/11/30', 'Adj Close': 4.253125}]
text: ["There happens a 'cup and handle' pattern in Amazon stock from 1999/07/15 to 1999/09/29."]
result: [{"ObjectName":["Amazon stock"],"DataName":"Adj Close","Position":[{"Begin":[51,1],"End":[104,1]}],"Trend":"cup and handle","Num":"None","Text":"a 'cup and handle' pattern in Amazon stock from 1999/07/15 to 1999/09/29"}]
reason: "The 'Amazon stock' in text corresponds to the 'Adj Close' column in data. The 'cup and handle' pattern is characterized by a curved, U-shaped formation (the 'cup') followed by a brief consolidation period represented by a smaller formation (the 'handle'). This pattern is occurred around 1999.07.15 to 1999.09.29 where the cup is from 1999.07.15 to 1999.8.26 and the handle is from 1999.8.27 to 1999.09.29."
"""

rounding_bottom = """
data: [{"Date": "1990/3/1", "Close": 16.8125}, {"Date": "1990/3/2", "Close": 17.0}, {"Date": "1990/3/5", "Close": 17.4375}, {"Date": "1990/3/6", "Close": 17.75}, {"Date": "1990/3/7", "Close": 17.6875}, {"Date": "1990/3/8", "Close": 17.6875}, {"Date": "1990/3/9", "Close": 17.75}, {"Date": "1990/3/12", "Close": 18.1875}, {"Date": "1990/3/13", "Close": 18.9375}, {"Date": "1990/3/14", "Close": 18.9375}, {"Date": "1990/3/15", "Close": 18.5}, {"Date": "1990/3/16", "Close": 18.75}, {"Date": "1990/3/19", "Close": 18.5625}, {"Date": "1990/3/20", "Close": 18.5625}, {"Date": "1990/3/21", "Close": 19.125}, {"Date": "1990/3/22", "Close": 18.5}, {"Date": "1990/3/23", "Close": 18.75}, {"Date": "1990/3/26", "Close": 18.625}, {"Date": "1990/3/27", "Close": 18.625}, {"Date": "1990/3/28", "Close": 18.4375}, {"Date": "1990/3/29", "Close": 18.125}, {"Date": "1990/3/30", "Close": 17.875}, {"Date": "1990/4/2", "Close": 18.125}, {"Date": "1990/4/3", "Close": 18.5}, {"Date": "1990/4/4", "Close": 18.5625}, {"Date": "1990/4/5", "Close": 18.125}, {"Date": "1990/4/6", "Close": 18.125}, {"Date": "1990/4/9", "Close": 17.875}, {"Date": "1990/4/10", "Close": 17.9375}, {"Date": "1990/4/11", "Close": 18.0625}, {"Date": "1990/4/12", "Close": 17.9375}, {"Date": "1990/4/16", "Close": 17.625}, {"Date": "1990/4/17", "Close": 17.5625}, {"Date": "1990/4/18", "Close": 17.5625}, {"Date": "1990/4/19", "Close": 17.5}, {"Date": "1990/4/20", "Close": 17.375}, {"Date": "1990/4/23", "Close": 17.0625}, {"Date": "1990/4/24", "Close": 17.5}, {"Date": "1990/4/25", "Close": 17.75}, {"Date": "1990/4/26", "Close": 17.75}, {"Date": "1990/4/27", "Close": 17.625}, {"Date": "1990/4/30", "Close": 17.6875}, {"Date": "1990/5/1", "Close": 17.6875}, {"Date": "1990/5/2", "Close": 17.625}, {"Date": "1990/5/3", "Close": 17.75}, {"Date": "1990/5/4", "Close": 17.6875}, {"Date": "1990/5/7", "Close": 17.75}, {"Date": "1990/5/8", "Close": 17.75}, {"Date": "1990/5/9", "Close": 17.6875}, {"Date": "1990/5/10", "Close": 17.4375}, {"Date": "1990/5/11", "Close": 17.75}, {"Date": "1990/5/14", "Close": 17.6875}, {"Date": "1990/5/15", "Close": 17.4375}, {"Date": "1990/5/16", "Close": 17.6875}, {"Date": "1990/5/17", "Close": 17.9375}, {"Date": "1990/5/18", "Close": 17.9375}, {"Date": "1990/5/21", "Close": 17.875}, {"Date": "1990/5/22", "Close": 17.5625}, {"Date": "1990/5/23", "Close": 17.3125}, {"Date": "1990/5/24", "Close": 17.3125}, {"Date": "1990/5/25", "Close": 17.25}, {"Date": "1990/5/29", "Close": 17.6875}, {"Date": "1990/5/30", "Close": 18.0625}, {"Date": "1990/5/31", "Close": 17.875}, {"Date": "1990/6/1", "Close": 17.8125}, {"Date": "1990/6/4", "Close": 18.125}, {"Date": "1990/6/5", "Close": 17.9375}, {"Date": "1990/6/6", "Close": 17.75}, {"Date": "1990/6/7", "Close": 17.5}, {"Date": "1990/6/8", "Close": 17.3125}, {"Date": "1990/6/11", "Close": 17.0625}, {"Date": "1990/6/12", "Close": 17.25}, {"Date": "1990/6/13", "Close": 17.0625}, {"Date": "1990/6/14", "Close": 17.375}, {"Date": "1990/6/15", "Close": 17.3125}, {"Date": "1990/6/18", "Close": 17.0}, {"Date": "1990/6/19", "Close": 16.875}, {"Date": "1990/6/20", "Close": 16.8125}, {"Date": "1990/6/21", "Close": 16.25}, {"Date": "1990/6/22", "Close": 15.8125}, {"Date": "1990/6/25", "Close": 15.8125}, {"Date": "1990/6/26", "Close": 15.875}, {"Date": "1990/6/27", "Close": 15.5625}, {"Date": "1990/6/28", "Close": 15.125}, {"Date": "1990/6/29", "Close": 15.0625}, {"Date": "1990/7/2", "Close": 14.875}, {"Date": "1990/7/3", "Close": 14.75}, {"Date": "1990/7/5", "Close": 14.5625}, {"Date": "1990/7/6", "Close": 14.6875}, {"Date": "1990/7/9", "Close": 14.5}, {"Date": "1990/7/10", "Close": 14.1875}, {"Date": "1990/7/11", "Close": 13.9375}, {"Date": "1990/7/12", "Close": 14.25}, {"Date": "1990/7/13", "Close": 14.5}, {"Date": "1990/7/16", "Close": 14.8125}, {"Date": "1990/7/17", "Close": 15.0625}, {"Date": "1990/7/18", "Close": 14.75}, {"Date": "1990/7/19", "Close": 15.0625}, {"Date": "1990/7/20", "Close": 14.5}, {"Date": "1990/7/23", "Close": 14.25}, {"Date": "1990/7/24", "Close": 13.8125}, {"Date": "1990/7/25", "Close": 14.0625}, {"Date": "1990/7/26", "Close": 13.625}, {"Date": "1990/7/27", "Close": 13.5625}, {"Date": "1990/7/30", "Close": 13.875}, {"Date": "1990/7/31", "Close": 13.25}, {"Date": "1990/8/1", "Close": 13.1875}, {"Date": "1990/8/2", "Close": 13.375}, {"Date": "1990/8/3", "Close": 12.5}, {"Date": "1990/8/6", "Close": 12.1875}, {"Date": "1990/8/7", "Close": 12.25}, {"Date": "1990/8/8", "Close": 12.75}, {"Date": "1990/8/9", "Close": 12.75}, {"Date": "1990/8/10", "Close": 12.25}, {"Date": "1990/8/13", "Close": 12.5}, {"Date": "1990/8/14", "Close": 12.6875}, {"Date": "1990/8/15", "Close": 12.9375}, {"Date": "1990/8/16", "Close": 12.4375}, {"Date": "1990/8/17", "Close": 11.8125}, {"Date": "1990/8/20", "Close": 11.625}, {"Date": "1990/8/21", "Close": 11.5}, {"Date": "1990/8/22", "Close": 12.1875}, {"Date": "1990/8/23", "Close": 11.25}, {"Date": "1990/8/24", "Close": 11.6875}, {"Date": "1990/8/27", "Close": 11.8125}, {"Date": "1990/8/28", "Close": 11.75}, {"Date": "1990/8/29", "Close": 11.9375}, {"Date": "1990/8/30", "Close": 12.0625}, {"Date": "1990/8/31", "Close": 11.375}, {"Date": "1990/9/4", "Close": 11.5}, {"Date": "1990/9/5", "Close": 11.5625}, {"Date": "1990/9/6", "Close": 11.125}, {"Date": "1990/9/7", "Close": 10.3125}, {"Date": "1990/9/10", "Close": 10.5}, {"Date": "1990/9/11", "Close": 10.1875}, {"Date": "1990/9/12", "Close": 10.125}, {"Date": "1990/9/13", "Close": 9.9375}, {"Date": "1990/9/14", "Close": 9.9375}, {"Date": "1990/9/17", "Close": 9.5}, {"Date": "1990/9/18", "Close": 9.375}, {"Date": "1990/9/19", "Close": 9.5}, {"Date": "1990/9/20", "Close": 9.4375}, {"Date": "1990/9/21", "Close": 9.3125}, {"Date": "1990/9/24", "Close": 9.0}, {"Date": "1990/9/25", "Close": 8.5}, {"Date": "1990/9/26", "Close": 8.875}, {"Date": "1990/9/27", "Close": 8.375}, {"Date": "1990/9/28", "Close": 8.5}, {"Date": "1990/10/1", "Close": 8.5625}, {"Date": "1990/10/2", "Close": 8.375}, {"Date": "1990/10/3", "Close": 8.4375}, {"Date": "1990/10/4", "Close": 8.625}, {"Date": "1990/10/5", "Close": 8.5625}, {"Date": "1990/10/8", "Close": 8.4375}, {"Date": "1990/10/9", "Close": 8.125}, {"Date": "1990/10/10", "Close": 8.1875}, {"Date": "1990/10/11", "Close": 8.25}, {"Date": "1990/10/12", "Close": 8.125}, {"Date": "1990/10/15", "Close": 7.5625}, {"Date": "1990/10/16", "Close": 7.625}, {"Date": "1990/10/17", "Close": 8.0625}, {"Date": "1990/10/18", "Close": 8.0625}, {"Date": "1990/10/19", "Close": 8.0625}, {"Date": "1990/10/22", "Close": 7.875}, {"Date": "1990/10/23", "Close": 8.0}, {"Date": "1990/10/24", "Close": 8.25}, {"Date": "1990/10/25", "Close": 8.0}, {"Date": "1990/10/26", "Close": 7.8125}, {"Date": "1990/10/29", "Close": 7.75}, {"Date": "1990/10/30", "Close": 7.8125}, {"Date": "1990/10/31", "Close": 7.625}, {"Date": "1990/11/1", "Close": 7.5625}, {"Date": "1990/11/2", "Close": 7.375}, {"Date": "1990/11/5", "Close": 7.25}, {"Date": "1990/11/6", "Close": 7.625}, {"Date": "1990/11/7", "Close": 7.4375}, {"Date": "1990/11/8", "Close": 7.375}, {"Date": "1990/11/9", "Close": 6.75}, {"Date": "1990/11/12", "Close": 7.0}, {"Date": "1990/11/13", "Close": 7.1875}, {"Date": "1990/11/14", "Close": 7.625}, {"Date": "1990/11/15", "Close": 7.75}, {"Date": "1990/11/16", "Close": 7.875}, {"Date": "1990/11/19", "Close": 7.875}, {"Date": "1990/11/20", "Close": 7.75}, {"Date": "1990/11/21", "Close": 7.8125}, {"Date": "1990/11/23", "Close": 7.8125}, {"Date": "1990/11/26", "Close": 7.625}, {"Date": "1990/11/27", "Close": 7.75}, {"Date": "1990/11/28", "Close": 8.1875}, {"Date": "1990/11/29", "Close": 8.0625}, {"Date": "1990/11/30", "Close": 8.0}, {"Date": "1990/12/3", "Close": 7.9375}, {"Date": "1990/12/4", "Close": 7.9375}, {"Date": "1990/12/5", "Close": 8.0}, {"Date": "1990/12/6", "Close": 7.9375}, {"Date": "1990/12/7", "Close": 8.125}, {"Date": "1990/12/10", "Close": 8.125}, {"Date": "1990/12/11", "Close": 8.625}, {"Date": "1990/12/12", "Close": 8.75}, {"Date": "1990/12/13", "Close": 8.625}, {"Date": "1990/12/14", "Close": 8.5}, {"Date": "1990/12/17", "Close": 8.375}, {"Date": "1990/12/18", "Close": 8.375}, {"Date": "1990/12/19", "Close": 8.75}, {"Date": "1990/12/20", "Close": 8.75}, {"Date": "1990/12/21", "Close": 8.5625}, {"Date": "1990/12/24", "Close": 8.6875}, {"Date": "1990/12/26", "Close": 9.0625}, {"Date": "1990/12/27", "Close": 9.375}, {"Date": "1990/12/28", "Close": 9.5625}, {"Date": "1990/12/31", "Close": 9.4375}, {"Date": "1991/1/2", "Close": 9.5}, {"Date": "1991/1/3", "Close": 9.0625}, {"Date": "1991/1/4", "Close": 8.8125}, {"Date": "1991/1/7", "Close": 8.6875}, {"Date": "1991/1/8", "Close": 8.8125}, {"Date": "1991/1/9", "Close": 8.625}, {"Date": "1991/1/10", "Close": 8.6875}, {"Date": "1991/1/11", "Close": 9.0625}, {"Date": "1991/1/14", "Close": 8.75}, {"Date": "1991/1/15", "Close": 8.75}, {"Date": "1991/1/16", "Close": 8.75}, {"Date": "1991/1/17", "Close": 9.25}, {"Date": "1991/1/18", "Close": 9.375}, {"Date": "1991/1/21", "Close": 9.25}, {"Date": "1991/1/22", "Close": 9.25}, {"Date": "1991/1/23", "Close": 9.5}, {"Date": "1991/1/24", "Close": 9.8125}, {"Date": "1991/1/25", "Close": 9.5625}, {"Date": "1991/1/28", "Close": 9.625}, {"Date": "1991/1/29", "Close": 9.8125}, {"Date": "1991/1/30", "Close": 10.3125}, {"Date": "1991/1/31", "Close": 10.125}, {"Date": "1991/2/1", "Close": 10.1875}, {"Date": "1991/2/4", "Close": 10.5}, {"Date": "1991/2/5", "Close": 10.3125}, {"Date": "1991/2/6", "Close": 9.9375}, {"Date": "1991/2/7", "Close": 9.375}, {"Date": "1991/2/8", "Close": 9.375}, {"Date": "1991/2/11", "Close": 9.6875}, {"Date": "1991/2/12", "Close": 9.5625}, {"Date": "1991/2/13", "Close": 9.8125}, {"Date": "1991/2/14", "Close": 9.8125}, {"Date": "1991/2/15", "Close": 9.9375}, {"Date": "1991/2/19", "Close": 10.0}, {"Date": "1991/2/20", "Close": 10.0}, {"Date": "1991/2/21", "Close": 10.0625}, {"Date": "1991/2/22", "Close": 10.25}, {"Date": "1991/2/25", "Close": 10.25}, {"Date": "1991/2/26", "Close": 10.1875}, {"Date": "1991/2/27", "Close": 10.375}, {"Date": "1991/2/28", "Close": 10.3125}, {"Date": "1991/3/1", "Close": 10.5625}, {"Date": "1991/3/4", "Close": 11.3125}, {"Date": "1991/3/5", "Close": 11.8125}, {"Date": "1991/3/6", "Close": 11.8125}, {"Date": "1991/3/7", "Close": 11.9375}, {"Date": "1991/3/8", "Close": 12.0625}, {"Date": "1991/3/11", "Close": 11.875}, {"Date": "1991/3/12", "Close": 11.4375}, {"Date": "1991/3/13", "Close": 11.4375}, {"Date": "1991/3/14", "Close": 11.25}, {"Date": "1991/3/15", "Close": 11.25}, {"Date": "1991/3/18", "Close": 11.125}, {"Date": "1991/3/19", "Close": 10.9375}, {"Date": "1991/3/20", "Close": 10.9375}, {"Date": "1991/3/21", "Close": 10.9375}, {"Date": "1991/3/22", "Close": 11.0625}, {"Date": "1991/3/25", "Close": 10.25}, {"Date": "1991/3/26", "Close": 10.375}, {"Date": "1991/3/27", "Close": 11.4375}, {"Date": "1991/3/28", "Close": 11.8125}, {"Date": "1991/4/1", "Close": 11.6875}, {"Date": "1991/4/2", "Close": 12.0625}, {"Date": "1991/4/3", "Close": 11.875}, {"Date": "1991/4/4", "Close": 11.6875}, {"Date": "1991/4/5", "Close": 11.5625}, {"Date": "1991/4/8", "Close": 11.625}, {"Date": "1991/4/9", "Close": 11.1875}, {"Date": "1991/4/10", "Close": 11.1875}, {"Date": "1991/4/11", "Close": 11.25}, {"Date": "1991/4/12", "Close": 11.4375}, {"Date": "1991/4/15", "Close": 11.5625}, {"Date": "1991/4/16", "Close": 11.375}, {"Date": "1991/4/17", "Close": 11.3125}, {"Date": "1991/4/18", "Close": 11.25}, {"Date": "1991/4/19", "Close": 11.3125}, {"Date": "1991/4/22", "Close": 10.875}, {"Date": "1991/4/23", "Close": 10.5}, {"Date": "1991/4/24", "Close": 10.75}, {"Date": "1991/4/25", "Close": 10.5625}, {"Date": "1991/4/26", "Close": 11.0}, {"Date": "1991/4/29", "Close": 10.8125}, {"Date": "1991/4/30", "Close": 10.625}, {"Date": "1991/5/1", "Close": 10.9375}, {"Date": "1991/5/2", "Close": 10.75}, {"Date": "1991/5/3", "Close": 10.9375}, {"Date": "1991/5/6", "Close": 11.3125}, {"Date": "1991/5/7", "Close": 11.0}, {"Date": "1991/5/8", "Close": 11.3125}, {"Date": "1991/5/9", "Close": 11.4375}, {"Date": "1991/5/10", "Close": 11.4375}, {"Date": "1991/5/13", "Close": 11.5625}, {"Date": "1991/5/14", "Close": 11.3125}, {"Date": "1991/5/15", "Close": 11.25}, {"Date": "1991/5/16", "Close": 11.4375}, {"Date": "1991/5/17", "Close": 11.4375}, {"Date": "1991/5/20", "Close": 11.875}, {"Date": "1991/5/21", "Close": 12.25}, {"Date": "1991/5/22", "Close": 12.3125}, {"Date": "1991/5/23", "Close": 12.1875}, {"Date": "1991/5/24", "Close": 12.375}, {"Date": "1991/5/28", "Close": 12.8125}, {"Date": "1991/5/29", "Close": 13.0}, {"Date": "1991/5/30", "Close": 13.0}, {"Date": "1991/5/31", "Close": 13.125}, {"Date": "1991/6/3", "Close": 13.5}, {"Date": "1991/6/4", "Close": 15.0625}, {"Date": "1991/6/5", "Close": 15.6875}, {"Date": "1991/6/6", "Close": 16.0625}, {"Date": "1991/6/7", "Close": 16.625}, {"Date": "1991/6/10", "Close": 16.625}, {"Date": "1991/6/11", "Close": 16.0625}, {"Date": "1991/6/12", "Close": 16.625}, {"Date": "1991/6/13", "Close": 16.5625}, {"Date": "1991/6/14", "Close": 16.75}, {"Date": "1991/6/17", "Close": 17.4375}, {"Date": "1991/6/18", "Close": 17.0}, {"Date": "1991/6/19", "Close": 17.0625}, {"Date": "1991/6/20", "Close": 17.125}, {"Date": "1991/6/21", "Close": 17.125}, {"Date": "1991/6/24", "Close": 16.9375}, {"Date": "1991/6/25", "Close": 16.75}, {"Date": "1991/6/26", "Close": 16.5625}, {"Date": "1991/6/27", "Close": 16.6875}, {"Date": "1991/6/28", "Close": 16.625}, {"Date": "1991/7/1", "Close": 16.875}, {"Date": "1991/7/2", "Close": 16.625}, {"Date": "1991/7/3", "Close": 16.75}, {"Date": "1991/7/5", "Close": 16.8125}, {"Date": "1991/7/8", "Close": 17.1875}, {"Date": "1991/7/9", "Close": 17.1875}, {"Date": "1991/7/10", "Close": 17.8125}, {"Date": "1991/7/11", "Close": 17.625}, {"Date": "1991/7/12", "Close": 18.0}, {"Date": "1991/7/15", "Close": 17.8125}, {"Date": "1991/7/16", "Close": 18.3125}, {"Date": "1991/7/17", "Close": 18.4375}, {"Date": "1991/7/18", "Close": 19.125}, {"Date": "1991/7/19", "Close": 19.4375}, {"Date": "1991/7/22", "Close": 19.125}, {"Date": "1991/7/23", "Close": 18.5}, {"Date": "1991/7/24", "Close": 18.1875}, {"Date": "1991/7/25", "Close": 19.0}, {"Date": "1991/7/26", "Close": 19.0625}, {"Date": "1991/7/29", "Close": 18.8125}, {"Date": "1991/7/30", "Close": 18.75}, {"Date": "1991/7/31", "Close": 19.0625}, {"Date": "1991/8/1", "Close": 18.875}, {"Date": "1991/8/2", "Close": 18.875}, {"Date": "1991/8/5", "Close": 18.625}, {"Date": "1991/8/6", "Close": 19.0}, {"Date": "1991/8/7", "Close": 19.125}, {"Date": "1991/8/8", "Close": 19.375}, {"Date": "1991/8/9", "Close": 19.375}, {"Date": "1991/8/12", "Close": 19.0}, {"Date": "1991/8/13", "Close": 18.3125}, {"Date": "1991/8/14", "Close": 18.5625}, {"Date": "1991/8/15", "Close": 18.3125}, {"Date": "1991/8/16", "Close": 17.875}, {"Date": "1991/8/19", "Close": 17.0625}, {"Date": "1991/8/20", "Close": 17.3125}, {"Date": "1991/8/21", "Close": 18.4375}, {"Date": "1991/8/22", "Close": 18.625}, {"Date": "1991/8/23", "Close": 18.9375}, {"Date": "1991/8/26", "Close": 19.0625}, {"Date": "1991/8/27", "Close": 18.9375}, {"Date": "1991/8/28", "Close": 19.375}, {"Date": "1991/8/29", "Close": 19.1875}, {"Date": "1991/8/30", "Close": 19.125}, {"Date": "1991/9/3", "Close": 19.25}, {"Date": "1991/9/4", "Close": 20.4375}, {"Date": "1991/9/5", "Close": 20.625}, {"Date": "1991/9/6", "Close": 21.0}, {"Date": "1991/9/9", "Close": 21.0625}, {"Date": "1991/9/10", "Close": 20.8125}, {"Date": "1991/9/11", "Close": 21.0}, {"Date": "1991/9/12", "Close": 21.1875}, {"Date": "1991/9/13", "Close": 20.8125}, {"Date": "1991/9/16", "Close": 21.0625}, {"Date": "1991/9/17", "Close": 21.125}, {"Date": "1991/9/18", "Close": 21.25}, {"Date": "1991/9/19", "Close": 21.5}, {"Date": "1991/9/20", "Close": 21.75}, {"Date": "1991/9/23", "Close": 21.375}, {"Date": "1991/9/24", "Close": 21.3125}, {"Date": "1991/9/25", "Close": 21.6875}, {"Date": "1991/9/26", "Close": 21.8125}, {"Date": "1991/9/27", "Close": 21.6875}, {"Date": "1991/9/30", "Close": 21.9375}, {"Date": "1991/10/1", "Close": 21.8125}, {"Date": "1991/10/2", "Close": 22.125}, {"Date": "1991/10/3", "Close": 21.75}, {"Date": "1991/10/4", "Close": 21.5625}, {"Date": "1991/10/7", "Close": 20.9375}, {"Date": "1991/10/8", "Close": 21.5625}, {"Date": "1991/10/9", "Close": 21.9375}, {"Date": "1991/10/10", "Close": 21.9375}, {"Date": "1991/10/11", "Close": 21.9375}, {"Date": "1991/10/14", "Close": 21.9375}, {"Date": "1991/10/15", "Close": 21.8125}, {"Date": "1991/10/16", "Close": 22.375}, {"Date": "1991/10/17", "Close": 22.3125}, {"Date": "1991/10/18", "Close": 22.1875}, {"Date": "1991/10/21", "Close": 22.4375}, {"Date": "1991/10/22", "Close": 22.875}, {"Date": "1991/10/23", "Close": 23.5}, {"Date": "1991/10/24", "Close": 23.25}, {"Date": "1991/10/25", "Close": 23.375}, {"Date": "1991/10/28", "Close": 24.4375}, {"Date": "1991/10/29", "Close": 24.5625}, {"Date": "1991/10/30", "Close": 24.8125}, {"Date": "1991/10/31", "Close": 25.0}, {"Date": "1991/11/1", "Close": 24.8125}, {"Date": "1991/11/4", "Close": 24.875}, {"Date": "1991/11/5", "Close": 25.875}, {"Date": "1991/11/6", "Close": 26.8125}, {"Date": "1991/11/7", "Close": 26.25}, {"Date": "1991/11/8", "Close": 26.25}, {"Date": "1991/11/11", "Close": 25.75}, {"Date": "1991/11/12", "Close": 25.25}, {"Date": "1991/11/13", "Close": 24.6875}, {"Date": "1991/11/14", "Close": 24.6875}, {"Date": "1991/11/15", "Close": 24.125}, {"Date": "1991/11/18", "Close": 24.1875}, {"Date": "1991/11/19", "Close": 23.5}, {"Date": "1991/11/20", "Close": 24.125}, {"Date": "1991/11/21", "Close": 24.4375}, {"Date": "1991/11/22", "Close": 24.875}, {"Date": "1991/11/25", "Close": 24.5}, {"Date": "1991/11/26", "Close": 24.375}, {"Date": "1991/11/27", "Close": 24.25}, {"Date": "1991/11/29", "Close": 23.9375}]
text: ["The stock of Goodyear Tire & Rubber company (GT) suffers a year-long 'rounding bottom' pattern from 1990.6.11 to 1991.6.3."]
result: [{"ObjectName":["The stock of Goodyear Tire & Rubber company (GT)"],"DataName":"Close","Position":[{"Begin":[70,1],"End":[317,1]}],"Trend":"rounding bottom","Num":"None","Text":"The stock of Goodyear Tire & Rubber company (GT) suffers a year-long 'rounding bottom' pattern"}]
reason: "The stock of Goodyear Tire & Rubber company (GT)' in text corresponds to the 'Close' column in data. The 'rounding bottom' takes the shape of a gradual and smooth curve resembling the bottom of a bowl which is from 1990.5.11 to 1991.6.3."
"""

double_top = """
data: [{'Date': '2018/6/27', 'Close': 83.025497}, {'Date': '2018/6/28', 'Close': 85.072502}, {'Date': '2018/6/29', 'Close': 84.989998}, {'Date': '2018/7/2', 'Close': 85.689003}, {'Date': '2018/7/3', 'Close': 84.697998}, {'Date': '2018/7/5', 'Close': 84.986504}, {'Date': '2018/7/6', 'Close': 85.531502}, {'Date': '2018/7/9', 'Close': 86.950996}, {'Date': '2018/7/10', 'Close': 87.153503}, {'Date': '2018/7/11', 'Close': 87.75}, {'Date': '2018/7/12', 'Close': 89.831001}, {'Date': '2018/7/13', 'Close': 90.651497}, {'Date': '2018/7/16', 'Close': 91.124496}, {'Date': '2018/7/17', 'Close': 92.196503}, {'Date': '2018/7/18', 'Close': 92.146004}, {'Date': '2018/7/19', 'Close': 90.648499}, {'Date': '2018/7/20', 'Close': 90.684998}, {'Date': '2018/7/23', 'Close': 90.099998}, {'Date': '2018/7/24', 'Close': 91.461998}, {'Date': '2018/7/25', 'Close': 93.180496}, {'Date': '2018/7/26', 'Close': 90.400002}, {'Date': '2018/7/27', 'Close': 90.863503}, {'Date': '2018/7/30', 'Close': 88.960999}, {'Date': '2018/7/31', 'Close': 88.872002}, {'Date': '2018/8/1', 'Close': 89.858498}, {'Date': '2018/8/2', 'Close': 91.716499}, {'Date': '2018/8/3', 'Close': 91.164497}, {'Date': '2018/8/6', 'Close': 92.387497}, {'Date': '2018/8/7', 'Close': 93.124001}, {'Date': '2018/8/8', 'Close': 94.325996}, {'Date': '2018/8/9', 'Close': 94.926003}, {'Date': '2018/8/10', 'Close': 94.315002}, {'Date': '2018/8/13', 'Close': 94.809998}, {'Date': '2018/8/14', 'Close': 95.982498}, {'Date': '2018/8/15', 'Close': 94.130997}, {'Date': '2018/8/16', 'Close': 94.325996}, {'Date': '2018/8/17', 'Close': 94.111}, {'Date': '2018/8/20', 'Close': 93.835503}, {'Date': '2018/8/21', 'Close': 94.170998}, {'Date': '2018/8/22', 'Close': 95.245003}, {'Date': '2018/8/23', 'Close': 95.144997}, {'Date': '2018/8/24', 'Close': 95.269501}, {'Date': '2018/8/27', 'Close': 96.384003}, {'Date': '2018/8/28', 'Close': 96.640999}, {'Date': '2018/8/29', 'Close': 99.904999}, {'Date': '2018/8/30', 'Close': 100.119003}, {'Date': '2018/8/31', 'Close': 100.635498}, {'Date': '2018/9/4', 'Close': 101.975502}, {'Date': '2018/9/5', 'Close': 101.740997}, {'Date': '2018/9/6', 'Close': 99.915497}, {'Date': '2018/9/7', 'Close': 98.6035}, {'Date': '2018/9/10', 'Close': 97.9505}, {'Date': '2018/9/11', 'Close': 97.357498}, {'Date': '2018/9/12', 'Close': 96.93}, {'Date': '2018/9/13', 'Close': 96.7935}, {'Date': '2018/9/14', 'Close': 96.809499}, {'Date': '2018/9/17', 'Close': 96.901497}, {'Date': '2018/9/18', 'Close': 97.052498}, {'Date': '2018/9/19', 'Close': 96.320999}, {'Date': '2018/9/20', 'Close': 97.214996}, {'Date': '2018/9/21', 'Close': 95.750504}, {'Date': '2018/9/24', 'Close': 96.718002}, {'Date': '2018/9/25', 'Close': 98.727501}, {'Date': '2018/9/26', 'Close': 98.7425}, {'Date': '2018/9/27', 'Close': 100.649002}, {'Date': '2018/9/28', 'Close': 100.150002}, {'Date': '2018/10/1', 'Close': 100.218002}, {'Date': '2018/10/2', 'Close': 98.565498}, {'Date': '2018/10/3', 'Close': 97.638}, {'Date': '2018/10/4', 'Close': 95.471001}, {'Date': '2018/10/5', 'Close': 94.482498}, {'Date': '2018/10/8', 'Close': 93.221001}, {'Date': '2018/10/9', 'Close': 93.515999}, {'Date': '2018/10/10', 'Close': 87.762497}, {'Date': '2018/10/11', 'Close': 85.968002}, {'Date': '2018/10/12', 'Close': 89.430496}, {'Date': '2018/10/15', 'Close': 88.047501}, {'Date': '2018/10/16', 'Close': 90.998001}, {'Date': '2018/10/17', 'Close': 91.586502}, {'Date': '2018/10/18', 'Close': 88.536003}, {'Date': '2018/10/19', 'Close': 88.2015}, {'Date': '2018/10/22', 'Close': 89.464996}, {'Date': '2018/10/23', 'Close': 88.434998}, {'Date': '2018/10/24', 'Close': 83.209999}, {'Date': '2018/10/25', 'Close': 89.108498}, {'Date': '2018/10/26', 'Close': 82.140503}, {'Date': '2018/10/29', 'Close': 76.944}, {'Date': '2018/10/30', 'Close': 76.521004}, {'Date': '2018/10/31', 'Close': 79.900497}, {'Date': '2018/11/1', 'Close': 83.276497}, {'Date': '2018/11/2', 'Close': 83.276497}, {'Date': '2018/11/5', 'Close': 81.389999}, {'Date': '2018/11/6', 'Close': 82.140503}, {'Date': '2018/11/7', 'Close': 87.774498}, {'Date': '2018/11/8', 'Close': 87.745499}, {'Date': '2018/11/9', 'Close': 85.621498}, {'Date': '2018/11/12', 'Close': 81.842499}, {'Date': '2018/11/13', 'Close': 81.558502}, {'Date': '2018/11/14', 'Close': 79.9505}, {'Date': '2018/11/15', 'Close': 80.972}, {'Date': '2018/11/16', 'Close': 79.670502}, {'Date': '2018/11/19', 'Close': 75.614502}, {'Date': '2018/11/20', 'Close': 74.773003}]
text: ["The chart of Amazon.com Inc. (AMZN) shows a double top pattern that formed in the stock between September and October 2018. After the pattern appears, shares plunges another 31%."]
result: [{"ObjectName":["Amazon.com Inc. (AMZN)"],"DataName":"Close","BeginIndex":[42,1],"EndIndex":[69,1],"Trend":"double top","Num":"None", "Text":"The chart of Amazon.com Inc. (AMZN) shows a double top pattern that formed in the stock between September and October 2018"}, 
        {"ObjectName":["Amazon.com Inc. (AMZN)"],"DataName":"Close","BeginIndex":[70,1],"EndIndex":[102,1],"Trend":"plunges","Num":"31%","Text":"shares plunges another 31%"}]
reason: "The 'Amazon.com Inc. (AMZN)  corresponds to the column 'Close' in data. The "Double Top" pattern is characterized by two distinct peaks and separated by a trough. This pattern often signifies a potential reversal from an uptrend to a downtrend, suggesting a shift in investor sentiment. The double top pattern in this data is from 2018.8.27 to 2018.10.4, and the two peaks exist at around 2018.09.05 and 2018.09.28. After this pattern, the value plunges from 2018.10.05 to 2018.11.20."
"""

triple_top = """
data: [{'time': '2010/3/10', 'price': 96.4}, {'time': '2010/3/11', 'price': 98.8}, {'time': '2010/3/12', 'price': 101.23}, {'time': '2010/3/13', 'price': 98.6}, {'time': '2010/3/14', 'price': 96.5}, {'time': '2010/3/15', 'price': 94.3}, {'time': '2010/3/16', 'price': 98.023}, {'time': '2010/3/17', 'price': 97.25}, {'time': '2010/3/18', 'price': 98.089}, {'time': '2010/3/19', 'price': 98.144}, {'time': '2010/3/20', 'price': 98.899}, {'time': '2010/3/21', 'price': 100.001}, {'time': '2010/3/22', 'price': 102.2}, {'time': '2010/3/23', 'price': 103.7}, {'time': '2010/3/24', 'price': 102.46}, {'time': '2010/3/25', 'price': 99.46}, {'time': '2010/3/26', 'price': 97.01}, {'time': '2010/3/27', 'price': 99.14}, {'time': '2010/3/28', 'price': 100.74}, {'time': '2010/3/29', 'price': 104.58}, {'time': '2010/3/30', 'price': 105.31}, {'time': '2010/3/31', 'price': 107.07}, {'time': '2010/4/1', 'price': 110.13}, {'time': '2010/4/2', 'price': 111.26}, {'time': '2010/4/3', 'price': 113.0}, {'time': '2010/4/4', 'price': 115.8}, {'time': '2010/4/5', 'price': 116.6}, {'time': '2010/4/6', 'price': 117.0}, {'time': '2010/4/7', 'price': 116.7}, {'time': '2010/4/8', 'price': 116.5}, {'time': '2010/4/9', 'price': 116.6}, {'time': '2010/4/10', 'price': 116.7}, {'time': '2010/4/11', 'price': 116.0}, {'time': '2010/4/12', 'price': 115.0}, {'time': '2010/4/13', 'price': 112.9}, {'time': '2010/4/14', 'price': 112.7}, {'time': '2010/4/15', 'price': 113.0}, {'time': '2010/4/16', 'price': 113.2}, {'time': '2010/4/17', 'price': 114.6}, {'time': '2010/4/18', 'price': 115.5}, {'time': '2010/4/19', 'price': 117.8}, {'time': '2010/4/20', 'price': 117.6}, {'time': '2010/4/21', 'price': 116.2}, {'time': '2010/4/22', 'price': 115.2}, {'time': '2010/4/23', 'price': 114.4}, {'time': '2010/4/24', 'price': 113.0}, {'time': '2010/4/25', 'price': 112.8}, {'time': '2010/4/26', 'price': 113.8}, {'time': '2010/4/27', 'price': 116.0}, {'time': '2010/4/28', 'price': 115.5}, {'time': '2010/4/29', 'price': 114.9}, {'time': '2010/4/30', 'price': 114.7}, {'time': '2010/5/1', 'price': 112.2}, {'time': '2010/5/2', 'price': 111.4}, {'time': '2010/5/3', 'price': 110.8}, {'time': '2010/5/4', 'price': 110.9}, {'time': '2010/5/5', 'price': 109.9}, {'time': '2010/5/6', 'price': 106.8}, {'time': '2010/5/7', 'price': 105.5}, {'time': '2010/5/8', 'price': 104.6}, {'time': '2010/5/9', 'price': 106.5}, {'time': '2010/5/10', 'price': 110.5}, {'time': '2010/5/11', 'price': 111.0}, {'time': '2010/5/12', 'price': 110.6}, {'time': '2010/5/13', 'price': 110.2}, {'time': '2010/5/14', 'price': 104.9}, {'time': '2010/5/15', 'price': 105.8}, {'time': '2010/5/16', 'price': 106.6}, {'time': '2010/5/17', 'price': 106.0}, {'time': '2010/5/18', 'price': 105.6}, {'time': '2010/5/19', 'price': 106.0}, {'time': '2010/5/20', 'price': 105.0}, {'time': '2010/5/21', 'price': 106.6}, {'time': '2010/5/22', 'price': 106.9}, {'time': '2010/5/23', 'price': 107.7}, {'time': '2010/5/24', 'price': 110.3}, {'time': '2010/5/25', 'price': 111.5}, {'time': '2010/5/26', 'price': 110.4}, {'time': '2010/5/27', 'price': 107.0}, {'time': '2010/5/28', 'price': 105.5}, {'time': '2010/5/29', 'price': 103.0}]
text: ["In Amazon stock moving averages, 'triple top' pattern happens from 2010/04/01 to 2010/05/05."]
result: [{"ObjectName":["Amazon stock moving averages"],"DataName":"price","Position":[{"Begin":[22,1],"End":[56,1]}],"Trend":"triple top","Num":"None","Text":"The "triple top" pattern happens from 2010/04/01 to 2010/05/05"}]
reason: "The 'Amazon stock moving averages' corresponds to the column 'price' in data. The 'triple top' pattern has three discernible peaks at approximatrely the same level, separated by troughs. The pattern in this data is from 2010.04.01 to 2010.05.05 and the three peaks are at about 2010.04.06, 2010.04.18 and 2010.04.27."
"""



@app.route('/api/test/postQuery/', methods=['POST'])
def post_query():
    params = request.json
    file_path = '{}/output.json'.format(FILE_ABS_PATH)
    data = read_json(file_path)
    print(data)
    return jsonify(data)


# 判断x轴属于什么类型，{time, category,linear}
def determine_x_axis_type(input_data):
    x_values = next(iter(input_data[0].values()))
    # print(x_values)
    # if list(input_data[0].keys())[0] == 'time' or list(input_data[0].keys())[0] == 'Time':
    #     return 'time'
    # 检查是否包含数字和日期
    # return 'category'
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
    # return 2
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
                "r": 228, "g": 148, "b": 68, "a": 1
            }, {
                "r": 168, "g": 124, "b": 159, "a": 1
            }, {
                "r": 133, "g": 182, "b": 178, "a": 1
            },
            {
                "r": 106, "g": 159, "b": 88, "a": 1
            }]
    cnt = 0
    for y in y_attribute:
        result['chartColor'][y] = color_hunt[cnt]
        cnt += 1
    print(result)
    return result



if __name__ == '__main__':
    app.run(debug=True)