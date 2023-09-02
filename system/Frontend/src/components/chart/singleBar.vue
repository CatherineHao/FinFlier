<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-07-10 13:45:50
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-09-02 00:37:36
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
                            <g>
                                <g v-if="overlayTag[2] == 1" class="animation-fade">
                                    <!-- <g> -->
                                    <rect v-for="(o, oi) in item.background.rectInfo" :key="'oi_' + oi"
                                        :x="o.x - 3 - chart_setting.size.width / 2" :y="0"
                                        :fill="colorTrans(overlay_setting[overlay_map[2]].currentColor)"
                                        :width="chart_setting.size.width + 6" :height="elHeight * .8" opacity="0.6">
                                    </rect>
                                    <!-- </g> -->
                                </g>
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
                            <rect :x="item.x - chart_setting.size.width / 2" :y="item.y"
                                :fill="colorTrans(chart_setting.currentColor)" :width="chart_setting.size.width"
                                :height="item.height"></rect>
                        </g>
                    </g>
                </g>
                <!-- Overlay -->
                <g id="overlay">
                    <g v-for="(item, i) in overlayData" :key="'overlay_' + i">
                        <Transition>
                            <g v-if="objectTag[item.objectName] == 1" style="transition: 0.4s;">
                                <g>
                                    <g v-if="overlayTag[0] == 1">
                                        <rect v-for="(o, oi) in item.color.rectInfo" :key="'oi_' + oi"
                                            :x="o.x - chart_setting.size.width / 2" :y="o.y"
                                            :fill="colorTrans(overlay_setting[overlay_map[0]].currentColor)"
                                            :width="chart_setting.size.width" :height="o.height" opacity="1"></rect>
                                    </g>
                                    <g v-if="overlayTag[1] == 1">
                                        <rect v-for="(o, oi) in item.bounding_box.rectInfo" :key="'oi_' + oi"
                                            :x="o.x - chart_setting.size.width / 2" :y="o.y" :fill="'none'"
                                            :width="chart_setting.size.width" :height="o.height"
                                            :stroke="colorTrans(overlay_setting[overlay_map[1]].currentColor)"
                                            :stroke-width="3" :stroke-dasharray="5.5" opacity="1"></rect>
                                    </g>
                                </g>
                                <g>
                                    <g v-if="overlayTag[3] == 1">
                                        <circle v-for="(o, oi) in item.marker.pos" :key="'oi_' + oi" :cx="o.x" :cy="o.y"
                                            r="7" :fill="colorTrans(overlay_setting[overlay_map[3]].currentColor)"></circle>
                                    </g>
                                    <g v-if="overlayTag[4] == 1">
                                        <path v-for="(o, oi) in item.label.pos" :key="'oi_' + oi"
                                            :d="'M' + o.x + ',' + (o.y) + 'L' + o.x + ',' + -10" fill="none"
                                            :stroke="colorTrans(overlay_setting[overlay_map[4]].currentColor)"
                                            stroke-width="3"></path>
                                    </g>
                                    <g v-if="overlayTag[5] == 1">
                                        <path v-if="item.text.lineTag == 1"
                                            :d="'M' + item.text.pos.x + ',' + (item.text.pos.y) + 'L' + item.text.pos.x + ',' + 0"
                                            fill="none" :stroke="colorTrans(overlay_setting[overlay_map[5]].currentColor)"
                                            stroke-width="3"></path>
                                    </g>
                                    <g v-if="overlayTag[6] == 1">
                                        <defs>
                                            <marker id="triangle" viewBox="0 0 10 10" refX="9" refY="5"
                                                markerUnits="strokeWidth" markerWidth="10" markerHeight="10" orient="auto">
                                                <path d="M 0 0 L 10 5 L 0 10 z" :fill="colorTrans(overlay_setting[overlay_map[6]].currentColor)" />
                                            </marker>
                                        </defs>
                                        <path
                                            :d="'M' + item.trend.pos.x1 + ',' + item.trend.pos.y1 + 'L' + item.trend.pos.x2 + ',' + item.trend.pos.y2"
                                            :stroke-width="3" marker-end="url(#triangle)"
                                            :stroke="colorTrans(overlay_setting[overlay_map[6]].currentColor)" fill="none">
                                        </path>
                                    </g>
                                    <g v-if="overlayTag[7] == 1">
                                        <path
                                            :d="'M' + (item.overall.pos.x1 - chart_setting.size.width / 2 - 10) + ',' + item.overall.pos.y + 'L' +( item.overall.pos.x2 + chart_setting.size.width / 2 + 10)+ ',' + item.overall.pos.y"
                                            :stroke-width="3"
                                            :stroke="colorTrans(overlay_setting[overlay_map[7]].currentColor)" fill="none">
                                        </path>
                                    </g>
                                    <g v-if="overlayTag[8] == 1">
                                        <path
                                            :d="'M' + item.special.pos.x + ',0' + 'L' + item.special.pos.x + ',' + (elHeight * .8)"
                                            :stroke-width="5"
                                            :stroke="colorTrans(overlay_setting[overlay_map[8]].currentColor)" fill="none">
                                        </path>
                                    </g>
                                </g>
                            </g>
                        </Transition>
                    </g>
                </g>
            </g>
        </svg>
        <div v-for="(item, i) in overlayData" :key="'overlay_' + i" :style="{
            'position': 'absolute',
            'top': `${.1 * elHeight}px`,
            'left': `${item.text.pos.x + .05 * elWidth - 75}px`,
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
            <div v-for="(o, oi) in item.label.pos" :key="'oi_' + oi" :style="{
                'position': 'absolute',
                'top': `${.1 * elHeight}px`,
                'left': `${o.x + .05 * elWidth - 75}px`,
                'width': '150px',
                'transition': '0.4s',
                'opacity': objectTag[item.objectName] == 1 && overlayTag[4] == 1 ? '1' : '0',
                'padding': '3px',
                'border': '2px solid',
                'border-radius': '10px',
                'background-color': 'white',
                'border-color': objectTag[item.objectName] == 1 && overlayTag[4] == 1 ? colorTrans(overlay_setting[overlay_map[5]].currentColor) : 'color',
            }">
                {{ item.label.text[oi] }}
            </div>
        </div>
    </div>
