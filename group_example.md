'''
data: [{'Time':'2017/1/1','Mini- and subcompact size':'0.61','Compact size':'0.35', 'Midsize to large':'0.04'},{'Time':'2018/1/1','Mini- and subcompact size':'0.49','Compact size':'0.41', 'Midsize to large':'0.10'},{'Time':'2019/1/1','Mini- and subcompact size':'0.33','Compact size':'0.54', 'Midsize to large':'0.13'},{'Time':'2020/1/1','Mini- and subcompact size':'0.35','Compact size':'0.33', 'Midsize to large':'0.32'},{'Time':'2021/1/1','Mini- and subcompact size':'0.37','Compact size':'0.28', 'Midsize to large':'0.35'},{'Time':'2022/1/1','Mini- and subcompact size':'0.37','Compact size':'0.31', 'Midsize to large':'0.32'},{'Time':'2023/1/1','Mini- and subcompact size':'0.30','Compact size':'0.30', 'Midsize to large':'0.40'}]
text: ["In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size."]
label: start
'''

result: [{\"ObjectName\":[\"NEVs that were subcompact and below\"],\"DataName\":\"Mini- and subcompact size\",\"Position\":[{\"Begin\":[0,1],\"End\":[0,1]}],\"Trend\":\"declined\",\"Num\":[30],\"Text\":\"the sales proportion of NEVs that were subcompact and below declined to 30% in 2023 from 61% in 2017\"},\n        {\"ObjectName\":[\"compact and midsize-to-large NEVs\"],\"DataName\":\"Compact size, Midsize to large\",\"Position\":[{\"Begin\":[0,2],\"End\":[0,3]}],\"Trend\":\"increased\",\"Num\":[70,39],\"Text\":\"the mix of compact and midsize-to-large NEVs increased to 70% in 2023 from 39% in 2017\"}]\nreason: \"The first object is 'NEVs that were subcompact and below', its value is 30% in 2023 and its descriptive phrase is 'the sales proportion of NEVs that were subcompact and below declined to 30% in 2023 from 61% in 2017'. The second object is 'compact and midsize-to-large NEVs', its value is 70% in 2023 and its descriptive phrase is 'the mix of compact and midsize-to-large NEVs increased to 70% in 2023 from 39% in 2017'.


# 清理后的result:
[{"ObjectName":["NEVs that were subcompact and below"],
    "DataName":"Mini- and subcompact size",
    "Position":[{"Begin":[0,1],"End":[0,1]}],
    "Trend":"declined",
    "Num":[30],
    "Text": "the sales proportion of NEVs that were subcompact and below declined to 30% in 2023 from 61% in 2017"
},        
{"ObjectName":["compact and midsize-to-large NEVs"],
    "DataName":"Compact size, Midsize to large",
    "Position":[{"Begin":[0,2],"End\":[0,3]}],
    "Trend":"increased",
    "Num":[70,39],
    "Text":"the mix of compact and midsize-to-large NEVs increased to 70% in 2023 from 39% in 2017"
}]

# hack需要的前端数据
[
    {
        'OriginText': 'In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size.',
        'Position': [{'Begin': ['Mini- and subcompact size', 0], 'End': ['Mini- and subcompact size', 6]}],  
        'ConversationInfo': [
            {
                'Position': [48,67], 
                'Text': 'subcompact and below', 
                'OverTag': 0, 
                'Type': 'ObjectName'
            },
            {
                'Position': [69,76], 
                'Text': 'declined', 
                'OverTag': 1, 
                'Type': 'Trend'
            },
            {
                'Position': [81,83], 
                'Text': '30%', 
                'OverTag': 1, 
                'Type': 'Num'
            },
            {
                'Position': [91,93], 
                'Text': '61%', 
                'OverTag': 1, 
                'Type': 'Num'
            }],
        'GraphicalOverlay': 
        [{
            'Text': 'the sales proportion of NEVs that were subcompact and below declined to 30%', 
            'Label': ['declined'], 
            'Marker': [{'Begin': ['Mini- and subcompact size', 0], 'End': ['Mini- and subcompact size', 6]}], 
            'Line': {'Begin': ['Mini- and subcompact size', 0], 'End': ['Mini- and subcompact size', 6], 'mean': 0.403, 'max': 0.61, 'min': 0.30}}]
    },
    {
        'OriginText': 'In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size.',
        'Position': [{"Begin": [2, 0], "End": [3, 6]}], # 这里要写列名，但是这个包含两个列，所以我第一个数字还是列号  
        'ConversationInfo': [
            {
                'Position': [143,181], 
                'Text': 'the mix of compact and midsize-to-large', 
                'OverTag': 0, 
                'Type': 'ObjectName'
            },
            {
                'Position': [188,196], 
                'Text': 'increased', 
                'OverTag': 1, 
                'Type': 'Trend'
            },
            {
                'Position': [201,203], 
                'Text': '70%', 
                'OverTag': 1, 
                'Type': 'Num'
            },
            {
                'Position': [210,212], 
                'Text': '39%', 
                'OverTag': 1, 
                'Type': 'Num'
            }],
        'GraphicalOverlay': 
        [{
            'Text': 'the mix of compact and midsize-to-large NEVs increased to 70% from 39%', 
            'Label': ['increased'], 
            'Marker': [{'Begin': [2, 0], 'End': [3, 6]}], # 同position问题
            'Line': {'Begin': [2，0], 'End': [3, 6], 'mean': 0.597, 'max': 0.70, 'min': 0.39}}]
    }
]


