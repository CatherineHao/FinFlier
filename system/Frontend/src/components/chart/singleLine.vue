<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-26 19:48:30
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-09-13 23:52:49
-->
<!--
 *                        _oo0oo_
 *                       o8888888o
 *                       88" . "88
 *                       (| -_- |)
 *                       0\  =  /0
 *                     ___/`---'\___
 *                   .' \\|     |// '.
 *                  / \\|||  :  |||// \
 *                 / _||||| -:- |||||- \
 *                |   | \\\  - /// |   |
 *                | \_|  ''\---/''  |_/ |
 *                \  .-\__  '-'  ___/-. /
 *              ___'. .'  /--.--\  `. .'___
 *           ."" '<  `.___\_<|>_/___.' >' "".
 *          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *          \  \ `_.   \_ __\ /__ _/   .-` /  /
 *      =====`-.____`.___ \_____/___.-`___.-'=====
 *                        `=---='
 * 
 * 
 *      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * 
 *            佛祖保佑     永不宕机     永无BUG
 -->

<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-26 19:48:30
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-29 00:10:20
-->
<template>
    <div ref="singleLineSvg"
        :style="{ height: realHeight + 'px', width: realWidth + 'px', 'transform': `translate(${-0 * (realWidth - scaleTag * realWidth) / 2}px, ${-0 * (realHeight - scaleTag * realHeight) / 2}px) scale(${scaleTag})`, 'transition': '0.4s', }">
        <svg :height="realHeight" :width="realWidth" xmlns="http://www.w3.org/2000/svg" :style="{
            'transition': '0.4s',
            'opacity': isShow == true ? '1' : '0'
        }">
            <g id="mainSingleLine_g"
                :transform="translate((.05 * elWidth + (realWidth - elWidth) / 2), (.1 * elHeight + (realHeight - elHeight) / 2))">

                <!-- <g> -->
                <!-- <g v-for="(item, i) in overlayData" :key="'overlay_' + i">
                            <Transition> -->
                <!-- <g v-if="objectTag[item.objectName] == 1" style="transition: 0.4s;">
                                    <g>
                                        <g v-if="overlayTag[2] == 1" class="animation-fade">
                                            <rect :x="barData[item.objectIndex].x - 3 - barData[item.objectIndex].width / 2" :y="0"
                                                :fill="colorTrans(overlay_setting[overlay_map[2]].currentColor)"
                                                :width="barData[item.objectIndex].width + 6" :height="elHeight * .8" opacity="0.6">
                                            </rect>
                                        </g>
                                    </g>
                                </g> -->
                <!-- </Transition>
                        </g>
                        </g> -->
                <g>
                    <g v-for="(o, i) in overlayData" :key="'Marker_' + i">
                        <Transition>
                            <g v-if="overlayTag[2] == 1 && objectTag[o.objectName] == 1" style="transition: 0.4s;">
                                <rect :x="o.bounding_box.pos.x1" :y="o.bounding_box.pos.y1"
                                    :width="o.bounding_box.pos.x2 - o.bounding_box.pos.x1"
                                    :height="o.bounding_box.pos.y2 - o.bounding_box.pos.y1"
                                    :fill="colorTrans(overlay_setting[overlay_map[2]].currentColor)"></rect>
                            </g>
                        </Transition>
                    </g>
                </g>

                <g>
                    <g :id="'xAxis' + stateTag"></g>
                    <g :id="'yAxis' + stateTag"></g>
                    <g id="axis_name">
                        <text  font-family="KoHo" font-style="oblique" font-size="22" text-anchor="end"
                            :transform="translate(axisPosition.xAxis[0], axisPosition.xAxis[1])">{{ chart_setting.axis.x }}</text>
                        <text  font-family="KoHo" font-style="oblique" font-size="22" text-anchor="start"
                            :transform="translate(axisPosition.yAxis[0], axisPosition.yAxis[1])">{{ chart_setting.axis.y }}</text>

                        <text style="font-size: 32px;" text-anchor="middle"  font-family="KoHo" font-style="oblique"
                            :transform="translate(.8 * elWidth / 2, -40)">{{ chart_setting.title }}</text>
                    </g>
                    <g id="singleline">
                        <path v-for="(o, i) in lineData" :key="'path' + i" :d="o.path" fill="none"
                            :stroke="overlayTag[0] == 1 ? '#d0d3c7' : colorTrans(chart_setting.currentColor)"
                            :stroke-width="chart_setting.size.width">
                        </path>
                    </g>
                </g>

                <g>
                    <g v-for="(o, i) in overlayData" :key="'Marker_' + i">
                        <Transition>
                            <g style="transition: 0.4s;">
                                <g v-if="overlayTag[0] == 1 && objectTag[o.objectName] == 1">
                                    <path v-for="(d, di) in o.color.lineInfo" :key="'path' + di" :d="d.path" fill="none"
                                        :stroke="colorTrans(chart_setting.currentColor)"
                                        :stroke-width="chart_setting.size.width">
                                    </path>
                                </g>
                                <g v-if="overlayTag[1] == 1 && objectTag[o.objectName] == 1">
                                    <rect :x="o.bounding_box.pos.x1" :y="o.bounding_box.pos.y1"
                                        :width="o.bounding_box.pos.x2 - o.bounding_box.pos.x1"
                                        :height="o.bounding_box.pos.y2 - o.bounding_box.pos.y1" :stroke-width="3"
                                        fill="none" :stroke="colorTrans(overlay_setting[overlay_map[1]].currentColor)">
                                    </rect>
                                </g>
                                <g v-if="overlayTag[3] == 1 && objectTag[o.objectName] == 1">
                                    <circle v-for="(m, m_i) in o.marker.pos" :key="'marker' + m_i" :r="5"
                                        :fill="colorTrans(overlay_setting[overlay_map[3]].currentColor)" :cx="m[0]"
                                        :cy="m[1]">
                                    </circle>
                                </g>
                                <g v-if="(overlayTag[4] == 1) && objectTag[o.objectName] == 1">
                                    <path v-for="(d, d_i) in o.label.pos" :key="'dd_' + d_i"
                                        :d="'M' + d[0] + ',' + d[1] + 'L' + (d[0] + position[o.label.lid + 'l' + d_i].left) + ',' + (-.1 * elHeight + 5 + + position[o.label.lid + 'l' + d_i].top)"
                                        fill="none" :stroke="colorTrans(overlay_setting[overlay_map[4]].currentColor)"
                                        :stroke-width="2"></path>
                                </g>
                                <g v-if="(overlayTag[5] == 1) && objectTag[o.objectName] == 1">
                                    <path v-if="o.text.lineTag == 1"
                                        :d="'M' + o.text.pos[0] + ',' + o.text.pos[1] + 'L' + (o.text.pos[0]) + ',' + (-.1 * elHeight + 5 + position[o.text.qid])"
                                        fill="none" :stroke="colorTrans(overlay_setting[overlay_map[5]].currentColor)"
                                        :stroke-width="2"></path>
                                </g>

                                <g v-if="overlayTag[6] == 1 && objectTag[o.objectName] == 1">
                                    <defs>
                                        <marker id="triangle" viewBox="0 0 10 10" refX="9" refY="5"
                                            markerUnits="strokeWidth" markerWidth="10" markerHeight="10" orient="auto">
                                            <path d="M 0 0 L 10 5 L 0 10 z"
                                                :fill="colorTrans(overlay_setting[overlay_map[6]].currentColor)" />
                                        </marker>
                                    </defs>
                                    <!-- <path
                                        :d="'M' + o.trend.pos.x1 + ',' + o.trend.pos.y1 + 'L' + o.trend.pos.x2 + ',' + o.trend.pos.y2"
                                        :stroke-width="2" marker-end="url(#triangle)"
                                        :stroke="colorTrans(overlay_setting[overlay_map[6]].currentColor)" fill="none">
                                    </path> -->
                                    <path
                                        :d="trendPath"
                                        :stroke-width="2" marker-end="url(#triangle)"
                                        :stroke="colorTrans(overlay_setting[overlay_map[6]].currentColor)" fill="none">
                                    </path>
                                </g>
                                <g v-if="(overlayTag[7] == 1) && objectTag[o.objectName] == 1">
                                    <path
                                        :d="'M' + o.overall.pos.x1 + ',' + o.overall.pos.y + 'L' + o.overall.pos.x2 + ',' + o.overall.pos.y"
                                        fill="none" :stroke="colorTrans(overlay_setting[overlay_map[7]].currentColor)"
                                        :stroke-width="2"></path>
                                </g>
                                <g v-if="(overlayTag[8] == 1) && objectTag[o.objectName] == 1">
                                    <path :d="'M' + o.text.pos.x + ',' + 0 + 'L' + o.text.pos.x + ',' + (.8 * elHeight)"
                                        fill="none" :stroke="colorTrans(overlay_setting[overlay_map[8]].currentColor)"
                                        :stroke-width="2"></path>
                                </g>
                            </g>
                        </Transition>
                    </g>
                </g>
            </g>
        </svg>
        <!-- <div> -->
        <!-- <div v-if=""> -->
        <div v-for="(item, i) in overlayData" :key="'overlay_' + i" :style="{
            'position': 'absolute',
            'top': `${0 * elHeight + position[item.text.qid].top}px`,
            'left': `${.05 * elWidth - 140 + (realWidth - elWidth) / 2 + item.text.pos.x + position[item.text.qid].left}px`,
            'width': '350px',
            'opacity': item.tag != -1 && (overlayTag[5] == 1) && objectTag[item.objectName] == 1 ? 1 : 0,
            'padding': '3px',
            'font-size': '22px',
            'border': '2px solid',
            'border-color': item.tag != -1 && (overlayTag[5] == 1) && objectTag[item.objectName] == 1 ? colorTrans(overlay_setting[overlay_map[5]].currentColor) : 'black',
            'border-radius': '10px',
            'background-color': 'white',
            'user-select': 'none',
            'z-index': (overlayTag[5] == 1) && objectTag[item.objectName] == 1 ? 100 : 1,
            'cursor': 'grab'
        }" @mousedown="startDrag($event, item.text.qid)" @mousemove="onDrag($event, item.text.qid)"
            @mouseup="stopDrag()">
            {{ item.text.text }}
        </div>
        <div v-for="(item, i) in overlayData" :key="'overlay_' + i" style="position: absolute; top: 0px; left: 0px;">
            <div v-for="(d, d_i) in item.label.pos" :key="'dd_' + d_i" :style="{
                'position': 'absolute',
            'font-size': '18px',
                'top': `${0 * elHeight + position[item.label.lid + 'l' + d_i].top}px`,
                'left': `${d[0] - 75 + .05 * elWidth + (realWidth - elWidth) / 2 + position[item.label.lid + 'l' + d_i].left}px`,
                'width': '150px',
                'opacity': item.tag != -1 && (overlayTag[4] == 1) && objectTag[item.objectName] == 1 ? 1 : 0,
                'padding': '3px',
                'border': '2px solid',
            'z-index': (overlayTag[4] == 1) && objectTag[item.objectName] == 1 ? 100 : 1,
                'border-color': item.tag != -1 && (overlayTag[4] == 1) && objectTag[item.objectName] == 1 ? colorTrans(overlay_setting[overlay_map[4]].currentColor) : 'white',
                'border-radius': '10px',
                'background-color': 'white',
                'user-select': 'none',
                'cursor': 'grab'
            }" @mousedown="startDrag($event, item.label.lid + 'l' + d_i)"
                @mousemove="onDrag($event, item.label.lid + 'l' + d_i)" @mouseup="stopDrag()">
                {{ item.label.text[d_i] }}
            </div>
        </div>
        <div :style="{
            'position': 'absolute',
            'top': `${80 + position['legend'].top}px`,
            'right': `${30 - position['legend'].left}px`,
            'user-select': 'none',
            'cursor': 'grab',
            'z-index': 1000
        }"  @mousedown="startDrag($event, 'legend')" @mousemove="onDrag($event, 'legend')" @mouseup="stopDrag()">
            <div style="display: flex;">
                <div :style="{'height': '24px', 'width': '24px', 'background-color': colorTrans(chart_setting.currentColor), 'margin-right': '10px' }"></div>
                <div style="font-size: 18px;">{{ chart_setting.attrName }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import { axisBottom, axisLeft, extent, line, scaleLinear, scalePoint, scaleUtc, select, timeFormat } from "d3";
import { useDataStore } from "@/stores/counter";
// import description_data from "@/assets/data/test.json"
export default {
    name: "singleLine",
    props: ['rawData', 'chartData', 'defaultTag', 'scaleTag', 'stateTag'],
    data () {
        return {
            realHeight: 100,
            realWidth: 100,
            elHeight: 100,
            elWidth: 100,
            isShow: false,
            lineData: [],
            overlayData: [],
            overlayTag: {},
            objectTag: {},
            axisPosition: {
                xAxis: [0, 0],
                yAxis: [0, 0]
            },
            yScale: null,
            overlay_setting: {},
            overlay_map: ['color', 'bounding box', 'background', 'marker', 'label', 'text', 'trend', 'overall', 'special'],
            chart_setting: {
                currentColor: {
                    r: 0,
                    g: 0,
                    b: 0,
                    a: 1
                },
                size: {
                    width: 100
                },
                axis: {
                    x: 'Position',
                    y: "Billions of dollars"
                }
            },
            drawGraphTag: 0,
            isDragging: false,
            startPosition: { legend: { x: 0, y: 0 } },
            position: { legend: { left: 0, top: 0 } },
            trendPath: ''
        };
    },
    methods: {
        startDrag (event, id) {
            this.isDragging = true;
            this.startPosition[id].x = event.clientX - this.position[id].left;
            this.startPosition[id].y = event.clientY - this.position[id].top;
            // console.log(this.startPosition);
        },
        onDrag (event, id) {
            if (this.isDragging) {
                console.log(id)
                this.position[id].left = event.clientX - this.startPosition[id].x;
                this.position[id].top = event.clientY - this.startPosition[id].y;
                // console.log(this.position.left)
                // console.log(id)
            }
        },
        stopDrag (id) {
            this.isDragging = false;
        },
        calcOverlay (lineData, chartData) {
            let over_all = [];
            let pos_tag = 0;
            if (Object.keys(this.position).length == 1) {
                pos_tag = 1;
            }

            for (let c_i in chartData) {
                let over_data = chartData[c_i];
                // console.log(over_data);
                let trendLineData = [54, 68, 84, 100];
                // let lineGen = line
                let pathLine = 'M';
                for (let i of trendLineData) {
                    // if (line)
                    pathLine += lineData[i].pos1[0] + ',' + lineData[i].pos1[1];
                    if (i != 141) pathLine += 'L';
                }
                console.log(pathLine)
                this.trendPath = pathLine;
                let position = over_data.Position[0];
                let overlayData = {
                    'objectName': over_data['ObjectName'],
                    'color': {
                        tag: -1,
                        lineInfo: []
                    },
                    'bounding_box': {
                        tag: -1,
                        pos1: [0, 0],
                        pos2: [0, 0]
                    },
                    'background': {
                        tag: -1,
                        pos1: [0, 0],
                        pos2: [0, 0]
                    },
                    'marker': { tag: -1, pos: [] },
                    'label': { tag: -1, pos: [], text: [], qid: [], lid: 'l' + c_i },
                    'text': { tag: -1, lineTag: 1, pos: [], text: '', qid: 't' + c_i },
                    'trend': { tag: -1, pos: [] },
                    'overall': { tag: -1, pos: [] },
                    'special': { tag: -1, pos: [] }
                }
                if (position['Begin'][1] == position['End'][1]) {
                    overlayData.label.tag = 1;
                    overlayData.text.tag = 1;
                    overlayData.label.text = over_data.GraphicalOverlay[0].Label;
                    overlayData.text.text = over_data.GraphicalOverlay[0].Text;
                    let cnt = parseInt(position['Begin'][1]);
                    let cnt_tag = 0;
                    let nodePos = [];

                    if (cnt == lineData.length) {
                        cnt--;
                        cnt_tag = 1;
                    }
                    if (cnt_tag == 0) {
                        overlayData.label.pos = [(lineData[cnt]['pos1'])];
                        overlayData.text.pos = (lineData[cnt]['pos1']);
                        overlayData.marker.pos.push(lineData[cnt]['pos1']);
                        nodePos = lineData[cnt]['pos1']
                    } else {
                        overlayData.label.pos = [(lineData[cnt]['pos2'])];
                        overlayData.text.pos = (lineData[cnt]['pos2']);
                        overlayData.marker.pos.push(lineData[cnt]['pos2']);
                        nodePos = lineData[cnt]['pos2'];
                    }
                    if (pos_tag) {
                        this.position[overlayData.label.lid + 'l0'] = { left: 0, top: 0 }
                        this.position[overlayData.text.qid] = { left: 0, top: 0 }
                        this.startPosition[overlayData.label.lid + 'l0'] = ({ x: 0, y: 0 });
                        this.startPosition[overlayData.text.qid] = ({ x: 0, y: 0 });
                    }
                    overlayData.background.rectInfo = {
                        x1: nodePos[0] - 10,
                        x2: nodePos[1] - 10,
                        y1: nodePos[0] + 10,
                        y2: nodePos[1] + 10
                    };
                    overlayData["bounding_box"].pos = {
                        x1: nodePos[0] - 10,
                        x2: nodePos[1] - 10,
                        y1: nodePos[0] + 10,
                        y2: nodePos[1] + 10
                    };
                } else {
                    let select_line = [];
                    overlayData.marker.tag = 1;
                    overlayData.label.tag = 1;
                    overlayData.text.tag = 1;
                    // console.log(over_data)
                    let y_max = -9999999;
                    let y_min = 99999999;
                    let x_max = -9999999;
                    let x_min = 99999999;
                    if (pos_tag) {
                        this.position[overlayData.label.lid + 'l0'] = { left: 0, top: 0 }
                        this.position[overlayData.text.qid] = { left: 0, top: 0 }
                        this.startPosition[overlayData.label.lid + 'l0'] = ({ x: 0, y: 0 });
                        this.startPosition[overlayData.text.qid] = ({ x: 0, y: 0 });
                        this.position[overlayData.label.lid + 'l1'] = { left: 0, top: 0 }
                        this.startPosition[overlayData.label.lid + 'l1'] = ({ x: 0, y: 0 });
                    }
                    console.log(this.position, this.startPosition)
                    overlayData.label.text = over_data.GraphicalOverlay[0].Label;
                    overlayData.text.text = over_data.GraphicalOverlay[0].Text;
                    let startNode = lineData[parseInt(position['Begin'][1])];
                    let endNode = lineData[parseInt(position['End'][1]) < lineData.length ? parseInt(position['End'][1]) : parseInt(position['End'][1]) - 1];
                    for (let i = parseInt(position['Begin'][1]); i <= parseInt(position['End'][1]); ++i) {
                        if (i < lineData.length) {
                            select_line.push(lineData[i]);
                            x_min = Math.min(lineData[i].pos1[0], x_min);
                            x_max = Math.max(lineData[i].pos2[0], x_max);
                            y_max = Math.max(lineData[i].pos1[1], y_max);
                            y_max = Math.max(lineData[i].pos2[1], y_max);
                            y_min = Math.min(lineData[i].pos1[1], y_min);
                            y_min = Math.min(lineData[i].pos2[1], y_min);
                        }
                        let cnt = i;
                        let cnt_tag = 0;
                        if (i == lineData.length) {
                            cnt--;
                            cnt_tag = 1;
                        }
                        if (cnt_tag == 0)
                            overlayData.marker.pos.push(lineData[cnt]['pos1']);
                        else
                            overlayData.marker.pos.push(lineData[cnt]['pos2']);
                    }
                    overlayData.color.lineInfo = select_line;
                    overlayData.background.rectInfo = {
                        x1: x_min,
                        x2: x_max,
                        y1: y_min,
                        y2: y_max
                    };
                    overlayData["bounding_box"].pos = {
                        x1: x_min,
                        x2: x_max,
                        y1: y_min,
                        y2: y_max
                    };
                    overlayData['text'].pos = {
                        x: (x_max + x_min) / 2,
                        y: (y_max + y_min) / 2
                    }
                    overlayData.special.pos = {
                        x: startNode.pos1[0],
                        y: startNode.pos2[1],
                    };
                    if (over_data.GraphicalOverlay[0].Label.length == 2) {
                        overlayData.label.pos = [
                            startNode.pos1, endNode.pos2
                        ]
                    } else if (over_data.GraphicalOverlay[0].Label.length == 1) {
                        overlayData.label.pos = [
                            startNode.pos1
                        ]
                    } else {
                        overlayData.label.pos = []
                    }

                    overlayData.trend.pos = {
                        x1: startNode.pos1[0],
                        y1: startNode.pos1[1],
                        x2: endNode.pos2[0],
                        y2: endNode.pos2[1],
                    };
                    overlayData.overall.pos = {
                        x1: startNode.pos1[0],
                        x2: endNode.pos2[0],
                        y: this.yScale(parseFloat(over_data.GraphicalOverlay[0].Line.min))
                    }
                }
                over_all.push(overlayData)
                // console.log(overlayData);
            }
            return over_all;
        },
        colorTrans (color) {
            return `rgba(${color.r}, ${color.g}, ${color.b}, ${color.a})`
        },
        translate (x, y) {
            return `translate(${x}, ${y})`;
        },
        dataType (data, scaleType) {
            if (scaleType == 'time') {
                return new Date(data);
            } else {
                return data;
            }
        },
        scale (data, scaleName, scaleType, range) {
            let scale_data = [];
            // console.log(scaleType)
            for (let i in data) {
                if (i == 'columns') continue;
                scale_data.push(data[i][scaleName]);
            }
            if (scaleType == 'category') {
                return scalePoint(scale_data, range).padding(1);
            }
            if (scaleType == 'linear') {
                let dataDomain = extent(scale_data, d => parseFloat(d));
                if (dataDomain[1] < 0) dataDomain[1] = 0;
                if (dataDomain[0] > 0) dataDomain[0] = 14000;
                // console.log(dataDomain);
                return scaleLinear(dataDomain, range);
            }
            if (scaleType == 'time') {
                let dataDomain = extent(scale_data, d => new Date(d));
                return scaleUtc(dataDomain, range);
            }
        },
        // calcPath (center) {

        // },
        calcLine (data, chart_info) {
            // if (this.defaultTag == 1) {
            // let width = this.elWidth * .9;
            let xName = chart_info.chartScale.x.scaleName;
            let yName = chart_info.chartScale.y.scaleName;
            this.chart_setting = {
                elWidth: this.elWidth,
                elHeight: this.elHeight,
                currentColor: chart_info.chartColor[chart_info.chartScale.y.attributeName[0]],
                attrName: chart_info.chartScale.y.attributeName[0],
                size: {
                    width: 3
                },
                axis: {
                    x: xName,
                    y: yName
                },
                isLegend: true,
                title: 'Title'
            }
            // console.log(this.chart_setting);
            const dataStore = useDataStore();
            dataStore.default_setting.chart_setting = this.chart_setting;
            dataStore.state_map['state' + dataStore.show_state]['chart_setting'] = this.chart_setting;
            dataStore.changeTag = 1;
            // }
            // else {
            //     const dataStore = useDataStore();
            //     this.chart_setting = dataStore.defaultTag.chart_setting;
            // }
            let width = this.chart_setting.elWidth * .9;
            let height = this.chart_setting.elHeight * .8;
            // let xName = chart_info.chartScale.x.attributeName;
            // let yName = chart_info.chartScale.y.attributeName[0];
            let xScale = this.scale(data, chart_info.chartScale.x.attributeName, chart_info.chartScale.x.scaleType, [0, width]);
            let yScale = this.scale(data, chart_info.chartScale.y.attributeName[0], chart_info.chartScale.y.scaleType, [height, 0]);
            // console.log(xScale, yScale);
            this.yScale = yScale;
            this.axisPosition = {
                xAxis: [width, yScale(14000) + 50],
                yAxis: [-.05 * width, -20]
            }
            // console.log(yScale);
            let xAxis = (g, x, height) => {
                g.attr("transform", `translate(0, ${height})`)
                    .call(axisBottom(x))
                    .attr('font-size', 20)
            }
            let yAxis = (g, y) => {
                g.attr("transform", `translate(${0}, 0)`)
                    .call(axisLeft(y).ticks(5).tickSizeOuter(0))
                    .attr('font-size', 20)
            }
            select("#xAxis" + this.stateTag).call(xAxis, xScale, height);
            select("#yAxis" + this.stateTag).call(yAxis, yScale);
            let lineGenerator = line().x(d => xScale(this.dataType(d[chart_info.chartScale.x.attributeName], chart_info.chartScale.x.scaleType))).y(d => yScale(d[chart_info.chartScale.y.attributeName[0]]));
            let lineData = new Array();
            for (let i in data) {
                if (i == 0 || i == 'columns') continue;
                lineData.push({
                    path: lineGenerator([data[i], data[i - 1]]),
                    fill: chart_info.chartColor[chart_info.chartScale.y.attributeName[0]],
                    data: [data[i - 1], data[i]],
                    pos1: [xScale(this.dataType(data[i - 1][chart_info.chartScale.x.attributeName], chart_info.chartScale.x.scaleType)), yScale(data[i - 1][chart_info.chartScale.y.attributeName[0]])],
                    pos2: [xScale(this.dataType(data[i][chart_info.chartScale.x.attributeName], chart_info.chartScale.x.scaleType)), yScale(data[i][chart_info.chartScale.y.attributeName[0]])]
                })
            }
            return lineData;
        }
    },
    created () { },
    mounted () {
        // this.elHeight = this.$refs.singleLineSvg.offsetHeight;
        // this.elWidth = this.$refs.singleLineSvg.offsetWidth;

        this.realHeight = document.getElementById('mainView').offsetHeight;
        this.realWidth = document.getElementById('mainView').offsetWidth;
        this.elHeight = document.getElementById('mainView').offsetHeight;
        this.elWidth = document.getElementById('mainView').offsetWidth;
        if (this.elHeight / 9 * 16 < this.elWidth) {
            this.elWidth = this.elHeight / 9 * 16;
        } else {
            this.elHeight = this.elWidth / 16 * 9;
        }
        // console.log(this.rawData, this.chartData);
        // if (this.defaultTag == 1) {
        this.drawGraphTag = 1;
        this.lineData = this.calcLine(this.rawData, this.chartData);
        // }
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations, state) => {
            if (this.defaultTag == 1) {
                this.chart_setting = dataStore.state_map[this.stateTag]['chart_setting'];
            }
            this.overlayData = this.calcOverlay(this.lineData, dataStore.graphicalOverlayData);
            let selObj = dataStore.selectObject;
            if (selObj != '') {
                if (selObj == -1) {
                    this.overlayTag = [0, 0, 0, 0, 0, 0, 0, 0, 0];
                } else {
                    this.overlayTag = dataStore.state_map[this.stateTag]['overlay_setting'][selObj]['overlay_tag'];
                    this.overlay_setting = dataStore.state_map[this.stateTag]['overlay_setting'][selObj];
                }
            }
            this.objectTag = dataStore.objectTag;
        })

        setTimeout(() => this.isShow = !this.isShow, 100);
    },
    components: {}
}
</script>

<style>
.title {
    font-family: KoHo;
    font-style: oblique;
    font-size: 16px;
}

/* we will explain what these classes do next! */

.v-enter-active,
.v-leave-active {
    transition: opacity 0.4s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}</style>
