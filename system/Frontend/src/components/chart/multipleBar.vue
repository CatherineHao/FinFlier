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
                        </g>
                    </Transition>
                </g>
            </g>
        </svg>
    </div>
</template>
<script>
import { axisBottom, axisLeft, extent, scaleLinear, scalePoint, scaleUtc, select } from "d3";
import { useDataStore } from "@/stores/counter";
import description_data from "@/assets/data/description.json"
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
            overlay_setting: {},
            overlay_map: ['color', 'bounding box', 'background', 'marker', 'label', 'text'],
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
        calcOverlay (barData, chartData) {
            console.log(barData, chartData);
            let overall_data = [];
            for (let c_i in chartData) {
                let over_data = chartData[c_i];
                let selectRectTag = {};
                let selectBar = [];
                let overlayData = {
                    'objectName': over_data['ObjectName'],
                    selectBar: []
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
                // console.log(selectBar);
                overlayData.selectBar = selectBar;
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
            }
            else {
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
            this.axisPosition = {
                xAxis: [width, yScale(0) + 20],
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
    created () {
    },
    mounted () {
        this.elHeight = this.$refs.singleBarSvg.offsetHeight;
        this.elWidth = this.$refs.singleBarSvg.offsetWidth;

        this.barData = this.calcBar(this.rawData, this.chartData)

        // console.log(this.overlayData);
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations) => {
            // console.log(mutations.events.key == "overlayTag");
            // if (mutations.events.key == "overlayTag") {
            //     console.log(this.overlayTag);
            this.chart_setting = dataStore.state_map['state0']['chart_setting'];
            this.overlayData = this.calcOverlay(this.barData, dataStore.graphicalOverlayData);
            // console.log(this.overlayData);
            this.overlayTag = dataStore.state_map['state0']['overlay_tag'];
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
