# question_2,question_3...后续对话，前端传给后端的格式如下
# 只有data+text+result+reason需要继承给后续问答，question_2和answer_2不需要继承给question_3
"""data: [{'Position':'United Kingdom','Billions of dollars':'59.9'},
	    {'Position':'Netherlands','Billions of dollars':'43.1'},
        {'Position':'France','Billions of dollars':'35.3'},
	    {'Position':'Canada','Billions of dollars': '30'},
        {'Position':'Japan','Billions of dollars':'29.6'}]
text: ["Investment by British investors accounted for 18 percent of new foreign direct investment expenditures. The Netherlands ($43.1 billion) was the second-largest investing country, followed by France ($35.3 billion)."]
result: [{"ObjectName":["Netherlands"],"DataName":"Billions of dollars","Position":[{"Begin":[1,1],"End":[1,1]}],"Trend":"None","Num":[43.1],"Text":"The Netherlands ($43.1 billion)"},{"ObjectName":["France"],"DataName":"Billions of dollars","Position":[{"Begin":[2,1],"End":[2,1]}],"Trend":"None","Num":[35.3],"Text":"France ($35.3 billion)"}]
reason: "The corresponding value for object "Netherlands" is "43.1", and its shortest descriptive phrase is "The Netherlands ($43.1 billion)". The corresponding value for object "France" is "35.3" and its shortest descriptive phrase is "France ($35.3 billion)""    
question: ["This is a question"]                
label: "following"
"""


# 前端传来的数据：
"""data: [{'Time': 'Jul 2022', 'Banks Balance Sheet (CNY Billion)': 679.0}, 
                        {'Time': 'Aug 2022', 'Banks Balance Sheet (CNY Billion)': 1250.0}, 
                        {'Time': 'Sep 2022', 'Banks Balance Sheet (CNY Billion)': 2470.0}, 
                        {'Time': 'Oct 2022', 'Banks Balance Sheet (CNY Billion)': 615.2}, 
                        {'Time': 'Nov 2022', 'Banks Balance Sheet (CNY Billion)': 1210.0}, 
                        {'Time': 'Dec 2022', 'Banks Balance Sheet (CNY Billion)': 1400.0}, 
                        {'Time': 'Jan 2023', 'Banks Balance Sheet (CNY Billion)': 4900.0}, 
                        {'Time': 'Feb 2023', 'Banks Balance Sheet (CNY Billion)': 1810.0}, 
                        {'Time': 'Mar 2023', 'Banks Balance Sheet (CNY Billion)': 3890.0}, 
                        {'Time': 'Apr 2023', 'Banks Balance Sheet (CNY Billion)': 718.8}, 
                        {'Time': 'May 2023', 'Banks Balance Sheet (CNY Billion)': 1360.0}, 
                        {'Time': 'Jun 2023', 'Banks Balance Sheet (CNY Billion)': 3050.0}, 
                        {'Time': 'Jul 2023', 'Banks Balance Sheet (CNY Billion)': 345.9}]
                text: ["China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter."]
                label: "start"
            """

# 后端返回的数据：
[{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 
'ConversationInfo': 
    [{'Trend': 'None', 
    'TrendPosition': None, 
    'Num': [345.9], 
    'NumPosition': [[27, 31]], 
    'ObjectName': ["China's banks"], 
    'ObjectPosition': [[0, 12]]}], 
'GraphicalOverlay': 
    [{'Text': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023", 
    'Label': [345.9], 
    'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 
    'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12], 
    'mean': 345.9, 
    'max': 345.9, 
    'min': 345.9}}]}, 
{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 
'ConversationInfo': 
    [{'Trend': 'None', 
    'TrendPosition': None, 
    'Num': [679], 
    'NumPosition': [[196, 198]], 
    'ObjectName': ['a year earlier'], 
    'ObjectPosition': [[208, 221]]}], 
'GraphicalOverlay': 
    [{'Text': 'The value is also much lower than CNY 679 billion a year earlier', 
    'Label': [679], 
    'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 
    'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12], 
    'mean': 345.9, 
    'max': 345.9, 
    'min': 345.9}}]}, 
{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 
'ConversationInfo': 
    [{'Trend': 'None', 
    'TrendPosition': None, 
    'Num': [3.05], 
    'NumPosition': [None], 
    'ObjectName': ['in June'], 
    'ObjectPosition': [[245, 251]]}], 
'GraphicalOverlay': 
    [{'Text': 'CNY 3.05 trillion in June', 
    'Label': [3050], 
    'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 
    'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11], 
    'mean': 3050.0, 
    'max': 3050.0, 
    'min': 3050.0}}]}, 
{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 
<!-- 'ConversationInfo': 
    [{'Trend': 'None', 
    'TrendPosition': None, 
    'Num': [15.73], 
    'NumPosition': [[273, 277]], 
'ObjectName': ['a record CNY 15.73 trillion loans'], 'ObjectPosition': [[260, 292]]}],  -->
<!-- 0828改成对应下面的状态： -->
    'ConversationInfo': 
    [{
    "Position": [273,277],
    "Text": "declined",
    "OverTag": 2,
    "Type": "Num"
    },
    <!-- {
    "Position": [[260,272],[278,292]],
    "Text": "a record CNY 15.73 trillion loans",
    "OverTag": 0,
    "Type": "ObjectName"
    }] -->
    {
    "Position": [[260,272]],
    "Text": "a record CNY",
    "OverTag": 0,
    "Type": "ObjectName"
    },
    {
    "Position": [[278,292]],
    "Text": "trillion loans",
    "OverTag": 0,
    "Type": "ObjectName"
    }
    ]
