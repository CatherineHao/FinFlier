<!--
 * @Description: Data Chart
 * @Author: Qing Shi
 * @Date: 2023-06-29 10:17:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2023-12-19 13:59:28
-->
<template>
    <div style="height: 100%; width: 100%;">
        <div style="font-family:KoHo; font-size: 22px; height: 40px; text-align: start; font-weight: bold; ">
            <img src="../assets/img/3.png" width="25" alt="">&nbsp; Data Chart
            <div style="float: right;">
                <svg t="1694324418790" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="8806" width="30" height="30">
                    <path d="M62.848 60.992h704v64h-704zM62.848 640.832h543.936v64H62.848z" p-id="8807"></path>
                    <path d="M702.848 60.992h64v320h-64zM62.848 113.536h64v527.296h-64z" p-id="8808"></path>
                    <path d="M70.528 498.304l218.24-117.312 30.4 56.32-218.304 117.376z" p-id="8809"></path>
                    <path
                        d="M298.432 375.04l144.896 274.176-56.576 29.888L241.92 404.928zM512 194.176h126.592v127.168H512zM663.296 448.448h128v320h-128z"
                        p-id="8810"></path>
                    <path d="M599.36 764.992l127.936 128 128.064-128z" p-id="8811"></path>
                </svg>
            </div>
            <hr>
        </div>
        <div style="height: calc(100% - 40px); width: 100%;">

            <div style="height: calc(70%); width: 100%;" v-loading="initChart" ref="mainView" id="mainView"><div class="overlayTag" style="position: absolute; top: 0px; left: 0px; background-color: rgb(99, 99, 99, .2);">
                        {{ typeof selObj != 'string' || selObj == '' ? 'Raw' : 'Narrative ' + (1 + parseInt(selObj.slice(-1))) }}</div>
                <component :is="tabs[chartType[chartData['chartType']]]" :rawData="rawData" :chartData="chartData"
                    :defaultTag="1" :scaleTag="1" :stateTag="'state0'" :objTag="selObj"></component>
            </div>
            <hr>
            <!-- display: flex; justify-content: space-between; align-items: center; -->
            <div ref="narrative_gallery" style="height: calc(30% - 0px); width: 100%; background-color: white; overflow-y: auto; display: flex;">
                <div v-for="(nar, nar_i) in narrative_num" :key="'nar' + nar_i"
                    style="height: 98%; width: 33%; border-radius: 5px; border: 1.5px solid rgba(99, 99, 99, .6); align-items: center; display: flex; justify-content: center; margin: 3px;">
                    <div class="overlayTag" :style="{'position': 'absolute', 'top': '5px', 'left': '10px', backgroundColor: selObj == 'object' + nar_i ? '#2f5597' : 'rgb(99, 99, 99, .2)', color: selObj == 'object' + nar_i ? 'white' : 'black'}">
                    
                        {{ 'Narrative ' + (nar_i + 1) }}</div>
                    <component :is="tabs[chartType[chartData['chartType']]]" :rawData="rawData" :chartData="chartData" style="margin-top: 60px;"
                        :defaultTag="1" :scaleTag=".33" :stateTag="'state0'" :objTag="'object' + (nar_i)"></component>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useDataStore } from "../stores/counter";
import singleBar from "./chart/singleBar.vue";
import singleLine from "./chart/singleLine.vue";
import multipleBar from "./chart/multipleBar.vue";
import multipleLine from "./chart/multipleLine.vue";
export default {
    name: "DataChart",
    props: [],
    data () {
        return {
            msg1: "Hello, main!",
            rawData: [],
            chartData: {},
            tabs: {
                'Single bar chart': 'singleBar',
                'Single line chart': 'singleLine',
                'Multiple bar chart': 'multipleBar',
                'Multiple line chart': 'multipleLine'
            },
            chartType: ['Single bar chart', 'Single line chart', 'Multiple bar chart', 'Multiple line chart'],
            chartValue: null,
            highlightType: ['Color', 'Area', 'Background'],
            highlightValue: [],
            annotationType: ['Marker', 'Label', 'Text'],
            annotationValue: [],
            othersType: ['Add Line (with Arrow)', 'Design Configuration'],
            otherValue: [],
            overlayTag: {
                highlight: {},
                annotation: {}
            },
            initChart: true,
            narrative_num: 0,
            selObj: -1
        };
    },
    methods: {},
    created () { },
    computed: {
        // initChart () {
        //     // console.log(this.chartData == null)
        //     return this.chartData == null;
        // }
    },
    mounted () {
        // console.log(chart_data)
        const dataStore = useDataStore()
        // console.log(dataStore.chart_data)

        dataStore.$subscribe(mutations => {
            // console.log(mutations);
            if (mutations.events.key == 'chart_data') {
                this.chartData = dataStore.chart_data;
                this.rawData = dataStore.data;
                this.initChart = false
                this.chartValue = this.chartData.chartType;
                console.log(this.tabs[this.chartType[this.chartData.chartType]]);
            }
            this.narrative_num = dataStore.narrative_num;
            this.selObj = dataStore.selectObject;
            // console.log(this.selObj, typeof(this.selObj))
            if (!(typeof (this.selObj)== 'string' && this.selObj == '')) {
                let nar_cnt = parseInt(this.selObj.slice(-1));
                this.$refs.narrative_gallery.scrollLeft = (nar_cnt) * this.$refs.narrative_gallery.offsetWidth / 3;
                console.log((nar_cnt - 1) * this.$refs.narrative_gallery.offWidth / 3, nar_cnt)
            }
        })
    },
    watch: {
        // highlightValue (newVal, oldVal) {
        //     this.overlayTag.highlight = {};
        //     const dataStore = useDataStore();
        //     for (let i in this.highlightValue) {
        //         this.overlayTag.highlight[this.highlightValue[i]] = 1;
        //     }
        //     dataStore.overlayTag = this.overlayTag;
        // },
        // annotationValue () {
        //     this.overlayTag.annotation = {};
        //     const dataStore = useDataStore();
        //     for (let i in this.annotationValue) {
        //         this.overlayTag.annotation[this.annotationValue[i]] = 1;
        //     }
        //     dataStore.overlayTag = this.overlayTag;
        // }
    },
    components: { singleBar, singleLine, multipleBar, multipleLine }
}
</script>

<style scoped>.overlayTag {
    /* font-family: KoHo; */
    /* background-color: rgb(99, 99, 99, .2); */
    border-radius: 10px;
    padding: 3px 10px 3px 10px;
    font-weight: 600;
    font-style: italic;
}</style>