</template>
<script>
import { axisBottom, axisLeft, extent, scaleLinear, scalePoint, select } from "d3";
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
            overlayData_test: [],
            overlayTag: {},
            objectTag: {},
            axisPosition: {
                xAxis: [0, 0],
                yAxis: [0, 0]
            },
            overlay_setting: {},
            xScale: null,
            yScale: null,
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
        calcOverlay (barData, chartData) {
            // console.log(barData, chartData);
            let over_all = [];
            for (let c_i in chartData) {
                let over_data = chartData[c_i];
                // console.log(over_data);
                let position = over_data.Position[0];
                let overlayData = {
                    'objectName': over_data['ObjectName'],
                    'color': {
                        tag: 1,
                        rectInfo: null
                    },
                    'bounding_box': {
                        tag: 1,
                        rectInfo: null
                    },
                    'background': {
                        tag: 1,
                        rectInfo: null
                    },
                    'marker': { tag: 1, pos: [] },
                    'label': { tag: 1, pos: [], text: [] },
                    'text': { tag: 1, lineTag: 1, pos: [], text: '' },
                    'trend': { tag: -1, pos: [] },
                    'overall': { tag: -1, pos: [] },
                    'special': { tag: 1, pos: [] }
                }
                if (position['Begin'][1] == position['End'][1]) {
                    overlayData.label.text = over_data.GraphicalOverlay[0].Label[0];
                    overlayData.text.text = over_data.GraphicalOverlay[0].Text;
                    let cnt = parseInt(position['Begin'][1]);
                    let rectInfo = barData[cnt];
                    let pos = {
                        x: barData[cnt].x,
                        y: barData[cnt].y
                    };
                    overlayData.label.pos = [pos];
                    overlayData.text.pos = pos;
                    overlayData.marker.pos = [pos];
                    overlayData.background.rectInfo = [rectInfo];
                    overlayData.color.rectInfo = [rectInfo];
                    overlayData["bounding_box"].rectInfo = [rectInfo];
                } else {
                    let pos = [];
                    let rectInfo = [];
                    let begin_pos = parseInt(position['Begin'][1]);
                    let end_pos = parseInt(position['End'][1])
                    for (let i = begin_pos; i <= end_pos; ++i) {
                        let cnt = i;
                        pos.push({
                            x: barData[cnt].x,
                            y: barData[cnt].y
                        });
                        rectInfo.push(barData[cnt]);
                    }
                    overlayData.marker.pos = pos;
                    overlayData.text.lineTag = -1;
                    overlayData.text.text = over_data.GraphicalOverlay[0].Text;
                    overlayData.text.pos = {
                        x: (barData[begin_pos].x + barData[end_pos].x) / 2,
                        y: (barData[begin_pos].y + barData[end_pos].y) / 2
                    }
                    if (over_data.GraphicalOverlay[0].Label.length == 1) {
                        overlayData.label.pos = [{
                            x: barData[begin_pos].x,
                            y: barData[begin_pos].y
                        }]
                    } else {
                        overlayData.label.pos = [{
                            x: barData[begin_pos].x,
                            y: barData[begin_pos].y
                        }, {
                            x: barData[end_pos].x,
                            y: barData[end_pos].y
                        }]
                    }
                    overlayData.label.text = over_data.GraphicalOverlay[0].Label;
                    overlayData.background.rectInfo = rectInfo;
                    overlayData.color.rectInfo = rectInfo;
                    overlayData["bounding_box"].rectInfo = rectInfo;
                    overlayData.overall.pos = {
                        x1: barData[begin_pos].x,
                        x2: barData[end_pos].x,
                        y: this.yScale(parseFloat(over_data.GraphicalOverlay[0].Line.mean))
                    };
                    overlayData.trend.pos = {
                        x1: barData[begin_pos].x,
                        x2: barData[end_pos].x,
                        y1: barData[begin_pos].y,
                        y2: barData[end_pos].y,
                    }
                }

                overlayData.special.pos = {
                    x: barData[parseInt(position['Begin'][1])].x,
                    y: barData[parseInt(position['Begin'][1])].y
                };


                console.log(overlayData);
                // overlayData.marker.tag = 1;
                // for (let i = parseInt(position['Begin'][1]); i <= parseInt(position['End'][1]); ++i) {
                //     let cnt = i;
                //     let cnt_tag = 0;
                //     if (i == barData.length) {
                //         cnt--;
                //         cnt_tag = 1;
                //     }
                //     if (cnt_tag == 0)
                //         overlayData.marker.pos.push(barData[cnt]['pos1']);
                //     else
                //         overlayData.marker.pos.push(barData[cnt]['pos2']);
                // }
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
        calcBar (data, chart_info) {
            if (this.defaultTag == 1) {
                let width = this.elWidth * .9;
                let xName = chart_info.chartScale.x.scaleName;
                let yName = chart_info.chartScale.y.scaleName;
                console.log(chart_info);
                this.chart_setting = {
                    elWidth: this.elWidth,
                    elHeight: this.elHeight,
                    currentColor: chart_info.chartColor[chart_info.chartScale.y.attributeName[0]],
                    size: {
                        width: (width / data.length > 20) ? .5 * (width / data.length) : (width / data.length)
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
            }
            else {
                const dataStore = useDataStore();
                this.chart_setting = dataStore.defaultTag.chart_setting;
            }
            let width = this.chart_setting.elWidth * .9;
            let height = this.chart_setting.elHeight * .8;
            let xName = chart_info.chartScale.x.scaleName;
            let yName = chart_info.chartScale.y.scaleName;
            let xScale = this.scale(data, chart_info.chartScale.x.attributeName, chart_info.chartScale.x.scaleType, [0, width]);
            let yScale = this.scale(data, chart_info.chartScale.y.attributeName[0], chart_info.chartScale.y.scaleType, [height, 0]);
            this.xScale = xScale;
            this.yScale = yScale;
            // console.log(xScale, yScale);
            this.axisPosition = {
                xAxis: [width, yScale(0) + 30],
                yAxis: [-.05 * width, -20]
            }
            // console.log(yScale);
            let xAxis = (g, x, height) => {
                g.attr("transform", `translate(0, ${height})`)
                    .call(axisBottom(x))
                // .call(g => g.selectAll(".title").data([title]).join("text")
                //     .attr("class", "title")
                //     .attr("x", width - 10)
                //     .attr("y", 18)
                //     .attr("fill", "currentColor")
                //     .attr("text-anchor", "start")
                //     .text(title))
            }
            let yAxis = (g, y) => {
                g.attr("transform", `translate(${0}, 0)`)
                    .call(axisLeft(y).ticks(5).tickSizeOuter(0))
                // .call(g => g.select(".domain").remove())
                // .call(g => g.selectAll(".title").data([title]).join("text")
                //     .attr("class", "title")
                //     .attr("x", -.05 * width)
                //     .attr("y", -20)
                //     .attr("fill", "currentColor")
                //     .attr("text-anchor", "start")
                //     .text(title))
            }
            select("#xAxis").call(xAxis, xScale, height);
            select("#yAxis").call(yAxis, yScale);
            // console.log('log 1')
            let barData = new Array();
            for (let i in data) {
                if (i == 'columns') continue;
                // console.log(data[i], data[i][chart_info.chartScale.x.attributeName], data[i][chart_info.chartScale.y.attributeName[0]])
                barData.push({
                    x: xScale(data[i][chart_info.chartScale.x.attributeName]),
                    y: yScale(data[i][chart_info.chartScale.y.attributeName[0]]),
                    fill: chart_info.chartColor[chart_info.chartScale.y.attributeName[0]],
                    data: data[i],
                    width: (width / data.length > 20) ? .5 * (width / data.length) : (width / data.length),
                    height: height - yScale(data[i][chart_info.chartScale.y.attributeName[0]])
                });
            }
            console.log(barData)
            return barData;
        }
    },
    created () {
    },
    mounted () {
        this.elHeight = this.$refs.singleBarSvg.offsetHeight;
        this.elWidth = this.$refs.singleBarSvg.offsetWidth;

        this.barData = this.calcBar(this.rawData, this.chartData)

        // this.overlayData = description_data;
        // console.log(this.overlayData);
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations) => {
            this.chart_setting = dataStore.state_map['state0']['chart_setting'];
            this.overlayTag = dataStore.state_map['state0']['overlay_tag'];
            // console.log(dataStore.state_map['state0']['overlay_setting'])
            this.overlayData = this.calcOverlay(this.barData, dataStore.graphicalOverlayData);
            this.overlay_setting = dataStore.state_map['state0']['overlay_setting']['object0'];
            console.log(this.overlay_setting)
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
}
</style>
