'''
Description: 
Author: Qing Shi
Date: 2023-09-01 22:43:55
LastEditors: Qing Shi
LastEditTime: 2023-09-01 22:43:56
'''
import json
import numpy as np
from count_position import find_position

# user_info: a string
user_info = """data: [{'Time': 'Aug 2022', 'Food inflation': 6.1}, 
                        {'Time': 'Sep 2022', 'Food inflation': 8.8}, 
                        {'Time': 'Oct 2022', 'Food inflation': 7.0}, 
                        {'Time': 'Nov 2022', 'Food inflation': 3.7}, 
                        {'Time': 'Dec 2022', 'Food inflation': 4.8}, 
                        {'Time': 'Jan 2023', 'Food inflation': 6.2}, 
                        {'Time': 'Feb 2023', 'Food inflation': 2.6}, 
                        {'Time': 'Mar 2023', 'Food inflation': 2.4}, 
                        {'Time': 'Apr 2023', 'Food inflation': 0.4}, 
                        {'Time': 'May 2023', 'Food inflation': 1.0}, 
                        {'Time': 'Jun 2023', 'Food inflation': 2.3}, 
                        {'Time': 'Jul 2023', 'Food inflation': -1.7}]
                text: ["Food prices in China declined by 1.7 percent year-on-year in July 2023, reversing from a 2.3 percent rise in the prior month while pointing to the first drop since March 2022."]
                label: "start"
            """
# result from gpt: a string 
result = "result: [{\"ObjectName\":[\"Food inflation\"],\"Position\":[{\"Begin\":[11,1],\"End\":[11,1]}],\"Trend\":\"declined\",\"Num\":[-1.7],\"Text\":\"Food prices in China declined by 1.7 percent year-on-year in July 2023\"},\n        {\"ObjectName\":[\"Food inflation\"],\"Position\":[{\"Begin\":[10,1],\"End\":[10,1]}],\"Trend\":\"None\",\"Num\":[2.3],\"Text\":\"a 2.3 percent rise in the prior month\"}]\n"

test_info = """data: [{"Time":"2022-Jul","Banks Balance Sheet (CNY Billion)":"679"},{"Time":"2022-Aug","Banks Balance Sheet (CNY Billion)":"1250"},{"Time":"2022-Sep","Banks Balance Sheet (CNY Billion)":"2470"},{"Time":"2022-Oct","Banks Balance Sheet (CNY Billion)":"615.2"},{"Time":"2022-Nov","Banks Balance Sheet (CNY Billion)":"1210"},{"Time":"2022-Dec","Banks Balance Sheet (CNY Billion)":"1400"},{"Time":"2023-Jan","Banks Balance Sheet (CNY Billion)":"4900"},{"Time":"2023-Feb","Banks Balance Sheet (CNY Billion)":"1810"},{"Time":"2023-Mar","Banks Balance Sheet (CNY Billion)":"3890"},{"Time":"2023-Apr","Banks Balance Sheet (CNY Billion)":"718.8"},{"Time":"2023-May","Banks Balance Sheet (CNY Billion)":"1360"},{"Time":"2023-Jun","Banks Balance Sheet (CNY Billion)":"3050"},{"Time":"2023-Jul","Banks Balance Sheet (CNY Billion)":"345.9"}]text: ["China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter."]label: "start"
"""

# 经过转换以后的convert_result是如下格式
# convert_result = [{"ObjectName":["Food inflation"],"Position":[{"Begin":[11,1],"End":[11,1]}],"Trend":"declined","Num": "None","Text":"Food prices in China declined by 1.7 percent year-on-year in July 2023"},
                # {"ObjectName":["Food inflation"],"Position":[{"Begin":[6,1],"End":[6,1]}],"Trend":"None","Num":[2.3],"Text":"a 2.3 percent rise in the prior month"}]
def transform_conversation_info(conversation_info):
    transformed = []
        
    for convert_item in conversation_info:
        trend = convert_item['Trend']
        trend_position = convert_item['TrendPosition']
        num = convert_item['Num']
        num_position = convert_item['NumPosition']
        object_name = convert_item['ObjectName']
        object_pos = convert_item['ObjectPosition']

        if trend:
            transformed.append({
                "Position": trend_position,
                "Text": trend,
                "OverTag": 1,
                "Type": "Trend"
            })

        if num and num_position[0] is not None:
            for i, n in enumerate(num):
                if object_pos and num_position and num_position[i]:
                    if object_pos != [None] and num_position[i][0] > object_pos[0][0] and num_position[i][1] < object_pos[0][1]:
                        overtag = 2
                    else: 
                        overtag = 1
                else:
                    overtag = 1

                transformed.append({
                    "Position": num_position[i],
                    "Text": str(n),
                    "OverTag": overtag,
                    "Type": "Num"
                })

        if object_name[0]:
            if num and num_position[0] is not None:
                if object_pos != [None] and num_position and num_position[0][0] > object_pos[0][0] and num_position[0][1] < object_pos[0][1]:

                    object_pos_1 = [object_pos[0][0], num_position[0][0] - 1]
                    object_pos_2 = [num_position[0][1] + 1, object_pos[0][1]]

                    transformed.append({
                        "Position": [object_pos_1,object_pos_2],
                        "Text": object_name[0],
                        "OverTag": 0,
                        "Type": "ObjectName"
                    })
                else:
                    transformed.append({
                    "Position": object_pos,
                    "Text": object_name[0],
                    "OverTag": 0,
                    "Type": "ObjectName"
                    })

            else:
                print('1')
                transformed.append({
                    "Position": object_pos,
                    "Text": object_name[0],
                    "OverTag": 0,
                    "Type": "ObjectName"
                })

    return transformed

