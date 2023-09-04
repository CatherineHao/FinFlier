<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-26 19:48:52
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-27 20:46:06
-->
<template>
    <div ref="singleBarSvg" style="height: 100%; width: 100%;">
        <svg height="100%" width="100%" xmlns="http://www.w3.org/2000/svg" :style="{
            'transition': '0.4s',
            'opacity': isShow == true ? '1' : '0',
            'transform': `scale(${scaleTag})`
        }">
            <g id="mainSingleBar_g" :transform="translate(.05 * elWidth, .1 * elHeight)">
                <g v-for="(item, i) in overlayData" :key="'overlay_' + i">
                    <Transition>
                        <g v-if="objectTag[item.objectName] == 1" style="transition: 0.4s;">
                            <g v-if="overlayTag[2] == 1" class="animation-fade">
                                <rect v-for="(o, oi) in item.selectBar" :key="'oi_' + oi"
                                    :x="o.x - (o.length - o.cnt - 1) * chart_setting.size.width / o.length + (o.length - 2) / 2 * chart_setting.size.width / o.length - 3"
                                    :y="0" :fill="colorTrans(overlay_setting[overlay_map[2]].currentColor)"
                                    :width="chart_setting.size.width / o.length + 6" :height="elHeight * .8" opacity="1">
                                </rect>
                            </g>
                        </g>
                    </Transition>
                </g>
                <g>
                    <g id="xAxis"></g>
                    <g id="yAxis"></g>
                    <g id="axis_name">
                        <text class="title" text-anchor="end"
                            :transform="translate(axisPosition.xAxis[0], axisPosition.xAxis[1])">{{ chart_setting.axis.x }}</text>
                        <text class="title" text-anchor="start"
                            :transform="translate(axisPosition.yAxis[0], axisPosition.yAxis[1])">{{ chart_setting.axis.y }}</text>
                    </g>
                    <g id="bar">
                        <g v-for="(item, i) in barData" :key="'single_bar_' + i">
                            <rect
                                :x="item.x - (item.length - item.cnt - 1) * chart_setting.size.width / item.length + (item.length - 2) / 2 * chart_setting.size.width / (item.length)"
                                :y="item.y" :fill="colorTrans(chart_setting.currentColor[item.yName])"
                                :width="chart_setting.size.width / item.length" :height="item.height"></rect>
                        </g>
                    </g>
                </g>
                <g v-for="(item, i) in overlayData" :key="'overlay_' + i">
                    <Transition>
                        <g v-if="objectTag[item.objectName] == 1" style="transition: 0.4s;">
                            <g v-if="overlayTag[0] == 1" class="animation-fade">
                                <rect v-for="(o, oi) in item.selectBar" :key="'oi_' + oi"
                                    :x="o.x - (o.length - o.cnt - 1) * chart_setting.size.width / o.length + (o.length - 2) / 2 * chart_setting.size.width / o.length"
                                    :y="o.y" :fill="colorTrans(overlay_setting[overlay_map[0]].currentColor)"
                                    :width="chart_setting.size.width / o.length" :height="o.height" opacity="1">
                                </rect>
                            </g>
                            <g v-if="overlayTag[1] == 1" class="animation-fade">
                                <rect v-for="(o, oi) in item.selectBar" :key="'oi_' + oi"
                                    :x="o.x - (o.length - o.cnt - 1) * chart_setting.size.width / o.length + (o.length - 2) / 2 * chart_setting.size.width / o.length"
                                    :y="o.y" :stroke="colorTrans(overlay_setting[overlay_map[1]].currentColor)" fill="none"
                                    stroke-width="3" :width="chart_setting.size.width / o.length" :height="o.height"
                                    opacity="1">
                                </rect>
                            </g>
                            <g v-if="overlayTag[3] == 1" class="animation-fade">
                                <circle v-for="(o, oi) in item.selectBar" :key="'oi_' + oi"
                                    :cx="o.x - (o.length - o.cnt - 1) * chart_setting.size.width / o.length + (o.length - 2) / 2 * chart_setting.size.width / o.length + chart_setting.size.width / (2 * o.length)"
                                    :cy="o.y" r="10" :fill="colorTrans(overlay_setting[overlay_map[3]].currentColor)"
                                    stroke="none" opacity="1">
                                </circle>
                            </g>
                            <g v-if="overlayTag[4] == 1" class="animation-fade">
                                <path v-for="(o, oi) in item.label" :key="'oi_' + oi"
                                    :d="'M' + (o.x + o.transTag * chart_setting.size.width / o.length) + ',' + (o.y) + 'L' + (o.x + o.transTag * chart_setting.size.width / o.length) + ',' + -(.1 * elHeight)"
                                    fill="none" :stroke="colorTrans(overlay_setting[overlay_map[4]].currentColor)"
                                    stroke-width="3">
                                </path>
                            </g>

                            <g v-if="overlayTag[5] == 1" class="animation-fade">
                                <path
                                    :d="'M' + (item.text.x + item.transTag * chart_setting.size.width / item.text.length) + ',' + (item.text.y) + 'L' + (item.text.x + item.transTag * chart_setting.size.width / item.text.length) + ',' + -(.1 * elHeight)"
                                    fill="none" :stroke="colorTrans(overlay_setting[overlay_map[5]].currentColor)"
                                    stroke-width="3"></path>
                            </g>
                            <g v-if="overlayTag[6] == 1" class="animation-fade">
                                
                            <defs>
                                <marker id="triangle" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth"
                                    markerWidth="10" markerHeight="10" orient="auto">
                                    <path d="M 0 0 L 10 5 L 0 10 z"
                                        :fill="colorTrans(overlay_setting[overlay_map[6]].currentColor)" />
                                </marker>
                            </defs>
                                <path
                                    :d="'M' + (item.trend[0].x + item.transTag * chart_setting.size.width / item.trend[0].length) + ',' + (item.trend[0].y) + 'L' + (item.trend[1].x + item.transTag * chart_setting.size.width / item.trend[1].length) + ',' + item.trend[1].y"
                                    fill="none" :stroke="colorTrans(overlay_setting[overlay_map[6]].currentColor)"
                                    stroke-width="3" marker-end="url(#triangle)"></path>
                            </g>
                        </g>
                    </Transition>
                </g>
            </g>
        </svg>

        <div v-for="(item, i) in overlayData" :key="'overlay_' + i" :style="{
            'position': 'absolute',
            'top': `${0 * elHeight}px`,
            'left': `${item.text.x + item.transTag * chart_setting.size.width / item.text.length + .05 * elWidth - 75}px`,
            'width': '150px',
            'transition': '0.4s',
            'opacity': objectTag[item.objectName] == 1 && overlayTag[5] == 1 ? '1' : '0',
            'padding': '3px',
            'border': '2px solid',
            'border-radius': '10px',
            'background-color': 'white',
            'border-color': objectTag[item.objectName] == 1 && overlayTag[5] == 1 ? colorTrans(overlay_setting[overlay_map[5]].currentColor) : 'color',
        }">
            {{ item.text.text }}
        </div>
        <div v-for="(item, i) in overlayData" :key="'overlay_' + i" style="position: absolute; top: 0px; left: 0px;">
            <div v-for="(o, oi) in item.label" :key="'oi_' + oi" :style="{
                'position': 'absolute',
                'top': `${0 * elHeight}px`,
                'left': `${o.x + o.transTag * chart_setting.size.width / o.length + .05 * elWidth - 75}px`,
                'width': '150px',
                'transition': '0.4s',
                'opacity': objectTag[item.objectName] == 1 && overlayTag[4] == 1 ? '1' : '0',
                'padding': '3px',
                'border': '2px solid',
                'border-radius': '10px',
                'background-color': 'white',
                'border-color': objectTag[item.objectName] == 1 && overlayTag[4] == 1 ? colorTrans(overlay_setting[overlay_map[5]].currentColor) : 'white',
            }">
                {{ item.label[oi].text }}
            </div>
        </div>
    </div>
