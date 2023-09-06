<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-26 19:48:41
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-27 20:29:10
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

                <g>
                    <g :id="'xAxis' + stateTag"></g>
                    <g :id="'yAxis' + stateTag"></g>
                    <g id="axis_name">
                        <text class="title" text-anchor="end"
                            :transform="translate(axisPosition.xAxis[0], axisPosition.xAxis[1])">{{ chart_setting.axis.x }}</text>
                        <text class="title" text-anchor="start"
                            :transform="translate(axisPosition.yAxis[0], axisPosition.yAxis[1])">{{ chart_setting.axis.y }}</text>
                    </g>
                    <g id="singleline">
                        <path v-for="(o, i) in lineData" :key="'path' + i" :d="o.path" fill="none"
                            :stroke="colorTrans(chart_setting.currentColor[o.attr])"
                            :stroke-width="chart_setting.size.width">
                        </path>
                    </g>
                </g>
                <g>
                    <g v-for="(o, i) in overlayData" :key="'overlay' + i">

                        <Transition>
                            <g v-if="objectTag[o.objectName] == 1">
                                <g v-if="overlayTag[3] == 1">
                                    <circle :r="5" :fill="colorTrans(overlay_setting[overlay_map[3]].currentColor)"
                                        :cx="o.x" :cy="o.y">
                                    </circle>
                                </g>
                                <g v-if="(overlayTag[4] == 1)">
                                    <path
                                        :d="'M' + o.x + ',' + o.y + 'L' + (o.x + position[o.labelPosTag].left) + ',' + (-0.1 * elHeight + 5 + position[o.labelPosTag].top)"
                                        fill="none" :stroke="colorTrans(overlay_setting[overlay_map[4]].currentColor)"
                                        :stroke-width="2">
                                    </path>
                                </g>
                                <g v-if="(overlayTag[5] == 1)">
                                    <path
                                        :d="'M' + o.x + ',' + o.y + 'L' + (o.x + position[o.textPosTag].left) + ',' + (-0.1 * elHeight + 5 + position[o.textPosTag].top)"
                                        fill="none" :stroke="colorTrans(overlay_setting[overlay_map[5]].currentColor)"
                                        :stroke-width="2">
                                    </path>
                                </g>
                            </g>

                        </Transition>
                    </g>
                </g>
            </g>
        </svg>

        <div v-for="(item, i) in overlayData" :key="'overlay_' + i" :style="{
            'position': 'absolute',
            'top': `${0 * elHeight + position[item.labelPosTag].top}px`,
            'left': `${.05 * elWidth - 75 + item.x + (realWidth - elWidth) / 2 + position[item.labelPosTag].left}px`,
            'width': '150px',
            'opacity': (overlayTag[4] == 1) && objectTag[item.objectName] == 1 ? 1 : 0,
            'padding': '3px',
            'border': '2px solid',
            'z-index': (overlayTag[4] == 1) && objectTag[item.objectName] == 1 ? 100 : 1,
            'border-color': (overlayTag[4] == 1) && objectTag[item.objectName] == 1 ? colorTrans(overlay_setting[overlay_map[4]].currentColor) : 'white',
            'border-radius': '10px',
            'background-color': 'white',
            'user-select': 'none',
            'cursor': 'grab'
        }" @mousedown="startDrag($event, item.labelPosTag)" @mousemove="onDrag($event, item.labelPosTag)"
            @mouseup="stopDrag()">
            {{ item.label }}
        </div>
        <div v-for="(item, i) in overlayData" :key="'overlay_' + i" :style="{
            'position': 'absolute',
            'top': `${0 * elHeight + position[item.textPosTag].top}px`,
            'left': `${.05 * elWidth + item.x + (realWidth - elWidth) / 2 - 75 + position[item.textPosTag].left}px`,
            'width': '150px',
            'opacity': (overlayTag[5] == 1) && objectTag[item.objectName] == 1 ? 1 : 0,
            'padding': '3px',
            'border': '2px solid',
            'z-index': (overlayTag[5] == 1) && objectTag[item.objectName] == 1 ? 100 : 1,
            'border-color': (overlayTag[5] == 1) && objectTag[item.objectName] == 1 ? colorTrans(overlay_setting[overlay_map[5]].currentColor) : 'white',
            'border-radius': '10px',
            'background-color': 'white',
            'user-select': 'none',
            'cursor': 'grab'
        }" @mousedown="startDrag($event, item.textPosTag)" @mousemove="onDrag($event, item.textPosTag)"
            @mouseup="stopDrag()">
            {{ item.text }}
        </div>
        <div :style="{
            'position': 'absolute',
            'top': `${80 + position['legend'].top}px`,
            'left': `${30 + position['legend'].left}px`,
            'user-select': 'none',
            'cursor': 'grab',
            'z-index': 1000
        }" @mousedown="startDrag($event, 'legend')" @mousemove="onDrag($event, 'legend')" @mouseup="stopDrag()">
            <div style="display: flex;" v-for="(o, i) in chart_setting.attrName" :key="'legend_' + i">
                <div
                    :style="{ 'height': '20px', 'width': '20px', 'background-color': colorTrans(chart_setting.currentColor[o]), 'margin-right': '10px' }">
                </div>
                <div>{{ o }}</div>
            </div>
        </div>
    </div>