def transform_result(result):
    transformed = []
    for item in result:
        conversation_info = item['ConversationInfo']
        transformed_conversation = transform_conversation_info(conversation_info)

        item_copy = item.copy()
        item_copy['ConversationInfo'] = transformed_conversation
        transformed.append(item_copy)
    return transformed

def result_to_frontend(user_info, result):
    # print(user_info.find("[\""))
    # print(user_info.find("\"]"))
    # print(user_info[user_info.find("[\""):user_info.find("\"]")+2])
    # print(json.loads(user_info[user_info.find("[\""):user_info.find("\"]")+2]))
          
    # user_info_data = json.loads(user_info[len("data")+2:user_info.find("text")].replace("\'", "\"")) # 从user_info中提取data，转成list
    user_info_data = json.loads(user_info[user_info.find("[{"):user_info.find("}]")+2].replace("\'", "\"")) # 从user_info中提取data，转成list
    user_info_text = json.loads(user_info[user_info.find("[\""):user_info.find("\"]")+2])[0] # 从user_info中提取text，转成string
    convert_result = json.loads(result[result.find("[{"):]) # 把gpt返回的string转成list
    # print(user_info_data)
    # print(convert_result)
    # print(user_info_text)
    
    result_frontend = []
    for index, convert_result_item in enumerate(convert_result):
        # print(convert_result_item)
        
        # 处理position
        # 原来的"Position":[{"Begin":[1,1],"End":[1,1]}]先row后col
        # 处理后的[{"Begin":["Mini- and subcompact size",6],"End":["Mini- and subcompact size",6]}] 先col_name后row
        position = []
        for p in convert_result_item['Position']:
            # print(p)
            begin_row = p["Begin"][0]
            begin_col = p["Begin"][1]
            begin_col_name = list(user_info_data[0].keys())[begin_col]
            end_row = p["End"][0]
            end_col = p["End"][1]
            end_col_name = list(user_info_data[0].keys())[end_col]
            position.append({"Begin":[begin_col_name, begin_row],"End":[end_col_name, end_row]})
        # print("position", position)


        mean, max, min = line_calculate(user_info_data, position[0]["Begin"], position[-1]["End"])

        # 0828 the new one:
        # "ConversationInfo":
        # [{
        #     "Position": [],
        #     "Text": "a",
        #     "OverTag": 0 background, 1 underline, 2 both,
        #     "Type": "ObjectName"/"Trend"/"Num"
        # },{}]

        # [{
        #     "Position": [21,28],
        #     "Text": "declined",
        #     "OverTag": 0
        #     "Type": "Trend"
        # },
        # {
        #     "Position": [None],
        #     "Text": "-1.7",
        #     "OverTag": 0
        #     "Type": "Num"
        # },
        # {
        #     "Position": [None],
        #     "Text": "Foof inflation",
        #     "OverTag": 0
        #     "Type": "OnjectName"
        # }
        # ]

        result_frontend.append({
            "OriginText": user_info_text,
            "Position": position,
            "ConversationInfo":[{
                "Trend": convert_result_item['Trend'],
                "TrendPosition": find_position(user_info_text, convert_result_item['Trend']),
                "Num": convert_result_item['Num'],
                "NumPosition": [find_position(user_info_text, str(i)) for i in convert_result_item['Num']] if convert_result_item['Num'] != "None" else None,  
                "ObjectName": convert_result_item['ObjectName'],
                "ObjectPosition": [find_position(user_info_text, i) for i in convert_result_item['ObjectName']]
            }],
            "GraphicalOverlay":[{
                "Text": convert_result_item['Text'],
                "Label": convert_result_item['Num'] if convert_result_item['Num'] else convert_result_item['Trend'], # 有num选num，无num选trend
                "Marker": position,
                "Line": {
                    "Begin": position[0]["Begin"],
                    "End": position[-1]["End"],
                    "mean": mean, 
                    "max" : max, 
                    "min" : min  
                }
            }]
        })

    return result_frontend

def line_calculate(user_info_data, begin, end):
    all_num = []
    if begin[0] == end[0]: # if同一列
        for i in range(begin[1],end[1]+1): # 所有行
            all_num.append(user_info_data[i][begin[0]])
    else: # if 多个object 不同列
        for i in range(begin[1],end[1]+1):
            all_num.append(user_info_data[i][begin[0]])
            all_num.append(user_info_data[i][end[0]])
    mean_num = np.mean(all_num)   
    max_num = max(all_num)
    min_num = min(all_num)

    return mean_num, max_num, min_num

if __name__ == '__main__':
    result_frontend = result_to_frontend(user_info, result)
    print(result_frontend)
    # format_new_result = transform_result(result_frontend)
#     example = [{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
# 'Position': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 
# 'ConversationInfo': 
#     [{'Trend': 'None', 
#     'TrendPosition': None, 
#     'Num': [15.73], 
#     'NumPosition': [[273, 277]], 
# 'ObjectName': ['a record CNY 15.73 trillion loans'], 'ObjectPosition': [[260, 292]]}],
# 'GraphicalOverlay': 
#     [{'Text': 'The value is also much lower than CNY 679 billion a year earlier', 
#     'Label': [679], 
#     'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 
#     'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12], 
#     'mean': 345.9, 
#     'max': 345.9, 
#     'min': 345.9}}]}]
    
#     format_new_result = transform_result(example)
#     print(format_new_result)


