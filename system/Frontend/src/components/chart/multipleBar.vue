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
                            <g>
                                <g v-if="overlayTag[2] == 1" class="animation-fade">
                                    <rect :x="barData[item.objectIndex].x - 3 - barData[item.objectIndex].width / 2" :y="0"
                                        :fill="colorTrans(overlay_setting[overlay_map[2]].currentColor)"
                                        :width="barData[item.objectIndex].width + 6" :height="elHeight * .8" opacity="0.6">
                                    </rect>
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
                                        <rect :x="barData[item.objectIndex].x - barData[item.objectIndex].width / 2"
                                            :y="barData[item.objectIndex].y"
                                            :fill="colorTrans(overlay_setting[overlay_map[0]].currentColor)"
                                            :width="barData[item.objectIndex].width"
                                            :height="barData[item.objectIndex].height" opacity="1"></rect>
                                    </g>
                                    <g v-if="overlayTag[1] == 1">
                                        <rect :x="barData[item.objectIndex].x - barData[item.objectIndex].width / 2"
                                            :y="barData[item.objectIndex].y" :fill="'none'"
                                            :width="barData[item.objectIndex].width"
                                            :height="barData[item.objectIndex].height"
                                            :stroke="colorTrans(overlay_setting[overlay_map[1]].currentColor)"
                                            :stroke-width="3" :stroke-dasharray="5.5" opacity="1"></rect>
                                    </g>
                                </g>
                                <g>
                                    <g v-if="overlayTag[3] == 1">
                                        <circle :cx="barData[item.objectIndex].x" :cy="barData[item.objectIndex].y" r="7"
                                            :fill="colorTrans(overlay_setting[overlay_map[3]].currentColor)"></circle>
                                    </g>
                                    <g v-if="overlayTag[4] == 1">
                                        <circle :cx="barData[item.objectIndex].x"
                                            :cy="barData[item.objectIndex].y + barData[item.objectIndex].height / 2" r="7"
                                            :fill="colorTrans(overlay_setting[overlay_map[4]].currentColor)"></circle>
                                        <path
                                            :d="'M' + barData[item.objectIndex].x + ',' + (barData[item.objectIndex].y + barData[item.objectIndex].height / 2) + 'L' + barData[item.objectIndex].x + ',' + -10"
                                            fill="none" :stroke="colorTrans(overlay_setting[overlay_map[4]].currentColor)"
                                            stroke-width="3"></path>
                                        <text :x="barData[item.objectIndex].x" :y="-20" text-anchor="middle">
                                            {{ item.overlay.annotation.label }}
                                        </text>
                                    </g>
                                    <g v-if="overlayTag[5] == 1">
                                        <circle :cx="barData[item.objectIndex].x"
                                            :cy="barData[item.objectIndex].y + barData[item.objectIndex].height / 2" r="7"
                                            :fill="colorTrans(overlay_setting[overlay_map[5]].currentColor)"></circle>
                                        <path
                                            :d="'M' + barData[item.objectIndex].x + ',' + (barData[item.objectIndex].y + barData[item.objectIndex].height / 2) + 'L' + barData[item.objectIndex].x + ',' + 0"
                                            fill="none" :stroke="colorTrans(overlay_setting[overlay_map[5]].currentColor)"
                                            stroke-width="3"></path>
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
            'left': `${barData[item.objectIndex].x + .05 * elWidth - 75}px`,
            'width': '150px',
            'transition': '0.4s',
            'opacity': objectTag[item.objectName] == 1 && overlayTag[5] == 1 ? '1' : '0',
            'padding': '3px',
            'border': '2px solid',
            'border-radius': '10px',
            'background-color': 'white'
        }">
            <!-- 'border-color': colorTrans(overlay_setting[overlay_map[5]].currentColor), -->
            {{ item.overlay.annotation.text }}
        </div>
    </div>
</template>
<script>
import { axisBottom, axisLeft, extent, scaleLinear, scalePoint, select } from "d3";
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
                console.log(dataDomain);
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
            console.log(xScale, yScale);
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
            console.log('log 1')
            let barData = new Array();
            for (let i in data) {
                if (i == 'columns') continue;
                console.log(data[i], data[i][chart_info.chartScale.x.attributeName], data[i][chart_info.chartScale.y.attributeName[0]])
                barData.push({
                    x: xScale(data[i][chart_info.chartScale.x.attributeName]),
                    y: yScale(data[i][chart_info.chartScale.y.attributeName[0]]),
                    fill: chart_info.chartColor[chart_info.chartScale.y.attributeName[0]],
                    data: data[i],
                    width: (width / data.length > 20) ? .5 * (width / data.length) : (width / data.length),
                    height: height- yScale(data[i][chart_info.chartScale.y.attributeName[0]])
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
        
        this.overlayData = description_data;
        // console.log(this.overlayData);
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations) => {
            // console.log(mutations.events.key == "overlayTag");
            // if (mutations.events.key == "overlayTag") {
            //     console.log(this.overlayTag);
            this.chart_setting = dataStore.state_map['state0']['chart_setting'];
            this.overlayTag = dataStore.state_map['state0']['overlay_tag'];
            console.log(dataStore.state_map['state0']['overlay_setting'])
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
}</style>
