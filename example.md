<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-19 14:38:25
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-19 14:42:22
-->
data1:





data 3- group:
gpt传给backend的结果有两个部分 result + reason
```json
result = [{"ObjectName":["Mini- and subcompact size"],"Position":[{"Begin":[1,6],"End":[1,6]}], "Trend":"declined","Num":[0.30],"Text":"the sales proportion of NEVs that were subcompact and below declined to 30%"},
{"ObjectName":["Mini- and subcompact size"],"Position":[{"Begin":[1,0],"End":[1,0]}], "Trend":"None","Num":[0.61],"Text":"from 61% in 2017"},
{"ObjectName":["Compact Size","Midsize to large"],"Position":[{"Begin":[2,6],"End":[2,6]},{"Begin":[3,6],"End":[3,6]}], "Trend":"upgrade trend","Num":[0.30,0.40],"Text":"the mix of compact and midsize-to-large NEVs increased to 70%"},
{"ObjectName":["Compact Size","Midsize to large"],"Position":[{"Begin":[2,0],"End":[2,0]},{"Begin":[3,0],"End":[3,0]}], "Trend":"None","Num":[0.35,0.04],"Text":"the mix of compact and midsize-to-large NEVs increased to 70% from 39%"}]
```

```js
reason = "The object in unit 1 is ‘Mini- and subcompact size’. Its compact size goes from '0.61' in 2017 to '0.30' in 2023. The subject in unit 2 is the combination of ‘Compact Size’ and ‘Midsize to large’. Its compact size goes from the combination from ‘0.35’ and ‘0.04’ in 2017 to '0.30' and '0.40' in 2023."
```

backend 直接将 reason返回，针对result处理成以下格式：
```json
{
    "OriginText": "In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size.",
    "Position": [{"Begin":["Mini- and subcompact size",6],"End":["Mini- and subcompact size",6]}],
    "ConversationInfo":[{
        "Trend": "declined",
        "TrendPosition": [69,76],
        "Num": [0.30],
        "NumPosition": [81,83],
        "ObjectName":"Mini- and subcompact size",
        "ObjectPosition": [48,67]
    }],
    "GraphicalOverlay":[{
        "Text": "the sales proportion of NEVs that were subcompact and below declined to 30%",
        "Label": "0.30",
        "Marker": [{"Begin":["Mini- and subcompact size",6],"End":["Mini- and subcompact size",6]}],
        "Line": {
            "Begin":["Mini- and subcompact size",6],
            "End": ["Mini- and subcompact size",6],
            "mean": "0.3",
            "max" : "0.3",
            "min" : "0.3"
        }
    }]
},
{
    "OriginText": "In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size.",
    "Position": [{"Begin":["Mini- and subcompact size",0],"End":["Mini- and subcompact size",0]}],
    "ConversationInfo":[{
        "Trend": "None",
        "TrendPosition": None,
        "Num": [0.61],
        "NumPosition": [91,93],
        "ObjectName":"Mini- and subcompact size",
        "ObjectPosition": [48,67]
    }],
    "GraphicalOverlay":[{
        "Text": "from 61% in 2017",
        "Label": "0.61",
        "Marker": [{"Begin":["Mini- and subcompact size",0],"End":["Mini- and subcompact size",0]}],
        "Line": {
            "Begin":["Mini- and subcompact size",0],
            "End": ["Mini- and subcompact size",0],
            "mean": "0.61",
            "max" : "0.61",
            "min" : "0.61"
        }
    }]
},
{
    "OriginText": "In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size.",
    "Position": [{"Begin":["Compact size",6],"End":["Compact size",6]},{"Begin":["Midsize to large",6],"End":["Midsize to large",6]}],
    "ConversationInfo":[{
        "Trend": "upgrade trend",
        "TrendPosition": [230,242],
        "Num": [0.30, 0.40],
        "NumPosition": [201,203], # 实际上原文中对应的是70%
        "ObjectName":"Midsize to large", # 但实际上在原文中对应的是compact and midsize-to-large NEVs
        "ObjectPosition": [154,186]
    }],
    "GraphicalOverlay":[{
        "Text": "the mix of compact and midsize-to-large NEVs increased to 70%",
        "Label": "0.70",
        "Marker": [{"Begin":["Compact size",6],"End":["Compact size",6]},{"Begin":["Midsize to large",6],"End":["Midsize to large",6]}],
        "Line": {
            "Begin":["Compact size",6],
            "End": ["Midsize to large",6],
            "mean": "0.35",
            "max" : "0.40",
            "min" : "0.30"
        }
    }]
},
{
    "OriginText": "In 2023, the sales proportion of NEVs that were subcompact and below declined to 30%, from 61% in 2017. During the same periods of comparison, the mix of compact and midsize-to-large NEVs increased to 70% from 39%, reflecting the upgrade trend in terms of vehicle size.",
    "Position": [{"Begin":["Compact size",0],"End":["Compact size",0]},{"Begin":["Midsize to large",0],"End":["Midsize to large",0]}],
    "ConversationInfo":[{
        "Trend": "None",
        "TrendPosition": None,
        "Num": [0.35, 0.04],
        "NumPosition": [210,212], 
        "ObjectName":"Midsize to large", 
        "ObjectPosition": [154,186]
    }],
    "GraphicalOverlay":[{
        "Text": "the mix of compact and midsize-to-large NEVs increased to 70% from 39%",
        "Label": "0.39",
        "Marker": [{"Begin":["Compact size",0],"End":["Compact size",0]},{"Begin":["Midsize to large",0],"End":["Midsize to large",0]}],
        "Line": {
            "Begin":["Compact size",0],
            "End": ["Midsize to large",0],
            "mean": "0.195",
            "max" : "0.35",
            "min" : "0.04"
        }
    }]
}