<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2023-07-10 13:45:50
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-07-14 12:03:18
-->
<template>
    <div ref="singleBarSvg" style="height: 100%; width: 100%;">
        <svg height="100%" width="100%" xmlns="http://www.w3.org/2000/svg" :style="{
            'transition': '0.4s',
            'opacity': isShow == true ? '1' : '0'
        }">
            <g id="mainSingleBar_g" :transform="translate(.05 * elWidth, .1 * elHeight)">
                <g>
                            <g id="xAxis"></g>
                            <g id="yAxis"></g>
                            <g id="bar">
                                <g v-for="(item, i) in barData" :key="'single_bar_' + i">
                                    <rect :x="item.x - item.width / 2" :y="item.y" :fill="item.fill" :width="item.width"
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
                                    <g v-if="overlayTag.highlight['Background'] == 1" class="animation-fade">
                                        <rect :x="barData[item.objectIndex].x - 3 - barData[item.objectIndex].width / 2"
                                            :y="0" :fill="item.color" :width="barData[item.objectIndex].width + 6"
                                            :height="elHeight * .8" opacity="0.6"></rect>
                                    </g>
                                    <g v-if="overlayTag.highlight['Color'] == 1">
                                        <rect :x="barData[item.objectIndex].x - barData[item.objectIndex].width / 2"
                                            :y="barData[item.objectIndex].y" :fill="item.color"
                                            :width="barData[item.objectIndex].width"
                                            :height="barData[item.objectIndex].height" opacity="1"></rect>
                                    </g>
                                    <g v-if="overlayTag.highlight['Area'] == 1">
                                        <rect :x="barData[item.objectIndex].x - barData[item.objectIndex].width / 2"
                                            :y="barData[item.objectIndex].y" :fill="'none'"
                                            :width="barData[item.objectIndex].width"
                                            :height="barData[item.objectIndex].height" :stroke="item.color"
                                            :stroke-width="3" :stroke-dasharray="5.5" opacity="1"></rect>
                                    </g>
                                </g>
                                <g>
                                    <g v-if="overlayTag.annotation['Marker'] == 1">
                                        <circle :cx="barData[item.objectIndex].x" :cy="barData[item.objectIndex].y" r="7"
                                            :fill="item.color"></circle>
                                    </g>
                                    <g v-if="overlayTag.annotation['Label'] == 1">
                                        <circle :cx="barData[item.objectIndex].x"
                                            :cy="barData[item.objectIndex].y + barData[item.objectIndex].height / 2" r="7"
                                            :fill="item.color"></circle>
                                        <path
                                            :d="'M' + barData[item.objectIndex].x + ',' + (barData[item.objectIndex].y + barData[item.objectIndex].height / 2) + 'L' + barData[item.objectIndex].x + ',' + -10"
                                            fill="none" :stroke="item.color" stroke-width="3"></path>
                                        <text :x="barData[item.objectIndex].x" :y="-20" text-anchor="middle">
                                            {{ item.overlay.annotation.label }}
                                        </text>
                                    </g>
                                    <g v-if="overlayTag.annotation['Text'] == 1">
                                        <circle :cx="barData[item.objectIndex].x"
                                            :cy="barData[item.objectIndex].y + barData[item.objectIndex].height / 2" r="7"
                                            :fill="item.color"></circle>
                                        <path
                                            :d="'M' + barData[item.objectIndex].x + ',' + (barData[item.objectIndex].y + barData[item.objectIndex].height / 2) + 'L' + barData[item.objectIndex].x + ',' + 0"
                                            fill="none" :stroke="item.color" stroke-width="3"></path>
                                        <!-- <foreignObject width="120" height="100" :x="barData[item.objectIndex].x - 60"
                                        :y=".6 * elHeight">

                                        <xhtml:body xmlns="http://www.w3.org/1999/xhtml">
                                            <xhtml:p style="font-size:14px;margin:0;">
                                                {{ item.overlay.annotation.text }}
                                            </xhtml:p>
                                        </xhtml:body>
                                    </foreignObject> -->
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
            // 'transform': `translate(${barData[item.objectIndex].x}px, ${0}px)`,
            'width': '150px',
            'transition': '0.4s',
            // objectTag[item.objectName] == 1 && overlayTag.annotation['Text'] == 1 ? 
            'opacity': objectTag[item.objectName] == 1 && overlayTag.annotation['Text'] == 1 ? '1' : '0',
            'padding': '3px',
            'border': '2px solid',
            'border-radius': '10px',
            'border-color': item.color,
            'background-color': 'white'
        }">
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
    props: ['rawData', 'chartData'],
    data () {
        return {
            elHeight: 100,
            elWidth: 100,
            isShow: false,
            barData: [],
            overlayData: [],
            overlayTag: {
                highlight: {},
                annotation: {}
            },
            objectTag: {}
        };
    },
    methods: {
        translate (x, y) {
            return `translate(${x}, ${y})`;
        },
        scale (data, scale_info, range) {
            let scale_data = [];
            for (let i in data) {
                if (i == 'columns') continue;
                scale_data.push(data[i][scale_info.scaleName]);
            }
            if (scale_info.scaleType == 'categorical') {
                return scalePoint(scale_data, range).padding(1);
            }
            if (scale_info.scaleType == 'quantitative') {
                let dataDomain = extent(scale_data, d => parseFloat(d));
                if (dataDomain[1] < 0) dataDomain[1] = 0;
                if (dataDomain[0] > 0) dataDomain[0] = 0
                return scaleLinear(dataDomain, range);
            }
        },
        // calcPath (center) {

        // },
        calcBar (data, chart_info) {
            let width = this.elWidth * .9;
            let height = this.elHeight * .8;
            let xName = chart_info.chartScale.x.scaleName;
            let yName = chart_info.chartScale.y.scaleName;
            let xScale = this.scale(data, chart_info.chartScale.x, [0, width]);
            let yScale = this.scale(data, chart_info.chartScale.y, [height, 0]);
            let xAxis = (g, x, width, height, title) => {
                g.attr("transform", `translate(0, ${height})`)
                    .call(axisBottom(x))
                    .call(g => g.selectAll(".title").data([title]).join("text")
                        .attr("class", "title")
                        .attr("x", width - 10)
                        .attr("y", 18)
                        .attr("fill", "currentColor")
                        .attr("text-anchor", "start")
                        .text(title))
            }
            let yAxis = (g, y, width, title) => {
                g.attr("transform", `translate(${0}, 0)`)
                    .call(axisLeft(y).ticks(5).tickSizeOuter(0))
                    // .call(g => g.select(".domain").remove())
                    .call(g => g.selectAll(".title").data([title]).join("text")
                        .attr("class", "title")
                        .attr("x", -.05 * width)
                        .attr("y", -20)
                        .attr("fill", "currentColor")
                        .attr("text-anchor", "start")
                        .text(title))
            }
            select("#xAxis").call(xAxis, xScale, width, height, chart_info.chartScale.x.scaleName);
            select("#yAxis").call(yAxis, yScale, width, chart_info.chartScale.y.scaleName);
            let barData = new Array();
            for (let i in data) {
                if (i == 'columns') continue;
                barData.push({
                    x: xScale(data[i][xName]),
                    y: yScale(data[i][yName]),
                    fill: chart_info.chartColor[yName],
                    data: data[i],
                    width: (width / data.length > 20) ? .5 * (width / data.length) : (width / data.length),
                    height: height - yScale(data[i][yName])
                });
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
        this.overlayData = description_data;
        // console.log(this.overlayData);
        const dataStore = useDataStore();
        dataStore.$subscribe((mutations) => {
            // console.log(mutations.events.key == "overlayTag");
            // if (mutations.events.key == "overlayTag") {
            //     console.log(this.overlayTag);
            this.overlayTag = dataStore.overlayTag;
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
    font-size: 12px;
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