<!-- end -->
'GraphicalOverlay': 
    [{'Text': 'after a record CNY 15.73 trillion loans in the first half of the year', 
    'Label': [15.73], 
    'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 
    'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11], 
    'mean': 3050.0, 
    'max': 3050.0, 
    'min': 3050.0}}]}]

# 0828 对应后端传来的数据：
[{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': 
    [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 'ConversationInfo': 
    [{'Position': None, 'Text': 'None', 'OverTag': 1, 'Type': 'Trend'}, {'Position': [27, 31], 'Text': '345.9', 'OverTag': 1, 'Type': 'Num'}], 
'GraphicalOverlay': 
    [{'Text': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023", 'Label': [345.9], 'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12], 'mean': 345.9, 'max': 345.9, 'min': 345.9}}]}, {'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': 
    [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 
'ConversationInfo': 
    [{'Position': None, 'Text': 'None', 'OverTag': 1, 'Type': 'Trend'}, {'Position': [196, 198], 'Text': '679', 'OverTag': 1, 'Type': 'Num'}], 
'GraphicalOverlay': 
    [{'Text': 'The value is also much lower than CNY 679 billion a year earlier', 'Label': [679], 'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12]}], 'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 12], 'End': ['Banks Balance Sheet (CNY Billion)', 12], 'mean': 345.9, 'max': 345.9, 'min': 345.9}}]}, 
{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': 
    [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 
'ConversationInfo': 
    [{'Position': None, 'Text': 'None', 'OverTag': 1, 'Type': 'Trend'}, {'Position': [[245, 251]], 'Text': 'in June', 'OverTag': 0, 'Type': 'ObjectName'}], 
'GraphicalOverlay': 
    [{'Text': 'CNY 3.05 trillion in June', 'Label': [3050], 'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11], 'mean': 3050.0, 'max': 3050.0, 'min': 3050.0}}]}, 
{'OriginText': "China's banks extended CNY 345.9 billion in new yuan loans in July 2023, the least since November of 2009 and well below market forecasts of CNY 800 billion. The value is also much lower than CNY 679 billion a year earlier and CNY 3.05 trillion in June, after a record CNY 15.73 trillion loans in the first half of the year. The reading adds to further evidence of a lacklustre economic recovery in China although July is usually a weak month for financing activities, with banks not in a rush to meet their lending targets at the beginning of the quarter.", 
'Position': 
    [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 
'ConversationInfo': 
    [{'Position': None, 'Text': 'None', 'OverTag': 1, 'Type': 'Trend'}, {'Position': [273, 277], 'Text': '15.73', 'OverTag': 2, 'Type': 'Num'}, {'Position': [[260, 272], [278, 292]], 'Text': 'a record CNY 15.73 trillion loans', 'OverTag': 0, 'Type': 'ObjectName'}], 
'GraphicalOverlay': 
    [{'Text': 'after a record CNY 15.73 trillion loans in the first half of the year', 'Label': [15.73], 'Marker': [{'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11]}], 'Line': {'Begin': ['Banks Balance Sheet (CNY Billion)', 11], 'End': ['Banks Balance Sheet (CNY Billion)', 11], 'mean': 3050.0, 'max': 3050.0, 'min': 3050.0}}]}]

# 前端传来的数据：
"""data: [{'Time': 'Aug 2022', 'Food inflation': 6.1}, 
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

# 后端返回的数据：
[{'OriginText': 'Food prices in China declined by 1.7 percent year-on-year in July 2023, reversing from a 2.3 percent rise in the prior month while pointing to the first drop since March 2022.', 
'Position': [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 
'ConversationInfo': 
    [{'Trend': 'declined', 
    'TrendPosition': [21, 28], 
    'Num': [-1.7], 
    'NumPosition': [None], 
    'ObjectName': ['Food prices in China'], 
    'ObjectPosition': [[0, 19]]}], 
'GraphicalOverlay': 
    [{'Text': 'Food prices in China declined by 1.7 percent year-on-year in July 2023', 
    'Label': [-1.7], 
    'Marker': [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 
    'Line': {'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11], 
    'mean': -1.7, 
    'max': -1.7, 
    'min': -1.7}}]}]

# 0828返回数据
[{'OriginText': 'Food prices in China declined by 1.7 percent year-on-year in July 2023, reversing from a 2.3 percent rise in the prior month while pointing to the first drop since March 2022.', 
'Position': 
    [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 
'ConversationInfo': 
    [{'Position': [21, 28], 'Text': 'declined', 'OverTag': 1, 'Type': 'Trend'}, {'Position': [[0, 19]], 'Text': 'Food prices in China', 'OverTag': 0, 'Type': 'ObjectName'}], 
'GraphicalOverlay': 
    [{'Text': 'Food prices in China declined by 1.7 percent year-on-year in July 2023', 'Label': [-1.7], 'Marker': [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 'Line': {'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11], 'mean': -1.7, 'max': -1.7, 'min': -1.7}}]}]

"""data: [{'Time': '2022 Q1', 'Unemployment rate': 7.3}, 
                        {'Time': '2022 Q2', 'Unemployment rate': 7.4}, 
                        {'Time': '2022 Q3', 'Unemployment rate': 7.3},
                        {'Time': '2022 Q4', 'Unemployment rate': 7.1}, 
                        {'Time': '2023 Q1', 'Unemployment rate': 7.1}, 
                       {'Time': '2023 Q2', 'Unemployment rate': 7.2}]
                text: ["The unemployment rate in France inched up to 7.2% in the second quarter of 2023 from 7.1% in the previous quarter, and the highest since Q4 2022, as the number of unemployed people increased by 20 thousand to 2.2 million."]
                label: "start"
            """

# 前端的数据：
"""data: [{'Time': 'Aug 2022', 'Food inflation': 6.1}, 
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

# 后端返回：
[{'OriginText': 'Food prices in China declined by 1.7 percent year-on-year in July 2023, reversing from a 2.3 percent rise in the prior month while pointing to the first drop since March 2022.', 
'Position': [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 
'ConversationInfo': 
    [{'Trend': 'declined', 
    'TrendPosition': [21, 28], 
    'Num': [-1.7], 
    'NumPosition': [None], 
    'ObjectName': ['Food prices in China'], 
    'ObjectPosition': [[0, 19]]}], 
'GraphicalOverlay': 
    [{'Text': 'Food prices in China declined by 1.7 percent year-on-year in July 2023', 
    'Label': [-1.7], 
    'Marker': [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 
    'Line': {'Begin': ['Food inflation', 11], 
    'End': ['Food inflation', 11], 
    'mean': -1.7, 
    'max': -1.7, 
    'min': -1.7}}]}]

# 0828返回数据
[{'OriginText': 'Food prices in China declined by 1.7 percent year-on-year in July 2023, reversing from a 2.3 percent rise in the prior month while pointing to the first drop since March 2022.', 
'Position': [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 
'ConversationInfo': 
    [{'Position': [21, 28], 'Text': 'declined', 'OverTag': 1, 'Type': 'Trend'}, {'Position': [[0, 19]], 'Text': 'Food prices in China', 'OverTag': 0, 'Type': 'ObjectName'}], 
'GraphicalOverlay': 
    [{'Text': 'Food prices in China declined by 1.7 percent year-on-year in July 2023', 'Label': [-1.7], 'Marker': [{'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11]}], 'Line': {'Begin': ['Food inflation', 11], 'End': ['Food inflation', 11], 'mean': -1.7, 'max': -1.7, 'min': -1.7}}]}]


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