</template>

<script>
import { axisBottom, axisLeft, extent, scaleLinear, scalePoint, scaleUtc, select } from "d3";
import { useDataStore } from "@/stores/counter";
export default {
    name: "singleBar",
    props: ['rawData', 'chartData', 'defaultTag', 'scaleTag'],
    data () {
        return {
            elHeight: 100,
            elWidth: 100,
            isShow: false,
            barData: [],
            overlayData: [],
            overlayTag: {},
            objectTag: {},
            axisPosition: {
                xAxis: [0, 0],
                yAxis: [0, 0]
            },
            xScale: null,
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
            }
        };
    },
    methods: {
        colorTrans (color) {
            return `rgba(${color.r}, ${color.g}, ${color.b}, ${color.a})`
        },
        calcOverlay (barData, chartData, scaleType) {
            let overall_data = [];
            for (let c_i in chartData) {
                let over_data = chartData[c_i];
                let selectRectTag = {};
                let selectBar = [];
                let overlayData = {
                    'objectName': over_data['ObjectName'],
                    transTag: parseFloat(over_data['GraphicalOverlay'][0]['transTag']),
                    selectBar: [],
                    label: [],
                    text: [],
                    trend: []
                }
                for (let j in chartData[c_i].Position) {
                    let t_pos = chartData[c_i].Position[j];
                    let rowName = t_pos['Begin'][0];
                    for (let k = t_pos['Begin'][1]; k <= t_pos['End'][1]; ++k) {
                        selectRectTag['R_' + rowName + '_C_' + k.toString()] = 1;
                    }
                }
                for (let i in barData) {
                    if (selectRectTag['R_' + barData[i].yName + '_C_' + barData[i].rowIndex] == 1) {
                        selectBar.push(barData[i]);
                    }
                }
                let labelData = [];
                let textData = [];
                let trendData = [];
                for (let i in over_data['GraphicalOverlay'][0]['LabelPos']) {
                    let t_d = over_data['GraphicalOverlay'][0]['LabelPos'][i];
                    labelData.push({
                        x: this.xScale(this.dataType(t_d.x, scaleType)),
                        y: this.yScale(t_d.y),
                        text: t_d.text,
                        transTag: parseFloat(over_data['GraphicalOverlay'][0]['transTag']),
                        length: barData[0].length
                    });
                    if (i == 0) {
                        textData = {
                            x: this.xScale(this.dataType(t_d.x, scaleType)),
                            y: this.yScale(t_d.y),
                            text: over_data['GraphicalOverlay'][0]['Text'],
                            transTag: parseFloat(over_data['GraphicalOverlay'][0]['transTag']),
                            length: barData[0].length
                        };
                    }
                }
                for (let i in over_data['GraphicalOverlay'][0]['Line']['pos']) {
                    let t_d = over_data['GraphicalOverlay'][0]['Line']['pos'][i];
                    trendData.push({
                        x: this.xScale(this.dataType(t_d.x, scaleType)),
                        y: this.yScale(t_d.y),
                        text: t_d.text,
                        transTag: parseFloat(over_data['GraphicalOverlay'][0]['transTag']),
                        length: barData[0].length
                    })
                }
                overlayData.selectBar = selectBar;
                overlayData.label = labelData;
                overlayData.text = textData;
                overlayData.trend = trendData;
                overall_data.push(overlayData);
            }
            return overall_data;
        },
        translate (x, y) {
            return `translate(${x}, ${y})`;
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
                if (dataDomain[0] > 0) dataDomain[0] = 0;
                if (dataDomain[1] < .7) dataDomain[1] = .7;
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
            } else {
                return data;
            }
        },
        calcBar (data, chart_info) {
            if (this.defaultTag == 1) {
                let width = this.elWidth * .9;
                let xName = chart_info.chartScale.x.scaleName;
                let yName = chart_info.chartScale.y.scaleName;
                // console.log(chart_info);
                let currentColor = {}
                for (let i in chart_info.chartScale.y.attributeName) {
                    currentColor[chart_info.chartScale.y.attributeName[i]] = (chart_info.chartColor[chart_info.chartScale.y.attributeName[i]]);
                }
                this.chart_setting = {
                    elWidth: this.elWidth,
                    elHeight: this.elHeight,
                    currentColor: currentColor,
                    size: {
                        width: (width / data.length > 20) ? .8 * (width / data.length) : (width / data.length)
                    },
                    axis: {
                        x: xName,
                        y: yName
                    }
                }
                // console.log(this.chart_setting);
                const dataStore = useDataStore();
                dataStore.default_setting.chart_setting = this.chart_setting;
                dataStore.state_map['state' + dataStore.show_state]['chart_setting'] = this.chart_setting;
            } else {
                const dataStore = useDataStore();
                this.chart_setting = dataStore.defaultTag.chart_setting;
            }
            let width = this.chart_setting.elWidth * .9;
            let height = this.chart_setting.elHeight * .8;
            let xName = chart_info.chartScale.x.scaleName;
            let yName = chart_info.chartScale.y.scaleName;
            let xScale = this.scale(data, chart_info.chartScale.x.attributeName, chart_info.chartScale.x.scaleType, [0, width]);
            this.xScale = xScale;
            let yScale = this.scale(data, chart_info.chartScale.y.attributeName[0], chart_info.chartScale.y.scaleType, [height, 0]);
            this.yScale = yScale;
            this.axisPosition = {
                xAxis: [width, yScale(0) + 20],
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
            select("#xAxis").call(xAxis, xScale, height);
            select("#yAxis").call(yAxis, yScale);
            let barData = new Array();
            for (let i in data) {
                if (i == 'columns') continue;
                let yLen = chart_info.chartScale.y.attributeName.length;
                for (let j in chart_info.chartScale.y.attributeName) {
                    let yName = chart_info.chartScale.y.attributeName[j];
                    barData.push({
                        x: xScale(this.dataType(data[i][chart_info.chartScale.x.attributeName], chart_info.chartScale.x.scaleType)),
                        y: yScale(data[i][yName]),
                        length: yLen,
                        cnt: j,
                        yName: yName,
                        fill: chart_info.chartColor[chart_info.chartScale.y.attributeName[j]],
                        data: data[i],
                        width: (width / data.length > 20) ? .5 * (width / data.length) : (width / data.length),
                        height: height - yScale(data[i][chart_info.chartScale.y.attributeName[j]]),
                        rowIndex: i,
                        columnIndex: j
                    });
                }
            }
            return barData;
        }
    },
    created () { },
    mounted () {
        this.elHeight = this.$refs.singleBarSvg.offsetHeight;
        this.elWidth = this.$refs.singleBarSvg.offsetWidth;
        if (this.elHeight / 9 * 16 < this.elWidth) {
            this.elWidth = this.elHeight / 9 * 16;
        } else {
            this.elHeight = this.elWidth / 16 * 9;
        }

        this.barData = this.calcBar(this.rawData, this.chartData)

        // console.log(this.overlayData);
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations) => {
            // console.log(mutations.events.key == "overlayTag");
            // if (mutations.events.key == "overlayTag") {
            //     console.log(this.overlayTag);
            this.chart_setting = dataStore.state_map['state0']['chart_setting'];
            // console.log(this.overlayData);
            this.overlayTag = dataStore.state_map['state0']['overlay_tag'];
            this.overlayData = this.calcOverlay(this.barData, dataStore.graphicalOverlayData, this.chartData.chartScale.x.scaleType);
            // console.log(dataStore.state_map['state0']['overlay_setting'])
            this.overlay_setting = dataStore.state_map['state0']['overlay_setting']['object0'];
            // console.log(this.overlay_setting[this.overlay_map[2]], this.overlay_map[2]);

            // }
            // if (mutations.events.key == "objectTag") {
            this.objectTag = dataStore.objectTag;
            //     console.log(this.objectTag);
            // }
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
}
</style>