</template>
<script>
import { axisBottom, axisLeft, extent, line, scaleLinear, scalePoint, scaleUtc, select, timeFormat } from "d3";
import { useDataStore } from "@/stores/counter";
import description_data from "@/assets/data/description.json"
export default {
    name: "singleBar",
    props: ['rawData', 'chartData', 'defaultTag', 'scaleTag', 'stateTag'],
    data () {
        return {
            realHeight: 100,
            realWidth: 100,
            elHeight: 100,
            elWidth: 100,
            isShow: false,
            lineData: [],
            nodeData: [],
            overlayData: [],
            overlayTag: {},
            objectTag: {},
            axisPosition: {
                xAxis: [0, 0],
                yAxis: [0, 0]
            },
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
                },
                attrName: []
            },
            isDragging: false,
            startPosition: { legend: { x: 0, y: 0 } },
            position: { legend: { left: 0, top: 0 } }
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
                // console.log(id)
                this.position[id].left = event.clientX - this.startPosition[id].x;
                this.position[id].top = event.clientY - this.startPosition[id].y;
                // console.log(this.position.left)
                // console.log(id)
            }
        },
        stopDrag (id) {
            this.isDragging = false;
        },
        calcOverlay (nodeData, chartData) {
            // console.log(this.nodeData)
            let over_all = [];
            let pos_tag = 0;
            if (Object.keys(this.position).length == 1) {
                pos_tag = 1;
            }
            for (let c_i in chartData) {
                let over_data = chartData[c_i];
                let position = over_data.Position[0];
                let overlayData = {}
                if (position['Begin'][1] == position['End'][1]) {
                    for (let i in nodeData) {
                        if (nodeData[i].columnIndex == position['Begin'][0] && nodeData[i].rowIndex == position['Begin'][1]) {
                            // console.log(over_data)
                            overlayData = nodeData[i];
                            overlayData['textPosTag'] = 't' + c_i;
                            overlayData['labelPosTag'] = 'l' + c_i;
                            overlayData['label'] = over_data.GraphicalOverlay[0].Label[0];
                            overlayData['text'] = over_data.GraphicalOverlay[0].Text;
                            overlayData['objectName'] = over_data['ObjectName'];
                            break;
                        }
                    }
                    if (pos_tag) {
                        this.position[overlayData['textPosTag']] = { left: 0, top: 0 }
                        this.startPosition[overlayData['textPosTag']] = ({ x: 0, y: 0 });
                        this.position[overlayData['labelPosTag']] = { left: 0, top: 0 }
                        this.startPosition[overlayData['labelPosTag']] = ({ x: 0, y: 0 });
                    }
                }
                over_all.push(overlayData)
            }
            return over_all;
        },
        colorTrans (color) {
            return `rgba(${color.r}, ${color.g}, ${color.b}, ${color.a})`
        },
        translate (x, y) {
            return `translate(${x}, ${y})`;
        },
        scale (data, scaleName, scaleType, range) {
            let scale_data = [];
            // console.log(scaleType)
            // console.log(typeof(scaleName))
            if (typeof (scaleName) == 'object') {
                for (let i in data) {
                    if (i == 'columns') continue;
                    for (let j of scaleName) {
                        scale_data.push(data[i][j]);
                    }
                }
            } else {
                for (let i in data) {
                    if (i == 'columns') continue;
                    scale_data.push(data[i][scaleName]);
                }
            }
            if (scaleType == 'category') {
                return scalePoint(scale_data, range).padding(1);
            }
            if (scaleType == 'linear') {
                let dataDomain = extent(scale_data, d => parseFloat(d));
                if (dataDomain[1] < 0) dataDomain[1] = 0;
                if (dataDomain[0] > 0) dataDomain[0] = 0;
                // console.log(dataDomain);
                return scaleLinear(dataDomain, range);
            }
            if (scaleType == 'time') {
                let dataDomain = extent(scale_data, d => new Date(d));
                return scaleUtc(dataDomain, range);
            }
        },
        dataType (data, scaleType) {
            if (scaleType == 'time') {
                return new Date(data);
            }
            else {
                return data;
            }
        },
        calcLine (data, chart_info) {
            // if (this.defaultTag == 1) {
            let width = this.elWidth * .9;
            let xName = chart_info.chartScale.x.scaleName;
            let yName = chart_info.chartScale.y.scaleName;
            // console.log(chart_info);
            let currentColor = [];
            // for (let i of chart_info.chartScale.y.attributeName) {
            //     currentColor.push()
            // }

            this.chart_setting = {
                elWidth: this.elWidth,
                elHeight: this.elHeight,
                currentColor: chart_info.chartColor,
                size: {
                    width: 2
                },
                axis: {
                    x: xName,
                    y: yName
                },
                attrName: chart_info.chartScale.y.attributeName,
                isLegend: true
            }
            // console.log(this.chart_setting.attrName);
            // console.log(chart_info.chartScale.y.attributeName)
            const dataStore = useDataStore();
            dataStore.default_setting.chart_setting = this.chart_setting;
            dataStore.state_map['state' + dataStore.show_state]['chart_setting'] = this.chart_setting;
            // }
            // else {
            //     const dataStore = useDataStore();
            //     this.chart_setting = dataStore.defaultTag.chart_setting;
            // }
            // let width = this.chart_setting.elWidth * .9;
            let height = this.chart_setting.elHeight * .8;
            // let xName = chart_info.chartScale.x.attributeName;
            // let yName = chart_info.chartScale.y.attributeName[0];
            let xScale = this.scale(data, chart_info.chartScale.x.attributeName, chart_info.chartScale.x.scaleType, [0, width]);
            let yScale = this.scale(data, chart_info.chartScale.y.attributeName, chart_info.chartScale.y.scaleType, [height, 0]);
            // console.log(xScale, yScale);

            this.axisPosition = {
                xAxis: [width, .8 * this.elHeight + 30],
                yAxis: [-.05 * width, -20]
            }
            // console.log(yScale);
            let xAxis = (g, x, height) => {
                g.attr("transform", `translate(0, ${height})`)
                    .call(axisBottom(x))
            }
            let yAxis = (g, y) => {
                g.attr("transform", `translate(${0}, 0)`)
                    .call(axisLeft(y).ticks(5).tickSizeOuter(0))
            }
            select("#xAxis" + this.stateTag).call(xAxis, xScale, height);
            select("#yAxis" + this.stateTag).call(yAxis, yScale);
            let vm = this;
            function lineGenerator (data, y_attr) {
                return line().x(d => xScale(vm.dataType(d[chart_info.chartScale.x.attributeName], chart_info.chartScale.x.scaleType))).y(d => yScale(d[y_attr]))(data);
            }
            let lineData = new Array();
            let nodeData = new Array();
            for (let i in data) {
                for (let j of chart_info.chartScale.y.attributeName) {
                    nodeData.push({
                        rowIndex: i,
                        columnIndex: j,
                        x: xScale(this.dataType(data[i][chart_info.chartScale.x.attributeName], chart_info.chartScale.x.scaleType)),
                        y: yScale(data[i][j])
                    });
                }
                if (i == 0 || i == 'columns') continue;
                for (let j of chart_info.chartScale.y.attributeName)
                    lineData.push({
                        path: lineGenerator([data[i], data[i - 1]], j),
                        fill: chart_info.chartColor[j],
                        data: [data[i - 1], data[i]],
                        attr: j
                    })
            }
            this.nodeData = nodeData;
            // console.log(lineData);
            return lineData;
        }
    },
    created () {
    },
    mounted () {
        // this.elHeight = this.$refs.singleLineSvg.offsetHeight;
        // this.elWidth = this.$refs.singleLineSvg.offsetWidth;
        this.realHeight = document.getElementById('mainView').offsetHeight;
        this.realWidth = document.getElementById('mainView').offsetWidth;
        this.elHeight = document.getElementById('mainView').offsetHeight;
        this.elWidth = document.getElementById('mainView').offsetWidth;
        // console.log(this.rawData, this.chartData);
        if (this.elHeight / 9 * 16 < this.elWidth) {
            this.elWidth = this.elHeight / 9 * 16;
        } else {
            this.elHeight = this.elWidth / 16 * 9;
        }
        this.lineData = this.calcLine(this.rawData, this.chartData);
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations, state) => {
            if (this.defaultTag == 1) {
                this.chart_setting = dataStore.state_map[this.stateTag]['chart_setting'];
            }
            this.overlayData = this.calcOverlay(this.nodeData, dataStore.graphicalOverlayData);
            let selObj = dataStore.selectObject;
            if (selObj != '') {
                // console.log()
                if (selObj == -1) {
                    this.overlayTag = [0, 0, 0, 0, 0, 0, 0, 0, 0];
                } else {
                    // console.log(selObj, dataStore.state_map[this.stateTag]['overlay_setting'][selObj]);
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
    font-family: 'operator Mono Lig';
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
