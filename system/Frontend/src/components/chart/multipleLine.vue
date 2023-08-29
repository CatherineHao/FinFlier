<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-08-26 19:48:41
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-08-27 20:29:10
-->
<template>
    <div ref="singleLineSvg" style="height: 100%; width: 100%;">
        <svg height="100%" width="100%" xmlns="http://www.w3.org/2000/svg" :style="{
            'transition': '0.4s',
            'opacity': isShow == true ? '1' : '0',
            'transform': `scale(${scaleTag})`
        }">
            <g id="mainSingleLine_g" :transform="translate(.05 * elWidth, .1 * elHeight)">

                <g>
                    <g id="xAxis"></g>
                    <g id="yAxis"></g>
                    <g id="axis_name">
                        <text class="title" text-anchor="end"
                            :transform="translate(axisPosition.xAxis[0], axisPosition.xAxis[1])">{{ chart_setting.axis.x }}</text>
                        <text class="title" text-anchor="start"
                            :transform="translate(axisPosition.yAxis[0], axisPosition.yAxis[1])">{{ chart_setting.axis.y }}</text>
                    </g>
                    <g id="singleline">
                        <path v-for="(o, i) in lineData" :key="'path' + i" :d="o.path" fill="none"
                            :stroke="colorTrans(chart_setting.currentColor[o.attr])" :stroke-width="chart_setting.size.width">
                        </path>
                    </g>
                </g>

            </g>
        </svg>
    </div>
</template>
<script>
import { axisBottom, axisLeft, extent, line, scaleLinear, scalePoint, scaleUtc, select, timeFormat } from "d3";
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
            lineData: [],
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
        // calcPath (center) {

        // },
        calcLine (data, chart_info) {
            if (this.defaultTag == 1) {
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
            // let xName = chart_info.chartScale.x.attributeName;
            // let yName = chart_info.chartScale.y.attributeName[0];
            let xScale = this.scale(data, chart_info.chartScale.x.attributeName, chart_info.chartScale.x.scaleType, [0, width]);
            let yScale = this.scale(data, chart_info.chartScale.y.attributeName, chart_info.chartScale.y.scaleType, [height, 0]);
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
            function lineGenerator (data, y_attr) {
            return line().x(d => xScale(new Date(d[chart_info.chartScale.x.attributeName]))).y(d => yScale(d[y_attr]))(data);}
            let lineData = new Array();
            for (let i in data) {
                if (i == 0 || i == 'columns') continue;
                for (let j of chart_info.chartScale.y.attributeName)
                lineData.push({
                    path: lineGenerator([data[i], data[i - 1]], j),
                    fill: chart_info.chartColor[j],
                    data: [data[i - 1], data[i]],
                    attr: j
                })
            }
            // console.log(lineData);
            return lineData;
        }
    },
    created () {
    },
    mounted () {
        this.elHeight = this.$refs.singleLineSvg.offsetHeight;
        this.elWidth = this.$refs.singleLineSvg.offsetWidth;
        // console.log(this.rawData, this.chartData);
        this.lineData = this.calcLine(this.rawData, this.chartData);

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
